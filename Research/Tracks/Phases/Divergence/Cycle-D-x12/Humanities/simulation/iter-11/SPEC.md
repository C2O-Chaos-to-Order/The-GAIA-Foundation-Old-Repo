# SIM-DV-HUM-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Noisier distances (noise 0.5) in the geography-tree Mantel test.

## Phase operationalization tested
HUM Divergence = language divergence tracking geography (P06).

## Sources this run draws on
P06 (re-read in full in DVB).

## Refinement from previous iteration
Derived from SIM-DV-HUM-C iteration 8: only noise and seed change.

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
 "sim_id": "SIM-DV-HUM-D",
 "iteration": 11,
 "kind": "geo_tree_mantel",
 "seed": 18511,
 "depth": 4,
 "L0": 1.0,
 "noise": 0.5,
 "perms": 999,
 "reps": 400,
 "alpha": 0.05,
 "tol_se": 4,
 "h1": 0.8
}
```

## Command
`python sim_hum.py iter-11` (run from `Humanities/simulation/`)
