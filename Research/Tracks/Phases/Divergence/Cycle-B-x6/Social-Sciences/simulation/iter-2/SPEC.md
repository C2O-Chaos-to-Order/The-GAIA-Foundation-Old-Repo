# SIM-DV-SOC-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same at eps = 0.4.

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Only eps and seed change from iteration 1.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | certainty mean 0.5 within 4 SE |
| H1 | hypothesis | no events within 0.1 of Eq. 6 |
| H2 | hypothesis | events within 0.1 of Eq. 6 |
| H3 | hypothesis | events add > 0.1 |
| R1 | reporting | per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-B",
 "iteration": 2,
 "kind": "siem",
 "seed": 16302,
 "agents": 490,
 "k": 8,
 "eps": 0.4,
 "T": 1000,
 "t0": 500,
 "reps": 5,
 "Ef": 0.05,
 "Ed": 10,
 "Es": 0.6,
 "cdrift": 0.1,
 "tol_se": 4,
 "h_tol": 0.1,
 "h3": 0.1
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
