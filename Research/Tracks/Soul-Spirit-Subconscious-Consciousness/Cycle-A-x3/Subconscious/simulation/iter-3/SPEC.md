# SIM-SUBC-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Toy version of K10's proposal (many memories reactivated in sleep, a few strung into a dream): if dreams merely sample reactivated memories, does 'dreamed items are remembered better' arise without dreams doing anything?

## Sources this run draws on
K10 (Budson & Paller 2025, memory theory of consciousness: sleep reactivation stays implicit; fragments of a subset form the dream).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean difference matches analytic expectation within 0.03 |
| H1 | hypothesis | dreamed > all other memories significant in >= 80% of studies |
| H2 | hypothesis | dreamed vs reactivated-not-dreamed significant <= 0.07 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy; reactivation gain is additive; dream selection uniform among reactivated items (K10 does not specify a selection rule). Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-A",
 "iteration": 3,
 "kind": "dream_sampling",
 "seed": 103,
 "subjects": 40,
 "memories": 100,
 "reactivated": 30,
 "dreamed": 3,
 "gain": 0.5,
 "noise": 1.0,
 "reps": 1000
}
```

## Command
`python sim_subc.py iter-3` (run from `Subconscious/simulation/`)
