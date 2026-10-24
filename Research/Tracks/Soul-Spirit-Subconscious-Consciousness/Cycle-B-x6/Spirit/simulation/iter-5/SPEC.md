# SIM-SPIRIT-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K20's meta-regression found mystical experience associated with larger death-anxiety reductions (B = 4.90, p = .050) across few studies. How often does a null moderator reach p < .05 with 8 studies under heterogeneity?

## Sources this run draws on
K20 (meta-regression B = 4.90, p = 0.050; 8 studies). The estimator K20 used is not re-run.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | tau 0 FE FPR ~ .05 |
| H1 | hypothesis | tau .4 FE FPR > .10 |
| R1 | reporting | FPRs |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One continuous moderator; DL-type tau for the t-test. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-B",
 "iteration": 5,
 "kind": "metareg_k8",
 "seed": 315,
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
 "reps": 6000
}
```

## Command
`python sim_spirit.py iter-5` (run from `Spirit/simulation/`)
