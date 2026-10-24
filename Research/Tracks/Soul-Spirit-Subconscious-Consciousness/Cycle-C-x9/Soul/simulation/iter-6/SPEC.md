# SIM-SOUL-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Smoother noise (sigma 2.5 voxels) as in more heavily smoothed fMRI.

## Sources this run draws on
K38 (as iteration 2).

## Refinement from previous iteration
Iteration 2 used sigma 1.5.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | voxel FPR |
| H1 | hypothesis | >= 50% |
| R1 | reporting | mean clusters |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 2.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 6,
 "kind": "null_clusters",
 "seed": 616,
 "n": 15,
 "grid": [
  40,
  48,
  40
 ],
 "sigma": 2.5,
 "alpha": 0.001,
 "k": 10,
 "reps": 40
}
```

## Command
`python sim_soul.py iter-6` (run from `Soul/simulation/`)
