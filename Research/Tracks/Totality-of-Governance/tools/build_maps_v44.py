#!/usr/bin/env python3
"""Build Maps & Matrix v44 = v43 (copied unchanged) + ToG 1 overlay. Grok Bot, 2026-10-25.
Usage: python3 Research/Tracks/Totality-of-Governance/tools/build_maps_v44.py
README.md in the output folder is kept; MANIFEST.sha256 is rewritten last."""
import csv, json, hashlib, os, shutil, collections, subprocess, sys
REPO=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','..'))
MM=f'{REPO}/Research/Maps-and-Matrix'
V43='v43-cycles-0-4-mr-track-abcd-phases-x12-conn0abcd'
V44='v44-cycles-0-4-mr-track-abcd-phases-x12-conn0abcd-tog1'
TOG='Research/Tracks/Totality-of-Governance/ToG-1-Constitutional-Commitments'
T=f'{REPO}/{TOG}'
src=f'{MM}/{V43}'; out=f'{MM}/{V44}'
os.makedirs(out,exist_ok=True)
CY=['Baseline','x3','x6','x9','x12']
CLAIMS={'Baseline':'claims/CLAIMS.csv','x3':'claims/CLAIMS_X3.csv','x6':'claims/CLAIMS_X6.csv','x9':'claims/CLAIMS_X9.csv','x12':'claims/CLAIMS_X12.csv'}
suf={'Baseline':'','x3':'_X3','x6':'_X6','x9':'_X9','x12':'_X12'}
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def rd(p): return list(csv.DictReader(open(p,encoding='utf-8',newline='')))
def wr(p,hdr,rows):
    os.makedirs(os.path.dirname(p),exist_ok=True)
    with open(p,'w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(hdr); w.writerows(rows)
inputs={}
def use(rel):
    p=f'{T}/{rel}'; inputs[f'{TOG}/{rel}']=sha(p); return p
# 1 copy v43 base unchanged (except README/MANIFEST, and files we extend)
EXT={'matrix/intersections_625.csv','graph/link_graph.json','graph/link_graph.mmd'}
copied=[]
for dp,_,fs in os.walk(src):
    for f in fs:
        rel=os.path.relpath(f'{dp}/{f}',src)
        if rel in ('README.md','MANIFEST.sha256'): continue
        os.makedirs(os.path.dirname(f'{out}/{rel}'),exist_ok=True)
        if rel not in EXT: shutil.copy2(f'{src}/{rel}',f'{out}/{rel}'); copied.append(rel)
# 2 claims all cycles
claims=[]; per=collections.OrderedDict()
for c in CY:
    rows=rd(use(f'{c}/'+CLAIMS[c]))
    per[c]=rows
    for r in rows:
        claims.append([c,r['claim_id'],r['clause'],r['class'],r['label'],r['status'],r.get('source_ids') or r.get('sources',''),f'{TOG}/{c}/{CLAIMS[c]}'])
wr(f'{out}/matrix/tog1_claims_all_cycles.csv',['cycle','claim_id','clause','class','label','status','sources_as_stated','source_file'],claims)
LABELS=['Established','Plausible','Philosophical/Spiritual','Hypothetical']
CLAUSES=['4.%d'%i for i in range(1,12)]+['cross-cutting']
rows=[]
for cl in CLAUSES:
    row=[cl]
    for c in CY: row.append(sum(1 for r in per[c] if r['clause']==cl))
    x=collections.Counter(r['label'] for r in per['x12'] if r['clause']==cl)
    row+= [x[l] for l in LABELS]
    rows.append(row)
tot=['TOTAL']+[len(per[c]) for c in CY]+[collections.Counter(r['label'] for r in per['x12'])[l] for l in LABELS]
rows.append(tot)
wr(f'{out}/matrix/tog1_clause_x_cycle.csv',['clause']+[f'claims_{c}' for c in CY]+[f'x12_{l}' for l in LABELS],rows)
# label x cycle
wr(f'{out}/matrix/tog1_label_x_cycle.csv',['label']+CY,[[l]+[collections.Counter(r['label'] for r in per[c])[l] for c in CY] for l in LABELS]+[['TOTAL']+[len(per[c]) for c in CY]])
# 3 domain map union
dom=collections.OrderedDict()
for c in CY:
    for r in rd(use(f'{c}/maps/DOMAIN_MAP{suf[c]}.csv')):
        k=(r['clause'],r['domain'])
        d=dom.setdefault(k,{'cycles':[],'label_x12':'','approval_x12':''})
        d['cycles'].append(c)
        if c=='x12': d['label_x12']=r['label']; d['approval_x12']=r.get('approval','')
wr(f'{out}/matrix/tog1_clause_domain_map.csv',['clause','domain','cycles_present','label_in_x12','approval_in_x12'],
   [[k[0],k[1],';'.join(v['cycles']),v['label_x12'] or 'not in x12',v['approval_x12'] or 'not in x12'] for k,v in sorted(dom.items(),key=lambda kv:(int(kv[0][0].split('.')[1]) if kv[0][0].startswith('4.') else 99,kv[0][1]))])
doms=sorted({k[1] for k,v in dom.items() if 'x12' in v['cycles']})
x12d={k for k,v in dom.items() if 'x12' in v['cycles']}
wr(f'{out}/matrix/tog1_clause_x_domain_x12.csv',['clause']+doms,[[cl]+[1 if (cl,d) in x12d else 0 for d in doms] for cl in CLAUSES[:-1]])
# 4 clause crosswalk x12 (verbatim columns) + per-cycle presence
cw=rd(use('x12/maps/CLAUSE_CROSSWALK_X12.csv'))
for c in CY[:-1]: use(f'{c}/maps/CLAUSE_CROSSWALK{suf[c]}.csv')
wr(f'{out}/matrix/tog1_clause_crosswalk_x12.csv',list(cw[0].keys())+['source_file'],[list(r.values())+[f'{TOG}/x12/maps/CLAUSE_CROSSWALK_X12.csv'] for r in cw])
# 5 links -> graph
NODE={'FoundationalReport1:Body':'R1','FoundationalReport2:Mind':'R2','FoundationalReport3:Soul':'R3','FoundationalReport4:Spirit':'R4','FoundationalReport5:Consciousness':'R5','FoundationalReport6:Earth':'R6','FoundationalReport7:UnifiedFramework':'R7','MasterLoveReport':'MR','SSSCtrack':'SOUL;SPIRIT;SUBC;CONS'}
for c in CY[:-1]: use(f'{c}/maps/LINKS{suf[c]}.csv')
links=rd(use('x12/maps/LINKS_X12.csv'))
lrows=[];edges=[]
LC={'Established':'E','Plausible':'P','Philosophical/Spiritual':'PS','Hypothetical':'H'}
for r in links:
    n=NODE.get(r['target'],'')
    lrows.append([r['link_id'],r['target'],r['relationship'],r['label'],r['scope'],n or 'no node in the v43 graph (not added)'])
    for t in n.split(';') if n else []:
        edges.append({'id':f"TG1-{len(edges)+1:02d}",'source':'TOG1','target':t,'type':'tog1: governance applicability','label_code':LC[r['label']],'framework_label':r['label'],'basis':r['link_id'],'statement':f"{r['relationship']} ({r['scope']}) [ToG 1 x12 LINKS_X12.csv, as stated]"})
wr(f'{out}/matrix/tog1_links_x12.csv',['link_id','target','relationship','label','scope','graph_node'],lrows)
g=json.load(open(f'{src}/graph/link_graph.json'))
g['version_label']=V44
g['nodes'].append({'id':'TOG1','label':'ToG 1 Constitutional Commitments (x12)','kind':'governance report','note':'Owner-supplied package; gate INDETERMINATE as recorded; charter GAIA-GOV-TOG-001 Proposed, not adopted'})
g['edges']+=edges
g['legend']['tog1']='TG1-* links from ToG 1 x12 LINKS_X12.csv to existing report/track nodes; labels as the package states (all Plausible)'
json.dump(g,open(f'{out}/graph/link_graph.json','w'),indent=1,ensure_ascii=False)
mmd=open(f'{src}/graph/link_graph.mmd').read().rstrip('\n')
mmd+='\n  TOG1[/"ToG 1 Constitutional Commitments (x12)"/]\n'+''.join(f'  TOG1 -.->|"{e["id"]} [{e["label_code"]}]"| {e["target"]}\n' for e in edges)
open(f'{out}/graph/link_graph.mmd','w').write(mmd)
# 6 intersections column by exact category-name match
loc={(r['alchemy'],r['being'],r['phase'],r['lens']):r for r in rd(use('x12/maps/MATRIX_625_LOCAL_INDEX.csv'))}
for c in CY[:-1]: use(f'{c}/maps/MATRIX_625_LOCAL_INDEX.csv')
with open(f'{src}/matrix/intersections_625.csv',encoding='utf-8',newline='') as f: ir=list(csv.reader(f))
hdr=ir[0]+['tog1_x12_local_cell_id','tog1_x12_status','tog1_x12_canonical_id_as_stated']
ix={h:i for i,h in enumerate(ir[0])}; matched=0; outrows=[]
for r in ir[1:]:
    k=(r[ix['alchemy']],r[ix['being']],r[ix['phase']],r[ix['lens']]); l=loc.get(k)
    if l: matched+=1
    outrows.append(r+([l['local_id'],l['status'],l['canonical_id']] if l else ['','','']))
wr(f'{out}/matrix/intersections_625.csv',hdr,outrows)
# 7 changes
ch=[]
for c in CY:
    for r in per[c]:
        ch.append(['claim',r['claim_id'],c,r['label'],(r.get('continuity') or r.get('change_from_baseline') or 'Baseline (first cycle)')])
wr(f'{out}/changes/tog1_changes.csv',['kind','id','tog1_cycle','label','continuity_as_stated'],ch)
# 8 validation
man={}
for c in CY:
    p=subprocess.run(['sha256sum','--check','--quiet','--strict','Provenance/MANIFEST.sha256'],cwd=f'{T}/{c}',capture_output=True,text=True)
    man[c]={'entries':sum(1 for l in open(f'{T}/{c}/Provenance/MANIFEST.sha256') if l.strip()),'result':'PASS' if p.returncode==0 else 'FAIL'}
ids=[x[1] for x in claims]
v={'version':V44,'built_on':V43,'checks':[
 {'id':'T1','check':'Each ToG 1 cycle Provenance/MANIFEST.sha256 verifies','result':'PASS' if all(m['result']=='PASS' for m in man.values()) else 'FAIL','detail':man},
 {'id':'T2','check':'Claim IDs unique across all five cycles','result':'PASS' if len(ids)==len(set(ids)) else 'FAIL','value':len(ids)},
 {'id':'T3','check':'Every claim label is one of the four framework labels','result':'PASS' if all(x[4] in LABELS for x in claims) else 'FAIL'},
 {'id':'T4','check':'Every x12 local 625 tuple matches exactly one v43 intersection by category names','result':'PASS' if matched==625 and len(loc)==625 else 'FAIL','value':matched},
 {'id':'T5','check':'Every graph edge added resolves to an existing v43 node','result':'PASS' if all(e['target'] in {n['id'] for n in g['nodes']} for e in edges) else 'FAIL','value':len(edges)},
 {'id':'T6','check':'All 625 x12 local tuples remain UNPLACED (no placement asserted)','result':'PASS' if all(l['status']=='UNPLACED' for l in loc.values()) else 'FAIL'},
 {'id':'T7','check':'v43 base files copied byte-identical','result':'PASS' if all(sha(f'{src}/{r}')==sha(f'{out}/{r}') for r in copied) else 'FAIL','value':len(copied)}],
 'unresolved_links_not_added':[r[0] for r in lrows if r[5].startswith('no node')],
 'inputs_sha256':inputs,
 'scope':'Grok Bot self-check of the overlay only. Not independent review. ToG 1 gate stays INDETERMINATE as recorded.'}
json.dump(v,open(f'{out}/validation/tog1_intake.json','w'),indent=1,ensure_ascii=False)
print(json.dumps({k['id']:k['result'] for k in v['checks']}),len(edges),'edges',len(claims),'claims',len(copied),'copied', 'unresolved',len(v['unresolved_links_not_added']))

# 9 manifest (all files except itself), paths relative to the version folder
ents=[]
for dp,_,fs in os.walk(out):
    for f in fs:
        rel=os.path.relpath(f'{dp}/{f}',out)
        if rel!='MANIFEST.sha256': ents.append((rel,sha(f'{out}/{rel}')))
with open(f'{out}/MANIFEST.sha256','w') as f:
    for rel,h in sorted(ents): f.write(f'{h}  {rel}\n')
print('manifest entries',len(ents))
