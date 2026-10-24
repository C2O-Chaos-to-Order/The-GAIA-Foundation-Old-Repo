# SIM-CONS-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. A pooled sample of 10,000 patients.

## Sources this run draws on
K32 (as iteration 2).

## Refinement from previous iteration
Iteration 2 tested N = 2000.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | RR 1 FPR <= .05 + 3 MC SE |
| H1 | hypothesis | power < .5 |
| R1 | reporting | power by N |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 2.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 6,
 "kind": "rare_association_power",
 "seed": 816,
 "N": 10000,
 "p_recall": 0.06,
 "p_aware_nonrecall": 0.005,
 "RR": 3.0,
 "N_grid": [
  10000,
  20000
 ],
 "reps": 1000
}
```

## Command
`python sim_cons.py iter-6` (run from `Consciousness/simulation/`)
