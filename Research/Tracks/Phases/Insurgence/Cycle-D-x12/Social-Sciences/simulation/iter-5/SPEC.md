# SIM-IN-SOC-D - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Region 3 (P40: both spread fully, random faster): (0.6, 0.9) and (0.8, 1.0) at k = 4, T = 1.

## Phase operationalization tested
SOC Insurgence = a costly behaviour (such as joining a protest) spreading through a network by social reinforcement (complex contagion, P40).

## Sources this run draws on
P40 (Wan, Riedl & Lazer 2025, PNAS 122:e2422892122, CC BY-NC-ND 4.0; read in full in IND, SI not read): adoption rule p(c), ring lattice vs rewired random regular networks, n = 250 k, p1* = 1 - (1 - 1/(k - 1))^(1/T); clustered networks outperform random by 5% in at most 22% of the p1 <= p2 space; minimal p2/p1 = 1.90 where clustering helps.

## Refinement from previous iteration
Iteration 5 of the x12 family for SOC; follows iteration 4 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | shares in [0, 1] |
| H1 | hypothesis | both >= 0.6, random faster |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
50 trials. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-D",
 "iteration": 5,
 "kind": "complex_contagion",
 "seed": 23305,
 "k": 4,
 "i": 2,
 "T": 1,
 "trials": 50,
 "pairs": [
  [
   0.6,
   0.9
  ],
  [
   0.8,
   1.0
  ]
 ],
 "h1_text": "both networks reach >= 0.6 and random reaches 60% in fewer steps",
 "h1_expr": "all(v['clustered'] >= 0.6 and v['random'] >= 0.6 and v['t60_random'] is not None and v['t60_clustered'] is not None and v['t60_random'] < v['t60_clustered'] for v in o.values())"
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
