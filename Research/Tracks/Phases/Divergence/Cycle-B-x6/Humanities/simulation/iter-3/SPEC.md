# SIM-DV-HUM-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same noise with 16 languages: does doubling the number of languages restore power?

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Only depth (8 -> 16 tips) and seed change from iteration 2.

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
 "iteration": 3,
 "kind": "geo_tree_mantel",
 "seed": 16503,
 "depth": 4,
 "L0": 1.0,
 "noise": 1.0,
 "perms": 999,
 "reps": 400,
 "alpha": 0.05,
 "tol_se": 4,
 "h1": 0.8
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
