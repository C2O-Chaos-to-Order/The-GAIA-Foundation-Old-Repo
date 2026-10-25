import csv, hashlib, itertools, json, platform, sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, deque

base=Path(__file__).resolve().parent
i=int(sys.argv[1]); here=base/f'iter-{i}';out=here/'outputs';out.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):(out/n).write_text(json.dumps(v,indent=2)+'\n')
def gate(states):
    return 'FAIL' if 'FAIL' in states else ('INDETERMINATE' if 'INDETERMINATE' in states else 'PASS')
def oracle(states):
    return 'PASS' if states.count('PASS')==len(states) else ('FAIL' if states.count('FAIL') else 'INDETERMINATE')
start=datetime.now(timezone.utc).isoformat();before=sha(here/'SPEC.md');input_hashes={};prior=None
if i>1:
    pp=base/f'iter-{i-1}/outputs/transfer.json';pr=base/f'iter-{i-1}/EXECUTION_RECORD.json'
    prior=json.loads(pp.read_text());input_hashes={str(p.relative_to(base)):sha(p) for p in [pp,pr]}
checks={};summary={}
if i==1:
    codes=('P','F','I','NA_OK','NA_UNSUPPORTED','NA_FORBIDDEN')
    def normalize(n,code):
        if code=='P':return 'PASS'
        if code=='F' or code=='NA_FORBIDDEN':return 'FAIL'
        if code=='I' or code=='NA_UNSUPPORTED':return 'INDETERMINATE'
        return 'FAIL' if n in (0,10) else 'PASS'
    def expected(n,c):
        table={'P':'PASS','F':'FAIL','I':'INDETERMINATE','NA_UNSUPPORTED':'INDETERMINATE','NA_FORBIDDEN':'FAIL','NA_OK':'PASS'}
        if c=='NA_OK' and n in {0,10}:return 'FAIL'
        return table[c]
    n=0;diff=0;badna=0;badmandatory=0;badfail=0;counts=Counter();unique=set()
    with (out/'applicability_fixtures.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['id','codes_by_clause','normalized_states','decision','oracle'])
        fixtures=itertools.chain(((j,) for j in range(11)),itertools.combinations(range(11),2))
        for slots in fixtures:
            for vals in itertools.product(codes,repeat=len(slots)):
                raw=['P']*11
                for j,c in zip(slots,vals):raw[j]=c
                norm=[normalize(j,c) for j,c in enumerate(raw)];actual=gate(norm);want=oracle([expected(j,c) for j,c in enumerate(raw)])
                n+=1;counts[actual]+=1;diff+=actual!=want;unique.add(tuple(raw))
                badna+=actual=='PASS' and 'NA_UNSUPPORTED' in raw
                badmandatory+=actual=='PASS' and any(raw[j] in ('NA_OK','NA_FORBIDDEN') for j in (0,10))
                badfail+=actual=='PASS' and any(c in ('F','NA_FORBIDDEN') for c in raw)
                w.writerow([n,'|'.join(raw),'|'.join(norm),actual,want])
    conditional=['P']*11;conditional[1]='NA_OK'
    transfer={'fictional':True,'decision':'PASS','clauses':[f'4.{j}' for j in range(1,12)],'states':['PASS']*11,'scope':'research-only','applicability_policy':'Toy nonwaivable4.1,4.11;other applicability determinations need explicit authorized rationale','authorization':'NOT REAL'}
    save('transfer.json',transfer)
    checks={'A1':n==2046,'A2':diff==0,'A3':badna==0,'A4':badmandatory==0,'A5':badfail==0,'A6':gate([normalize(j,c) for j,c in enumerate(conditional)])=='PASS','A7':len(transfer['states'])==11 and transfer['fictional'] and (out/'applicability_fixtures.csv').is_file()}
    summary={'fixtures':n,'unique_raw_vectors':len(unique),'outcomes':dict(counts),'oracle_mismatches':diff,'unsupported_na_passes':badna,'mandatory_waiver_passes':badmandatory}
elif i==2:
    nodes=['S1','S2','C1','C2','SYN','GATE'];optional=[(0,2),(0,3),(1,2),(1,3),(2,4),(3,4)]
    n=0;diff=0;unsafe=0;unrelatedbad=0
    def closure(root,edges):
        seen=set();q=deque([root])
        while q:
            a=q.popleft()
            for s,t in edges:
                if s==a and t not in seen:seen.add(t);q.append(t)
        return seen
    def acyclic(edges):
        indegree=[0]*6
        for a,b in edges:indegree[b]+=1
        q=deque(k for k in range(6) if indegree[k]==0);visited=0
        while q:
            a=q.popleft();visited+=1
            for s,t in edges:
                if s==a:
                    indegree[t]-=1
                    if indegree[t]==0:q.append(t)
        return visited==6
    with (out/'dependency_cases.jsonl').open('w') as f:
        for bits in itertools.product((0,1),repeat=6):
            edges=[e for b,e in zip(bits,optional) if b]+[(4,5)]
            reach=[[False]*6 for _ in range(6)]
            for a,b in edges:reach[a][b]=True
            for k in range(6):
                for a in range(6):
                    for b in range(6):reach[a][b]=reach[a][b] or (reach[a][k] and reach[k][b])
            for rootnode in range(6):
                descendants=closure(rootnode,edges);expected={j for j in range(6) if reach[rootnode][j]}
                states=['FAIL' if j==rootnode else ('INDETERMINATE' if j in descendants else 'PASS') for j in range(6)]
                n+=1;diff+=descendants!=expected
                unsafe+=any(states[j]=='PASS' for j in descendants|{rootnode})
                unrelatedbad+=any(states[j]!='PASS' for j in set(range(6))-descendants-{rootnode})
                f.write(json.dumps({'edges':[[nodes[a],nodes[b]] for a,b in edges],'invalidated':nodes[rootnode],'dependent_unknown':[nodes[j] for j in sorted(descendants)],'states':dict(zip(nodes,states))},separators=(',',':'))+'\n')
    save('transfer.json',{'fictional':True,'decision':'PASS','support_current':True,'scope':prior['scope'],'provenance_conformance':'NOT A FULL PROV VALIDATOR','authorization':'NOT REAL'})
    checks={'D1':prior['fictional'] and prior['states']==['PASS']*11,'D2':n==384,'D3':diff==0,'D4':unsafe==0,'D5':unrelatedbad==0,'D6':not acyclic([(2,4),(4,2),(4,5)]),'D7':json.loads((out/'transfer.json').read_text())['fictional']}
    summary={'dependency_graphs':64,'root_invalidation_cases':n,'closure_mismatches':diff,'invalidated_or_dependent_passes':unsafe,'unrelated_state_errors':unrelatedbad}
elif i==3:
    pairs=list(itertools.combinations(range(4),2));n=0;diff=0;unsafe=0;samepass=0;mutantfalse=0;counts=Counter();example=None
    with (out/'role_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['producer','reviewer1','reviewer2','owner','conflict_mask','competence1','competence2','proper','identity_only_mutant'])
        for people in itertools.product(range(4),repeat=4):
            author,r1,r2,owner=people
            for mask in range(64):
                conflicts={pairs[b] for b in range(6) if mask&(1<<b)}
                edges={tuple(sorted((a,b))) for a,b in [(author,r1),(author,r2),(r1,r2)] if a!=b}
                distinct=author!=r1 and author!=r2 and r1!=r2
                for c1,c2 in itertools.product((False,True),repeat=2):
                    good=distinct and c1 and c2 and not any(e in conflicts for e in edges)
                    want=len({author,r1,r2})==3 and sum([c1,c2])==2 and len(edges&conflicts)==0
                    actual='PASS' if good else 'FAIL';mutant='PASS' if distinct else 'FAIL'
                    n+=1;counts[actual]+=1;diff+=good!=want;unsafe+=actual=='PASS' and not want
                    samepass+=actual=='PASS' and author in (r1,r2)
                    if mutant=='PASS' and actual!='PASS':
                        mutantfalse+=1
                        if example is None:example={'roles':people,'conflict_mask':mask,'competence':[c1,c2],'proper':actual,'mutant':mutant}
                    w.writerow(list(people)+[mask,c1,c2,actual,mutant])
    save('identity_mutant_counterexample.json',example)
    save('transfer.json',{'fictional':True,'decision':'PASS','roles':{'producer':0,'reviewer1':1,'reviewer2':2,'owner':0},'declared_conflicts':[],'competence_assumed':[True,True],'scope':prior['scope'],'actual_review':'NONE','authorization':'NOT REAL'})
    checks={'R1':prior['fictional'] and prior['support_current'],'R2':n==65536,'R3':diff==0,'R4':unsafe==0,'R5':samepass==0,'R6':mutantfalse>0,'R7':json.loads((out/'transfer.json').read_text())['actual_review']=='NONE'}
    summary={'role_cases':n,'outcomes':dict(counts),'oracle_mismatches':diff,'same_author_review_passes':samepass,'identity_only_false_passes':mutantfalse}
elif i==4:
    atoms=('read:docA','draft:docA','read:docB','draft:docB');subsets=[{atoms[j] for j in range(4) if bits&(1<<j)} for bits in range(16)]
    n=0;diff=0;unsafe=0;unknownpass=0;mutantfalse=0;counts=Counter()
    with (out/'delegation_cases.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['parent_mask','child_mask','child_expiry','issuer_verification','subject_match','version_match','proper','child_only_mutant'])
        for pm,parent in enumerate(subsets):
            for cm,child in enumerate(subsets):
                for expiry,verified,subject,version in itertools.product((4,8,12),('P','F','I'),(False,True),(False,True)):
                    bad=(not child<=parent) or expiry>10 or expiry<5 or not subject or not version or verified=='F'
                    actual='FAIL' if bad else ('INDETERMINATE' if verified=='I' else 'PASS')
                    good=all([len(child-parent)==0,5<=expiry<=10,subject,version,verified=='P'])
                    fail=any([bool(child-parent),expiry not in range(5,11),subject is False,version is False,verified=='F'])
                    want='PASS' if good else ('FAIL' if fail else 'INDETERMINATE')
                    mutant='PASS' if expiry>=5 and subject and version and verified=='P' else ('INDETERMINATE' if verified=='I' else 'FAIL')
                    n+=1;counts[actual]+=1;diff+=actual!=want;unsafe+=actual=='PASS' and not good;unknownpass+=verified=='I' and actual=='PASS'
                    mutantfalse+=mutant=='PASS' and actual!='PASS'
                    w.writerow([pm,cm,expiry,verified,subject,version,actual,mutant])
    grant={'fictional':True,'decision':'PASS','parent_capabilities':['read:docA','draft:docA'],'child_capabilities':['read:docA'],'parent_expiry':10,'child_expiry':8,'checked_at':5,'next_model_clock_origin':6,'next_model_relative_expiry':2,'subject':'fictional-agent','purpose':'research-only','policy_version':1,'actual_authorization':'NONE'}
    save('transfer.json',grant)
    checks={'G1':prior['fictional'] and prior['decision']=='PASS','G2':n==9216,'G3':diff==0,'G4':unsafe==0,'G5':unknownpass==0,'G6':'read:docA' in grant['child_capabilities'] and set(grant['child_capabilities'])<=set(grant['parent_capabilities']) and 5<=grant['child_expiry']<=10,'G7':mutantfalse>0}
    summary={'delegation_cases':n,'outcomes':dict(counts),'oracle_mismatches':diff,'unsafe_passes':unsafe,'unknown_issuer_passes':unknownpass,'child_only_mutant_false_passes':mutantfalse}
elif i==5:
    alphabet=('CHECK','COMMIT','REVOKE','CHANGE','EXPIRE','REVIEW','APPROVE','TICK')
    def fresh():return {'clock':0,'expiry':prior['next_model_relative_expiry'],'version':1,'reviewed':1,'approved':1,'epoch':0,'basis':True,'cache':None}
    def valid(s):return s['basis'] and s['clock']<=s['expiry'] and s['reviewed']==s['version'] and s['approved']==s['version']
    def apply(s,e):
        s=dict(s);permit=False;mutant=False
        if e=='CHECK':s['cache']=(s['clock'],s['version'],s['epoch']) if valid(s) else None
        elif e=='COMMIT':
            mutant=s['cache'] is not None
            permit=mutant and valid(s) and s['cache'][1]==s['version'] and s['cache'][2]==s['epoch']
        elif e=='REVOKE':s['basis']=False;s['approved']=None;s['epoch']+=1
        elif e=='CHANGE':s['version']+=1;s['reviewed']=None;s['approved']=None;s['epoch']+=1
        elif e=='EXPIRE':s['clock']=s['expiry']+1;s['approved']=None;s['epoch']+=1
        elif e=='TICK':
            old=s['clock'];s['clock']+=1
            if old<=s['expiry']<s['clock']:s['approved']=None;s['epoch']+=1
        elif e=='REVIEW':
            if s['basis']:
                s['reviewed']=s['version'];s['expiry']=s['clock']+2;s['approved']=None;s['epoch']+=1
        elif e=='APPROVE':
            if s['basis'] and s['reviewed']==s['version'] and s['clock']<=s['expiry']:s['approved']=s['version'];s['epoch']+=1
        return s,permit,mutant
    n=0;steps=0;unsafe=0;mutantbad=0;commits=0;goodcommits=0;review_bad=0;example=None
    with (out/'race_traces.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['events','proper_commit_bits','cached_mutant_commit_bits','unsafe_mutant_bits','final_clock','final_version','final_epoch','basis_active'])
        for events in itertools.product(alphabet,repeat=5):
            s=fresh();pb=[];mb=[];ub=[];n+=1
            for e in events:
                old=dict(s);s,p,m=apply(s,e);steps+=1
                expected=e=='COMMIT' and old['cache'] is not None and all([old['basis'],old['clock']<=old['expiry'],old['reviewed']==old['version'],old['approved']==old['version'],old['cache'][1]==old['version'],old['cache'][2]==old['epoch']])
                unsafe+=p and not expected
                if e=='COMMIT':commits+=1;goodcommits+=p
                bad=m and not expected;mutantbad+=bad
                if bad and example is None:example={'events':events,'at_event':steps%5,'old_state':old,'proper':p,'mutant':m}
                review_bad+=e=='REVIEW' and s['approved'] is not None
                pb.append('1' if p else '0');mb.append('1' if m else '0');ub.append('1' if bad else '0')
            w.writerow(['|'.join(events),''.join(pb),''.join(mb),''.join(ub),s['clock'],s['version'],s['epoch'],s['basis']])
    def lastpermit(seq):
        s=fresh();p=False
        for e in seq:s,p,m=apply(s,e)
        return p
    save('cache_mutant_counterexample.json',example)
    save('transfer.json',{'fictional':True,'hardening_unsafe_commits':unsafe,'cache_only_unsafe_commits':mutantbad,'traces':n,'horizon':5,'actual_execution_of_external_action':False,'overall_gate':'INDETERMINATE'})
    checks={'T1':prior['fictional'] and 'read:docA' in prior['child_capabilities'] and prior['child_expiry']-prior['next_model_clock_origin']==2,'T2':n==32768 and steps==163840,'T3':unsafe==0,'T4':mutantbad>0,'T5':not lastpermit(['CHECK','REVOKE','COMMIT']),'T6':not lastpermit(['CHECK','CHANGE','REVIEW','APPROVE','COMMIT']),'T7':review_bad==0}
    summary={'trace_count':n,'event_steps':steps,'commit_attempt_steps':commits,'permitted_commit_steps':goodcommits,'unsafe_hardened_commit_steps':unsafe,'unsafe_cache_only_commit_steps':mutantbad,'review_auto_approval_errors':review_bad}
elif i==6:
    factors=['evidence','rights','safety','independent_review','authority','remedy'];n=0;counts=Counter();diff=0;missingpass=0
    def proper(v):return gate(v)
    mutants={'ignore_unknown':lambda v:'FAIL' if 'FAIL' in v else 'PASS','majority':lambda v:'PASS' if v.count('PASS')>=4 else 'FAIL','owner_override':lambda v:'PASS' if v[4]=='PASS' else proper(v),'metadata_is_proof':lambda v:'PASS'}
    false=Counter();examples={}
    with (out/'assurance_vectors.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(factors+['proper','oracle']+list(mutants))
        for values in itertools.product(('PASS','FAIL','INDETERMINATE'),repeat=6):
            n+=1;result=proper(values);want=oracle(list(values));counts[result]+=1;diff+=result!=want
            missingpass+=result=='PASS' and (values[3]!='PASS' or values[4]!='PASS')
            badoutputs={name:fn(values) for name,fn in mutants.items()}
            for name,val in badoutputs.items():
                if val=='PASS' and result!='PASS':
                    false[name]+=1
                    if name not in examples:examples[name]={'states':dict(zip(factors,values)),'proper':result,'mutant':val}
            w.writerow(list(values)+[result,want]+list(badoutputs.values()))
    save('mutant_counterexamples.json',examples)
    save('transfer.json',{'fictional':True,'overall_research_gate':'INDETERMINATE','independent_review':'NONE','ethics_review':'NONE','actual_authorization':'NONE','predecessor_race_unsafe':prior['hardening_unsafe_commits'],'limits':'Only a stipulated finite model;no factual entailment,real actor credentials,rights effectiveness or legal validation'})
    checks={'I1':prior['fictional'] and prior['hardening_unsafe_commits']==0,'I2':n==729,'I3':dict(counts)=={'PASS':1,'FAIL':665,'INDETERMINATE':63},'I4':diff==0,'I5':len(false)==4 and all(false[m]>0 for m in mutants),'I6':prior['cache_only_unsafe_commits']>0,'I7':missingpass==0,'I8':json.loads((out/'transfer.json').read_text())['overall_research_gate']=='INDETERMINATE'}
    summary={'assurance_vectors':n,'outcomes':dict(counts),'oracle_mismatches':diff,'callable_mutant_false_passes':dict(false),'missing_review_or_authority_passes':missingpass}
else:raise ValueError('Iteration must be1..6')
summary['checks']={k:'PASS' if v else 'FAIL' for k,v in checks.items()};summary['scope']='Synthetic model outputs,not independent/empirical assurance'
save('results.json',summary)
record={'id':f'TOG1-X6-RUN-{i}','iteration':i,'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'seed':None,'deterministic':True,'runner_sha256':sha(Path(__file__)),'spec_before_sha256':before,'spec_after_sha256':sha(here/'SPEC.md'),'inputs_sha256':input_hashes,'outputs_sha256':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file()},'checks':summary['checks'],'independent_review':False,'overall_gate':'INDETERMINATE','external_actions':0}
(here/'EXECUTION_RECORD.json').write_text(json.dumps(record,indent=2)+'\n')
