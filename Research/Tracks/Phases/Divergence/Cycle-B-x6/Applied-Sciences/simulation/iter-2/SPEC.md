# SIM-DV-APP-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Control: with no driver advantage (sd = 0) driver labels are neutral, so shares should not differ by CCF class.

## Phase operationalization tested
As iteration 1 (control).

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Only sd, H1 mode and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mutations per birth within 4 SE |
| H1 | hypothesis | no enrichment within 4 binomial SE |
| R1 | reporting | shares |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1; binomial SE ignores clustering of mutations within clones, so it is optimistic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-B",
 "iteration": 2,
 "kind": "bep_drivers",
 "seed": 16402,
 "reps": 40,
 "N": 10000,
 "b0": 0.5,
 "d0": 0.3,
 "sd": 0.0,
 "u": 1.0,
 "q": 0.05,
 "hi": 0.5,
 "lo_min": 0.01,
 "lo_max": 0.3,
 "tol_se": 4,
 "h1": 2.0,
 "h1_mode": "null"
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
