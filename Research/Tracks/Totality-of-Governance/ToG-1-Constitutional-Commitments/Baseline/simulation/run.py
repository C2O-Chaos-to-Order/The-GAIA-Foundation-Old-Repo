import csv, hashlib, itertools, json, platform, sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

base=Path(__file__).resolve().parent
out=base/'outputs'
out.mkdir(exist_ok=True)
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def aggregate(states):
    if len(states)!=11: return 'INDETERMINATE'
    if any(s not in ('PASS','FAIL','INDETERMINATE') for s in states): raise ValueError('Invalid control state')
    if 'FAIL' in states: return 'FAIL'
    if 'INDETERMINATE' in states: return 'INDETERMINATE'
    return 'PASS'
def identity(author, reviewer):
    return 'PASS' if author and reviewer and author.strip() and reviewer.strip() and author.strip().casefold()!=reviewer.strip().casefold() else 'INDETERMINATE'
start=datetime.now(timezone.utc).isoformat()
before=digest(base/'SPEC.md')
counts=Counter(); mismatch=0; unsafe=0; encoded=set(); total=0
with (out/'exhaustive.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['state_vector_PFI','model_decision','oracle_decision'])
    for states in itertools.product(('PASS','FAIL','INDETERMINATE'), repeat=11):
        total+=1
        result=aggregate(states)
        oracle='FAIL' if states.count('FAIL')>0 else ('PASS' if states.count('PASS')==11 else 'INDETERMINATE')
        mismatch+=result!=oracle
        unsafe+=result=='PASS' and any(s!='PASS' for s in states)
        counts[result]+=1
        code=''.join({'PASS':'P','FAIL':'F','INDETERMINATE':'I'}[s] for s in states)
        encoded.add(code); w.writerow([code,result,oracle])
fixtures=[]
for token in ('FAIL','INDETERMINATE'):
    for i in range(11):
        states=['PASS']*11; states[i]=token
        fixtures.append({'id':f'{token}-{i+1:02d}','states':states,'expected':token,'actual':aggregate(states)})
unknown=['PASS']*10+['INDETERMINATE']
failed=['PASS']*10+['FAIL']
ignore_unknown=lambda s: 'FAIL' if 'FAIL' in s else 'PASS'
majority=lambda s: 'PASS' if s.count('PASS')>len(s)//2 else 'FAIL'
mutants={'ignore_unknown_rejected':ignore_unknown(unknown)!=aggregate(unknown),'majority_rejected':majority(failed)!=aggregate(failed)}
invalid_raised=False
try: aggregate(['PASS']*10+['BOGUS'])
except ValueError: invalid_raised=True
identity_fixtures=[('agent-a','agent-a','INDETERMINATE'),('agent-a',' AGENT-A ','INDETERMINATE'),('agent-a','','INDETERMINATE'),('','reviewer-b','INDETERMINATE'),('agent-a','reviewer-b','PASS')]
checks={
'V1':total==177147 and len(encoded)==177147,
'V2':mismatch==0,
'V3':counts['PASS']==1,
'V4':unsafe==0,
'V5':dict(counts)=={'PASS':1,'INDETERMINATE':2047,'FAIL':175099},
'V6':len(fixtures)==22 and all(x['actual']==x['expected'] for x in fixtures),
'V7':aggregate(['PASS']*10)=='INDETERMINATE' and invalid_raised,
'V8':all(aggregate(unknown)=='INDETERMINATE' for _ in range(12)),
'V9':all(mutants.values()),
'V10':aggregate(['PASS']*9+['FAIL','INDETERMINATE'])=='FAIL',
'V11':all(identity(a,b)==expected for a,b,expected in identity_fixtures),
'V12':before==digest(base/'SPEC.md')}
summary={'vectors':total,'outcomes':dict(counts),'oracle_mismatches':mismatch,'unsafe_passes':unsafe,'checks':{k:'PASS' if v else 'FAIL' for k,v in checks.items()},'mutation_controls':mutants,'fixtures':fixtures,'identity_fixtures':[{'author':a,'reviewer':b,'expected':e,'actual':identity(a,b)} for a,b,e in identity_fixtures],'empirical_validation':False,'independent_review':False,'research_gate':'INDETERMINATE'}
(out/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
record={'execution_id':'GAIA-RES-TOG1-C0-RUN-001','baseline_executions':1,'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'seed':None,'deterministic':True,'spec_sha256':before,'spec_after_sha256':digest(base/'SPEC.md'),'script_sha256':digest(Path(__file__)),'outputs':{p.name:digest(p) for p in sorted(out.iterdir()) if p.is_file()},'test_results':summary['checks'],'independent_rerun':'NOT PERFORMED','gate_authorization':'NOT GRANTED'}
(base/'EXECUTION_RECORD.json').write_text(json.dumps(record,indent=2)+'\n')
