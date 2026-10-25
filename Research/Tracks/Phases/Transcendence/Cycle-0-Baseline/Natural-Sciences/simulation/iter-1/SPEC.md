# SIM-TR-NAT-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P97's projection model of a proto-multicellular life cycle (N 30, eta 8, p1 0.1, mu 0): is zero investment optimal for the counterfactual f2, is theta* > 0 for the life-cycle growth rate F, does moving from 0 to theta* raise F and lower f2, does breaking the s + b = 1 tradeoff raise both, and does particle fitness f1 differ from F?

## Phase operationalization tested
NAT Transcendence = an evolutionary transition in individuality: particles come to form a new, higher-level individual (P97). Competing reading: 'fitness decoupling' (P97 argues it is a metaphor with limits).

## Sources this run draws on
P97 (Bourrat, Doulcier, Rose, Rainey & Hammerschmidt 2022, 'Tradeoff breaking as a model of evolutionary transitions in individuality and limits of the fitness-decoupling metaphor', eLife, PMC9470156, CC BY 4.0; read in full in TR0 incl. decision letter and author response): ETI; fitness decoupling; Section 3.3 projection model with N size classes, k_i = 2^(i-1), s = theta, b = 1 - theta, p_i, g_i, m_i, alpha_i, gamma_i, beta_i; F = ln lambda; f2 = ln(1 - delta_1 + beta_1) counterfactual; Fig 5 (N 30, eta 8, p1 0.1, mu 0); tradeoff breaking; reviewers: incommensurability not novel, tradeoff breaking not sufficient as an ETI marker.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the long-run particle growth rate from iterating the model equals ln(dominant eigenvalue) at theta* |
| H1 | hypothesis | the counterfactual optimum is zero investment in collective survival (argmax f2 = 0), as P97 states |
| H2 | hypothesis | the whole-life-cycle optimum theta* is positive (N 30, eta 8, p1 0.1) |
| H3 | hypothesis | moving from theta 0 to theta* raises F and lowers f2 (the fitness-decoupling observation P97 reproduces in Fig 5) |
| H4 | hypothesis | breaking the tradeoff (s and b both raised by 0.05 from theta*) raises both F and f2 above their theta* values |
| H5 | hypothesis | within-collective particle fitness f1 at theta* differs from F by more than 0.01 (a non-commensurable measure) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's implementation. beta_i is the agent's reading of a formula garbled in the extracted text (sqrt(p_1) x 1/2 x ((1 + alpha_i) m_i + gamma_i m_{i+1})); g_N = 0; theta grid step 0.001; f1 = ln(1 + gamma_1) from P97's f1 with k_2 = 2 and mu 0. A pass reproduces P97's qualitative Fig 5 result under that reading, not its exact numbers. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-NAT-0",
 "iteration": 1,
 "kind": "etr_tradeoff",
 "seed": 39101,
 "N": 30,
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
   "the counterfactual optimum is zero investment in collective survival (argmax f2 = 0), as P97 states",
   "o['theta0'] == 0.0"
  ],
  [
   "the whole-life-cycle optimum theta* is positive (N 30, eta 8, p1 0.1)",
   "o['theta_star'] > 0"
  ],
  [
   "moving from theta 0 to theta* raises F and lowers f2 (the fitness-decoupling observation P97 reproduces in Fig 5)",
   "o['F_at_star'] > o['F_at_0'] and o['f2_at_star'] < o['f2_at_0']"
  ],
  [
   "breaking the tradeoff (s and b both raised by 0.05 from theta*) raises both F and f2 above their theta* values",
   "o['broken']['0.05']['F'] > o['F_at_star'] and o['broken']['0.05']['f2'] > o['f2_at_star']"
  ],
  [
   "within-collective particle fitness f1 at theta* differs from F by more than 0.01 (a non-commensurable measure)",
   "abs(o['f1_at_star'] - o['F_at_star']) > 0.01"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
