# SIM-IN-APP-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INB-APP iter-2 (P32 symptomatic subgroup) on a new seed.

## Phase operationalization tested
APP Insurgence = superspreading in a subgroup.

## Sources this run draws on
P32 (McKee et al. 2024, Epidemiol Infect 152:e121, CC BY; read in full in INB): 9,591 index cases, 67% zero secondary cases, 3% > 5, negative binomial mean 0.88, k 0.27, top 17% produce 80%. Table 4.

## Refinement from previous iteration
Iteration 10 of the x12 family for APP; follows iteration 9 (see Purpose).

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
 "iteration": 10,
 "kind": "offspring_profile",
 "seed": 23410,
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
`python sim_app.py iter-10` (run from `Applied-Sciences/simulation/`)
