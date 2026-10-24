# SIM-SOUL-D - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K53 validated the veridical NDE scale on 17 cases with 14 raters (Krippendorff alpha 0.49, 95% CI 0.40-0.58). How precise is alpha with 17 cases?

## Sources this run draws on
K53: 17 cases, 11 human + 3 LLM raters, four-level ratings, overall alpha 0.49 (0.40-0.58). Latent model and cut points ILLUSTRATIVE (latent ICC 0.5 gives alpha near 0.45).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | alpha(perfect) = 1 |
| H1 | hypothesis | 95% range of alpha >= .15 |
| R1 | reporting | quantiles |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Interval-metric alpha on ordinal ratings; raters exchangeable. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 5,
 "kind": "alpha_precision",
 "seed": 1105,
 "cases": 17,
 "raters": 14,
 "latent_icc": 0.5,
 "cuts": [
  -0.8,
  0.0,
  0.8
 ],
 "reps": 2000,
 "h1": 0.15
}
```

## Command
`python sim_soul.py iter-5` (run from `Soul/simulation/`)
