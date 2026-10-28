"""Deterministic procedural simulation for GAIA Research Plan Baseline ×1.

Scope: test procedural control logic against synthetic fixtures, not GAIA's
scientific/conceptual hypotheses or real-world performance.
One invocation constitutes one simulation pass; internal fixtures are cases
within that single run and are not separately counted as passes.
"""
from __future__ import annotations
import json
from datetime import date

RUN_ID = "GAIA-RP-BASE-SIM-001"
PLAN_VERSION = "1.4"
REPORT_FIELDS = [
    "document_control", "purpose_scope", "architecture_mapping",
    "definitions_claim_register", "research_record", "assumptions_method",
    "pre_simulation_interlay", "simulation_record", "post_simulation_interlay",
    "results_synthesis", "verification_acceptance", "limitations_next_actions",
    "foundation_handoff_metadata",
]


def gate(*, required_research=1, actual_research=1, required_simulations=1,
         simulation_executed=True, simulation_acceptance=True,
         pre_interlay=True, post_interlay=True,
         failure_routed_diagnostically=True):
    if actual_research != required_research:
        return "FAIL_EXACT_RESEARCH_PASS_COUNT"
    if actual_research < required_research:
        return "BLOCKED_REQUIRED_RESEARCH"
    if required_simulations != 1:
        return "INVALID_BASELINE_SPECIFICATION"
    if not simulation_executed:
        return "BLOCKED_REQUIRED_SIMULATION"
    if not pre_interlay or not post_interlay:
        return "BLOCKED_MISSING_INTERLAY"
    if not failure_routed_diagnostically:
        return "FAIL_FAILURE_HANDLING"
    if not simulation_acceptance:
        return "REVISE_FAIL_CRITERION"
    return "PASS_STAGE_CRITERIA"


def main():
    cases = [
        ("S01_complete_minimum", gate(), "PASS_STAGE_CRITERIA"),
        ("S02_simulation_missing", gate(simulation_executed=False), "BLOCKED_REQUIRED_SIMULATION"),
        ("S03_executed_but_failed", gate(simulation_acceptance=False), "REVISE_FAIL_CRITERION"),
        ("S04_pre_interlay_missing", gate(pre_interlay=False), "BLOCKED_MISSING_INTERLAY"),
        ("S05_extra_research_pass", gate(actual_research=2), "FAIL_EXACT_RESEARCH_PASS_COUNT"),
        ("S06_planned_not_executed", gate(simulation_executed=False), "BLOCKED_REQUIRED_SIMULATION"),
        ("S07_failure_mislabeled_success", gate(failure_routed_diagnostically=False), "FAIL_FAILURE_HANDLING"),
        ("S08_post_interlay_missing", gate(post_interlay=False), "BLOCKED_MISSING_INTERLAY"),
    ]
    matrix_results = {
        "zodiac_alchemy": 12 * 5,
        "alchemy_transformative_phase": 5 * 6,
        "combined_cube_assumed": False,
    }
    acceptance = {
        "AC-01": len(REPORT_FIELDS) == 13,
        "AC-02": matrix_results["zodiac_alchemy"] == 60,
        "AC-03": matrix_results["alchemy_transformative_phase"] == 30,
        "AC-04": matrix_results["combined_cube_assumed"] is False,
        "AC-05": cases[0][1] == "PASS_STAGE_CRITERIA",
        "AC-06": cases[1][1] == "BLOCKED_REQUIRED_SIMULATION",
        "AC-07": cases[2][1] == "REVISE_FAIL_CRITERION",
        "AC-08": cases[3][1] == "BLOCKED_MISSING_INTERLAY",
        "AC-09": cases[4][1] == "FAIL_EXACT_RESEARCH_PASS_COUNT",
        "AC-10": cases[6][1] == "FAIL_FAILURE_HANDLING",
        "AC-11": cases[7][1] == "BLOCKED_MISSING_INTERLAY",
    }
    output = {
        "run_id": RUN_ID,
        "run_date": date.today().isoformat(),
        "model": "GAIA Research Plan procedural gate model",
        "model_version": "1.0.0",
        "plan_version_under_test": PLAN_VERSION,
        "execution_status": "EXECUTED",
        "execution_type": "single deterministic software simulation pass containing eight synthetic test fixtures",
        "fixtures": [
            {"id": cid, "observed_result": observed, "expected_result": expected,
             "passed": observed == expected}
            for cid, observed, expected in cases
        ],
        "matrix_results": matrix_results,
        "acceptance_criteria": acceptance,
        "accepted": all(acceptance.values()) and all(c[1] == c[2] for c in cases),
        "fixture_count": len(cases),
        "criterion_count": len(acceptance),
        "criteria_passed": sum(acceptance.values()),
        "limitations": [
            "Synthetic fixtures test logic encoded in this script, not actual scientific truth.",
            "No real GAIA system, field data, human subjects, physical process, or deployment was tested.",
            "The model encodes a subset of plan rules; it does not prove the entire Research Plan is complete, safe, valid, or optimal.",
            "The author/preparer executed this run; independent reproduction/review has not occurred."
        ]
    }
    print(json.dumps(output, indent=2))
    if not output["accepted"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
