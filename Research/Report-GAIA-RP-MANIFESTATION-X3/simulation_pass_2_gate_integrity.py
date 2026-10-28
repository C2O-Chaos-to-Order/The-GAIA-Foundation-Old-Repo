#!/usr/bin/env python3
"""Manifestation x3 simulation pass 2: multiplier and gate integrity."""
import json
from datetime import date
RUN_ID="GAIA-RP-MANIFESTATION-X3-SIM-002"
MODEL_VERSION="1.0.0"

def assess(case):
    research=case.get("research",[]); sims=case.get("simulations",[])
    if len(research)!=3: return "BLOCKED_RESEARCH_PASS_COUNT"
    if len({p.get("id") for p in research})!=3: return "FAIL_DUPLICATE_RESEARCH_ID"
    if len({p.get("scope") for p in research})!=3: return "FAIL_NON_DISTINCT_RESEARCH_SCOPE"
    if len(sims)!=3: return "BLOCKED_SIMULATION_PASS_COUNT"
    if len({s.get("id") for s in sims})!=3: return "FAIL_DUPLICATE_SIMULATION_ID"
    if any(not s.get("executed",False) for s in sims): return "BLOCKED_UNEXECUTED_SIMULATION"
    if any(not s.get("pre_interlay",False) or not s.get("post_interlay",False) for s in sims): return "BLOCKED_MISSING_INTERLAY"
    if any(s.get("criterion_status")!="PASS" for s in sims): return "FAIL_ACCEPTANCE_CRITERION"
    return "PASS_STAGE_CRITERIA"

def rp(i): return {"id":f"R{i}","scope":f"distinct research scope {i}"}
def sp(i,status="PASS",executed=True,pre=True,post=True): return {"id":f"S{i}","executed":executed,"pre_interlay":pre,"post_interlay":post,"criterion_status":status}
def base(): return {"research":[rp(1),rp(2),rp(3)],"simulations":[sp(1),sp(2),sp(3)]}

cases=[]
def add(cid,c,exp):
    obs=assess(c); cases.append({"id":cid,"expected_result":exp,"observed_result":obs,"passed":obs==exp})
c=base(); add("G01_complete_three_by_three",c,"PASS_STAGE_CRITERIA")
c=base(); c["simulations"]=c["simulations"][:2]; add("G02_only_two_simulations",c,"BLOCKED_SIMULATION_PASS_COUNT")
c=base(); c["simulations"][2]["id"]="S2"; add("G03_duplicate_simulation_id",c,"FAIL_DUPLICATE_SIMULATION_ID")
c=base(); c["simulations"][1]["executed"]=False; add("G04_unexecuted_run",c,"BLOCKED_UNEXECUTED_SIMULATION")
c=base(); c["simulations"][2]["criterion_status"]="FAIL"; add("G05_executed_but_failed_criterion",c,"FAIL_ACCEPTANCE_CRITERION")
c=base(); c["simulations"][0]["post_interlay"]=False; add("G06_missing_post_interlay",c,"BLOCKED_MISSING_INTERLAY")
c=base(); c["research"][2]["scope"]=c["research"][1]["scope"]; add("G07_relabelled_research_scope",c,"FAIL_NON_DISTINCT_RESEARCH_SCOPE")
c=base(); c["research"]=c["research"][:2]; add("G08_only_two_research_passes",c,"BLOCKED_RESEARCH_PASS_COUNT")
c=base(); c["simulations"][1]["criterion_status"]="INDETERMINATE"; add("G09_indeterminate_is_not_pass",c,"FAIL_ACCEPTANCE_CRITERION")
checks={f"AC-T2-{i:02d}":case["passed"] for i,case in enumerate(cases,1)}
checks["AC-T2-10"]=all(c["passed"] for c in cases)
out={"run_id":RUN_ID,"run_date":date.today().isoformat(),"model":"Multiplier and stage-gate integrity","model_version":MODEL_VERSION,"execution_status":"EXECUTED","execution_type":"one deterministic software simulation run with nine synthetic fixtures","required_research_passes":3,"required_simulation_passes":3,"fixtures":cases,"acceptance_criteria":checks,"criterion_count":len(checks),"criteria_passed":sum(checks.values()),"fixture_count":len(cases),"accepted":all(checks.values()),"limitations":["Synthetic gate cases only; not a simulation of the GAIA intelligence itself.","The test encodes selected rules; it does not independently validate the full research plan.","A failed executed run is an attempt but does not satisfy its success criterion.","No independent reproduction or review performed."]}
print(json.dumps(out,indent=2))
if not out["accepted"]: raise SystemExit(1)
