# SIM-CONS-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Consciousness x Justice. K47: Chinese neurologists' preference never to limit life-sustaining treatment differed across UWS, MCS and LIS vignettes (47%, 63%, 67%) at p = .052. Was the survey powered to detect differences of that size?

## Sources this run draws on
K47 (Li et al. 2024): 360 questionnaires, three vignette groups; 47%, 63%, 67%; p = .052. Equal groups of 120 are ILLUSTRATIVE (group sizes not used).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MC = noncentral chi-square |
| H1 | hypothesis | power < .8 |
| R1 | reporting | power by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pearson chi-square, 3 x 2. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 4,
 "kind": "chisq_3group",
 "seed": 814,
 "props": [
  0.47,
  0.63,
  0.67
 ],
 "n_per_group": 120,
 "reps": 20000,
 "n_grid": [
  120,
  200,
  300
 ]
}
```

## Command
`python sim_cons.py iter-4` (run from `Consciousness/simulation/`)
