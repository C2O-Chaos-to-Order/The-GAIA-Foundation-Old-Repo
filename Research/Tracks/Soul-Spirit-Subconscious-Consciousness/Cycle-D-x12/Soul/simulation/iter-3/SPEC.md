# SIM-SOUL-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K55 reports that, entered together, existential 'mattering' 'fully mediated' the effects of comprehension and purpose on mind-upload approval. Does that pattern follow from the published correlation matrix alone?

## Sources this run draws on
K55 Table 2 zero-order correlations (comprehension-purpose .62, comprehension-mattering .57, purpose-mattering .53; with approval -.09, -.08, -.19).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim betas = analytic |
| H1 | hypothesis | comprehension and purpose betas within +/-.03 |
| R1 | reporting | betas |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Standardised OLS; K55's unstandardised B values are not reproduced. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 3,
 "kind": "collinear_betas",
 "seed": 1103,
 "R_xx": [
  [
   1,
   0.62,
   0.57
  ],
  [
   0.62,
   1,
   0.53
  ],
  [
   0.57,
   0.53,
   1
  ]
 ],
 "r_xy": [
  -0.09,
  -0.08,
  -0.19
 ],
 "n": 500000,
 "h1": 0.03
}
```

## Command
`python sim_soul.py iter-3` (run from `Soul/simulation/`)
