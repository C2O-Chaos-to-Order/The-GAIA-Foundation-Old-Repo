# SIM-IN-SOC-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
No escalation with heavy-tailed initial sizes (eta = 1.5): P39 says this alone reproduces Richardson.

## Phase operationalization tested
SOC Insurgence = an armed conflict growing from its first year to a large war by escalation (P39).

## Sources this run draws on
P39 (Clauset, Walter, Cederman & Gleditsch 2026, Sci Adv 12:eaeb1705, CC BY-NC 4.0; read in full in INC): Eq. 2 model, alpha = 2.1, q_hat = 0.47, x_min = 1000, Richardson alpha_hat = 1.53 for x >= 7061; 44% of civil-war escalation factors are 1; 'roughly a 10% ex ante risk of a doubling ... about a 1% risk of increasing by an order of magnitude'. Double Pareto form and clamping are the agent's readings (P39's SI not read).

## Refinement from previous iteration
Iteration 2 of the x9 family for SOC; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MLE recovers eta |
| H1 | hypothesis | see text |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-C",
 "iteration": 2,
 "kind": "escalation_war",
 "seed": 22302,
 "mode": "tail",
 "n": 100000,
 "sets": [
  [
   "none15",
   0,
   1.5,
   0.47
  ]
 ],
 "h1_text": "tail within 0.1 of 1.53",
 "h1_expr": "abs(o['none15']['alpha_hat'] - 1.53) <= 0.1"
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
