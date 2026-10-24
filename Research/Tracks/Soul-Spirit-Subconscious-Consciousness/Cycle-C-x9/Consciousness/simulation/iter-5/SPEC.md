# SIM-CONS-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Refinement: with five critical tests at power .9, does a true theory still often fail one?

## Sources this run draws on
K42, K41 (as iteration 1).

## Refinement from previous iteration
Iteration 1 used three tests at power .8.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = power^m |
| H1 | hypothesis | P(>= 1 failure) >= .4 |
| H2 | hypothesis | posterior after 1 failure >= .5 |
| R1 | reporting | posterior |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 5,
 "kind": "predictions_battery",
 "seed": 815,
 "m": 5,
 "power": 0.9,
 "q_false": 0.3,
 "prior": 0.5,
 "f_test": 1,
 "h2_threshold": 0.5,
 "reps": 200000
}
```

## Command
`python sim_cons.py iter-5` (run from `Consciousness/simulation/`)
