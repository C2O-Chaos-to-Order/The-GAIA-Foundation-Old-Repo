# SIM-DV-HUM-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Reproduce P12's binomial threshold for a recurrent sound correspondence (worked example 0.0032) and check whether alpha = 0.01 reproduces its Figure 5 ranges.

## Phase operationalization tested
HUM Divergence = distinguishing inherited (cognate) correspondences from chance among diverged languages.

## Sources this run draws on
P12 (read in full): Eq. 11-13, worked English-French /f/-/p/ example, Figure 5 ranges [0.0002, 0.0015) and [0.0015, 0.0043).

## Refinement from previous iteration
New run family within HUM (second P12 principle).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | exact = 0.0032 (4 d.p.) |
| V2 | validation | MC within 4 SE |
| H1 | hypothesis | alpha 0.01 reproduces both ranges on the 0.0001 grid |
| R1 | reporting | ranges |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
P12 does not state alpha for Figure 5; alpha = 0.01 is our reading, pre-registered. Half-open intervals read as the last grid point below the bound. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-A",
 "iteration": 2,
 "kind": "recurrence_threshold",
 "seed": 15502,
 "n": 100,
 "mc": 1000000,
 "alpha": 0.01,
 "tol_se": 4
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
