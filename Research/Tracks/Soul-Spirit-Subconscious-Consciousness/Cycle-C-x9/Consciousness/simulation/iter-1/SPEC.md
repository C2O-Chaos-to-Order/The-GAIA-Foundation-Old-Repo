# SIM-CONS-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K42 (the IIT-GNWT adversarial collaboration) found results that align with some predictions of each theory while challenging key tenets of both; K41 warns against treating single failed predictions as falsification. How often does a TRUE theory fail at least one of several critical tests?

## Sources this run draws on
K42 (Cogitate Consortium 2025, Nature; n = 256; preregistered predictions); K41 (He 2025). Power, number of tests and the false-theory pass rate are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = power^m |
| H1 | hypothesis | P(>= 1 failure | true) >= .4 |
| H2 | hypothesis | posterior after 1 failure >= .5 |
| R1 | reporting | posterior by failures |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Independent tests; binary pass/fail. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 1,
 "kind": "predictions_battery",
 "seed": 811,
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
`python sim_cons.py iter-1` (run from `Consciousness/simulation/`)
