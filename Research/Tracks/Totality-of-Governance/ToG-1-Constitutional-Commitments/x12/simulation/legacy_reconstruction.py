FIELDS=('record_id','scope','rationale','authority','version','evidence_ref')
def assess(record,verification):
    reasons=[f'{k}:missing_or_invalid_type' for k in FIELDS if not isinstance(record.get(k),str) or not record.get(k,'').strip()]
    if record.get('scope')!='research-only':reasons.append('scope_mismatch')
    if record.get('version')!='v1':reasons.append('version_mismatch')
    decision='FAIL' if verification=='FAIL' else ('INDETERMINATE' if reasons or verification=='INDETERMINATE' else 'PASS')
    return decision,reasons
