# SIM-SOUL-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Would doubling K38's sample (n = 30) make a non-significant region informative at d = 0.8?

## Sources this run draws on
K38 (as iteration 1).

## Refinement from previous iteration
Iteration 1 tested n = 15.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MC = noncentral t |
| H1 | hypothesis | power(n 30, d .8) < .5 |
| R1 | reporting | grid |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 7,
 "kind": "small_n_power",
 "seed": 617,
 "n_grid": [
  15,
  20,
  30,
  40,
  60
 ],
 "d_grid": [
  0.5,
  0.8
 ],
 "alpha": 0.001,
 "n_test": 30,
 "d_test": 0.8,
 "reps": 200000
}
```

## Command
`python sim_soul.py iter-7` (run from `Soul/simulation/`)
