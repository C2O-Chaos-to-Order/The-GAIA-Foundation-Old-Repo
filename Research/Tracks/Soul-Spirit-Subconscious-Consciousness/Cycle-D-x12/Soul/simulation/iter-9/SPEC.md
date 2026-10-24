# SIM-SOUL-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Uncertain vs believers (-0.28 vs -0.20 [-0.37, -0.04]).

## Sources this run draws on
K55 (as iteration 4).

## Refinement from previous iteration
Iteration 4 compared uncertain vs no afterlife.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim z = analytic |
| H1 | hypothesis | |z| < 1.96 |
| R1 | reporting | z, p |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 9,
 "kind": "slope_diff",
 "seed": 1109,
 "b1": -0.28,
 "ci1": [
  -0.43,
  -0.12
 ],
 "b2": -0.2,
 "ci2": [
  -0.37,
  -0.04
 ],
 "reps": 500000
}
```

## Command
`python sim_soul.py iter-9` (run from `Soul/simulation/`)
