# SIM-SPIRIT-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K52 pools 16 effect sizes (8 studies) on death anxiety after psychedelics: d = 0.70 [0.42, 0.97], I^2 = 96.3%. What does the prediction interval look like?

## Sources this run draws on
K52: d = 0.70 (95% CI 0.42-0.97), k = 16, I^2 = 96.3%.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | coverage >= .95 |
| H1 | hypothesis | PI includes 0 |
| R1 | reporting | tau, PI |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Assumes equal within-study variances and ignores the dependence of 16 effects from 8 studies. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 6,
 "kind": "meta_pi",
 "seed": 1206,
 "k": 16,
 "d": 0.7,
 "ci": [
  0.42,
  0.97
 ],
 "I2": 0.963,
 "reps": 400000
}
```

## Command
`python sim_spirit.py iter-6` (run from `Spirit/simulation/`)
