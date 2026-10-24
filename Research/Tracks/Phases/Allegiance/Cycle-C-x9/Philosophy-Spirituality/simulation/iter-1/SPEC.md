# SIM-AL-PHI-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
One betrayal, no errors: does TFT stay locked in an echo, do GTFT and CTFT restore cooperation, and does CTFT (the betrayer accepts punishment) restore it within 2 rounds?

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
| H1 | hypothesis | TFT never restores mutual cooperation |
| H2 | hypothesis | GTFT and CTFT always restore |
| H3 | hypothesis | CTFT restores within 2 rounds on average |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical analogy; payoffs and strategies are standard game theory chosen by the agent, not P63. Smoke test (seed 99, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); thresholds were not changed after it. Smoke showed H1 and H2 supported; H3 foreknowledge by reasoning (2 rounds).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-C",
 "iteration": 1,
 "kind": "betrayal_echo",
 "seed": 27601,
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
 "reps": 50,
 "hyps": [
  [
   "TFT never restores mutual cooperation",
   "o['TFT']['frac_restored'] == 0"
  ],
  [
   "GTFT and CTFT always restore",
   "o['GTFT']['frac_restored'] == 1 and o['CTFT']['frac_restored'] == 1"
  ],
  [
   "CTFT restores within 2 rounds on average",
   "o['CTFT']['mean_rounds_to_restore'] <= 2"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
