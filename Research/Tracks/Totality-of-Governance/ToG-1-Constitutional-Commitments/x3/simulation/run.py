import csv, hashlib, itertools, json, platform, sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

base=Path(__file__).resolve().parent
iteration=int(sys.argv[1])
here=base/f'iter-{iteration}'
out=here/'outputs'
out.mkdir(exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,value): (out/name).write_text(json.dumps(value,indent=2)+'\n')
def gate(states):
    if len(states)<1:return 'INDETERMINATE'
    if any(x not in ('PASS','FAIL','INDETERMINATE') for x in states):raise ValueError('Invalid state')
    if 'FAIL' in states:return 'FAIL'
    if 'INDETERMINATE' in states:return 'INDETERMINATE'
    return 'PASS'
def gate11(states):return gate(states) if len(states)==11 else 'INDETERMINATE'
start=datetime.now(timezone.utc).isoformat()
spec_before=sha(here/'SPEC.md')
input_hashes={}
checks={}
if iteration==1:
    counts=Counter();mismatches=0;unsafe=0;n=0
    with (out/'state_vectors.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['state_vector','actual','oracle'])
        for states in itertools.product(('PASS','FAIL','INDETERMINATE'),repeat=11):
            n+=1;actual=gate11(states)
            oracle='FAIL' if states.count('FAIL') else ('PASS' if states.count('PASS')==11 else 'INDETERMINATE')
            counts[actual]+=1;mismatches+=actual!=oracle;unsafe+=actual=='PASS' and any(x!='PASS' for x in states)
            w.writerow([''.join({'PASS':'P','FAIL':'F','INDETERMINATE':'I'}[x] for x in states),actual,oracle])
    def screen(r):
        if r.get('known_forgery'):return 'FAIL'
        fields_ok=bool(r.get('locator')) and r.get('evidence_version')=='v1' and r.get('evidence_scope')=='tog1-research' and r.get('valid_until',-1)>=100
        if not fields_ok:return 'INDETERMINATE'
        return r.get('state','INDETERMINATE')
    original=[{'clause':f'4.{i}','state':'PASS','locator':f'synthetic://evidence/{i}','evidence_version':'v1','evidence_scope':'tog1-research','valid_until':101,'known_forgery':False} for i in range(1,12)]
    defects=[('missing_locator','locator',''),('expired','valid_until',99),('wrong_scope','evidence_scope','different-scope'),('wrong_version','evidence_version','v0'),('known_forgery','known_forgery',True)]
    cases=[]
    for i in range(11):
        for name,field,val in defects:
            records=[dict(x) for x in original];records[i][field]=val
            states=[screen(x) for x in records]
            cases.append({'id':f'E-{i+1}-{name}','defect':name,'clause':f'4.{i+1}','actual':gate11(states),'expected':'FAIL' if name=='known_forgery' else 'INDETERMINATE'})
    screened=[screen(r) for r in original]
    save('screened_valid.json',{'fictional':True,'records':original,'screened_states':screened,'decision':gate11(screened),'scope':'tog1-research','warning':'Synthetic metadata accepted by assumption; not authenticated evidence'})
    save('defect_fixtures.json',cases)
    bad=False
    try:gate11(['PASS']*10+['BOGUS'])
    except ValueError:bad=True
    checks={'E1':n==177147,'E2':mismatches==0,'E3':dict(counts)=={'PASS':1,'FAIL':175099,'INDETERMINATE':2047},'E4':unsafe==0,'E5':len(cases)==55 and all(x['actual']==x['expected'] for x in cases),'E6':gate11(screened)=='PASS','E7':gate11(['PASS']*10)=='INDETERMINATE' and bad}
    summary={'vector_count':n,'outcomes':dict(counts),'oracle_mismatches':mismatches,'unsafe_passes':unsafe,'defect_fixtures':len(cases),'defect_outcomes':dict(Counter(c['actual'] for c in cases)),'novelty':'Reconstructed rule plus a metadata screen; no original Baseline bytes available'}
elif iteration==2:
    previous=base/'iter-1/outputs/screened_valid.json'
    prior=json.loads(previous.read_text());input_hashes[str(previous.relative_to(base))]=sha(previous)
    previous_record=base/'iter-1/EXECUTION_RECORD.json'
    input_hashes[str(previous_record.relative_to(base))]=sha(previous_record)
    factors=['reviewer_distinct','competence','conflict_clear','review_current','owner_approval','scope_correct']
    counts=Counter();n=0;mismatch=0;unsafe=0;mutant_falsepass=0
    with (out/'review_vectors.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(factors+['actual','oracle','identity_only_mutant'])
        for states in itertools.product(('PASS','FAIL','INDETERMINATE'),repeat=6):
            n+=1;actual=gate(prior['screened_states']+list(states));oracle='FAIL' if 'FAIL' in states else ('PASS' if states.count('PASS')==6 else 'INDETERMINATE')
            mutant='PASS' if states[0]=='PASS' else states[0]
            counts[actual]+=1;mismatch+=actual!=oracle;unsafe+=actual=='PASS' and states.count('PASS')!=6
            mutant_falsepass+=mutant=='PASS' and actual!='PASS'
            w.writerow(list(states)+[actual,oracle,mutant])
    sameauthor=['FAIL']+['PASS']*5
    conflicted=['PASS','PASS','FAIL','PASS','PASS','PASS']
    missingreview=['PASS','PASS','PASS','INDETERMINATE','PASS','PASS']
    checks={'R1':len(prior['screened_states'])==11 and prior['decision']=='PASS' and all(x=='PASS' for x in prior['screened_states']),'R2':n==729,'R3':mismatch==0,'R4':dict(counts)=={'PASS':1,'FAIL':665,'INDETERMINATE':63},'R5':unsafe==0,'R6':gate(sameauthor)!='PASS' and gate(conflicted)!='PASS','R7':mutant_falsepass>0,'R8':gate(missingreview)=='INDETERMINATE'}
    save('ready_state.json',{'fictional':True,'decision':gate(prior['screened_states']+['PASS']*6),'review_factors':dict.fromkeys(factors,'PASS'),'clause_states':prior['screened_states'],'warning':'Fictional all-valid fixture, not owner approval or independent review'})
    summary={'vector_count':n,'outcomes':dict(counts),'oracle_mismatches':mismatch,'unsafe_passes':unsafe,'identity_only_mutant_false_passes':mutant_falsepass,'novelty':'Adds explicit synthetic review/authority conditions to actual iter1 screened fixture'}
elif iteration==3:
    previous=base/'iter-2/outputs/ready_state.json'
    prior=json.loads(previous.read_text());input_hashes[str(previous.relative_to(base))]=sha(previous)
    previous_record=base/'iter-2/EXECUTION_RECORD.json';input_hashes[str(previous_record.relative_to(base))]=sha(previous_record)
    alphabet=('TICK','REVOKE','EXPIRE','CHANGE','REVIEW','APPROVE','INCIDENT')
    def initial():return {'time':0,'version':1,'reviewed_version':1,'approved_version':1,'valid_until':2,'basis_active':True,'incident':False,'review_current':True,'authorization':True}
    def decision(s):
        if not s['basis_active'] or s['incident']:return 'FAIL'
        if s['time']>s['valid_until'] or not s['review_current'] or s['reviewed_version']!=s['version'] or not s['authorization'] or s['approved_version']!=s['version']:return 'INDETERMINATE'
        return 'PASS'
    def event(s,e):
        s=dict(s)
        if e=='TICK':s['time']+=1
        elif e=='REVOKE':s['basis_active']=False;s['authorization']=False
        elif e=='EXPIRE':s['time']=s['valid_until']+1
        elif e=='CHANGE':s['version']+=1;s['review_current']=False;s['authorization']=False
        elif e=='INCIDENT':s['incident']=True;s['review_current']=False;s['authorization']=False
        elif e=='REVIEW':
            if s['basis_active'] and not s['incident']:
                s['review_current']=True;s['reviewed_version']=s['version'];s['valid_until']=s['time']+2
        elif e=='APPROVE':
            if s['basis_active'] and not s['incident'] and s['review_current'] and s['reviewed_version']==s['version'] and s['time']<=s['valid_until']:
                s['authorization']=True;s['approved_version']=s['version']
        if not s['basis_active'] or s['incident'] or s['time']>s['valid_until'] or s['approved_version']!=s['version']:
            s['authorization']=False
        return s
    def runseq(events):
        s=initial();history=[]
        for e in events:s=event(s,e);history.append((dict(s),decision(s)))
        return s,history
    total=0;steps=0;unsafe=0;postbad=0;mismatch=0;counts=Counter();finalcounts=Counter()
    with (out/'lifecycle_traces.jsonl').open('w') as f:
        for seq in itertools.product(alphabet,repeat=4):
            total+=1;s,hist=runseq(seq)
            for st,actual in hist:
                steps+=1;counts[actual]+=1
                allowed=all([st['basis_active'],not st['incident'],st['time']<=st['valid_until'],st['review_current'],st['reviewed_version']==st['version'],st['authorization'],st['approved_version']==st['version']])
                oracle='FAIL' if (not st['basis_active'] or st['incident']) else ('PASS' if allowed else 'INDETERMINATE')
                mismatch+=actual!=oracle;unsafe+=actual=='PASS' and not allowed
                postbad+=actual=='PASS' and (not st['basis_active'] or st['incident'])
            finalcounts[hist[-1][1]]+=1
            f.write(json.dumps({'events':seq,'history':[{'state':st,'decision':d} for st,d in hist]},separators=(',',':'))+'\n')
    def last(seq):return runseq(seq)[1][-1][1]
    mutant1={'fixture':['REVOKE'],'mutant':'PASS','correct':last(['REVOKE'])}
    mutant2={'fixture':['EXPIRE','REVIEW'],'mutant':'PASS','correct':last(['EXPIRE','REVIEW'])}
    checks={'L1':prior['fictional'] and prior['decision']=='PASS','L2':total==2401 and steps==9604,'L3':unsafe==0 and mismatch==0,'L4':postbad==0,'L5':last(['EXPIRE','REVIEW','TICK'])=='INDETERMINATE','L6':last(['EXPIRE','REVIEW','APPROVE'])=='PASS','L7':last(['CHANGE','APPROVE'])=='INDETERMINATE','L8':last(['TICK','TICK','TICK'])=='INDETERMINATE','L9':last(['CHANGE','REVIEW'])=='INDETERMINATE','L10':mutant1['correct']!='PASS' and mutant2['correct']!='PASS'}
    save('mutation_counterexamples.json',[mutant1,mutant2])
    summary={'trace_count':total,'event_steps':steps,'post_event_outcomes':dict(counts),'final_outcomes':dict(finalcounts),'oracle_mismatches':mismatch,'unsafe_passes':unsafe,'post_revocation_or_incident_passes':postbad,'novelty':'Extends static iter2 readiness to bounded time/version/event traces'}
else:raise ValueError('Iteration must be1,2,3')
summary['checks']={k:'PASS' if v else 'FAIL' for k,v in checks.items()}
summary['scope']='Synthetic consistency testing only; no independent review or real-world authorization'
save('results.json',summary)
record={'id':f'TOG1-X3-RUN-{iteration}','iteration':iteration,'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'seed':None,'deterministic':True,'spec_before_sha256':spec_before,'spec_after_sha256':sha(here/'SPEC.md'),'runner_sha256':sha(Path(__file__)),'input_sha256':input_hashes,'output_sha256':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file()},'checks':summary['checks'],'same_author':True,'independent_review':False,'research_gate':'INDETERMINATE','real_authorization':False}
(here/'EXECUTION_RECORD.json').write_text(json.dumps(record,indent=2)+'\n')
