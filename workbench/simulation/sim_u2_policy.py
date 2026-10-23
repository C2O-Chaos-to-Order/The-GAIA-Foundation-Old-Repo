import itertools, csv, copy
from common import *
GATES=['consent','rights','provenance','authority','safety','ecology']
LENSES=['Truth','Integrity','Love','Justice','Wisdom']
def validate_flags(values):
    if any(v is not True and v is not False and v is not None for v in values):raise ValueError('Invalid tri-state')
def review(gates,lenses,empirical,evidence):
    values=[gates.get(g) for g in GATES]+[lenses.get(l) for l in LENSES]
    validate_flags(values+[evidence])
    if any(v is False for v in values):return 'DENY'
    if any(v is None for v in values):return 'HOLD'
    if empirical and evidence is not True:return 'HOLD'
    return 'ALLOW_SCOPED'
def spec_oracle(gates,lenses,evidence):
    row=list(gates.values())+list(lenses.values())
    failed=sum(v is False for v in row);unknown=sum(v is None for v in row)
    return 'DENY' if failed else ('HOLD' if unknown or evidence is not True else 'ALLOW_SCOPED')
def request_digest(request):return digest(canonical(request))
def verify_approval(request,approval,permission,permission_revision,used,now,revoked=False):
    if permission is not True or revoked:return 'DENY'
    if approval.get('digest')!=request_digest(request):return 'DENY'
    if approval.get('actor')!=request.get('actor'):return 'DENY'
    if approval.get('permission_revision')!=permission_revision:return 'DENY'
    if now>=approval['expires'] or approval['nonce'] in used:return 'DENY'
    return 'ALLOW_SCOPED'
def run():
    rec=Recorder('GAIA-SIM-U2',__file__,ROOT/'simulation/specs/U2.md')
    rows=[];mismatches=0;unsafe=0;counts={'ALLOW_SCOPED':0,'HOLD':0,'DENY':0}
    def assess(label,gates,lenses,evidence):
        nonlocal mismatches,unsafe
        observed=review(gates,lenses,True,evidence);expected=spec_oracle(gates,lenses,evidence)
        mismatches+=observed!=expected;counts[observed]+=1
        if observed=='ALLOW_SCOPED' and not all(v is True for v in list(gates.values())+list(lenses.values())+[evidence]):unsafe+=1
        rows.append({'scenario':label,'gates':json.dumps(gates),'lenses':json.dumps(lenses),'evidence':str(evidence),'expected':expected,'actual':observed})
    all_gates={g:True for g in GATES};all_lenses={l:True for l in LENSES}
    for index,values in enumerate(itertools.product([True,False,None],repeat=6)):
        for evidence in [True,False,None]:assess(f'gates-{index}-{evidence}',dict(zip(GATES,values)),all_lenses,evidence)
    for index,values in enumerate(itertools.product([True,False,None],repeat=5)):assess(f'lenses-{index}',all_gates,dict(zip(LENSES,values)),True)
    rec.check('sweep_scenario_count',len(rows),2430);rec.check('sweep_mismatches',mismatches,0);rec.check('unsafe_allows',unsafe,0)
    rec.check('unknown_consent_holds',review({**all_gates,'consent':None},all_lenses,True,True),'HOLD')
    rec.check('failed_rights_denies',review({**all_gates,'rights':False},all_lenses,True,True),'DENY')
    rec.check('evidence_false_holds',review(all_gates,all_lenses,True,False),'HOLD')
    rec.check('interpretive_study_no_empirical_claim',review(all_gates,all_lenses,False,None),'ALLOW_SCOPED')
    try:review({**all_gates,'rights':'yes'},all_lenses,True,True);caught=False
    except ValueError:caught=True
    rec.check('malformed_flag_rejected',caught,True)
    request={'actor':'local-owner','action':'synthetic_export','resource':'fixture-1','arguments':{'scope':'public','revision':1},'schema_version':'1'}
    approval={'actor':'local-owner','digest':request_digest(request),'permission_revision':3,'expires':200,'nonce':'fixture-nonce'}
    cases=[]
    def binding(name,req=None,ap=None,permission=True,rev=3,used=None,now=100,revoked=False,expected='DENY'):
        result=verify_approval(req or request,ap or approval,permission,rev,set() if used is None else used,now,revoked)
        rec.check('binding_'+name,result,expected);cases.append({'name':name,'actual':result,'expected':expected})
    binding('valid',expected='ALLOW_SCOPED')
    for field,value in [('actor','other'),('action','external_send'),('resource','other'),('arguments',{'scope':'private','revision':1}),('schema_version','2')]:binding('changed_'+field,req={**request,field:value})
    binding('expiry_boundary',now=200);binding('expired',now=201);binding('revoked',revoked=True);binding('permission_false',permission=False);binding('permission_unknown',permission=None);binding('permission_revision',rev=4);binding('nonce_replay',used={'fixture-nonce'})
    used=set();first=verify_approval(request,approval,True,3,used,100)
    if first=='ALLOW_SCOPED':used.add(approval['nonce'])
    second=verify_approval(request,approval,True,3,used,100)
    rec.check('sequential_single_use',[first,second],['ALLOW_SCOPED','DENY'])
    mutation_probes=[('unknown_as_allow','ALLOW_SCOPED',review({**all_gates,'consent':None},all_lenses,True,True)),('ignored_binding','ALLOW_SCOPED',verify_approval({**request,'resource':'other'},approval,True,3,set(),100)),('failed_gate_as_hold','HOLD',review({**all_gates,'rights':False},all_lenses,True,True))]
    for name,mutated,correct in mutation_probes:rec.check('detect_mutation_'+name,mutated!=correct,True)
    with (ROOT/'simulation/results/U2_state_sweep.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    (ROOT/'simulation/results/U2_binding_cases.json').write_text(json.dumps(cases,indent=2))
    return rec.finish({'sweep_configurations':len(rows),'decision_counts':counts,'binding_scenarios':len(cases),'handwritten_mutation_probes':3,'mutation_probes_detected':sum(mutated!=correct for _,mutated,correct in mutation_probes)},['Finite authored policy and oracle; not independent or universal ethical validation','Permission and approval stores are trusted synthetic inputs','No concurrent nonce consumption or external action tested','Digest binding is not cryptographic identity or authorization proof','No AI prompt-injection resistance demonstrated by this policy sweep'])
if __name__=='__main__':run()
