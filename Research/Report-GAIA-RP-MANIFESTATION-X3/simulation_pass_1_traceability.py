#!/usr/bin/env python3
"""Manifestation x3 simulation pass 1: requirements/evidence traceability.

One execution, containing synthetic fixture cases. This tests encoded process
rules only; it does not validate GAIA's conceptual hypotheses or research quality.
"""
import json
from datetime import date

RUN_ID = "GAIA-RP-MANIFESTATION-X3-SIM-001"
MODEL_VERSION = "1.0.0"

def assess(bundle):
    reqs = bundle.get("requirements", [])
    req_ids = [r.get("id") for r in reqs]
    if len(req_ids) != len(set(req_ids)):
        return "FAIL_DUPLICATE_REQUIREMENT_ID"
    source_ids = set(bundle.get("source_ids", []))
    known_evidence = set(bundle.get("evidence_ids", []))
    criteria = set(bundle.get("criteria_ids", []))
    all_criteria_evidenced = True
    used_sources, used_evidence, used_criteria = set(), set(), set()
    for req in reqs:
        if not req.get("source_id") or req["source_id"] not in source_ids:
            return "FAIL_SOURCE_TRACEABILITY"
        used_sources.add(req["source_id"])
        eids = req.get("evidence_ids", [])
        if not eids or any(e not in known_evidence for e in eids):
            return "INDETERMINATE_EVIDENCE_GAP"
        used_evidence.update(eids)
        cids = req.get("criterion_ids", [])
        if not cids or any(c not in criteria for c in cids):
            all_criteria_evidenced = False
        used_criteria.update(cids)
    if not all_criteria_evidenced:
        return "INDETERMINATE_CRITERION_GAP"
    if source_ids != used_sources or known_evidence != used_evidence or criteria != used_criteria:
        return "INDETERMINATE_ORPHANED_REGISTERED_RECORD"
    return "PASS_TRACEABLE"

def bundle_ok():
    return {"source_ids":["SRC-1","SRC-2"],"evidence_ids":["EV-1","EV-2"],"criteria_ids":["AC-1","AC-2"],"requirements":[
        {"id":"REQ-1","source_id":"SRC-1","evidence_ids":["EV-1"],"criterion_ids":["AC-1"]},
        {"id":"REQ-2","source_id":"SRC-2","evidence_ids":["EV-2"],"criterion_ids":["AC-2"]}]}

cases=[]
def run_case(cid, bundle, expected):
    actual=assess(bundle)
    cases.append({"id":cid,"expected_result":expected,"observed_result":actual,"passed":actual==expected})

b=bundle_ok(); run_case("T01_complete_bidirectional_trace",b,"PASS_TRACEABLE")
b=bundle_ok(); b["requirements"][1]["evidence_ids"]=[]; run_case("T02_missing_evidence",b,"INDETERMINATE_EVIDENCE_GAP")
b=bundle_ok(); b["requirements"][0]["source_id"]="SRC-UNKNOWN"; run_case("T03_orphan_source",b,"FAIL_SOURCE_TRACEABILITY")
b=bundle_ok(); b["requirements"][1]["id"]="REQ-1"; run_case("T04_duplicate_requirement_id",b,"FAIL_DUPLICATE_REQUIREMENT_ID")
b=bundle_ok(); b["requirements"][0]["criterion_ids"]=["AC-UNKNOWN"]; run_case("T05_unmapped_acceptance_criterion",b,"INDETERMINATE_CRITERION_GAP")
b=bundle_ok(); b["requirements"][0].pop("source_id"); run_case("T06_missing_source_link",b,"FAIL_SOURCE_TRACEABILITY")
b=bundle_ok(); b["requirements"][1]["evidence_ids"]=["EV-NOT-REGISTERED"]; run_case("T07_unregistered_evidence",b,"INDETERMINATE_EVIDENCE_GAP")
b=bundle_ok(); b["source_ids"].append("SRC-ORPHAN"); run_case("T08_orphan_registered_source",b,"INDETERMINATE_ORPHANED_REGISTERED_RECORD")
checks={
 "AC-T1-01":cases[0]["passed"], "AC-T1-02":cases[1]["passed"],
 "AC-T1-03":cases[2]["passed"], "AC-T1-04":cases[3]["passed"],
 "AC-T1-05":cases[4]["passed"], "AC-T1-06":cases[5]["passed"],
 "AC-T1-07":cases[6]["passed"], "AC-T1-08":cases[7]["passed"],
 "AC-T1-09":all(c["passed"] for c in cases),
}
out={"run_id":RUN_ID,"run_date":date.today().isoformat(),"model":"Requirements-to-evidence traceability gate","model_version":MODEL_VERSION,"execution_status":"EXECUTED","execution_type":"one deterministic software simulation run with eight synthetic fixtures","fixtures":cases,"acceptance_criteria":checks,"criterion_count":len(checks),"criteria_passed":sum(checks.values()),"fixture_count":len(cases),"accepted":all(checks.values()),"limitations":["Synthetic fixtures only; no production dataset or GAIA system tested.","Passing code behavior does not validate the completeness or truth of the requirement set.","No independent reproduction or review performed."]}
print(json.dumps(out,indent=2))
if not out["accepted"]: raise SystemExit(1)
