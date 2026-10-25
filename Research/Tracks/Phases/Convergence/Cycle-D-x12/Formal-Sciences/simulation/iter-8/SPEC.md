# SIM-CV-FOR-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Seven-state gambler's ruin and stubborn agents.

## Phase operationalization tested
FOR Convergence = convergence to stationarity (P78).

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | 7-state gambler's ruin: limit depends on start (max difference > 0.1) |
| H2 | hypothesis | stubborn ends: no consensus (spread > 0.5) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication-extension. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-D",
 "iteration": 8,
 "kind": "markov_converge",
 "seed": 33208,
 "T": [
  [
   1,
   0,
   0,
   0,
   0,
   0,
   0
  ],
  [
   0.5,
   0,
   0.5,
   0,
   0,
   0,
   0
  ],
  [
   0,
   0.5,
   0,
   0.5,
   0,
   0,
   0
  ],
  [
   0,
   0,
   0.5,
   0,
   0.5,
   0,
   0
  ],
  [
   0,
   0,
   0,
   0.5,
   0,
   0.5,
   0
  ],
  [
   0,
   0,
   0,
   0,
   0.5,
   0,
   0.5
  ],
  [
   0,
   0,
   0,
   0,
   0,
   0,
   1
  ]
 ],
 "V0": [
  0.14285714285714285,
  0.14285714285714285,
  0.14285714285714285,
  0.14285714285714285,
  0.14285714285714285,
  0.14285714285714285,
  0.14285714285714285
 ],
 "V0_alt": [
  0,
  1,
  0,
  0,
  0,
  0,
  0
 ],
 "report_n": [
  10,
  100
 ],
 "n_max": 600,
 "degroot_x0": [
  0,
  0.2,
  0.4,
  0.5,
  0.6,
  0.8,
  1
 ],
 "degroot_steps": 600,
 "hyps": [
  [
   "7-state gambler's ruin: limit depends on start (max difference > 0.1)",
   "o['alt']['max_diff'] > 0.1"
  ],
  [
   "stubborn ends: no consensus (spread > 0.5)",
   "o['degroot']['spread'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_for.py iter-8` (run from `Formal-Sciences/simulation/`)
