# SIM-SUBC-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K34 argues that common calibration methods do not target the upper subliminal threshold. Where does a standard 1-up-2-down staircase on objective accuracy put the stimulus relative to that threshold?

## Sources this run draws on
K34 (Elbaz, Yaron & Mudrik 2025): calibration methods yielded strikingly low accuracy for the upper subliminal threshold; staircase procedure (Levitt 1971) as one of the compared methods. Observer parameters are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | analytic accuracy at theta1 |
| H1 | hypothesis | >= 80% of observers calibrated to accuracy >= .60 |
| R1 | reporting | ratio to theta1 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Weibull 2AFC observers; no lapses; one staircase rule. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 2,
 "kind": "staircase_subliminal",
 "seed": 512,
 "observers": 500,
 "a_lo": 20.0,
 "a_hi": 60.0,
 "b": 2.0,
 "eps": 0.025,
 "x0": 100.0,
 "step": 8.0,
 "trials": 80
}
```

## Command
`python sim_subc.py iter-2` (run from `Subconscious/simulation/`)
