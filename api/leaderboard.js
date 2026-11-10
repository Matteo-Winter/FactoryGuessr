// Leaderboard for "Wo & Wann?" (Vercel serverless function, no dependencies).
//
// Storage: Upstash Redis over its REST API. Vercel's Upstash integration sets
// KV_REST_API_URL/_TOKEN (or UPSTASH_REDIS_REST_URL/_TOKEN), possibly with a custom prefix.
// Without them every request answers 503 and the game keeps working without a leaderboard.
//
// Identity: each browser creates a random token. The first browser that claims a name owns it;
// another browser gets "taken". One token holds one name, so changing the name moves the entry
// instead of creating a second one. Only the SHA-256 of the token is stored.
//
// Ranking: the best round per player, as average points per image (max 10,000).
// Only rounds with at least MIN_IMAGES images count.
//
// GET  /api/leaderboard?me=<name>                      → {top:[…], me, total}
// POST /api/leaderboard {action:"claim", name, token}  → {ok, name} | 409 taken | 400 invalid
// POST /api/leaderboard {action:"score", name, token, points:[…]} → {ok, counted, avg, best, improved, rank, total}

const crypto = require('crypto');

const MIN_IMAGES = 5;
const MAX_IMAGES = 9;
const MAX_POINTS = 10000; // per image: 5,000 place + 5,000 time
const TOP = 50;
const K = { owner: 'ww:owner', byToken: 'ww:bytoken', stats: 'ww:stats', board: 'ww:board' };
// Obvious slurs and insults; matched against the normalised name key.
const BLOCKED = ['hitler', 'nazi', 'heilhitler', 'nigger', 'nigga', 'neger', 'fotze', 'fuck', 'fick', 'wichser', 'hurensohn', 'schlampe', 'penis', 'vagina', 'porn', 'kanake', 'schwuchtel', 'spast', 'behindert', 'adolf'];

const envBySuffix = (re) => { const k = Object.keys(process.env).find((x) => re.test(x)); return k ? process.env[k] : undefined; };
const URL_ = envBySuffix(/(KV_REST_API|UPSTASH_REDIS_REST)_URL$/);
const TOKEN_ = envBySuffix(/(KV_REST_API|UPSTASH_REDIS_REST)_TOKEN$/);

async function redis(path, body) {
  const r = await fetch(URL_.replace(/\/$/, '') + path, {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + TOKEN_, 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  const data = await r.json();
  if (!r.ok || data.error) throw new Error('redis: ' + (data.error || r.status));
  return data;
}
const cmd = async (...args) => (await redis('', args)).result;
const pipe = async (cmds) => (await redis('/pipeline', cmds)).map((x) => { if (x.error) throw new Error('redis: ' + x.error); return x.result; });
const multi = async (cmds) => (await redis('/multi-exec', cmds)).map((x) => { if (x.error) throw new Error('redis: ' + x.error); return x.result; });

// Display name: NFKC, single spaces, 2–20 characters, letters/digits plus space . _ ' -
function cleanName(raw) {
  if (typeof raw !== 'string') return null;
  const name = raw.normalize('NFKC').replace(/\s+/g, ' ').trim();
  if ([...name].length < 2 || [...name].length > 20) return null;
  if (!/^[\p{L}\p{N}][\p{L}\p{N} ._'-]*$/u.test(name)) return null;
  return name;
}
// Uniqueness key: case-insensitive and without spaces/punctuation, so "Max M", "max-m" and "MaxM" are one name.
const nameKey = (name) => name.toLocaleLowerCase('de').replace(/[ ._'-]/g, '');
const isBlocked = (key) => BLOCKED.some((w) => key.includes(w));
const tokenHash = (t) => (typeof t === 'string' && /^[a-f0-9]{32,64}$/.test(t) ? crypto.createHash('sha256').update(t).digest('hex') : null);

function send(res, status, obj) {
  res.statusCode = status;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  res.end(JSON.stringify(obj));
}
async function readBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') return JSON.parse(req.body);
  let s = '';
  for await (const chunk of req) { s += chunk; if (s.length > 4096) throw new Error('too large'); }
  return s ? JSON.parse(s) : {};
}
function clientIp(req) {
  return String(req.headers['x-forwarded-for'] || req.socket?.remoteAddress || 'unknown').split(',')[0].trim();
}
// Fixed one-hour window per key; true while under the limit.
async function underLimit(key, max) {
  const [n] = await pipe([['INCR', key], ['EXPIRE', key, 3600, 'NX']]);
  return n <= max;
}
const parseStats = (s) => { try { return s ? JSON.parse(s) : null; } catch (e) { return null; } };

async function leaderboard(meName) {
  const flat = await cmd('ZREVRANGE', K.board, 0, TOP - 1, 'WITHSCORES');
  const keys = [];
  for (let i = 0; i < flat.length; i += 2) keys.push(flat[i]);
  const meKey = meName && cleanName(meName) ? nameKey(cleanName(meName)) : null;
  const [stats, total, meRank, meStats] = await pipe([
    keys.length ? ['HMGET', K.stats, ...keys] : ['ECHO', '[]'],
    ['ZCARD', K.board],
    meKey ? ['ZREVRANK', K.board, meKey] : ['ECHO', ''],
    meKey ? ['HGET', K.stats, meKey] : ['ECHO', ''],
  ]);
  const top = keys.map((key, i) => {
    const st = parseStats(Array.isArray(stats) ? stats[i] : null) || {};
    return { rank: i + 1, name: st.name || key, avg: Number(flat[i * 2 + 1]), rounds: st.rounds || 0 };
  });
  let me = null;
  if (meKey && meRank !== null && meRank !== '') {
    const st = parseStats(meStats) || {};
    me = { rank: meRank + 1, name: st.name || meKey, avg: st.best || 0, rounds: st.rounds || 0 };
  }
  return { top, me, total, minImages: MIN_IMAGES };
}

async function claim(body, ip) {
  const name = cleanName(body.name), th = tokenHash(body.token);
  if (!name || !th) return [400, { error: 'invalid' }];
  const key = nameKey(name);
  if (key.length < 2 || isBlocked(key)) return [400, { error: 'invalid' }];
  if (!(await underLimit('ww:rl:claim:' + ip, 30))) return [429, { error: 'rate' }];

  const [set, owner, oldKey] = await pipe([['HSETNX', K.owner, key, th], ['HGET', K.owner, key], ['HGET', K.byToken, th]]);
  if (!set && owner !== th) return [409, { error: 'taken' }];

  if (oldKey && oldKey !== key) {
    // Name change: move the entry so this player is never listed twice.
    const [oldStats, oldScore] = await pipe([['HGET', K.stats, oldKey], ['ZSCORE', K.board, oldKey]]);
    const st = { ...(parseStats(oldStats) || { best: 0, rounds: 0 }), name };
    const ops = [['HSET', K.byToken, th, key], ['HSET', K.stats, key, JSON.stringify(st)],
      ['HDEL', K.owner, oldKey], ['HDEL', K.stats, oldKey], ['ZREM', K.board, oldKey]];
    if (oldScore !== null) ops.push(['ZADD', K.board, oldScore, key]);
    await multi(ops);
  } else {
    // New name, or the same name with different spelling ("max" → "Max").
    const st = parseStats(await cmd('HGET', K.stats, key)) || { best: 0, rounds: 0 };
    st.name = name;
    await pipe([['HSET', K.byToken, th, key], ['HSET', K.stats, key, JSON.stringify(st)]]);
  }
  return [200, { ok: true, name }];
}

async function score(body) {
  const name = cleanName(body.name), th = tokenHash(body.token), pts = body.points;
  if (!name || !th) return [400, { error: 'invalid' }];
  if (!Array.isArray(pts) || pts.length < 1 || pts.length > MAX_IMAGES ||
      !pts.every((p) => Number.isInteger(p) && p >= 0 && p <= MAX_POINTS)) return [400, { error: 'invalid' }];
  const key = nameKey(name);
  if ((await cmd('HGET', K.owner, key)) !== th) return [403, { error: 'not_owner' }];
  if (!(await underLimit('ww:rl:score:' + th, 120))) return [429, { error: 'rate' }];

  const st = parseStats(await cmd('HGET', K.stats, key)) || { name, best: 0, rounds: 0 };
  const avg = Math.round(pts.reduce((a, b) => a + b, 0) / pts.length);
  const counted = pts.length >= MIN_IMAGES;
  const improved = counted && avg > (st.best || 0);
  st.name = name;
  st.rounds = (st.rounds || 0) + (counted ? 1 : 0);
  if (improved) { st.best = avg; st.at = Date.now(); }
  const ops = [['HSET', K.stats, key, JSON.stringify(st)]];
  if (improved) ops.push(['ZADD', K.board, avg, key]);
  await pipe(ops);
  const [rank, total] = await pipe([['ZREVRANK', K.board, key], ['ZCARD', K.board]]);
  return [200, { ok: true, counted, avg, best: st.best || 0, improved, rank: rank === null ? null : rank + 1, total, minImages: MIN_IMAGES }];
}

module.exports = async (req, res) => {
  if (!URL_ || !TOKEN_) return send(res, 503, { error: 'not_configured' });
  try {
    if (req.method === 'GET') {
      const me = new URL(req.url, 'http://x').searchParams.get('me');
      return send(res, 200, await leaderboard(me));
    }
    if (req.method === 'POST') {
      let body;
      try { body = await readBody(req); } catch (e) { return send(res, 400, { error: 'invalid' }); }
      const [status, obj] = body.action === 'claim' ? await claim(body, clientIp(req))
        : body.action === 'score' ? await score(body) : [400, { error: 'invalid' }];
      return send(res, status, obj);
    }
    res.setHeader('Allow', 'GET, POST');
    return send(res, 405, { error: 'method' });
  } catch (e) {
    console.error(e);
    return send(res, 500, { error: 'server' });
  }
};
