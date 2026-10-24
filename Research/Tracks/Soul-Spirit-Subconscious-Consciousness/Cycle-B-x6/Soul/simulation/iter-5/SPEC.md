# SIM-SOUL-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K17 pooled five failed mortality-salience replications; K18's bias-corrected estimates go as low as nonsignificance. Against which effect sizes is a pooled null of that size informative?

## Sources this run draws on
K17 (Treger, Benau & Timko 2023): five studies, pooled effects not different from zero; K18 (Schindler et al. 2023): g = 0.34 [0.26, 0.41], bias-corrected range -0.36 to 0.15. n per group (50) is ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated = analytic |
| H1 | hypothesis | power(.34) >= .95 |
| H2 | hypothesis | power(.15) < .5 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Fixed-effect pooling; equal n; illustrative. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-B",
 "iteration": 5,
 "kind": "pooled_null_power",
 "seed": 215,
 "k": 5,
 "n_per_group": 50,
 "g_grid": [
  0.15,
  0.34
 ],
 "reps": 20000
}
```

## Command
`python sim_soul.py iter-5` (run from `Soul/simulation/`)
