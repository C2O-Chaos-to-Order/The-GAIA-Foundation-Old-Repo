# SIM-DV-HUM-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Low-noise end of the power curve for eight tips (noise sd 0.25).

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Only noise and seed change from iteration 1. (The recurrence-threshold follow-up was not run: that kind's checks are tied to P12's n = 100 table, so changing n would break its validation; disclosed.)

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | null rate |
| H1 | hypothesis | power >= 0.8 |
| R1 | reporting | power |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-B",
 "iteration": 6,
 "kind": "geo_tree_mantel",
 "seed": 16506,
 "depth": 3,
 "L0": 1.0,
 "noise": 0.25,
 "perms": 999,
 "reps": 400,
 "alpha": 0.05,
 "tol_se": 4,
 "h1": 0.8
}
```

## Command
`python sim_hum.py iter-6` (run from `Humanities/simulation/`)
