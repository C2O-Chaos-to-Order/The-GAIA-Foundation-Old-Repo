# SIM-IN-APP-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-APP iter-7 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
APP Insurgence = emergence driven by a few superspreaders (P32).

## Sources this run draws on
P32 (McKee et al. 2024, Epidemiol Infect 152:e121, CC BY; read in full in INB): 9,591 index cases, 67% zero secondary cases, 3% > 5, negative binomial mean 0.88, k 0.27, top 17% produce 80%.

## Refinement from previous iteration
Iteration 7 of the x12 family for APP; follows iteration 6 (see Purpose).

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
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-D",
 "iteration": 7,
 "kind": "offspring_profile",
 "seed": 23407,
 "m": 0.88,
 "k": 0.27,
 "n": 9591,
 "reps": 200,
 "tol": 0.02,
 "p_zero": 0.67,
 "p_gt5": 0.03,
 "p_top80": 0.17
}
```

## Command
`python sim_app.py iter-7` (run from `Applied-Sciences/simulation/`)
