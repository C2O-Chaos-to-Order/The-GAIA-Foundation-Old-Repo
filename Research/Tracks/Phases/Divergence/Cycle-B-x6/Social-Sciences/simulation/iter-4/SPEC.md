# SIM-DV-SOC-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Measurement caution for 'convergence' and 'divergence' claims: can a negative catch-up slope (beta-convergence) appear while cross-country dispersion stays constant?

## Phase operationalization tested
SOC Divergence/convergence measured as change in cross-unit dispersion (as P11 does with SDs) vs as a regression slope.

## Sources this run draws on
No source read for beta/sigma convergence in this track (economic convergence-club literature not reached); the AR(1) identities are standard statistics. Relevant to P11's dispersion measures only as a caution.

## Refinement from previous iteration
New run family (SOC economic-convergence gap).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean beta within 4 SE of rho^T - 1 |
| H1 | hypothesis | beta < 0 by > 4 SE |
| H2 | hypothesis | SD ratio within 0.95-1.05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Stationary Gaussian AR(1); not an economic model. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-B",
 "iteration": 4,
 "kind": "galton_beta",
 "seed": 16304,
 "countries": 100,
 "rho": 0.95,
 "sd_e": 0.1,
 "T": 20,
 "reps": 500,
 "sd0_mult": 1.0,
 "tol_se": 4,
 "h2_text": "within 0.95-1.05 (no sigma-convergence)",
 "h2_expr": "abs(r-1)<=0.05"
}
```

## Command
`python sim_soc.py iter-4` (run from `Social-Sciences/simulation/`)
