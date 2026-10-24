# SIM-DV-SOC-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Seed replication of beta- vs sigma-convergence.

## Phase operationalization tested
SOC Divergence/convergence measured by dispersion vs slope.

## Sources this run draws on
Standard AR(1) identities; P19 now supplies the dispersion measure (SD of log income) used in this literature.

## Refinement from previous iteration
Derived from SIM-DV-SOC-C iteration 9: seed replication (only the seed changes).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean beta within 4 SE |
| H1 | hypothesis | beta < 0 by > 4 SE |
| H2 | hypothesis | SD ratio within 0.95-1.05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Replication: same parameters, new seed; the hypothesis verdicts are expected to repeat DVC's.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-D",
 "iteration": 9,
 "kind": "galton_beta",
 "seed": 18309,
 "countries": 125,
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
`python sim_soc.py iter-9` (run from `Social-Sciences/simulation/`)
