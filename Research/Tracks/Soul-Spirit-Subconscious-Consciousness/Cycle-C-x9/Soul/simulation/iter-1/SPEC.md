# SIM-SOUL-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K38 imaged 15 people reliving 'recalled experiences of death' and reports no activation in primary sensorimotor or limbic areas. At n = 15 and p < .001, how informative is a non-significant region?

## Sources this run draws on
K38 (Ruiz et al. 2026): n = 15; whole-brain threshold p < 0.001 uncorrected, k >= 10. Effect sizes ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MC = noncentral t |
| H1 | hypothesis | power(n 15, d .8) < .5 |
| R1 | reporting | grid |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Voxel/ROI-level one-sample test; ignores smoothing and small-volume correction. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 1,
 "kind": "small_n_power",
 "seed": 611,
 "n_grid": [
  15,
  30,
  60
 ],
 "d_grid": [
  0.5,
  0.8,
  1.0
 ],
 "alpha": 0.001,
 "n_test": 15,
 "d_test": 0.8,
 "reps": 200000
}
```

## Command
`python sim_soul.py iter-1` (run from `Soul/simulation/`)
