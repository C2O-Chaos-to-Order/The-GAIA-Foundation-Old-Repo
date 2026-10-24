# SIM-SUBC-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Refinement of SIM-SUBC-A iteration 3: if dreams preferentially sample strongly encoded reactivated memories (a selection rule K10 does not specify), does 'dreamed beats reactivated-but-not-dreamed' appear even though dreaming does nothing?

## Sources this run draws on
K10 (Budson & Paller 2025).

## Refinement from previous iteration
Cycle A used uniform selection among reactivated memories; here selection depends on encoding strength (beta).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | beta = 0 rate <= 0.07 |
| H1 | hypothesis | beta = 1: significant in >= 80% |
| R1 | reporting | by beta |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy; encoding strength drives both recall and dream selection; no causal role for dreams. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-B",
 "iteration": 3,
 "kind": "dream_selection",
 "seed": 113,
 "subjects": 40,
 "memories": 100,
 "reactivated": 30,
 "dreamed": 3,
 "gain": 0.5,
 "noise": 1.0,
 "beta_list": [
  0.0,
  0.5,
  1.0
 ],
 "beta_test": 1.0,
 "reps": 500
}
```

## Command
`python sim_subc.py iter-3` (run from `Subconscious/simulation/`)
