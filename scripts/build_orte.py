# Builds the playable Orte: reads public/assets/panoramas/_local/index.json (+ one .json solution per image),
# writes web JPGs (max 4096x2048, q86) to public/assets/orte/ and all solutions to public/data/orte.json.
# Run from the repo root: python3 scripts/build_orte.py   (needs Pillow)
import json,re,os,sys
from PIL import Image
src='public/assets/panoramas/_local/';dst='public/assets/orte/'
files=json.load(open(src+'index.json'));orte=[]
for f in files:
    base=f.rsplit('.',1)[0];sol=json.load(open(src+base+'.json'))
    im=Image.open(src+f).convert('RGB')
    if im.width>4096: im=im.resize((4096,2048),Image.LANCZOS)
    out=dst+base+'.jpg';im.save(out,'JPEG',quality=86,progressive=True,optimize=True)
    oid=re.sub(r'-local(-test)?$','',sol.get('id',base))
    sol['id']=oid;sol['group']=re.sub(r'(\d)[a-z]$',r'\1',oid);sol.setdefault('block','production')
    sol['panorama_path']='assets/orte/'+base+'.jpg';sol['source_file']=f
    orte.append(sol);print(f'{oid:5} {sol["group"]:4} {im.width}x{im.height} {os.path.getsize(out)//1024} KB')
# Pilot scenes from scenes.json keep their image there; _local/pilots/<scene id>.json adds the full solution text.
scenes={x['id']:x for x in json.load(open('public/data/scenes.json'))['scenes']}
pd=src+'pilots/'
for f in sorted(os.listdir(pd)) if os.path.isdir(pd) else []:
    if not f.endswith('.json'): continue
    sol=json.load(open(pd+f));sc=scenes[sol.pop('pilot_of')]
    sol.update(year=sc['year'],country_de=sc['country_de'],panorama_path=sc['panorama_path'],group=sol['id'],scene_id=sc['id'])
    orte.append(sol);print(f'{sol["id"]:5} pilot {sc["id"]}')
json.dump({"schema_version":1,"note":"Spielbare Orte (KI-Rekonstruktionen, nicht historisch freigegeben). Gleiche 'group' = Varianten desselben Orts; pro Runde höchstens eine.","orte":orte},open('public/data/orte.json','w'),ensure_ascii=False,indent=1)
