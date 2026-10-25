# SIM-AS-PHI-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
q 0.3, r 0.2

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
| H1 | hypothesis | q 0.3 with r 0.2: at least half reach the top |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-PHI-D",
 "iteration": 3,
 "kind": "ascent_ladder2",
 "seed": 38603,
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
 "q_fixed": 0.3,
 "r": 0.2,
 "hyps": [
  [
   "q 0.3 with r 0.2: at least half reach the top",
   "o['frac_top'] >= 0.5"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
