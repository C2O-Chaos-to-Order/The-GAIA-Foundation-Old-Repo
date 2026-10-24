# SIM-IN-APP-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same with P32's symptomatic subgroup (mean 2.06, k 0.43; P32 Table 4: 44% zero, 9% > 5).

## Phase operationalization tested
APP Insurgence = superspreading in a subgroup.

## Sources this run draws on
P32 (McKee et al. 2024, Epidemiol Infect 152:e121, CC BY; read in full in INB): 9,591 index cases, 67% zero secondary cases, 3% > 5, negative binomial mean 0.88, k 0.27, top 17% produce 80%. Table 4.

## Refinement from previous iteration
Iteration 2 of the x6 family for APP; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | zero share vs analytic |
| H1 | hypothesis | zero within 0.02 |
| H2 | hypothesis | > 5 within 0.02 |
| H3 | hypothesis | top-80% within 0.02 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Top-80% share not reported by P32 for this subgroup; 0.2 used as a placeholder (H3 not meaningful, disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-B",
 "iteration": 2,
 "kind": "offspring_profile",
 "seed": 21402,
 "m": 2.06,
 "k": 0.43,
 "n": 697,
 "reps": 500,
 "tol": 0.02,
 "p_zero": 0.44,
 "p_gt5": 0.09,
 "p_top80": 0.2
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
