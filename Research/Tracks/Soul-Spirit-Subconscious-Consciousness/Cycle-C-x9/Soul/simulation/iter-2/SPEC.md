# SIM-SOUL-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K38's whole-brain maps used p < .001 uncorrected with a 10-voxel extent. How often does pure noise produce at least one such 'activation'?

## Sources this run draws on
K38: p < 0.001 uncorrected, k >= 10 voxels; n = 15. Grid size and smoothness ILLUSTRATIVE (a small 40x48x40 grid; real brains have more voxels, which would raise the rate).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | voxel FPR = alpha |
| H1 | hypothesis | >= 50% of null datasets show a cluster |
| R1 | reporting | mean clusters |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Gaussian noise smoothed by a Gaussian kernel; no anatomy. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 2,
 "kind": "null_clusters",
 "seed": 612,
 "n": 15,
 "grid": [
  40,
  48,
  40
 ],
 "sigma": 1.5,
 "alpha": 0.001,
 "k": 10,
 "reps": 40
}
```

## Command
`python sim_soul.py iter-2` (run from `Soul/simulation/`)
