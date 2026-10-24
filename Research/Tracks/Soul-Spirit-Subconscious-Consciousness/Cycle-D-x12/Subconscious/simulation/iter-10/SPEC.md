# SIM-SUBC-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. A conventional small sample (100 per group), d = 0.2.

## Sources this run draws on
K63 (as iteration 1).

## Refinement from previous iteration
Iteration 1 used K63's group sizes.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | BF range |
| H1 | hypothesis | <= .05 |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-D",
 "iteration": 10,
 "kind": "bf_null_design",
 "seed": 1310,
 "n1": 100,
 "n2": 100,
 "d_grid": [
  0.0,
  0.2
 ],
 "d_test": 0.2,
 "reps": 1000,
 "h1": 0.05
}
```

## Command
`python sim_subc.py iter-10` (run from `Subconscious/simulation/`)
