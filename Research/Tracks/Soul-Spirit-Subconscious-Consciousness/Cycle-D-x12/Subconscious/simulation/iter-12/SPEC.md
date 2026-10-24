# SIM-SUBC-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Only 20 regions.

## Sources this run draws on
K56 (as iteration 3).

## Refinement from previous iteration
Iteration 3 used 50 states.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | analytic |
| H1 | hypothesis | >= .6 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 3.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-D",
 "iteration": 12,
 "kind": "ecological_inflation",
 "seed": 1312,
 "states": 20,
 "per_state": 2000,
 "b_ind": 0.05,
 "state_noise": 0.02,
 "reps": 200,
 "h1": 0.6
}
```

## Command
`python sim_subc.py iter-12` (run from `Subconscious/simulation/`)
