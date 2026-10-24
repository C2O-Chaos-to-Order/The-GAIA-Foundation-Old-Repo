# SIM-SPIRIT-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K49 (Barrett, Johnson & Griffiths 2015) validates the MEQ30 'complete mystical experience' criterion against the MEQ43 (Table 2). Do the reported agreement statistics follow from the table?

## Sources this run draws on
K49 Table 2 (TP 80, FP 14, FN 4, TN 86; N = 184); reported hit 0.95, false alarm 0.14, proportion correct 90.2%, d' = 3.464.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | rates reproduce |
| V2 | validation | sim hit = analytic |
| H1 | hypothesis | no convention reproduces d' within 0.1 |
| R1 | reporting | kappa, d' |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Standard signal-detection conventions only; K49 does not state its d' formula. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 1,
 "kind": "meq_contingency",
 "seed": 1201,
 "TP": 80,
 "FP": 14,
 "FN": 4,
 "TN": 86,
 "reported_dprime": 3.464,
 "reps": 20000
}
```

## Command
`python sim_spirit.py iter-1` (run from `Spirit/simulation/`)
