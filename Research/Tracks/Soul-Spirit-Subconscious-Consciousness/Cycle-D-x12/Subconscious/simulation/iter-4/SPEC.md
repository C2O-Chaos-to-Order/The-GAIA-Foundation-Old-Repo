# SIM-SUBC-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Informativeness against d = 0.3.

## Sources this run draws on
K63 (as iteration 1).

## Refinement from previous iteration
Iteration 1 tested d = 0.2.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | BF range |
| H1 | hypothesis | P(BF01>=3|d=.3) <= .05 |
| R1 | reporting | rates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-D",
 "iteration": 4,
 "kind": "bf_null_design",
 "seed": 1304,
 "n1": 309,
 "n2": 272,
 "d_grid": [
  0.3
 ],
 "d_test": 0.3,
 "reps": 1000,
 "h1": 0.05
}
```

## Command
`python sim_subc.py iter-4` (run from `Subconscious/simulation/`)
