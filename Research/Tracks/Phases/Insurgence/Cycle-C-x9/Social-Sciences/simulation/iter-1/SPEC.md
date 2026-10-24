# SIM-IN-SOC-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Escalation versus no escalation (P39 Eq. 2; eta = 2.0, q = 0.47): does escalation give a Richardson-like tail (alpha within 0.2 of 1.53) while no escalation gives a steeper one (>= 1.8)?

## Phase operationalization tested
SOC Insurgence = an armed conflict growing from its first year to a large war by escalation (P39).

## Sources this run draws on
P39 (Clauset, Walter, Cederman & Gleditsch 2026, Sci Adv 12:eaeb1705, CC BY-NC 4.0; read in full in INC): Eq. 2 model, alpha = 2.1, q_hat = 0.47, x_min = 1000, Richardson alpha_hat = 1.53 for x >= 7061; 44% of civil-war escalation factors are 1; 'roughly a 10% ex ante risk of a doubling ... about a 1% risk of increasing by an order of magnitude'. Double Pareto form and clamping are the agent's readings (P39's SI not read).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | MLE recovers eta |
| H1 | hypothesis | see text |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
100,000 wars per set. Foreknowledge: a smoke run (20,000 wars) gave 1.73 with escalation. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-C",
 "iteration": 1,
 "kind": "escalation_war",
 "seed": 22301,
 "mode": "tail",
 "n": 100000,
 "sets": [
  [
   "esc",
   1,
   2.0,
   0.47
  ],
  [
   "none",
   0,
   2.0,
   0.47
  ]
 ],
 "h1_text": "escalation tail within 0.2 of 1.53 and no-escalation tail >= 1.8",
 "h1_expr": "abs(o['esc']['alpha_hat'] - 1.53) <= 0.2 and o['none']['alpha_hat'] >= 1.8"
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
