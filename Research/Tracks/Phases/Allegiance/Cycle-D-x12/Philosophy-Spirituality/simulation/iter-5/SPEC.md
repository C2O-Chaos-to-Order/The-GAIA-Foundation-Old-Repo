# SIM-AL-PHI-D - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of ALC iter-1 with 500 repetitions: GTFT repair time within 0.3 of 1/q - 0.3 = 2.73?

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
| H1 | hypothesis | GTFT mean rounds to restore within 0.3 of 2.73 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical analogy; payoffs and strategies are standard game theory chosen by the agent, not P63.Agent's expectation from ALC (2.74 at 50 repetitions).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-D",
 "iteration": 5,
 "kind": "betrayal_echo",
 "seed": 28605,
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
 "T": 200,
 "t0": 10,
 "reps": 500,
 "hyps": [
  [
   "GTFT mean rounds to restore within 0.3 of 2.73",
   "abs(o['GTFT']['mean_rounds_to_restore'] - 2.73) < 0.3"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-5` (run from `Philosophy-Spirituality/simulation/`)
