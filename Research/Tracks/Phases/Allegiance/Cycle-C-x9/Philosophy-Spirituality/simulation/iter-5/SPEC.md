# SIM-AL-PHI-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Royce: forgiveness does not restore 'unscarred love'. With CTFT, is the betrayer's mean payoff over a 50-round game below the never-betrayed 3 (the betrayal gain of +2 is outweighed by the -3 of accepted punishment), and does the relationship nevertheless end in full cooperation?

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
| H1 | hypothesis | CTFT betrayer's mean payoff below 3 |
| H2 | hypothesis | CTFT always restores cooperation |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical analogy; payoffs and strategies are standard game theory chosen by the agent, not P63.Foreknowledge by reasoning before the run: CTFT gives the betrayer 5 then 0, so its mean is (3T - 1)/T = 2.98; the analogy to 'scarred' love is the agent's and loose.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-C",
 "iteration": 5,
 "kind": "betrayal_echo",
 "seed": 27605,
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
 "e": 0.0,
 "T": 50,
 "t0": 10,
 "reps": 20,
 "hyps": [
  [
   "CTFT betrayer's mean payoff below 3",
   "o['CTFT']['mean_payoff'] < 3"
  ],
  [
   "CTFT always restores cooperation",
   "o['CTFT']['frac_restored'] == 1"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-5` (run from `Philosophy-Spirituality/simulation/`)
