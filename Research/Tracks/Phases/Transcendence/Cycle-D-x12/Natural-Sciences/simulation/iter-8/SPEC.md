# SIM-TR-NAT-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P97's model with N 100: decoupling pattern?

## Phase operationalization tested
NAT Transcendence = an evolutionary transition in individuality; fitness decoupling vs tradeoff breaking (P97).

## Sources this run draws on
P97 (Bourrat, Doulcier, Rose, Rainey & Hammerschmidt 2022, 'Tradeoff breaking as a model of evolutionary transitions in individuality and limits of the fitness-decoupling metaphor', eLife, PMC9470156, CC BY 4.0; read in full in TR0 incl. decision letter and author response): ETI; fitness decoupling; Section 3.3 projection model with N size classes, k_i = 2^(i-1), s = theta, b = 1 - theta, p_i, g_i, m_i, alpha_i, gamma_i, beta_i; F = ln lambda; f2 = ln(1 - delta_1 + beta_1) counterfactual; Fig 5 (N 30, eta 8, p1 0.1, mu 0); tradeoff breaking; reviewers: incommensurability not novel, tradeoff breaking not sufficient as an ETI marker.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the long-run particle growth rate from iterating the model equals ln(dominant eigenvalue) at theta* |
| H1 | hypothesis | the counterfactual optimum is zero investment (argmax f2 = 0) |
| H2 | hypothesis | the life-cycle optimum theta* is positive |
| H3 | hypothesis | moving from theta 0 to theta* raises F and lowers f2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's implementation. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-NAT-D",
 "iteration": 8,
 "kind": "etr_tradeoff",
 "seed": 43108,
 "N": 100,
 "eta": 8.0,
 "p1": 0.1,
 "dtheta": 0.001,
 "iters": 3000,
 "breaks": [
  0.05,
  0.1
 ],
 "hyps": [
  [
   "the counterfactual optimum is zero investment (argmax f2 = 0)",
   "o['theta0'] == 0.0"
  ],
  [
   "the life-cycle optimum theta* is positive",
   "o['theta_star'] > 0"
  ],
  [
   "moving from theta 0 to theta* raises F and lowers f2",
   "o['F_at_star'] > o['F_at_0'] and o['f2_at_star'] < o['f2_at_0']"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-8` (run from `Natural-Sciences/simulation/`)
