# SIM-SPIRIT-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Spirit x Justice (K21): radical-healing themes came from two focus groups in each of three communities. How likely is a theme held in a minority of groups to be missed entirely?

## Sources this run draws on
K21 (Morkel, Suffla & Malherbe 2026): six focus groups across three communities.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated = analytic |
| H1 | hypothesis | 10% theme missed with p >= .5 |
| R1 | reporting | miss probability |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Independent groups; ignores within-group dynamics; says nothing about K21's analysis quality. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-B",
 "iteration": 6,
 "kind": "qual_saturation",
 "seed": 316,
 "groups": 6,
 "p_grid": [
  0.05,
  0.1,
  0.2,
  0.3,
  0.5
 ],
 "p_test": 0.1,
 "reps": 200000
}
```

## Command
`python sim_spirit.py iter-6` (run from `Spirit/simulation/`)
