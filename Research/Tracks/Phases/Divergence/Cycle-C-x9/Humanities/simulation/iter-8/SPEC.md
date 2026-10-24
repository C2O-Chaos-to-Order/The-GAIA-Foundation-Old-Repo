# SIM-DV-HUM-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Power of a geography-tree Mantel test with 16 languages and low noise (0.25).

## Phase operationalization tested
HUM Divergence = language divergence tracking geography (P06).

## Sources this run draws on
P06 (re-read in full in DVB).

## Refinement from previous iteration
depth 3 -> 4 at noise 0.25.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | null rate |
| H1 | hypothesis | power >= 0.8 |
| R1 | reporting | power |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-C",
 "iteration": 8,
 "kind": "geo_tree_mantel",
 "seed": 17508,
 "depth": 4,
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
`python sim_hum.py iter-8` (run from `Humanities/simulation/`)
