# SIM-DV-SOC-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Contrast: start with twice the stationary dispersion, so dispersion truly shrinks; beta is the same.

## Phase operationalization tested
As iteration 4.

## Sources this run draws on
As iteration 4.

## Refinement from previous iteration
Only initial dispersion, H2 and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean beta within 4 SE |
| H1 | hypothesis | beta < 0 by > 4 SE |
| H2 | hypothesis | SD ratio < 0.8 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-B",
 "iteration": 5,
 "kind": "galton_beta",
 "seed": 16305,
 "countries": 100,
 "rho": 0.95,
 "sd_e": 0.1,
 "T": 20,
 "reps": 500,
 "sd0_mult": 2.0,
 "tol_se": 4,
 "h2_text": "below 0.8 (real sigma-convergence)",
 "h2_expr": "r<0.8"
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
