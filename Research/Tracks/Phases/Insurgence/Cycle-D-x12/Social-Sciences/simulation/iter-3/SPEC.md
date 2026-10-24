# SIM-IN-SOC-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Higher degree (k = 6): does clustering help only where p2/p1 >= 1.9 (P40's minimum ratio)?

## Phase operationalization tested
SOC Insurgence = a costly behaviour (such as joining a protest) spreading through a network by social reinforcement (complex contagion, P40).

## Sources this run draws on
P40 (Wan, Riedl & Lazer 2025, PNAS 122:e2422892122, CC BY-NC-ND 4.0; read in full in IND, SI not read): adoption rule p(c), ring lattice vs rewired random regular networks, n = 250 k, p1* = 1 - (1 - 1/(k - 1))^(1/T); clustered networks outperform random by 5% in at most 22% of the p1 <= p2 space; minimal p2/p1 = 1.90 where clustering helps.

## Refinement from previous iteration
Iteration 3 of the x12 family for SOC; follows iteration 2 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | shares in [0, 1] |
| H1 | hypothesis | min ratio >= 1.9 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-D",
 "iteration": 3,
 "kind": "complex_contagion",
 "seed": 23303,
 "k": 6,
 "i": 2,
 "T": 1,
 "trials": 20,
 "pairs": [
  [
   0.1,
   0.1
  ],
  [
   0.1,
   0.2
  ],
  [
   0.1,
   0.3
  ],
  [
   0.1,
   0.4
  ],
  [
   0.1,
   0.5
  ],
  [
   0.1,
   0.6
  ],
  [
   0.1,
   0.7
  ],
  [
   0.1,
   0.8
  ],
  [
   0.1,
   0.9
  ],
  [
   0.1,
   1.0
  ],
  [
   0.2,
   0.2
  ],
  [
   0.2,
   0.3
  ],
  [
   0.2,
   0.4
  ],
  [
   0.2,
   0.5
  ],
  [
   0.2,
   0.6
  ],
  [
   0.2,
   0.7
  ],
  [
   0.2,
   0.8
  ],
  [
   0.2,
   0.9
  ],
  [
   0.2,
   1.0
  ],
  [
   0.3,
   0.3
  ],
  [
   0.3,
   0.4
  ],
  [
   0.3,
   0.5
  ],
  [
   0.3,
   0.6
  ],
  [
   0.3,
   0.7
  ],
  [
   0.3,
   0.8
  ],
  [
   0.3,
   0.9
  ],
  [
   0.3,
   1.0
  ],
  [
   0.4,
   0.4
  ],
  [
   0.4,
   0.5
  ],
  [
   0.4,
   0.6
  ],
  [
   0.4,
   0.7
  ],
  [
   0.4,
   0.8
  ],
  [
   0.4,
   0.9
  ],
  [
   0.4,
   1.0
  ],
  [
   0.5,
   0.5
  ],
  [
   0.5,
   0.6
  ],
  [
   0.5,
   0.7
  ],
  [
   0.5,
   0.8
  ],
  [
   0.5,
   0.9
  ],
  [
   0.5,
   1.0
  ],
  [
   0.6,
   0.6
  ],
  [
   0.6,
   0.7
  ],
  [
   0.6,
   0.8
  ],
  [
   0.6,
   0.9
  ],
  [
   0.6,
   1.0
  ],
  [
   0.7,
   0.7
  ],
  [
   0.7,
   0.8
  ],
  [
   0.7,
   0.9
  ],
  [
   0.7,
   1.0
  ],
  [
   0.8,
   0.8
  ],
  [
   0.8,
   0.9
  ],
  [
   0.8,
   1.0
  ],
  [
   0.9,
   0.9
  ],
  [
   0.9,
   1.0
  ],
  [
   1.0,
   1.0
  ]
 ],
 "h1_text": "every grid point where clustered beats random by >= 0.05 has p2/p1 >= 1.9",
 "h1_expr": "min([float(q.split(',')[1]) / float(q.split(',')[0]) for q, v in o.items() if v['clustered'] - v['random'] >= 0.05] or [99]) >= 1.9"
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
