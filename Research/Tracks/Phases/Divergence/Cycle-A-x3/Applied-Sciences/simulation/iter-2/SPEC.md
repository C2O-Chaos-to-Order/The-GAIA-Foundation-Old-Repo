# SIM-DV-APP-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same at N = 20,000 cells: does a larger population make the 1/f fit tighter?

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Iteration 1 at N = 5,000; this iteration quadruples N.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | N reached, bookkeeping exact |
| H1 | hypothesis | median R^2 >= 0.98 |
| R1 | reporting | R^2 per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-A",
 "iteration": 2,
 "kind": "clonal_branching_reps",
 "seed": 15402,
 "N": 20000,
 "birth": 1.0,
 "death": 0.3,
 "u": 2.0,
 "fmin": 0.1,
 "fmax": 0.4,
 "reps": 5,
 "h1": 0.98
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
