# SIM-AL-PHI-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Long game (T 2000) with e 0.01: TFT below 2.5?

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
| H1 | hypothesis | TFT mean payoff below 2.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical analogy; payoffs and strategies are standard game theory chosen by the agent, not P63.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-D",
 "iteration": 3,
 "kind": "betrayal_echo",
 "seed": 28603,
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
 "e": 0.01,
 "T": 2000,
 "t0": 10,
 "reps": 30,
 "hyps": [
  [
   "TFT mean payoff below 2.5",
   "o['TFT']['mean_payoff'] < 2.5"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
