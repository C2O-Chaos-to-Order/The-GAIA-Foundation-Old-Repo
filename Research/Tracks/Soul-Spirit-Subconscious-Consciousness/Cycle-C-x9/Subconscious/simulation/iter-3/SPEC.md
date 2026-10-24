# SIM-SUBC-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Using K34's empirical design (9 mask ISIs, 64 trials each), how often does the naive rule 'highest level not significantly above chance' overestimate the subliminal threshold?

## Sources this run draws on
K34: 9 ISIs (0-200 ms), 64 trials each; concern that threshold overestimation leads to overestimating the functions of consciousness. Psychometric parameters ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | binomial sanity |
| H1 | hypothesis | overestimates in >= 50% |
| R1 | reporting | exact share, mean difference |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Weibull observers; one-sided binomial test per level. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 3,
 "kind": "constant_stimuli_threshold",
 "seed": 513,
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
 "n_per": 64,
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
`python sim_subc.py iter-3` (run from `Subconscious/simulation/`)
