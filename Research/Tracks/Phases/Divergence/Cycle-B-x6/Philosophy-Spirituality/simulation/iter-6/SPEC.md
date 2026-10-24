# SIM-DV-PHI-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Schism-tree imbalance with stronger heritable rate variation (het = 1.0).

## Phase operationalization tested
PHI Divergence = denominational branching as a tree (P14).

## Sources this run draws on
P14 (read in full in DVA).

## Refinement from previous iteration
DVA used het = 0.5; only het and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Yule count within 4 SE |
| H1 | hypothesis | heritable rates raise Colless > 4 SE |
| R1 | reporting | results |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA: pure birth. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-B",
 "iteration": 6,
 "kind": "schism_yule",
 "seed": 16606,
 "lam": 1.0,
 "T": 3.0,
 "tips": 30,
 "het": 1.0,
 "reps": 1000,
 "cap": 2000,
 "tol_se": 4
}
```

## Command
`python sim_phi.py iter-6` (run from `Philosophy-Spirituality/simulation/`)
