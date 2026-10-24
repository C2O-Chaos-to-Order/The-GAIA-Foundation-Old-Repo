# SIM-CONS-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle D iteration with changed assumptions; it is not a new source-based question. Auxiliary verified with probability 0.9.

## Sources this run draws on
K58 (as iteration 2).

## Refinement from previous iteration
Iteration 2 used q 0.5.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | analytic |
| H1 | hypothesis | >= .4 |
| R1 | reporting | posterior |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 2.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 7,
 "kind": "auxiliary_test",
 "seed": 1407,
 "q_grid": [
  0.5,
  0.9
 ],
 "prior": 0.5,
 "power": 0.8,
 "f_aux": 0.5,
 "q_test": 0.9,
 "reps": 1000000,
 "h1": 0.4
}
```

## Command
`python sim_cons.py iter-7` (run from `Consciousness/simulation/`)
