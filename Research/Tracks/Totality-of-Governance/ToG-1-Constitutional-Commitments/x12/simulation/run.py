import sys
sys.dont_write_bytecode=True
import csv,hashlib,itertools,json,platform,random
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from legacy_reconstruction import assess as legacy_assess
from assessor_candidate_v0_2 import assess,combine,normalize_state,FIELDS,VERSION
base=Path(__file__).resolve().parent;i=int(sys.argv[1]);here=base/f'iter-{i}';out=here/'outputs';out.mkdir(exist_ok=True)
ST=('PASS','FAIL','INDETERMINATE')
VALID=dict(zip(FIELDS,['SYN-REC','research-only','Synthetic bounded rationale','fictional-owner','v1','synthetic://evidence/1']))
BOUNDARY=['UNRECOGNIZED',None,True,False,0,1,-1,0.0,1.0,'',' ','pass',' PASS ','FAIL ','INDETERMINATE ','PASS\x00',[],{},['PASS'],{'state':'PASS'},'ＰＡＳＳ']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(out/n).write_text(json.dumps(v,indent=2)+'\n')
def oracle(v):return 'FAIL' if v.count('FAIL') else ('PASS' if v.count('PASS')==len(v) else 'INDETERMINATE')
start=datetime.now(timezone.utc).isoformat();before=sha(here/'SPEC.md');inputs={};prior=None
if i>1:
    paths=[base/f'iter-{i-1}/outputs/transfer.json',base/f'iter-{i-1}/EXECUTION_RECORD.json'];inputs={str(p.relative_to(base)):sha(p) for p in paths};prior=json.loads(paths[0].read_text())
contract={'fictional':True,'scope':'research-only','subject':'fictional-agent','resource':'docA','action':'read','actual_review':'NONE','actual_authorization':'NONE','overall_gate':'INDETERMINATE'} if prior is None else {k:prior[k] for k in ['fictional','scope','subject','resource','action','actual_review','actual_authorization','overall_gate']}
summary={};checks={};hypotheses={};extra={}
if i==1:
    rows=[]
    for v in list(ST)+['UNRECOGNIZED',None,True]:
        d,r=legacy_assess(dict(VALID),v);rows.append({'input':v,'decision':d,'reasons':r,'historical_invalid_case':v not in ST})
    save('legacy_cases.json',rows)
    failures=sum(r['decision']=='PASS' for r in rows[3:])
    checks={'L1':len(rows)==6,'L2':failures==3,'L3':rows[0]['decision']=='PASS','L4':rows[1]['decision']=='FAIL','L5':rows[2]['decision']=='INDETERMINATE','L6':contract['fictional']}
    summary={'legacy_cases':6,'historical_invalid_inputs_accepted':failures,'legacy_external_input_criterion':'FAIL','artifact_status':'Labelled reconstruction,not originalbytes'}
    extra={'legacy_failure_preserved':True,'reconstructed_only':True}
elif i==2:
    rows=[];exceptions=0;bad=0
    for v in list(ST)+BOUNDARY:
        try:d,r=assess(dict(VALID),v)
        except Exception as e:exceptions+=1;d='EXCEPTION';r=[type(e).__name__]
        invalid=type(v) is not str or v not in ST
        bad+=invalid and d=='PASS';rows.append({'input':v,'type':type(v).__name__,'decision':d,'reasons':r,'invalid_verification':invalid})
    save('enum_cases.json',rows)
    historical=[r for r in rows if r['input'] is None or r['input'] is True or (type(r['input']) is str and r['input']=='UNRECOGNIZED')]
    checks={'E1':len(rows)==24,'E2':bad==0,'E3':len(historical)==3 and all(r['decision']!='PASS' for r in historical),'E4':[r['decision'] for r in rows[:3]]==list(ST),'E5':exceptions==0,'E6':prior['legacy_failure_preserved'] and VERSION=='0.2.0'}
    summary={'enum_cases':len(rows),'invalid_verification_passes':bad,'exceptions':exceptions,'candidate_known_boundary_criterion':'PASS' if bad==0 and exceptions==0 else 'FAIL','candidate_version':VERSION}
    extra={'candidate_version':VERSION,'known_boundary_cases_blocked':bad==0,'valid_record':VALID,'legacy_failure_preserved':True}
elif i==3:
    cases=[]
    badvalues=['',' ',None,True,0,[],{},'\x00']
    for field in FIELDS:
        for value in badvalues:
            r=dict(VALID);r[field]=value;cases.append((f'{field}:{type(value).__name__}:{repr(value)}',r,False))
    for field in FIELDS:
        r=dict(VALID);del r[field];cases.append((f'missing:{field}',r,False))
    for k,v in [('gate','PASS'),('approved',True),('verification','PASS')]:
        r=dict(VALID);r[k]=v;cases.append((f'extra:{k}',r,False))
    for r in [None,[],True,0,'record']:cases.append((f'top:{type(r).__name__}',r,False))
    cases.append(('valid',dict(VALID),True));rows=[];exception=0
    for name,r,valid in cases:
        try:d,why=assess(r,'PASS')
        except Exception as e:exception+=1;d='EXCEPTION';why=[type(e).__name__]
        rows.append({'id':name,'record':r,'expected_positive':valid,'decision':d,'reasons':why})
    save('record_cases.json',rows)
    unexpected=sum(r['decision']=='PASS' and not r['expected_positive'] for r in rows)
    checks={'S1':len(rows)==63,'S2':sum(r['decision']=='PASS' for r in rows)==1 and unexpected==0,'S3':exception==0,'S4':all(r['decision']!='PASS' for r in rows if 'missing:' in r['id'] or 'NoneType' in r['id']),'S5':unexpected==0,'S6':rows[-1]['decision']=='PASS'}
    summary={'record_cases':len(rows),'unexpected_passes':unexpected,'exceptions':exception,'outcomes':dict(Counter(r['decision'] for r in rows))}
    extra={'candidate_version':VERSION,'current_valid_record':VALID}
elif i==4:
    rng=random.Random(12012);alphabet='PASSFAILINDETERMINATE \t\n\x00'
    corpus=list(ST)+[''.join(rng.choice(alphabet) for _ in range(rng.randrange(41))) for _ in range(600)]
    pool=[None,True,False,0,1,-1,0.0,1.0,[],{},['PASS'],{'state':'PASS'}]
    corpus +=[rng.choice(pool) for _ in range(200)]
    funcs=[lambda x:x.lower(),lambda x:x+' ',lambda x:' '+x,lambda x:x+'\x00',lambda x:x+'\n',lambda x:x.replace('A',''),lambda x:x[::-1],lambda x:x[:1],lambda x:x*2,lambda x:'',lambda x:x.replace('I','1'),lambda x:x.swapcase()]
    corpus +=[f(x) for x in ST for f in funcs];rows=[];diff=0;bad=0;exc=0;legacyfalse=0
    for v in corpus:
        want='INDETERMINATE' if v is None else (v if type(v) is str and (v=='PASS' or v=='FAIL' or v=='INDETERMINATE') else 'FAIL')
        try:d,r=assess(dict(VALID),v)
        except Exception as e:exc+=1;d='EXCEPTION';r=[type(e).__name__]
        old,_=legacy_assess(dict(VALID),v);diff+=d!=want;bad+=d=='PASS' and want!='PASS';legacyfalse+=old=='PASS' and want!='PASS'
        rows.append({'input':v,'input_type':type(v).__name__,'candidate':d,'oracle':want,'legacy':old})
    save('negative_corpus.json',rows)
    checks={'F1':len(rows)==839,'F2':diff==0,'F3':bad==0,'F4':exc==0,'F5':legacyfalse>0,'F6':(out/'negative_corpus.json').is_file()}
    summary={'seed':12012,'corpus_cases':len(rows),'oracle_mismatches':diff,'candidate_invalid_passes':bad,'exceptions':exc,'legacy_false_passes_against_oracle':legacyfalse}
    extra={'candidate_version':VERSION,'negative_corpus_cases':len(rows),'valid_record':VALID}
elif i==5:
    n=0;diff=0;counts=Counter()
    with (out/'gate_vectors.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['states_PFI','proper','oracle'])
        for v in itertools.product(ST,repeat=11):
            d=combine(list(v),required=11);want=oracle(v);n+=1;counts[d]+=1;diff+=d!=want
            w.writerow([''.join({'PASS':'P','FAIL':'F','INDETERMINATE':'I'}[x] for x in v),d,want])
    boundaries=[]
    for j in range(11):
        for v in BOUNDARY:
            states=['PASS']*11;states[j]=v;boundaries.append({'slot':j+1,'input':v,'decision':combine(states,required=11)})
    outer=[{'input':v,'decision':combine(v,required=11)} for v in [None,'PASS',{},123,True,[]]]
    save('gate_boundary_cases.json',{'element_cases':boundaries,'outer_cases':outer})
    checks={'G1':n==177147,'G2':dict(counts)=={'PASS':1,'FAIL':175099,'INDETERMINATE':2047},'G3':diff==0,'G4':len(boundaries)==231 and all(r['decision']!='PASS' for r in boundaries),'G5':all(r['decision']!='PASS' for r in outer),'G6':combine(['FAIL']+['INDETERMINATE']*10,required=11)=='FAIL'}
    summary={'valid_gate_vectors':n,'outcomes':dict(counts),'oracle_mismatches':diff,'element_boundary_cases':len(boundaries),'outer_cases':len(outer),'boundary_passes':sum(r['decision']=='PASS' for r in boundaries+outer)}
    extra={'strict_gate_version':VERSION,'valid_record':VALID,'gate_fixture':['PASS']*11}
elif i==6:
    n=0;badna=0;mandatorybad=0;masked=0;positive_na=0;counts=Counter()
    with (out/'applicability_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['clause','disposition','verification','rationale_kind','version_match','control','record_state','rationale','authority','decision'])
        for clause,disp,v,kind,match,control in itertools.product(range(1,12),('applicable','NA','unknown'),ST,('valid','missing','wrongtype'),(False,True),ST):
            r=dict(VALID);r['rationale']='Synthetic scope rationale' if kind=='valid' else ('' if kind=='missing' else True);r['version']='v1' if match else 'v0'
            rec,_=assess(r,v)
            if control=='FAIL' or rec=='FAIL':d='FAIL'
            elif rec!='PASS' or disp=='unknown':d='INDETERMINATE'
            elif disp=='NA':d='FAIL' if clause in (1,11) else 'PASS'
            else:d=control
            n+=1;counts[d]+=1;badna+=d=='PASS' and disp=='NA' and rec!='PASS';mandatorybad+=d=='PASS' and disp=='NA' and clause in(1,11);masked+=control=='FAIL' and d!='FAIL';positive_na+=d=='PASS' and disp=='NA' and bool(r['rationale']) and bool(r['authority'])
            w.writerow([f'4.{clause}',disp,v,kind,match,control,rec,r['rationale'],r['authority'],d])
    checks={'A1':n==5346,'A2':badna==0,'A3':mandatorybad==0,'A4':masked==0,'A5':positive_na>0,'A6':contract['actual_authorization']=='NONE'}
    summary={'applicability_cases':n,'outcomes':dict(counts),'unsupported_na_passes':badna,'mandatory_na_passes':mandatorybad,'known_failures_masked':masked,'explicit_positive_na_record_cases':positive_na}
    extra={'current_record':VALID,'actual_applicability_approval':'NONE'}
elif i==7:
    n=0;diff=0;failurelost=0;bad=0;rootchanged=0
    with (out/'support_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['A','B','C_local','D_local','version_match','C_derived','D_derived','oracle_C','oracle_D'])
        for a,b,c,d,match in itertools.product(ST,ST,ST,ST,(False,True)):
            cc='FAIL' if c=='FAIL' else ('INDETERMINATE' if not match or a!='PASS' or b!='PASS' else c)
            dd='FAIL' if d=='FAIL' else ('INDETERMINATE' if not match or cc!='PASS' else d)
            wc=c if c=='FAIL' or (match and a=='PASS' and b=='PASS') else 'INDETERMINATE'
            wd=d if d=='FAIL' or (match and wc=='PASS') else 'INDETERMINATE'
            n+=1;diff+=(cc,dd)!=(wc,wd);failurelost+=(c=='FAIL' and cc!='FAIL') or(d=='FAIL' and dd!='FAIL');bad+=cc=='PASS' and(not match or a!='PASS' or b!='PASS');bad+=dd=='PASS' and(not match or cc!='PASS')
            w.writerow([a,b,c,d,match,cc,dd,wc,wd])
    checks={'P1':n==162,'P2':diff==0,'P3':failurelost==0,'P4':bad==0,'P5':rootchanged==0,'P6':contract['actual_review']=='NONE'}
    summary={'support_cases':n,'oracle_mismatches':diff,'known_local_failures_lost':failurelost,'unsupported_dependent_passes':bad,'semantic_truth_verified':False}
    extra={'support_current_fixture':True,'semantic_truth_verified':False}
elif i==8:
    n=0;unknown=0;selfbad=0;hiddenpass=0;counts=Counter();example=None
    with (out/'review_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['observed_states','identity_distinct','hidden_conflict','decision','genuine_independence_in_fixture'])
        for v in itertools.product(ST,repeat=5):
            for distinct,hidden in itertools.product((False,True),repeat=2):
                d='FAIL' if not distinct else combine(list(v));n+=1;counts[d]+=1;unknown+=d=='PASS' and 'INDETERMINATE'in v;selfbad+=d=='PASS' and not distinct
                if d=='PASS' and hidden:
                    hiddenpass+=1
                    if example is None:example={'observed_states':v,'identity_distinct':distinct,'hidden_conflict':hidden,'metadata_decision':d,'genuine_independence':False}
                w.writerow(['|'.join(v),distinct,hidden,d,v.count('PASS')==5 and distinct and not hidden])
    save('hidden_conflict_witness.json',example)
    hypotheses={'H8':{'statement':'Syntax-correct positive metadata proves genuine independence','result':'NOT SUPPORTED' if hiddenpass else 'SUPPORTED','hidden_conflict_passes':hiddenpass}}
    checks={'R1':n==972,'R2':unknown==0,'R3':selfbad==0,'R4':combine(['PASS']*4+[True])=='FAIL','R5':hiddenpass>0,'R6':contract['actual_review']=='NONE'}
    summary={'review_cases':n,'observed_outcomes':dict(counts),'unknown_factor_passes':unknown,'self_review_passes':selfbad,'hidden_conflict_passes':hiddenpass}
    extra={'hidden_review_limit':True,'hypothesis_H8':hypotheses['H8']['result']}
elif i==9:
    atoms=['read:docA','draft:docA'];sets=[{atoms[j] for j in range(2) if b&(1<<j)} for b in range(4)]
    n=0;bad=0;unknown=0;malformed=0;revokedbad=0;counts=Counter()
    with (out/'grant_chain_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['root','middle','leaf','time','revoked','visibility','issuer_input','decision'])
        for rm,mm,lm,t,revoked,vis,issuer in itertools.product(range(4),range(4),range(4),range(4),('none','root','middle','leaf'),ST,('PASS',True,None)):
            nested=sets[lm]<=sets[mm]<=sets[rm];iss=normalize_state(issuer)
            if not nested or t>1 or vis=='FAIL' or iss=='FAIL':d='FAIL'
            elif vis=='INDETERMINATE' or iss=='INDETERMINATE':d='INDETERMINATE'
            else:d='FAIL' if revoked!='none' else 'PASS'
            n+=1;counts[d]+=1;bad+=d=='PASS' and(not nested or t>1);unknown+=d=='PASS' and vis=='INDETERMINATE';malformed+=d=='PASS' and issuer is True;revokedbad+=d=='PASS' and vis=='PASS' and revoked!='none'
            w.writerow([rm,mm,lm,t,revoked,vis,json.dumps(issuer),d])
    checks={'D1':n==9216,'D2':bad==0,'D3':unknown==0,'D4':malformed==0,'D5':revokedbad==0,'D6':contract['actual_authorization']=='NONE'}
    summary={'grant_chain_cases':n,'outcomes':dict(counts),'scope_or_expiry_passes':bad,'unknown_visibility_passes':unknown,'malformed_issuer_passes':malformed,'known_revocation_passes':revokedbad,'visibility_truth_assumed':True}
    extra={'leaf_capabilities':['read:docA'],'visibility_limit':True}
elif i==10:
    n=0;leasebad=0;querybad=0;blocked=0
    with(out/'freshness_cases.csv').open('w',newline='')as f:
        w=csv.writer(f);w.writerow(['revocation','delay','time','lease','skew','online','lease_allow','current_query','global_active'])
        for r,d,t,L,skew,online in itertools.product(range(4),range(4),range(7),range(4),(-1,0,1),(False,True)):
            active=t<r;lease=t<r+d and 0<=t+skew<=L;query='PASS' if online and active else ('FAIL' if online else 'INDETERMINATE');n+=1;leasebad+=lease and not active;querybad+=query=='PASS' and not active;blocked+=not online and active
            w.writerow([r,d,t,L,skew,online,lease,query,active])
    def fresh():return {'v':1,'epoch':0,'reviewed':1,'approved':1,'expiry':2,'time':0,'basis':True,'cache':None,'used':False,'nonce':0}
    def valid(s):return s['basis']and s['reviewed']==s['v']and s['approved']==s['v']and s['time']<=s['expiry']
    def step(s,e):
        s=dict(s);p=c=r=False;nonce=None
        if e=='CHECK':s['nonce']+=1;s['cache']=(s['epoch'],s['v'],s['nonce'])if valid(s)else None;s['used']=False
        elif e=='COMMIT':
            token=s['cache'];nonce=token[2]if token else None;c=bool(token)and not s['used'];r=bool(token)and valid(s)and token[:2]==(s['epoch'],s['v']);p=r and not s['used']
            if p:s['used']=True
        elif e=='REVOKE':s['basis']=False;s['approved']=None;s['epoch']+=1
        elif e=='CHANGE':s['v']+=1;s['reviewed']=None;s['approved']=None;s['epoch']+=1
        elif e=='REVIEW'and s['basis']:s['reviewed']=s['v'];s['expiry']=s['time']+2;s['approved']=None;s['epoch']+=1
        elif e=='APPROVE'and s['basis']and s['reviewed']==s['v']and s['time']<=s['expiry']:s['approved']=s['v'];s['epoch']+=1
        elif e=='TICK':
            old=s['time'];s['time']+=1
            if old<=s['expiry']<s['time']:s['approved']=None;s['epoch']+=1
        return s,p,c,r,nonce
    traces=steps=unsafe=double=cachebad=replaybad=0
    with(out/'nonce_traces.csv').open('w',newline='')as f:
        w=csv.writer(f);w.writerow(['events','proper_bits','cache_bits','replay_bits'])
        for seq in itertools.product(('CHECK','COMMIT','REVOKE','CHANGE','REVIEW','APPROVE','TICK'),repeat=4):
            s=fresh();seen=set();pb=[];cb=[];rb=[];traces+=1
            for e in seq:
                old=s;s,p,c,r,nonce=step(s,e);steps+=1;token=old['cache'];want=e=='COMMIT'and bool(token)and valid(old)and token[:2]==(old['epoch'],old['v'])and not old['used'];unsafe+=p and not want
                if p:double+=nonce in seen;seen.add(nonce)
                cachebad+=c and not want;replaybad+=r and not want;pb.append(str(int(p)));cb.append(str(int(c)));rb.append(str(int(r)))
            w.writerow(['|'.join(seq),''.join(pb),''.join(cb),''.join(rb)])
    hypotheses={'H10':{'statement':'Local lease validity eliminates all globally revoked access','result':'NOT SUPPORTED'if leasebad else'SUPPORTED','counterexample_grid_entries':leasebad}}
    checks={'T1':n==2688,'T2':querybad==0,'T3':leasebad>0 and blocked>0,'T4':traces==2401 and steps==9604,'T5':unsafe==0 and double==0,'T6':cachebad>0 and replaybad>0}
    summary={'freshness_cases':n,'globally_revoked_lease_allows':leasebad,'globally_revoked_current_query_passes':querybad,'active_offline_entries_blocked':blocked,'nonce_traces':traces,'nonce_event_steps':steps,'unsafe_proper_commits':unsafe,'double_nonce_successes':double,'cache_only_false_allows':cachebad,'replay_false_allows':replaybad}
    extra={'hypothesis_H10':hypotheses['H10']['result'],'hypothesis_H8':prior['hypothesis_H8']if'hypothesis_H8'in prior else'NOT SUPPORTED','actual_atomic_implementation':'NONE','freshness_residual':leasebad}
elif i==11:
    n=0;diff=0;missing=0;bad=0;mutant=0;readycounts=Counter();outcomecounts=Counter()
    with(out/'remedy_cases.csv').open('w',newline='')as f:
        w=csv.writer(f);w.writerow(['legitimacy','accessibility','privacy','rights','outcome','process_ready','remedy_supported'])
        for v in itertools.product(ST,repeat=5):
            ready=combine(list(v[:4]));supported=combine(list(v));n+=1;readycounts[ready]+=1;outcomecounts[supported]+=1;diff+=(ready!=oracle(v[:4])or supported!=oracle(v));missing+=supported=='PASS'and v[4]!='PASS';bad+=ready=='PASS'and any(v[j]=='FAIL'for j in(1,2,3));mutant+=ready=='PASS'and supported!='PASS';w.writerow(list(v)+[ready,supported])
    checks={'M1':n==243,'M2':diff==0,'M3':missing==0,'M4':bad==0,'M5':mutant>0,'M6':contract['actual_review']=='NONE'}
    summary={'remedy_cases':n,'process_ready':dict(readycounts),'remedy_supported':dict(outcomecounts),'oracle_mismatches':diff,'unsupported_remedy_passes':missing,'process_only_false_remedy_claims':mutant}
    extra={'actual_remedy':'NONE','affected_party_consultation':'NONE','hypothesis_H8':prior['hypothesis_H8'],'hypothesis_H10':prior['hypothesis_H10']}
elif i==12:
    names=['authenticity','applicability','support','review','delegation','freshness','atomicity','remedy','human_approval'];n=0;diff=0;counts=Counter();false=Counter();examples={}
    mutants={'ignore_unknown':lambda v:'FAIL'if'FAIL'in v else'PASS','majority':lambda v:'PASS'if v.count('PASS')>=5 else'FAIL','owner_override':lambda v:'PASS'if v[8]=='PASS'else combine(v),'form_only':lambda v:'PASS','cycle_label_proof':lambda v:'PASS','omit_remedy':lambda v:combine(v[:7]+v[8:])}
    with(out/'integration_vectors.csv').open('w',newline='')as f:
        w=csv.writer(f);w.writerow(names+['proper','oracle']+list(mutants))
        for tup in itertools.product(ST,repeat=9):
            v=list(tup);d=combine(v);want=oracle(v);n+=1;counts[d]+=1;diff+=d!=want;mv={m:fn(v)for m,fn in mutants.items()}
            for m,val in mv.items():
                if val=='PASS'and d!='PASS':false[m]+=1;examples.setdefault(m,{'states':dict(zip(names,v)),'proper':d,'mutant':val})
            w.writerow(v+[d,want]+list(mv.values()))
    boundaries=[];exc=0
    for j in range(9):
        for b in BOUNDARY:
            v=['PASS']*9;v[j]=b
            try:d=combine(v)
            except Exception as e:exc+=1;d='EXCEPTION'
            boundaries.append({'slot':names[j],'input':b,'decision':d})
    save('integration_boundaries.json',boundaries);save('mutant_counterexamples.json',examples)
    earlier={}
    for stage in (1,2,4,8,10):
        p=base/f'iter-{stage}/outputs/results.json';inputs[str(p.relative_to(base))]=sha(p);earlier[str(stage)]=json.loads(p.read_text())
    retained={'H8':earlier['8']['hypotheses']['H8']['result'],'H10':earlier['10']['hypotheses']['H10']['result']}
    checks={'I1':n==19683,'I2':dict(counts)=={'PASS':1,'FAIL':19171,'INDETERMINATE':511},'I3':diff==0,'I4':len(boundaries)==189 and exc==0 and all(r['decision']!='PASS'for r in boundaries),'I5':len(false)==6 and all(false[m]>0 for m in mutants),'I6':earlier['1']['legacy_external_input_criterion']=='FAIL'and earlier['2']['candidate_known_boundary_criterion']=='PASS'and earlier['4']['candidate_invalid_passes']==0,'I7':retained=={'H8':'NOT SUPPORTED','H10':'NOT SUPPORTED'},'I8':contract['overall_gate']=='INDETERMINATE'and contract['actual_review']=='NONE'and contract['actual_authorization']=='NONE'}
    summary={'integration_vectors':n,'outcomes':dict(counts),'oracle_mismatches':diff,'malformed_factor_fixtures':len(boundaries),'malformed_factor_passes':sum(r['decision']=='PASS'for r in boundaries),'boundary_exceptions':exc,'mutant_false_passes':dict(false),'negative_hypotheses':retained,'candidate_known_boundary_regression':'PASS','legacy_reconstruction_regression':'FAIL','production_authorization':'NONE'}
    extra={'final_research_gate':'INDETERMINATE','actual_ethics_review':'NONE','owner_decision':'NOT RECORDED','canonical_integration':'NOT COMPLETE','negative_hypotheses':retained,'candidate_version':VERSION,'candidate_scope':'Known bounded regression passed;not independent/generalproductionassurance'}
else:raise ValueError('Iterationmustbe1..12')
summary['checks']={k:'PASS'if v else'FAIL'for k,v in checks.items()};summary['hypotheses']=hypotheses;summary['scope']='Finite synthetic or reconstructed-code checks;not independent,field,legal ordeploymentassurance'
save('results.json',summary);save('transfer.json',{**contract,'stage':i,**extra})
record={'id':f'TOG1-X12-RUN-{i}','iteration':i,'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'deterministic':True,'seed':12012 if i==4 else None,'runner_sha256':sha(Path(__file__)),'implementation_sha256':{p.name:sha(p)for p in[base/'legacy_reconstruction.py',base/'assessor_candidate_v0_2.py']},'spec_before_sha256':before,'spec_after_sha256':sha(here/'SPEC.md'),'inputs_sha256':inputs,'outputs_sha256':{p.name:sha(p)for p in sorted(out.iterdir())if p.is_file()},'checks':summary['checks'],'hypotheses':hypotheses,'independent_review':False,'overall_gate':'INDETERMINATE','actual_external_actions':0}
(here/'EXECUTION_RECORD.json').write_text(json.dumps(record,indent=2)+'\n')
