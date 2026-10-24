# SIM-AL-PHI-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Error rate 0.02: CTFT above TFT and GTFT?

## Phase operationalization tested
PHI Allegiance = treason, retaliation and atonement (agent's analogy to P63's Royce).

## Sources this run draws on
P63 (SEP 'Josiah Royce', rev. 15 Jan 2026; read in full in ALC): treason, 'the hell of the irrevocable', atonement by a steadfastly loyal servant; forgiveness does not restore 'unscarred love'. The game-theoretic reading is the agent's analogy only.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | CTFT payoff > TFT |
| H2 | hypothesis | CTFT payoff > GTFT |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical analogy; payoffs and strategies are standard game theory chosen by the agent, not P63.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-D",
 "iteration": 2,
 "kind": "betrayal_echo",
 "seed": 28602,
 "strategies": {
  "TFT": {
   "kind": "TFT"
  },
  "GTFT": {
   "kind": "GTFT",
   "q": 0.33
  },
  "CTFT": {
   "kind": "CTFT"
  }
 },
 "e": 0.02,
 "T": 500,
 "t0": 10,
 "reps": 100,
 "hyps": [
  [
   "CTFT payoff > TFT",
   "o['CTFT']['mean_payoff'] > o['TFT']['mean_payoff']"
  ],
  [
   "CTFT payoff > GTFT",
   "o['CTFT']['mean_payoff'] > o['GTFT']['mean_payoff']"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
