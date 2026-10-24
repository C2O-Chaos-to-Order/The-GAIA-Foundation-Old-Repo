# SIM-SPIRIT-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K20 pooled 8 studies on psychedelics and death anxiety (d = 0.70) with high heterogeneity. How well do standard random-effects CIs cover the truth with so few studies?

## Sources this run draws on
K20 (Cohorst & Kajonius 2026): 8 studies, d = 0.70 [0.42, 0.97], high heterogeneity. Study sizes here are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | tau 0 coverage >= .93 |
| H1 | hypothesis | tau .4 DL coverage < .90 |
| R1 | reporting | coverage |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal approximations; two-group variance formula. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-B",
 "iteration": 2,
 "kind": "small_k_meta",
 "seed": 312,
 "k": 8,
 "mu": 0.7,
 "n_lo": 15,
 "n_hi": 60,
 "tau_grid": [
  0.0,
  0.2,
  0.4
 ],
 "tau_test": 0.4,
 "reps": 4000
}
```

## Command
`python sim_spirit.py iter-2` (run from `Spirit/simulation/`)
