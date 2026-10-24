# SIM-SPIRIT-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K40 describes LSD dose-response curves plateauing around 100 ug, with considerable variability between studies. Can a handful of studies distinguish a plateau from a curve that still rises?

## Sources this run draws on
K40 (Hirschfeld et al. 2023): sigmoid-like increase plateauing at around 100 ug; considerable variability; doses up to 200 ug. Curve, noise and study counts ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Emax(ED50) = Emax/2 |
| H1 | hypothesis | plateau called >= 50% |
| R1 | reporting | true rise |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Study means only; Welch t-test 200 vs 100 ug. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 4,
 "kind": "dose_plateau",
 "seed": 714,
 "doses": [
  25,
  50,
  100,
  200
 ],
 "Emax": 100.0,
 "ED50": 50.0,
 "h": 2.0,
 "sd_between": 15.0,
 "k100": 6,
 "k200": 3,
 "reps": 20000
}
```

## Command
`python sim_spirit.py iter-4` (run from `Spirit/simulation/`)
