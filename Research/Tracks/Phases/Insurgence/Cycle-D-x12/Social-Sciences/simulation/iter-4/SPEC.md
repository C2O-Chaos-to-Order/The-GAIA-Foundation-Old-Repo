# SIM-IN-SOC-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Epidemic-like threshold on random networks (P40: p1* = 1/3 at k = 4, T = 1): simple contagion p1 = p2 from 0.2 to 0.5.

## Phase operationalization tested
SOC Insurgence = a costly behaviour (such as joining a protest) spreading through a network by social reinforcement (complex contagion, P40).

## Sources this run draws on
P40 (Wan, Riedl & Lazer 2025, PNAS 122:e2422892122, CC BY-NC-ND 4.0; read in full in IND, SI not read): adoption rule p(c), ring lattice vs rewired random regular networks, n = 250 k, p1* = 1 - (1 - 1/(k - 1))^(1/T); clustered networks outperform random by 5% in at most 22% of the p1 <= p2 space; minimal p2/p1 = 1.90 where clustering helps.

## Refinement from previous iteration
Iteration 4 of the x12 family for SOC; follows iteration 3 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | shares in [0, 1] |
| H1 | hypothesis | transition near p1* |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
50 trials per value. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-D",
 "iteration": 4,
 "kind": "complex_contagion",
 "seed": 23304,
 "k": 4,
 "i": 2,
 "T": 1,
 "trials": 50,
 "pairs": [
  [
   0.2,
   0.2
  ],
  [
   0.25,
   0.25
  ],
  [
   0.3,
   0.3
  ],
  [
   0.35,
   0.35
  ],
  [
   0.4,
   0.4
  ],
  [
   0.45,
   0.45
  ],
  [
   0.5,
   0.5
  ]
 ],
 "h1_text": "random-network share < 0.2 at p <= 0.25 and > 0.5 at p >= 0.45",
 "h1_expr": "all(o[q]['random'] < 0.2 for q in ['0.2,0.2', '0.25,0.25']) and all(o[q]['random'] > 0.5 for q in ['0.45,0.45', '0.5,0.5'])"
}
```

## Command
`python sim_soc.py iter-4` (run from `Social-Sciences/simulation/`)
