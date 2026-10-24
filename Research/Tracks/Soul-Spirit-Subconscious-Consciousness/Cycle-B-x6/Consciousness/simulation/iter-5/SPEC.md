# SIM-CONS-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Sensitivity of SIM-CONS-A iteration 1: with weak report demand (r = 0.5) and a higher reportability threshold (tau = 0.8), does the no-report pattern still hold?

## Sources this run draws on
K13 (as Cycle A).

## Refinement from previous iteration
Cycle A used r = 1.5, tau = 0.5.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | g = 0 contrast ~ 0 |
| H1 | hypothesis | reduction >= 50% |
| H2 | hypothesis | >= 80% visible above tau |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As Cycle A. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-B",
 "iteration": 5,
 "kind": "report_confound",
 "seed": 415,
 "trials": 20000,
 "stim": 0.0,
 "theta": 0.0,
 "g": 1.0,
 "r": 0.5,
 "noise": 0.5,
 "tau": 0.8
}
```

## Command
`python sim_cons.py iter-5` (run from `Consciousness/simulation/`)
