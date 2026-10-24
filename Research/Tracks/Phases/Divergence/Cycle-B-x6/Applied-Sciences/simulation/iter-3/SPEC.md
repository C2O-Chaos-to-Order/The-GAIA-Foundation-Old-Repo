# SIM-DV-APP-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Stronger drivers (sd = 1.0).

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Only sd and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mutations per birth within 4 SE |
| H1 | hypothesis | driver share high-CCF >= 2x low-CCF |
| R1 | reporting | shares |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-B",
 "iteration": 3,
 "kind": "bep_drivers",
 "seed": 16403,
 "reps": 40,
 "N": 10000,
 "b0": 0.5,
 "d0": 0.3,
 "sd": 1.0,
 "u": 1.0,
 "q": 0.05,
 "hi": 0.5,
 "lo_min": 0.01,
 "lo_max": 0.3,
 "tol_se": 4,
 "h1": 2.0,
 "h1_mode": "enrich"
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
