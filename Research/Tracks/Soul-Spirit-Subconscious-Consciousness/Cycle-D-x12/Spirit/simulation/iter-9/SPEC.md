# SIM-SPIRIT-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Smaller expectancy effect (+/-2 points).

## Sources this run draws on
K50, K51 (as iteration 5).

## Refinement from previous iteration
Iteration 5 used +/-3.5.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | FPR |
| H1 | hypothesis | >= .5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 5.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 9,
 "kind": "expectancy_bias",
 "seed": 1209,
 "n1": 17,
 "n2": 18,
 "sd": 8.5,
 "e": 2.0,
 "reps": 50000,
 "h1": 0.5
}
```

## Command
`python sim_spirit.py iter-9` (run from `Spirit/simulation/`)
