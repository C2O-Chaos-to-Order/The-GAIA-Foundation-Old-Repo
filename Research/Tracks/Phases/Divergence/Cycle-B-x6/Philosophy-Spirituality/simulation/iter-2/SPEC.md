# SIM-DV-PHI-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Stronger return (mu = 0.5, x = 4): does the mean-field estimate fail when multiplicity is small?

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Only mu and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Yule control |
| V2 | validation | stationary mean |
| H1 | hypothesis | mean-field within 10% |
| R1 | reporting | means |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-B",
 "iteration": 2,
 "kind": "split_merge",
 "seed": 16602,
 "lam": 1.0,
 "mu": 0.5,
 "Ty": 3.0,
 "reps_y": 2000,
 "T": 30.0,
 "reps": 2000,
 "tol_se": 4
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
