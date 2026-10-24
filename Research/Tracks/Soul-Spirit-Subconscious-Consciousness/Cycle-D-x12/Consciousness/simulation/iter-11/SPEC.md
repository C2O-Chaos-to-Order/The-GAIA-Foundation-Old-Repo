# SIM-CONS-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K59 pre-registers three questions (location, timing, connectivity) on which GNWT and IIT diverge, as K42 did. With three tests at power .8, how often does a true theory fail at least one, and what does one failure do to its posterior?

## Sources this run draws on
K59 (questions Q1-Q3), K42 (as in Cycle C).

## Refinement from previous iteration
Same model as SIM-CONS-C iteration 1, applied to K59's design.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = power^m |
| H1 | hypothesis | P(>= 1 failure) >= .4 |
| H2 | hypothesis | posterior after 1 failure >= .5 |
| R1 | reporting | posterior |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Independent tests; K59's predictions are weighted and correlated. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 11,
 "kind": "predictions_battery",
 "seed": 1411,
 "m": 3,
 "power": 0.8,
 "q_false": 0.3,
 "prior": 0.5,
 "f_test": 1,
 "h2_threshold": 0.5,
 "reps": 200000
}
```

## Command
`python sim_cons.py iter-11` (run from `Consciousness/simulation/`)
