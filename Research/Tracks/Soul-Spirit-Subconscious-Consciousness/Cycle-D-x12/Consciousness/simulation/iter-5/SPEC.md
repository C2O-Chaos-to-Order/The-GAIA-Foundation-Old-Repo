# SIM-CONS-D - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Weaker evidence bound (BF >= 3).

## Sources this run draws on
K59 (as iteration 1).

## Refinement from previous iteration
Iteration 1 used BF 10.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | <= 5% |
| H1 | hypothesis | >= 50% |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 5,
 "kind": "bf_sequential",
 "seed": 1405,
 "d_grid": [
  0.0,
  0.5,
  0.8,
  1.2
 ],
 "n_min": 9,
 "n_max": 15,
 "bound": 3,
 "reps": 1000,
 "h1": 0.5
}
```

## Command
`python sim_cons.py iter-5` (run from `Consciousness/simulation/`)
