# SIM-CONS-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
With 12 true factors in 92 items and n = 1,403, how strong must loadings be for parallel analysis to recover 12, and what loading makes '12 components explain 44%' consistent?

## Sources this run draws on
K14 (dimensions as above).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | lambda .75 recovers k in >= 90% |
| H1 | hypothesis | lambda .6 recovers exactly 12 in >= 90% |
| H2 | hypothesis | lambda .6: first 12 components explain .44 +- .05 |
| R1 | reporting | variance explained by lambda |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Simple structure, equal loadings, orthogonal factors; principal components for variance explained. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-A",
 "iteration": 3,
 "kind": "factor_recovery",
 "seed": 403,
 "p": 92,
 "k": 12,
 "n": 1403,
 "lambda_grid": [
  0.4,
  0.5,
  0.6,
  0.75
 ],
 "lambda_test": 0.6,
 "reps": 10,
 "n_null": 20,
 "q": 0.95
}
```

## Command
`python sim_cons.py iter-3` (run from `Consciousness/simulation/`)
