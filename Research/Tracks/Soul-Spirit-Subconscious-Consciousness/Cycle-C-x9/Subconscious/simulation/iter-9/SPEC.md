# SIM-SUBC-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Does doubling trials per level (128) remove the naive rule's overestimation?

## Sources this run draws on
K34 (as iteration 3).

## Refinement from previous iteration
Iteration 3 used 64 trials per level.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | binomial sanity |
| H1 | hypothesis | overestimates in >= 50% |
| R1 | reporting | exact share |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 3.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 9,
 "kind": "constant_stimuli_threshold",
 "seed": 519,
 "levels": [
  0,
  8.33,
  16.67,
  25,
  33.33,
  58.33,
  100,
  141.7,
  200
 ],
 "n_per": 128,
 "a_lo": 20.0,
 "a_hi": 80.0,
 "b": 2.0,
 "lapse": 0.02,
 "eps": 0.025,
 "alpha": 0.05,
 "observers": 2000
}
```

## Command
`python sim_subc.py iter-9` (run from `Subconscious/simulation/`)
