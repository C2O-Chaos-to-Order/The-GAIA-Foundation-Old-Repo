# SIM-SPIRIT-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Refinement: if acute effects DO have a modest causal effect (0.2) plus the common cause, how much of the observed correlation is causal?

## Sources this run draws on
K39 (as iteration 1).

## Refinement from previous iteration
Iteration 1 had no causal ASE effect.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim r = analytic |
| H1 | hypothesis | r >= .30 |
| R1 | reporting | share significant |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 5,
 "kind": "mediation_confound",
 "seed": 715,
 "n": 100,
 "confound": 0.8,
 "direct_ase": 0.2,
 "reps": 2000
}
```

## Command
`python sim_spirit.py iter-5` (run from `Spirit/simulation/`)
