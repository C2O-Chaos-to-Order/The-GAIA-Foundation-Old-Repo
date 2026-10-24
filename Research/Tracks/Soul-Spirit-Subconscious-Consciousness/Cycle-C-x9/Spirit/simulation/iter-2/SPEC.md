# SIM-SPIRIT-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K45 retained 379 of 654 participants at the post-experience time point. If dropout depends on how the experience went, how far can a completer-only correlation drift?

## Sources this run draws on
K45 (Lipson et al. 2026): 654 at Timepoint 1, 379 at Timepoint 3; attrition bias named as a limitation. True correlation (.2) and dropout strength ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | random dropout unbiased |
| H1 | hypothesis | |shift| >= .05 at m 1 |
| R1 | reporting | by m |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Logistic selection on the outcome only. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 2,
 "kind": "attrition_mnar",
 "seed": 712,
 "n": 654,
 "rho": 0.2,
 "m_grid": [
  0.0,
  0.5,
  1.0
 ],
 "m_test": 1.0,
 "retain_target": 0.5795,
 "reps": 1000
}
```

## Command
`python sim_spirit.py iter-2` (run from `Spirit/simulation/`)
