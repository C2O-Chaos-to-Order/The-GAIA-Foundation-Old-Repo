# SIM-DV-SOC-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Seed replication of the selection-convergence run.

## Phase operationalization tested
SOC Divergence = widening dispersion of incomes across countries (P19), and how sample selection can hide it.

## Sources this run draws on
P19 (Pritchett 1997, 'Divergence, Big Time', J. Econ. Perspectives 11(3):3-17; read in full in DVC from a third-party-hosted JSTOR copy): within the 'advanced capitalist' sample 'something like convergence ... is almost tautological' (De Long 1988, as reported); the SD of log GDP per capita across all countries rose. The random-walk model is the agent's, not P19's.

## Refinement from previous iteration
Derived from SIM-DV-SOC-C iteration 1: seed replication (only the seed changes).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | full-sample slope within 4 SE of (1+beta)^T - 1 |
| H1 | hypothesis | selected-sample slope below full-sample slope by > 4 SE |
| H2 | hypothesis | full-sample SD ratio > 1.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Twelve ten-year periods, growth sd 0.15 per period: agent's choices. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Replication: same parameters, new seed; the hypothesis verdicts are expected to repeat DVC's.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-D",
 "iteration": 1,
 "kind": "selection_convergence",
 "seed": 18301,
 "countries": 125,
 "T": 12,
 "reps": 500,
 "sd0": 0.4,
 "g": 0.15,
 "beta": 0.0,
 "sd_e": 0.15,
 "top_k": 17,
 "tol_se": 4,
 "h2_text": "> 1.5 (P19-like widening)",
 "h2_expr": "r>1.5"
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
