import csv, hashlib, itertools, json, platform, sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
base=Path(__file__).resolve().parent
i=int(sys.argv[1]);here=base/f'iter-{i}';out=here/'outputs';out.mkdir(exist_ok=True)
ST=('PASS','FAIL','INDETERMINATE')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(out/n).write_text(json.dumps(v,indent=2)+'\n')
def gate(v):return 'FAIL' if 'FAIL' in v else ('INDETERMINATE' if 'INDETERMINATE' in v else 'PASS')
def oracle(v):return 'PASS' if v.count('PASS')==len(v) else ('FAIL' if v.count('FAIL') else 'INDETERMINATE')
start=datetime.now(timezone.utc).isoformat();specbefore=sha(here/'SPEC.md');inputs={};prior=None
if i>1:
    paths=[base/f'iter-{i-1}/outputs/transfer.json',base/f'iter-{i-1}/EXECUTION_RECORD.json']
    inputs={str(p.relative_to(base)):sha(p) for p in paths};prior=json.loads(paths[0].read_text())
contract={'fictional':True,'scope':'research-only','subject':'fictional-agent','resource':'docA','action':'read','actual_review':'NONE','actual_authorization':'NONE','overall_gate':'INDETERMINATE'} if prior is None else {k:prior[k] for k in ['fictional','scope','subject','resource','action','actual_review','actual_authorization','overall_gate']}
checks={};summary={};hypotheses={};extra={}
if i==1:
    fields=['record_id','scope','rationale','authority','version','evidence_ref']
    valid=dict(zip(fields,['SYN-REC-1','research-only','Synthetic bounded scope determination','fictional-owner','v1','synthetic://record/1']))
    def assess(r,verification):
        reasons=[f'{k}:missing_or_invalid_type' for k in fields if not isinstance(r.get(k),str) or not r.get(k,'').strip()]
        if r.get('scope')!='research-only':reasons.append('scope_mismatch')
        if r.get('version')!='v1':reasons.append('version_mismatch')
        result='FAIL' if verification=='FAIL' else ('INDETERMINATE' if reasons or verification=='INDETERMINATE' else 'PASS')
        return result,reasons
    n=0;unsafe=0;unk=0;forgery=0;counts=Counter()
    with (out/'record_cases.jsonl').open('w') as f:
        for present in itertools.product((False,True),repeat=6):
            r={k:valid[k] for k,p in zip(fields,present) if p}
            for v in ST:
                actual,reasons=assess(r,v);n+=1;counts[actual]+=1
                unsafe+=actual=='PASS' and (not all(present) or bool(reasons))
                unk+=v=='INDETERMINATE' and actual=='PASS';forgery+=v=='FAIL' and actual!='FAIL'
                f.write(json.dumps({'record':r,'verification':v,'decision':actual,'reasons':reasons},separators=(',',':'))+'\n')
    defects=[('rationale',''),('authority',' '),('scope','production'),('version','v0'),('record_id',1),('rationale',False),('authority',[]),('version',None),('evidence_ref',None),('record_id','')]
    malformed=[]
    for k,val in defects:
        r=dict(valid);r[k]=val;actual,reasons=assess(r,'PASS');malformed.append({'field':k,'value':val,'decision':actual,'reasons':reasons})
    save('malformed_fixtures.json',malformed)
    extra={'decision':'PASS','structured_record':valid,'verification_assumed':'PASS','rationale_quality_not_empirically_verified':True}
    checks={'V1':n==192 and len(malformed)==10,'V2':unsafe==0,'V3':unk==0,'V4':forgery==0,'V5':all(r['decision']!='PASS' and r['reasons'] for r in malformed),'V6':assess(valid,'PASS')[0]=='PASS','V7':contract['fictional'] and contract['scope']=='research-only' and all('reasons' in r for r in malformed)}
    summary={'record_patterns':n,'malformed_fixtures':10,'pattern_outcomes':dict(counts),'invalid_or_missing_passes':unsafe,'unknown_verification_passes':unk,'known_forgery_misclassified':forgery}
elif i==2:
    n=0;diff=0;unsup=0;mandatorybad=0;failedbad=0;counts=Counter()
    with (out/'applicability_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['clause','disposition','authority','rationale_kind','scope_fresh','control_state','rationale_text','authority_record','decision','oracle'])
        for clause,disposition,authority,rationale,fresh,control in itertools.product(range(1,12),('applicable','not_applicable','unknown'),ST,('valid','missing','wrong_scope'),(False,True),ST):
            if control=='FAIL':actual='FAIL'
            elif disposition=='unknown':actual='INDETERMINATE'
            elif disposition=='applicable':actual=control
            elif clause in (1,11) or authority=='FAIL':actual='FAIL'
            elif authority!='PASS' or rationale!='valid' or not fresh:actual='INDETERMINATE'
            else:actual='PASS'
            if control=='FAIL' or (disposition=='not_applicable' and (clause in {1,11} or authority=='FAIL')):want='FAIL'
            elif disposition=='applicable':want=control
            elif disposition=='not_applicable' and all([clause not in {1,11},authority=='PASS',rationale=='valid',fresh]):want='PASS'
            else:want='INDETERMINATE'
            n+=1;counts[actual]+=1;diff+=actual!=want
            unsup+=actual=='PASS' and disposition=='not_applicable' and not (authority=='PASS' and rationale=='valid' and fresh)
            mandatorybad+=actual=='PASS' and disposition=='not_applicable' and clause in (1,11);failedbad+=control=='FAIL' and actual!='FAIL'
            text='Synthetic conditional scope rationale' if rationale=='valid' else ('' if rationale=='missing' else 'Different scope rationale')
            authref='synthetic://owner/disposition' if authority=='PASS' else None
            w.writerow([f'4.{clause}',disposition,authority,rationale,fresh,control,text,authref,actual,want])
    checks={'A1':prior['fictional'] and prior['decision']=='PASS','A2':n==1782,'A3':diff==0,'A4':unsup==0,'A5':mandatorybad==0,'A6':failedbad==0,'A7':len(prior['structured_record'])==6 and (out/'applicability_cases.csv').is_file()}
    summary={'applicability_cases':n,'outcomes':dict(counts),'oracle_mismatches':diff,'unsupported_na_passes':unsup,'mandatory_na_passes':mandatorybad,'known_failure_masked':failedbad}
    extra={'decision':'PASS','application_disposition_record':prior['structured_record'],'toy_nonwaivable_clauses':['4.1','4.11'],'owner_adoption':'NONE'}
elif i==3:
    n=0;diff=0;badtime=0;stale=0;unknown=0;counts=Counter()
    allowed={(g,u,x) for g in range(4) for u in range(4) for x in range(4) if g<=u and u<x}
    with (out/'provenance_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['generated','used','invalidated','current_version_match','verification','decision','oracle'])
        for g,u,x,match,v in itertools.product(range(4),range(4),range(4),(False,True),ST):
            order_ok=g<=u<x
            actual='FAIL' if not order_ok or v=='FAIL' else ('INDETERMINATE' if not match or v=='INDETERMINATE' else 'PASS')
            want='PASS' if (g,u,x) in allowed and match and v=='PASS' else ('FAIL' if (g,u,x) not in allowed or v=='FAIL' else 'INDETERMINATE')
            n+=1;counts[actual]+=1;diff+=actual!=want;badtime+=actual=='PASS' and u>=x;stale+=actual=='PASS' and not match;unknown+=actual=='PASS' and v=='INDETERMINATE'
            w.writerow([g,u,x,match,v,actual,want])
    checks={'P1':prior['fictional'] and prior['scope']=='research-only','P2':n==384,'P3':diff==0,'P4':badtime==0,'P5':stale==0,'P6':unknown==0,'P7':counts['PASS']>0}
    summary={'time_version_cases':n,'outcomes':dict(counts),'oracle_mismatches':diff,'at_or_after_invalidation_passes':badtime,'stale_version_passes':stale,'unknown_verification_passes':unknown}
    extra={'decision':'PASS','support_current':True,'semantic_truth_verified':False,'full_prov_validator':False}
elif i==4:
    factors=['competence','declared_conflict_clear','review_current','independence_assessment'];n=0;unk=0;selfbad=0;stale=0;hiddenpass=0;counts=Counter();example=None
    with (out/'reviewer_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(factors+['identity_distinct','version_match','latent_actual_conflict','observed_policy','fact_independence_valid'])
        for vals in itertools.product(ST,repeat=4):
            for distinct,match,hidden in itertools.product((False,True),repeat=3):
                actual='FAIL' if 'FAIL' in vals or not distinct else ('INDETERMINATE' if 'INDETERMINATE' in vals or not match else 'PASS')
                fact_valid=vals.count('PASS')==4 and distinct and match and not hidden
                n+=1;counts[actual]+=1;unk+=actual=='PASS' and 'INDETERMINATE' in vals;selfbad+=actual=='PASS' and not distinct;stale+=actual=='PASS' and not match
                if actual=='PASS' and hidden:
                    hiddenpass+=1
                    if example is None:example={'observed':dict(zip(factors,vals)),'identity_distinct':distinct,'version_match':match,'latent_actual_conflict':hidden,'policy':actual,'genuine_independence':False}
                w.writerow(list(vals)+[distinct,match,hidden,actual,fact_valid])
    save('hidden_conflict_counterexample.json',example)
    hypotheses={'H4':{'statement':'Metadata PASS always establishes genuine independence','result':'SUPPORTED' if hiddenpass==0 else 'NOT SUPPORTED','counterexamples':hiddenpass,'scope':'Constructed information-limit witness,not empirical reviewer failure rate'}}
    checks={'R1':prior['fictional'] and prior['support_current'],'R2':n==648,'R3':unk==0,'R4':selfbad==0,'R5':stale==0,'R6':hiddenpass>0 and example is not None,'R7':contract['actual_review']=='NONE' and contract['overall_gate']=='INDETERMINATE'}
    summary={'reviewer_cases':n,'observed_outcomes':dict(counts),'unknown_factor_passes':unk,'self_review_passes':selfbad,'stale_review_passes':stale,'hidden_conflict_passes':hiddenpass}
    extra={'decision':'PASS','review_fixture':'Synthetic fully specified positive metadata only','hidden_truth_limitation':True,'hypothesis_H4':hypotheses['H4']['result']}
elif i==5:
    atoms=['read:docA','draft:docA','read:docB'];sets=[{atoms[j] for j in range(3) if b&(1<<j)} for b in range(8)]
    n=0;diff=0;revokedpass=0;widepass=0;unk=0;mutantfalse=0;counts=Counter()
    with (out/'delegation_chain_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['root_mask','middle_mask','leaf_mask','revoked_node','time','version_match','issuer','proper','leaf_only_mutant'])
        for rm,mm,lm,revoked,t,match,v in itertools.product(range(8),range(8),range(8),('none','root','middle','leaf'),range(3),(False,True),ST):
            nested=sets[lm]<=sets[mm]<=sets[rm]
            bad=not nested or revoked!='none' or t>1 or not match or v=='FAIL'
            actual='FAIL' if bad else ('INDETERMINATE' if v=='INDETERMINATE' else 'PASS')
            want='PASS' if nested and revoked=='none' and t<=1 and match and v=='PASS' else ('INDETERMINATE' if nested and revoked=='none' and t<=1 and match and v=='INDETERMINATE' else 'FAIL')
            mutant='PASS' if revoked!='leaf' and t<=1 and match and v=='PASS' else 'FAIL'
            n+=1;counts[actual]+=1;diff+=actual!=want;revokedpass+=actual=='PASS' and revoked!='none';widepass+=actual=='PASS' and not nested;unk+=actual=='PASS' and v=='INDETERMINATE';mutantfalse+=mutant=='PASS' and actual!='PASS'
            w.writerow([rm,mm,lm,revoked,t,match,v,actual,mutant])
    checks={'D1':prior['fictional'] and prior['actual_review']=='NONE','D2':n==36864,'D3':diff==0,'D4':revokedpass==0,'D5':widepass==0,'D6':unk==0,'D7':mutantfalse>0}
    summary={'delegation_chain_cases':n,'outcomes':dict(counts),'oracle_mismatches':diff,'revoked_ancestor_or_leaf_passes':revokedpass,'scope_amplification_passes':widepass,'unknown_issuer_passes':unk,'leaf_only_mutant_false_passes':mutantfalse}
    extra={'decision':'PASS','root_capabilities':atoms,'middle_capabilities':['read:docA','draft:docA'],'leaf_capabilities':['read:docA'],'root_expiry':3,'middle_expiry':2,'leaf_expiry':1,'revocation_observation_assumed_complete':True,'hypothesis_H4':prior['hypothesis_H4']}
elif i==6:
    n=0;strictbad=0;offlinebad=0;leasebad=0;offlineactiveblocked=0;leaseallowed=0
    with (out/'freshness_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['revoked_at','delivery_delay','request_time','lease_expiry','clock_skew','authority_online','globally_active','replica_observes_revocation','lease_allows','strict_query','lease_globally_unauthorized'])
        for r,d,t,L,s,online in itertools.product(range(5),range(5),range(9),range(5),(-1,0,1),(False,True)):
            active=t<r;observed=t>=r+d;lease=not observed and 0<=t+s<=L
            strict='PASS' if online and active else ('FAIL' if online else 'INDETERMINATE')
            n+=1;strictbad+=strict=='PASS' and not active;offlinebad+=not online and strict=='PASS';leasebad+=lease and not active;leaseallowed+=lease;offlineactiveblocked+=not online and active
            w.writerow([r,d,t,L,s,online,active,observed,lease,strict,lease and not active])
    witness={'same_visible_inputs':{'replica_observes_revocation':False,'request_time':2,'lease_expiry':4,'clock_skew':0,'authority_online':False},'world_active':{'revoked_at':4,'delivery_delay':0,'globally_active':True},'world_revoked':{'revoked_at':1,'delivery_delay':4,'globally_active':False},'conclusion':'Identical local observation cannot by itself reveal which global state holds.'}
    save('indistinguishability_witness.json',witness)
    hypotheses={'H6':{'statement':'A locally valid lease eliminates every globally revoked access','result':'SUPPORTED' if leasebad==0 else 'NOT SUPPORTED','globally_unauthorized_lease_allow_cases':leasebad,'scope':'Finite delay/skew witness,not measured latency or a deployment failure rate'}}
    checks={'F1':prior['fictional'] and 'read:docA' in prior['leaf_capabilities'],'F2':n==6750,'F3':strictbad==0,'F4':offlinebad==0,'F5':(out/'freshness_cases.csv').is_file(),'F6':witness['world_active']['globally_active']!=witness['world_revoked']['globally_active'],'F7':leasebad>0 and offlineactiveblocked>0}
    summary={'freshness_cases':n,'strict_query_globally_unauthorized_passes':strictbad,'offline_strict_passes':offlinebad,'lease_allowed_cases':leaseallowed,'globally_unauthorized_lease_allow_cases':leasebad,'offline_active_cases_blocked':offlineactiveblocked}
    extra={'freshness_limit':True,'lease_residual_cases':leasebad,'strict_query_bad_cases':strictbad,'actual_distributed_network':'NONE','hypothesis_H4':prior['hypothesis_H4'],'hypothesis_H6':hypotheses['H6']['result']}
elif i==7:
    events=('CHECK_A','CHECK_B','CHANGE','COMMIT_A','COMMIT_B','REVOKE','AUTHORIZE')
    def fresh():return {'version':1,'epoch':0,'basis':True,'approved':1,'nonce':0,'cache':{'A':None,'B':None},'used':{'A':False,'B':False}}
    def valid(s):return s['basis'] and s['approved']==s['version']
    def step(s,e):
        s={**s,'cache':dict(s['cache']),'used':dict(s['used'])};proper=False;cached=False;replay=False;nonce=None
        if e.startswith('CHECK_'):
            worker=e[-1];s['nonce']+=1;s['cache'][worker]=(s['epoch'],s['version'],s['nonce']) if valid(s) else None;s['used'][worker]=False
        elif e.startswith('COMMIT_'):
            worker=e[-1];token=s['cache'][worker];nonce=token[2] if token else None
            cached=bool(token) and not s['used'][worker]
            replay=bool(token) and valid(s) and token[:2]==(s['epoch'],s['version'])
            proper=replay and not s['used'][worker]
            if proper:s['used'][worker]=True
        elif e=='CHANGE':s['version']+=1;s['epoch']+=1;s['approved']=None
        elif e=='REVOKE':s['basis']=False;s['approved']=None;s['epoch']+=1
        elif e=='AUTHORIZE' and s['basis']:s['approved']=s['version'];s['epoch']+=1
        return s,proper,cached,replay,nonce
    n=0;steps=0;unsafe=0;double=0;cachebad=0;replaybad=0;good=0;examples={}
    with (out/'atomic_traces.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['events','proper_bits','cache_only_bits','replay_mutant_bits','final_version','final_epoch','basis'])
        for seq in itertools.product(events,repeat=5):
            s=fresh();seen=set();pb=[];cb=[];rb=[];n+=1
            for pos,e in enumerate(seq,1):
                old=s;s,p,c,r,nonce=step(s,e);steps+=1
                want=False
                if e.startswith('COMMIT_'):
                    worker=e[-1];token=old['cache'][worker]
                    want=bool(token) and old['basis'] and old['approved']==old['version'] and token[0]==old['epoch'] and token[1]==old['version'] and not old['used'][worker]
                unsafe+=p and not want;good+=p
                if p:
                    double+=nonce in seen;seen.add(nonce)
                if c and not want:
                    cachebad+=1
                    examples.setdefault('cache_only',{'events':seq,'at_event':pos,'old_state':old,'proper':p,'mutant':c})
                if r and not want:
                    replaybad+=1
                    examples.setdefault('replay',{'events':seq,'at_event':pos,'old_state':old,'proper':p,'mutant':r})
                pb.append(str(int(p)));cb.append(str(int(c)));rb.append(str(int(r)))
            w.writerow(['|'.join(seq),''.join(pb),''.join(cb),''.join(rb),s['version'],s['epoch'],s['basis']])
    save('atomic_counterexamples.json',examples)
    s=fresh();s,*_=step(s,'CHECK_A');s,p,*_=step(s,'COMMIT_A')
    checks={'C1':prior['freshness_limit'] and prior['lease_residual_cases']>0,'C2':n==16807 and steps==84035,'C3':unsafe==0,'C4':double==0,'C5':cachebad>0,'C6':replaybad>0,'C7':p is True}
    summary={'atomic_traces':n,'event_steps':steps,'permitted_commit_steps':good,'unsafe_hardened_commit_steps':unsafe,'same_nonce_double_successes':double,'cache_only_false_allow_steps':cachebad,'replay_false_allow_steps':replaybad}
    extra={'atomic_contract_checked':True,'atomic_implementation':'NONE','predicate_unsafe_commits':unsafe,'hypothesis_H4':prior['hypothesis_H4'],'hypothesis_H6':prior['hypothesis_H6']}
elif i==8:
    names=['legitimate','accessible','predictable','equitable','transparent','rights_compatible','learning','engagement_dialogue','privacy_protected','outcome_verified']
    n=0;diff=0;missingpass=0;badready=0;false_remedy=0;readycounts=Counter();remedycounts=Counter()
    with (out/'remedy_vectors.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(names+['process_ready','remedy_supported','process_only_mutant'])
        for v in itertools.product(ST,repeat=10):
            ready=gate(v[:9]);remedy=gate(v);wantready=oracle(v[:9]);wantremedy=oracle(v)
            n+=1;readycounts[ready]+=1;remedycounts[remedy]+=1;diff+=(ready!=wantready or remedy!=wantremedy)
            missingpass+=remedy=='PASS' and v[9]!='PASS';badready+=ready=='PASS' and (v[1]=='FAIL' or v[8]=='FAIL')
            false_remedy+=ready=='PASS' and remedy!='PASS'
            w.writerow(list(v)+[ready,remedy,ready])
    checks={'M1':prior['atomic_implementation']=='NONE','M2':n==59049,'M3':diff==0,'M4':missingpass==0,'M5':badready==0,'M6':false_remedy>0,'M7':contract['actual_review']=='NONE'}
    summary={'remedy_vectors':n,'process_ready_outcomes':dict(readycounts),'remedy_supported_outcomes':dict(remedycounts),'oracle_mismatches':diff,'unsupported_remedy_passes':missingpass,'process_only_false_remedy_passes':false_remedy}
    extra={'actual_remedy':'NONE','actual_affected_party_consultation':'NONE','process_is_not_outcome':True,'hypothesis_H4':prior['hypothesis_H4'],'hypothesis_H6':prior['hypothesis_H6']}
elif i==9:
    factors=['evidence_authenticity','applicability_authority','support_currentness','reviewer_independence','delegation_bounds','policy_freshness','atomicity','remedy_outcome','human_approval']
    mutant={'ignore_unknown':lambda v:'FAIL' if 'FAIL' in v else 'PASS','majority':lambda v:'PASS' if v.count('PASS')>=5 else 'FAIL','owner_override':lambda v:'PASS' if v[8]=='PASS' else gate(v),'form_only':lambda v:'PASS','cycle_count_override':lambda v:'PASS','process_without_remedy':lambda v:gate(v[:7]+v[8:])}
    n=0;diff=0;missingpass=0;counts=Counter();false=Counter();examples={}
    with (out/'integrated_vectors.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(factors+['proper','oracle']+list(mutant))
        for v in itertools.product(ST,repeat=9):
            actual=gate(v);want=oracle(v);n+=1;counts[actual]+=1;diff+=actual!=want
            missingpass+=actual=='PASS' and any(v[j]!='PASS' for j in (3,7,8))
            mv={name:fn(v) for name,fn in mutant.items()}
            for name,decision in mv.items():
                if decision=='PASS' and actual!='PASS':
                    false[name]+=1;examples.setdefault(name,{'states':dict(zip(factors,v)),'proper':actual,'mutant':decision})
            w.writerow(list(v)+[actual,want]+list(mv.values()))
    save('integrated_counterexamples.json',examples)
    earlier={}
    for stage,key in [(4,'H4'),(6,'H6')]:
        p=base/f'iter-{stage}/outputs/results.json';inputs[str(p.relative_to(base))]=sha(p);earlier[key]=json.loads(p.read_text())['hypotheses'][key]['result']
    checks={'I1':prior['actual_remedy']=='NONE','I2':n==19683,'I3':dict(counts)=={'PASS':1,'FAIL':19171,'INDETERMINATE':511},'I4':diff==0,'I5':len(false)==6 and all(false[m]>0 for m in mutant),'I6':missingpass==0,'I7':earlier=={'H4':'NOT SUPPORTED','H6':'NOT SUPPORTED'} and prior['hypothesis_H4']=='NOT SUPPORTED' and prior['hypothesis_H6']=='NOT SUPPORTED','I8':contract['overall_gate']=='INDETERMINATE' and contract['actual_review']=='NONE' and contract['actual_authorization']=='NONE'}
    summary={'integrated_vectors':n,'outcomes':dict(counts),'oracle_mismatches':diff,'callable_mutant_false_passes':dict(false),'missing_review_remedy_or_authority_passes':missingpass,'retained_hypothesis_findings':earlier}
    extra={'overall_research_gate':'INDETERMINATE','independent_review':'NONE','ethics_review':'NONE','owner_decision':'NOT RECORDED','actual_remedy':'NONE','hypothesis_findings':earlier}
else:raise ValueError('Iteration must be1..9')
summary['checks']={k:'PASS' if v else 'FAIL' for k,v in checks.items()}
summary['hypotheses']=hypotheses
summary['scope']='Finite synthetic rules only;not independent,legal or empirical effectiveness assurance'
save('results.json',summary)
save('transfer.json',{**contract,'stage':i,**extra})
record={'id':f'TOG1-X9-RUN-{i}','iteration':i,'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'deterministic':True,'seed':None,'runner_sha256':sha(Path(__file__)),'spec_before_sha256':specbefore,'spec_after_sha256':sha(here/'SPEC.md'),'inputs_sha256':inputs,'outputs_sha256':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file()},'checks':summary['checks'],'hypothesis_results':hypotheses,'independent_review':False,'overall_gate':'INDETERMINATE','external_actions':0}
(here/'EXECUTION_RECORD.json').write_text(json.dumps(record,indent=2)+'\n')
