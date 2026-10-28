#!/usr/bin/env python3
"""Manifestation x3 simulation pass 3: matrix applicability and governance."""
import json
from datetime import date
RUN_ID="GAIA-RP-MANIFESTATION-X3-SIM-003"
MODEL_VERSION="1.0.0"

def assess(case):
    zodiac_count=case.get("zodiac_count",12); alchemy_count=case.get("alchemy_count",5); phase_count=case.get("phase_count",6)
    if zodiac_count*alchemy_count != 60 or alchemy_count*phase_count != 30: return "FAIL_MATRIX_CARDINALITY"
    if case.get("combined_cube_assumed",False): return "FAIL_UNJUSTIFIED_COMBINED_CUBE"
    for cell in case.get("cells",[]):
        if cell.get("status") not in {"DEFINED","NOT_APPLICABLE"}: return "INDETERMINATE_CELL_STATUS"
        if cell["status"]=="DEFINED" and not cell.get("operational_definition"): return "INDETERMINATE_CELL_DEFINITION"
        if cell["status"]=="NOT_APPLICABLE" and not cell.get("rationale"): return "INDETERMINATE_NA_RATIONALE"
    if case.get("dependency_status")=="PROPOSED" and case.get("promote_proposed_to_confirmed",False): return "FAIL_PROPOSED_AS_FACT"
    if case.get("conflict_status")=="UNKNOWN" and case.get("close_unknown_without_evidence",False): return "FAIL_UNKNOWN_CLOSED_WITHOUT_EVIDENCE"
    if case.get("authority_scope")!="CURRENT_V14_SEQUENCE_ONLY": return "FAIL_AUTHORITY_SCOPE"
    return "PASS_GOVERNANCE_CONTROLS"

def base(): return {"zodiac_count":12,"alchemy_count":5,"phase_count":6,"combined_cube_assumed":False,"cells":[{"status":"DEFINED","operational_definition":"defined for this fixture"},{"status":"NOT_APPLICABLE","rationale":"fixture's declared scope excludes this cell"}],"dependency_status":"PROPOSED","promote_proposed_to_confirmed":False,"conflict_status":"UNKNOWN","close_unknown_without_evidence":False,"authority_scope":"CURRENT_V14_SEQUENCE_ONLY"}
cases=[]
def add(cid,c,exp):
    obs=assess(c); cases.append({"id":cid,"expected_result":exp,"observed_result":obs,"passed":obs==exp})
add("M01_valid_categorical_structure",base(),"PASS_GOVERNANCE_CONTROLS")
c=base(); c["combined_cube_assumed"]=True; add("M02_assumed_360_cell_cube",c,"FAIL_UNJUSTIFIED_COMBINED_CUBE")
c=base(); c["cells"][0].pop("operational_definition"); add("M03_cell_without_operational_definition",c,"INDETERMINATE_CELL_DEFINITION")
c=base(); c["cells"][1].pop("rationale"); add("M04_na_without_rationale",c,"INDETERMINATE_NA_RATIONALE")
c=base(); c["dependency_status"]="PROPOSED"; c["promote_proposed_to_confirmed"]=True; add("M05_proposed_dependency_promoted_without_evidence",c,"FAIL_PROPOSED_AS_FACT")
c=base(); c["close_unknown_without_evidence"]=True; add("M06_unknown_conflict_closed_without_evidence",c,"FAIL_UNKNOWN_CLOSED_WITHOUT_EVIDENCE")
c=base(); c["authority_scope"]="ALL_FOUNDATION_WORK"; add("M07_authority_scope_overgeneralized",c,"FAIL_AUTHORITY_SCOPE")
c=base(); c["zodiac_count"]=11; add("M08_wrong_matrix_cardinality",c,"FAIL_MATRIX_CARDINALITY")
c=base(); c["cells"][1]["rationale"]=""; add("M09_empty_na_rationale",c,"INDETERMINATE_NA_RATIONALE")
checks={f"AC-T3-{i:02d}":case["passed"] for i,case in enumerate(cases,1)}
checks["AC-T3-10"]=all(c["passed"] for c in cases)
out={"run_id":RUN_ID,"run_date":date.today().isoformat(),"model":"Matrix applicability and governance-status controls","model_version":MODEL_VERSION,"execution_status":"EXECUTED","execution_type":"one deterministic software simulation run with nine synthetic fixtures","matrix_results":{"zodiac_alchemy":12*5,"alchemy_transformative_phase":5*6,"combined_cube_assumed":False},"authority_resolution":"User's direct instruction to proceed with Manifestation x3 is treated as authorization to use Research Plan v1.4 for this current baseline-to-Manifestation sequence only. The older Foundation seven-report extension is retained unchanged; this is not a blanket supersession of other scopes.","fixtures":cases,"acceptance_criteria":checks,"criterion_count":len(checks),"criteria_passed":sum(checks.values()),"fixture_count":len(cases),"accepted":all(checks.values()),"limitations":["The model tests governance labels and fixture-level applicability controls, not the truth of any conceptual category.","The twelve Zodiac identities/meanings are not supplied by this categorical test and remain to be specified in domain research.","No independent reproduction or review performed."]}
print(json.dumps(out,indent=2))
if not out["accepted"]: raise SystemExit(1)
