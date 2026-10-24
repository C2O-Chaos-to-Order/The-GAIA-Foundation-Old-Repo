# SIM-SUBC-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K25 describes how subjective ('I saw nothing') and objective awareness measures give different thresholds. In a single-process model with NO unconscious route, does above-chance discrimination on subjectively unseen trials still appear?

## Sources this run draws on
K25 (Jimenez et al. 2025): subjective vs objective awareness thresholds; blindsight-style criterion (report of no awareness plus above-chance objective performance).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | d' = 0 gives 0.5 |
| V2 | validation | simulated = analytic |
| H1 | hypothesis | unseen accuracy >= .55 |
| R1 | reporting | share unseen |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Equal-variance Gaussian signal detection; visibility and discrimination read from the same evidence. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-B",
 "iteration": 5,
 "kind": "objective_subjective",
 "seed": 115,
 "d_grid": [
  0.0,
  0.5,
  1.0,
  1.5
 ],
 "d_test": 1.0,
 "c": 1.0,
 "trials": 400000
}
```

## Command
`python sim_subc.py iter-5` (run from `Subconscious/simulation/`)
