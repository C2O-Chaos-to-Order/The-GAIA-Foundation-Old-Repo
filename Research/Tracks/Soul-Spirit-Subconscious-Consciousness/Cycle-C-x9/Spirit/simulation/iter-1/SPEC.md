# SIM-SPIRIT-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K39 notes strong correlations between acute subjective (mystical) effects and lasting therapeutic outcomes, while pharmacology studies question whether those effects are necessary. Can a common cause alone produce a correlation of that kind?

## Sources this run draws on
K39 (Atiq et al. 2025): correlations between acute subjective effects and enduring outcomes; non-hallucinogenic psychoplastogens effective in preclinical models. Path values ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim r = analytic |
| H1 | hypothesis | r >= .30 with no ASE effect |
| R1 | reporting | share significant |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Linear-normal common-cause model. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 1,
 "kind": "mediation_confound",
 "seed": 711,
 "n": 100,
 "confound": 0.8,
 "direct_ase": 0.0,
 "reps": 2000
}
```

## Command
`python sim_spirit.py iter-1` (run from `Spirit/simulation/`)
