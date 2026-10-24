# SIM-DV-PHI-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Schism-tree imbalance with weak heritable rate variation (het 0.25).

## Phase operationalization tested
PHI Divergence = denominational branching as a tree (P14).

## Sources this run draws on
P14 (read in full in DVA).

## Refinement from previous iteration
het -> 0.25.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Yule count within 4 SE |
| H1 | hypothesis | heritable rates raise Colless > 4 SE |
| R1 | reporting | results |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-C",
 "iteration": 8,
 "kind": "schism_yule",
 "seed": 17608,
 "lam": 1.0,
 "T": 3.0,
 "tips": 30,
 "het": 0.25,
 "reps": 1000,
 "cap": 2000,
 "tol_se": 4
}
```

## Command
`python sim_phi.py iter-8` (run from `Philosophy-Spirituality/simulation/`)
