# SIM-AL-PHI-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Forgiveness rate: GTFT with q 0.1, 0.33, 0.6 after one betrayal: does repair take about 1/q rounds (within 1/q + 1 at q 0.33) and fall with q?

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
| H1 | hypothesis | rounds to restore fall with q |
| H2 | hypothesis | q 0.33: mean rounds <= 1/q + 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical analogy; payoffs and strategies are standard game theory chosen by the agent, not P63.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-C",
 "iteration": 4,
 "kind": "betrayal_echo",
 "seed": 27604,
 "strategies": {
  "q0.1": {
   "kind": "GTFT",
   "q": 0.1
  },
  "q0.33": {
   "kind": "GTFT",
   "q": 0.33
  },
  "q0.6": {
   "kind": "GTFT",
   "q": 0.6
  }
 },
 "e": 0.0,
 "T": 300,
 "t0": 10,
 "reps": 200,
 "hyps": [
  [
   "rounds to restore fall with q",
   "o['q0.1']['mean_rounds_to_restore'] > o['q0.33']['mean_rounds_to_restore'] > o['q0.6']['mean_rounds_to_restore']"
  ],
  [
   "q 0.33: mean rounds <= 1/q + 1",
   "o['q0.33']['mean_rounds_to_restore'] <= 1/0.33 + 1"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-4` (run from `Philosophy-Spirituality/simulation/`)
