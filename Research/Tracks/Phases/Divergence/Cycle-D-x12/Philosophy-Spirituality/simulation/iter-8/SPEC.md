# SIM-DV-PHI-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Faster merging (mu 0.5).

## Phase operationalization tested
PHI Divergence = differentiation paired with return (formal skeleton; P07, P08, P18).

## Sources this run draws on
P07, P08 (read in full in DVB); P18 (read in full in DVC).

## Refinement from previous iteration
Derived from SIM-DV-PHI-C iteration 5: only mu and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Yule control |
| V2 | validation | stationary mean |
| H1 | hypothesis | mean-field within 10% |
| R1 | reporting | means |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-D",
 "iteration": 8,
 "kind": "split_merge",
 "seed": 18608,
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
`python sim_phi.py iter-8` (run from `Philosophy-Spirituality/simulation/`)
