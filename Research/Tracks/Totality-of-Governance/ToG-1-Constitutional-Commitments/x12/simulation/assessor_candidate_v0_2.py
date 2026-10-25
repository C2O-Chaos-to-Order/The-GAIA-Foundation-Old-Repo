VERSION='0.2.0'
STATES=('PASS','FAIL','INDETERMINATE')
FIELDS=('record_id','scope','rationale','authority','version','evidence_ref')
def normalize_state(value):
    if value is None:return 'INDETERMINATE'
    if type(value) is not str or value not in STATES:return 'FAIL'
    return value

def assess(record,verification):
    state=normalize_state(verification)
    reasons=[]
    if verification is None:reasons.append('verification_missing')
    elif type(verification) is not str or verification not in STATES:reasons.append('verification_invalid')
    if state=='FAIL':return 'FAIL',reasons or ['verification_failed']
    if type(record) is not dict:return 'FAIL',reasons+['record_not_exact_dict']
    if any(type(k) is not str for k in record):return 'FAIL',reasons+['record_key_not_string']
    if set(record)-set(FIELDS):return 'FAIL',reasons+['unexpected_fields']
    invalid=False;missing=False
    for name in FIELDS:
        if name not in record or record[name] is None:
            missing=True;reasons.append(name+':missing_or_null')
        elif type(record[name]) is not str:
            invalid=True;reasons.append(name+':wrong_type')
        elif '\x00' in record[name]:
            invalid=True;reasons.append(name+':nul')
        elif not record[name].strip():
            missing=True;reasons.append(name+':blank')
    if invalid:return 'FAIL',reasons
    if record.get('scope')!='research-only':missing=True;reasons.append('scope_mismatch')
    if record.get('version')!='v1':missing=True;reasons.append('version_mismatch')
    if missing or state=='INDETERMINATE':return 'INDETERMINATE',reasons or ['verification_indeterminate']
    return 'PASS',reasons

def combine(values,required=None):
    if values is None:return 'INDETERMINATE'
    if type(values) is not list:return 'FAIL'
    normalized=[normalize_state(v) for v in values]
    if 'FAIL' in normalized:return 'FAIL'
    if not normalized or (required is not None and len(normalized)!=required):return 'INDETERMINATE'
    return 'INDETERMINATE' if 'INDETERMINATE' in normalized else 'PASS'
