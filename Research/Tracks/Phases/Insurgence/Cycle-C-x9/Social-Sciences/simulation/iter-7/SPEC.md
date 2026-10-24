# SIM-IN-SOC-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Civil-war mean reversion (P39 Fig. 2C: large civil wars de-escalate around 500 deaths per year): does an agent-chosen reversion (kappa = 0.3) make the tail markedly lighter than unconditioned escalation (q = 0.25, about 4-year wars)?

## Phase operationalization tested
SOC Insurgence = a civil war self-limiting as it grows (P39).

## Sources this run draws on
P39 (Clauset, Walter, Cederman & Gleditsch 2026, Sci Adv 12:eaeb1705, CC BY-NC 4.0; read in full in INC): Eq. 2 model, alpha = 2.1, q_hat = 0.47, x_min = 1000, Richardson alpha_hat = 1.53 for x >= 7061; 44% of civil-war escalation factors are 1; 'roughly a 10% ex ante risk of a doubling ... about a 1% risk of increasing by an order of magnitude'. Double Pareto form and clamping are the agent's readings (P39's SI not read).

## Refinement from previous iteration
Iteration 7 of the x9 family for SOC; follows iteration 6 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MLE recovers eta |
| H1 | hypothesis | see text |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Parametric stand-in; P39 uses the empirical conditional distribution. Not smoke-tested. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-C",
 "iteration": 7,
 "kind": "escalation_war",
 "seed": 22307,
 "mode": "civil",
 "kappa": 0.3,
 "n": 100000,
 "sets": [
  [
   "civil",
   1,
   2.0,
   0.25
  ],
  [
   "free",
   1,
   2.0,
   0.25
  ]
 ],
 "h1_text": "tail at least 0.3 lighter with reversion",
 "h1_expr": "o['civil']['alpha_hat'] - o['free']['alpha_hat'] >= 0.3"
}
```

## Command
`python sim_soc.py iter-7` (run from `Social-Sciences/simulation/`)
