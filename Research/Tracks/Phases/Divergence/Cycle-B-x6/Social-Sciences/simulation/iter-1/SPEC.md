# SIM-DV-SOC-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
SIEM approximation follow-up: does doubling links per step (k = 8) change the DVA results against P03's Eq. 6?

## Phase operationalization tested
SOC Divergence = sustained polarisation under homophily and external events (P03).

## Sources this run draws on
P03 (Condie & Condie 2021; read in full in DVA).

## Refinement from previous iteration
DVA iteration 1 used k = 4 (P03's default not stated in the text read); only k and seed change.

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
As DVA: not P03's code. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-B",
 "iteration": 1,
 "kind": "siem",
 "seed": 16301,
 "agents": 490,
 "k": 8,
 "eps": 0.2,
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
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
