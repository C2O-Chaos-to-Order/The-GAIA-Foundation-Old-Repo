# SIM-AS-PHI-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P90's ascent with varied dispositions: with q ~ Beta(1, 3) across 20,000 lovers, do at least 80% reach the top within 2000 encounters, and do those who reach it have a higher mean q?

## Phase operationalization tested
PHI Ascendence = the ascent of love driven by incoherence (P90).

## Sources this run draws on
P90 (Reeve, 'Plato on Friendship and Eros', Stanford Encyclopedia of Philosophy, first published 20 Feb 2004, substantive revision 14 Jun 2023; read in full in AS0): Diotima's ascent from one body to all bodies, souls, laws and practices, sciences and the beautiful itself; incoherence at lower stages leads the correct lover 'to climb to the next stage'; 'valuing appropriately is still valuing'; Alcibiades as love that did not lead to the beautiful itself; Phaedrus' winged soul and three successive incarnations.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | shares in [0, 1] and rungs within range |
| H1 | hypothesis | dispositions q ~ Beta(1, 3): at least 80% reach the top within 2000 encounters |
| H2 | hypothesis | lovers who reach the top have a higher mean q than those who do not |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; Beta(1, 3) is the agent's choice. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-PHI-A",
 "iteration": 1,
 "kind": "ascent_ladder2",
 "seed": 35601,
 "cover": [
  0.2,
  0.4,
  0.6,
  0.8,
  0.95,
  1.0
 ],
 "reps": 20000,
 "n_max": 2000,
 "q_dist": [
  1,
  3
 ],
 "hyps": [
  [
   "dispositions q ~ Beta(1, 3): at least 80% reach the top within 2000 encounters",
   "o['frac_top'] >= 0.8"
  ],
  [
   "lovers who reach the top have a higher mean q than those who do not",
   "o['mean_q_not'] is None or o['mean_q_reached'] > o['mean_q_not']"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
