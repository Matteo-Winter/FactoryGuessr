#!/usr/bin/env python3
"""Export true perspective (rectilinear) views from an equirectangular panorama.

Every output pixel is cast as a 3D ray, rotated by pitch and yaw, converted to
longitude/latitude and sampled from the source image with bilinear filtering
and horizontal wrap-around. These are NOT 2D crops: the zenith/nadir views show
exactly what a 360 viewer shows when looking straight up/down.

Angle convention (identical to Pannellum, the viewer in public/index.html):
    yaw   0 = horizontal centre of the image, positive = to the right,
          +/-180 = the left/right image edge (the wrap-around seam)
    pitch 0 = horizon, +90 = zenith (top row), -90 = nadir (bottom row)
    hfov  horizontal field of view in degrees

Usage:
    python3 scripts/export_panorama_views.py public/assets/panoramas/gb-1840-textile-mill.jpg
    python3 scripts/export_panorama_views.py <image> --out qa-output/<name> --size 1024 --hfov 90
    python3 scripts/export_panorama_views.py <image> --view 180,0,40 --view 45,-60,90

Output folder: one PNG per view, contact_sheet.jpg and manifest.json.
The tool never approves an image ("approved": false). The only number it adds is
a seam jump measured in a perspective view; it points a human reviewer at
problems and does not prove correct geometry. There is deliberately no pole
score: candidates tried on the baseline images did not separate the visibly
swirled poles from correct ones, so poles are judged by eye.
Requires: NumPy and Pillow (python3 -m pip install -r requirements-qa.txt).
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError

# name, yaw, pitch, hfov (None = use --hfov)
DEFAULT_VIEWS = [
    ("front_yaw000", 0.0, 0.0, None),
    ("right_yaw090", 90.0, 0.0, None),
    ("seam_yaw180", 180.0, 0.0, None),
    ("left_yaw270", -90.0, 0.0, None),
    ("zenith_pitch+90", 0.0, 90.0, None),
    ("nadir_pitch-90", 0.0, -90.0, None),
    ("seam_closeup_yaw180", 180.0, 0.0, 40.0),
]
SEAM_COLOR = np.array([255, 0, 200], dtype=np.uint8)


def view_rays(yaw_deg, pitch_deg, hfov_deg, width, height):
    """Return (lon, lat) in radians for every pixel of a rectilinear view."""
    if not 0 < hfov_deg < 180:
        raise ValueError("hfov must be between 0 and 180 degrees")
    f = (width / 2) / math.tan(math.radians(hfov_deg) / 2)
    x = np.arange(width, dtype=np.float64) + 0.5 - width / 2
    y = -(np.arange(height, dtype=np.float64) + 0.5 - height / 2)
    x, y = np.meshgrid(x, y)
    z = np.full_like(x, f)
    p, w = math.radians(pitch_deg), math.radians(yaw_deg)
    # pitch: rotate around the camera x-axis (positive = look up)
    y1 = y * math.cos(p) + z * math.sin(p)
    z1 = -y * math.sin(p) + z * math.cos(p)
    # yaw: rotate around the vertical axis (positive = turn right)
    x2 = x * math.cos(w) + z1 * math.sin(w)
    z2 = -x * math.sin(w) + z1 * math.cos(w)
    lon = np.arctan2(x2, z2)
    lat = np.arctan2(y1, np.hypot(x2, z2))
    return lon, lat


def sample(equi, lon, lat):
    """Bilinear lookup in an equirectangular uint8 array; wraps horizontally."""
    h, w = equi.shape[:2]
    u = (lon / (2 * math.pi) + 0.5) * w - 0.5
    v = (0.5 - lat / math.pi) * h - 0.5
    v = np.clip(v, 0, h - 1)
    x0 = np.floor(u).astype(np.int64)
    y0 = np.floor(v).astype(np.int64)
    fx = (u - x0)[..., None]
    fy = (v - y0)[..., None]
    x1 = (x0 + 1) % w
    x0 = x0 % w
    y1 = np.minimum(y0 + 1, h - 1)
    px = lambda yy, xx: equi[yy, xx].astype(np.float32)  # convert only the gathered pixels
    top = px(y0, x0) * (1 - fx) + px(y0, x1) * fx
    bottom = px(y1, x0) * (1 - fx) + px(y1, x1) * fx
    return np.clip(top * (1 - fy) + bottom * fy + 0.5, 0, 255).astype(np.uint8)


def seam_mask(lon):
    """Pixels where the view crosses the +/-180 degree meridian (image edge)."""
    jump_x = np.abs(np.diff(lon, axis=1)) > math.pi
    jump_y = np.abs(np.diff(lon, axis=0)) > math.pi
    mask = np.zeros(lon.shape, dtype=bool)
    mask[:, :-1] |= jump_x
    mask[:-1, :] |= jump_y
    return mask


def render_view(equi, yaw, pitch, hfov, width, height):
    lon, lat = view_rays(yaw, pitch, hfov, width, height)
    return sample(equi, lon, lat), seam_mask(lon)


def seam_view_diagnostics(equi, size=512, hfov=40.0):
    """In a narrow perspective view centred on the seam, compare the jump across
    the seam meridian with the mean of all other neighbouring-column differences."""
    img, mask = render_view(equi, 180.0, 0.0, hfov, size, size)
    img = img.astype(np.float32)
    band = slice(size // 10, size - size // 10)
    diffs = np.abs(img[band, 1:] - img[band, :-1]).mean(axis=(0, 2))
    cols = np.where(mask[band].any(axis=0))[0]
    seam_cols = [c for c in cols if c < size - 1]
    seam = float(diffs[seam_cols].mean()) if seam_cols else float("nan")
    ref = float(np.delete(diffs, seam_cols).mean())  # mean, not median: texture-poor images have a zero median
    return {
        "seam_view_hfov": hfov,
        "seam_jump": round(seam, 3),
        "ordinary_column_step_mean": round(ref, 3),
        "seam_vs_ordinary_ratio": round(seam / ref, 3) if ref > 1e-6 else None,
    }


def label_font(size):
    for name in ("Arial.ttf", "Helvetica.ttc", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def overlay_seam(img, mask):
    out = img.copy()
    rows = np.arange(mask.shape[0])[:, None]
    dashed = mask & ((rows // 6) % 2 == 0)  # dashed so the real seam stays visible
    out[dashed] = SEAM_COLOR
    return out


def contact_sheet(equi, views, src_name, meta, tile=360):
    font, small = label_font(18), label_font(14)
    cols = 4
    rows = math.ceil(len(views) / cols)
    pad, label_h, header_h = 12, 26, 70
    overview_w = cols * tile + (cols - 1) * pad
    overview_h = overview_w // 2
    W = overview_w + 2 * pad
    H = header_h + overview_h + pad + rows * (tile + label_h + pad) + pad
    sheet = Image.new("RGB", (W, H), (18, 18, 18))
    d = ImageDraw.Draw(sheet)
    d.text((pad, 10), f"{src_name}  ·  {meta['width']}×{meta['height']}  ·  NOT APPROVED – manual QA required", fill=(240, 240, 240), font=font)
    d.text((pad, 38), "Perspective views via spherical remapping (Pannellum convention). Magenta dashes = ±180° seam meridian (image edge).", fill=(170, 170, 170), font=small)
    # equirectangular overview with view centres
    ov = Image.fromarray(equi).resize((overview_w, overview_h), Image.BILINEAR)
    sheet.paste(ov, (pad, header_h))
    od = ImageDraw.Draw(sheet)
    for x in (pad, pad + overview_w - 1):
        od.line([(x, header_h), (x, header_h + overview_h)], fill=tuple(SEAM_COLOR), width=3)
    for i, v in enumerate(views):
        cx = pad + (v["yaw"] / 360 + 0.5) % 1.0 * overview_w
        cy = header_h + (0.5 - v["pitch"] / 180) * overview_h
        cy = min(max(cy, header_h + 10), header_h + overview_h - 10)
        od.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], outline=(255, 210, 0), width=3)
        od.text((cx + 12, cy - 9), str(i + 1), fill=(255, 210, 0), font=font)
    y0 = header_h + overview_h + pad
    for i, v in enumerate(views):
        r, c = divmod(i, cols)
        x = pad + c * (tile + pad)
        y = y0 + r * (tile + label_h + pad)
        thumb = np.asarray(Image.fromarray(v["image"]).resize((tile, tile), Image.LANCZOS)).copy()
        small_mask = np.asarray(Image.fromarray(v["mask"].astype(np.uint8) * 255).resize((tile, tile), Image.BOX)) > 0
        thumb = Image.fromarray(overlay_seam(thumb, small_mask))
        sheet.paste(thumb, (x, y + label_h))
        d.text((x, y + 3), f"{i + 1}  {v['name']}  yaw {v['yaw']:g}° pitch {v['pitch']:g}° hfov {v['hfov']:g}°", fill=(230, 230, 230), font=small)
    return sheet


def parse_view(text):
    parts = [float(p) for p in text.split(",")]
    if len(parts) not in (2, 3):
        raise argparse.ArgumentTypeError("view must be yaw,pitch[,hfov]")
    return parts


def export(path: Path, out_dir: Path, size=1024, hfov=90.0, extra_views=(), defaults=True, sheet=True):
    with Image.open(path) as im:
        equi = np.asarray(im.convert("RGB"), dtype=np.uint8)
    h, w = equi.shape[:2]
    out_dir.mkdir(parents=True, exist_ok=True)
    specs = [(n, y, p, hf or hfov) for n, y, p, hf in DEFAULT_VIEWS] if defaults else []
    for parts in extra_views:
        y, p = parts[0], parts[1]
        hf = parts[2] if len(parts) > 2 else hfov
        specs.append((f"custom_yaw{y:g}_pitch{p:g}_hfov{hf:g}", y, p, hf))
    views, files = [], []
    for name, yaw, pitch, hf in specs:
        img, mask = render_view(equi, yaw, pitch, hf, size, size)
        fname = f"{len(views) + 1:02d}_{name}.png"
        Image.fromarray(img).save(out_dir / fname)
        views.append({"name": name, "yaw": yaw, "pitch": pitch, "hfov": hf, "image": img, "mask": mask})
        files.append({"file": fname, "yaw": yaw, "pitch": pitch, "hfov": hf, "size": [size, size], "contains_seam": bool(mask.any())})
    manifest = {
        "source": str(path),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "width": w,
        "height": h,
        "aspect_ratio_2_to_1": w == 2 * h,
        "convention": "Pannellum: yaw 0 = image centre, +yaw right, ±180 = seam; +pitch up",
        "views": files,
        "seam_view": seam_view_diagnostics(equi),
        "poles": "no automatic metric: inspect zenith/nadir views by eye (see docs/PANORAMA_QA_PROBES.md)",
        "manual_qa_required": True,
        "approved": False,
    }
    if sheet:
        contact_sheet(equi, views, path.name, manifest).save(out_dir / "contact_sheet.jpg", quality=90)
        manifest["contact_sheet"] = "contact_sheet.jpg"
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--out", type=Path, help="output folder (default: qa-output/<image name>); with several images a subfolder per image")
    parser.add_argument("--size", type=int, default=1024, help="square view size in pixels (default 1024)")
    parser.add_argument("--hfov", type=float, default=90.0, help="field of view for the standard views (default 90)")
    parser.add_argument("--view", type=parse_view, action="append", default=[], metavar="YAW,PITCH[,HFOV]", help="extra view, repeatable")
    parser.add_argument("--only-custom", action="store_true", help="skip the standard views")
    parser.add_argument("--no-sheet", action="store_true", help="skip contact_sheet.jpg")
    args = parser.parse_args(argv)
    status = 0
    for path in args.images:
        if args.out and len(args.images) == 1:
            out = args.out
        else:
            out = (args.out or Path("qa-output")) / path.stem
        try:
            m = export(path, out, args.size, args.hfov, args.view, not args.only_custom, not args.no_sheet)
        except (OSError, ValueError, UnidentifiedImageError) as exc:
            print(f"{path}\n  ERROR: {exc}")
            status = 1
            continue
        sv = m["seam_view"]
        print(f"{path} -> {out}/")
        print(f"  {m['width']}x{m['height']} | {len(m['views'])} views | seam-view jump/ordinary {sv['seam_vs_ordinary_ratio']}")
        print("  NOT APPROVED: open contact_sheet.jpg and check seam, poles, distortions, history and rights by eye")
    return status


if __name__ == "__main__":
    sys.exit(main())
