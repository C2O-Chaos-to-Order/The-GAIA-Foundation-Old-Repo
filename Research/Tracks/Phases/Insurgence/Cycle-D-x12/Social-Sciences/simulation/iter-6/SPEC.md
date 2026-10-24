# SIM-IN-SOC-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Deterministic complex contagion (p1 = 0, p2 = 1; the classic case where clustering wins): clustered minus random >= 0.5?

## Phase operationalization tested
SOC Insurgence = a costly behaviour (such as joining a protest) spreading through a network by social reinforcement (complex contagion, P40).

## Sources this run draws on
P40 (Wan, Riedl & Lazer 2025, PNAS 122:e2422892122, CC BY-NC-ND 4.0; read in full in IND, SI not read): adoption rule p(c), ring lattice vs rewired random regular networks, n = 250 k, p1* = 1 - (1 - 1/(k - 1))^(1/T); clustered networks outperform random by 5% in at most 22% of the p1 <= p2 space; minimal p2/p1 = 1.90 where clustering helps.

## Refinement from previous iteration
Iteration 6 of the x12 family for SOC; follows iteration 5 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | shares in [0, 1] |
| H1 | hypothesis | clustered >> random |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
50 trials. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-D",
 "iteration": 6,
 "kind": "complex_contagion",
 "seed": 23306,
 "k": 4,
 "i": 2,
 "T": 1,
 "trials": 50,
 "pairs": [
  [
   0.0,
   1.0
  ]
 ],
 "h1_text": "clustered share exceeds random by at least 0.5",
 "h1_expr": "o['0.0,1.0']['clustered'] - o['0.0,1.0']['random'] >= 0.5"
}
```

## Command
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
