import sys,json
from pathlib import Path
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'simulation'))
from legacy_reconstruction import assess as old
from assessor_candidate_v0_2 import assess as new
r={'record_id':'SYN','scope':'research-only','rationale':'Synthetic scope','authority':'fictional-owner','version':'v1','evidence_ref':'synthetic://evidence/1'}
rows=[]
for value in ['UNRECOGNIZED',None,True]:
    legacy,_=old(dict(r),value);candidate,reasons=new(dict(r),value)
    rows.append({'input':value,'legacy':legacy,'candidate':candidate,'candidate_reasons':reasons,'known_boundary_blocks_pass':candidate!='PASS'})
print(json.dumps(rows,indent=2))
raise SystemExit(0 if all(row['known_boundary_blocks_pass'] for row in rows) else 1)
