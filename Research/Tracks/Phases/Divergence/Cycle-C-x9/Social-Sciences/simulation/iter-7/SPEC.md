# SIM-DV-SOC-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Two clubs with equal mean growth (g_b = g_a): does overall divergence still appear from the rest's heterogeneity alone?

## Phase operationalization tested
As iteration 6.

## Sources this run draws on
P19 (Pritchett 1997, 'Divergence, Big Time', J. Econ. Perspectives 11(3):3-17; read in full in DVC from a third-party-hosted JSTOR copy): within the 'advanced capitalist' sample 'something like convergence ... is almost tautological' (De Long 1988, as reported); the SD of log GDP per capita across all countries rose. The random-walk model is the agent's, not P19's.

## Refinement from previous iteration
Only g_b and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | finite positive ratios |
| H1 | hypothesis | club A within-SD ratio < 1 by > 4 SE |
| H2 | hypothesis | overall SD ratio > 1.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 6. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-C",
 "iteration": 7,
 "kind": "two_clubs",
 "seed": 17307,
 "reps": 500,
 "n_a": 17,
 "n_b": 108,
 "ya0": 0.5,
 "yb0": -0.5,
 "sd_a0": 0.4,
 "sd_b0": 0.4,
 "T": 12,
 "g_a": 0.15,
 "g_b": 0.15,
 "beta_a": -0.05,
 "beta_b": 0.0,
 "sd_ea": 0.05,
 "sd_eb": 0.2,
 "tol_se": 4,
 "h2": 1.5
}
```

## Command
`python sim_soc.py iter-7` (run from `Social-Sciences/simulation/`)
