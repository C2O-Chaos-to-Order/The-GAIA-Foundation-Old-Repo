# SIM-CONS-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Two failures out of three (the situation K42 reports for key tenets of both theories), same power and prior.

## Sources this run draws on
K42 (as iteration 1).

## Refinement from previous iteration
Iteration 1 tested one failure.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = power^m |
| H1 | hypothesis | P(>= 1 failure) >= .4 |
| H2 | hypothesis | posterior after 2 failures >= .5 |
| R1 | reporting | posterior |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. K42's predictions were weighted and not independent; this is a cartoon.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 8,
 "kind": "predictions_battery",
 "seed": 818,
 "m": 3,
 "power": 0.8,
 "q_false": 0.3,
 "prior": 0.5,
 "f_test": 2,
 "h2_threshold": 0.5,
 "reps": 200000
}
```

## Command
`python sim_cons.py iter-8` (run from `Consciousness/simulation/`)
