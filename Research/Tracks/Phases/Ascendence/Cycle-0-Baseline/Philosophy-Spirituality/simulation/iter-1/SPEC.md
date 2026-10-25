# SIM-AS-PHI-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
A toy of the ascent P90 reports from Diotima's speech: rungs covering more of the beautiful things met (0.2, 0.4, 0.6, 0.8, 0.95, 1); a lover climbs on meeting an uncovered case with probability q. Does q = 0 stop the ascent, does q = 1 always reach the top, does halving q double the encounters, and is the last step the longest?

## Phase operationalization tested
PHI Ascendence = the ascent of love from one beautiful body to the beautiful itself (Diotima's ladder, scala amoris; P90).

## Sources this run draws on
P90 (Reeve, 'Plato on Friendship and Eros', Stanford Encyclopedia of Philosophy, first published 20 Feb 2004, substantive revision 14 Jun 2023; read in full in AS0): Diotima's ascent from one body to all bodies, souls, laws and practices, sciences and the beautiful itself; incoherence at lower stages leads the correct lover 'to climb to the next stage'; 'valuing appropriately is still valuing'; Alcibiades as love that did not lead to the beautiful itself; Phaedrus' winged soul and three successive incarnations.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated mean encounters to the top (q = 1) within 4 SE of the analytic sum |
| H1 | hypothesis | q = 0 (inconsistency met but no rational desire to resolve it; an Alcibiades-like case in the toy): nobody reaches the top |
| H2 | hypothesis | q = 1: everyone reaches the top within 2000 encounters |
| H3 | hypothesis | halving q roughly doubles the encounters needed (ratio of means between 1.9 and 2.1) |
| H4 | hypothesis | the encounters needed are dominated by the last non-top rung (c 0.95): its analytic share 1/(1 - 0.95) of the q = 1 analytic mean exceeds 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical: a formal toy of a philosophical reading, not a test of Plato or of P90. Coverage values, q and the 'first beloved weight' contrast (n_total_loved 100) are the agent's choices. 20,000 replicate ascents per q.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-PHI-0",
 "iteration": 1,
 "kind": "ascent_ladder",
 "seed": 34601,
 "cover": [
  0.2,
  0.4,
  0.6,
  0.8,
  0.95,
  1.0
 ],
 "q_values": [
  1.0,
  0.5,
  0.0
 ],
 "reps": 20000,
 "n_max": 2000,
 "n_total_loved": 100,
 "hyps": [
  [
   "q = 0 (inconsistency met but no rational desire to resolve it; an Alcibiades-like case in the toy): nobody reaches the top",
   "o['by_q']['0.0']['frac_top'] == 0"
  ],
  [
   "q = 1: everyone reaches the top within 2000 encounters",
   "o['by_q']['1.0']['frac_top'] == 1.0"
  ],
  [
   "halving q roughly doubles the encounters needed (ratio of means between 1.9 and 2.1)",
   "1.9 <= o['by_q']['0.5']['mean_steps']/o['by_q']['1.0']['mean_steps'] <= 2.1"
  ],
  [
   "the encounters needed are dominated by the last non-top rung (c 0.95): its analytic share 1/(1 - 0.95) of the q = 1 analytic mean exceeds 0.5",
   "(1/(1-0.95))/o['by_q']['1.0']['analytic_mean'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
