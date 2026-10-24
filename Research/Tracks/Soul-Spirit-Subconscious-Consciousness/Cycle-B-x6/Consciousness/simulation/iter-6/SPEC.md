# SIM-CONS-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness of SIM-CONS-A iteration 2 for K14's questionnaire: with 5-point skewed ordinal items, does Kaiser still over-extract and parallel analysis not?

## Sources this run draws on
K14 (92 items, 1,403 respondents).

## Refinement from previous iteration
Cycle A used normal items.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | PA retains 0 in >= 90% |
| H1 | hypothesis | Kaiser >= 10 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pearson correlations on ordinal items (as many applied analyses do). Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-B",
 "iteration": 6,
 "kind": "kaiser_likert",
 "seed": 416,
 "p": 92,
 "n": 1403,
 "thresholds": [
  -1.0,
  -0.2,
  0.6,
  1.4
 ],
 "reps": 12,
 "n_null": 20,
 "q": 0.95
}
```

## Command
`python sim_cons.py iter-6` (run from `Consciousness/simulation/`)
