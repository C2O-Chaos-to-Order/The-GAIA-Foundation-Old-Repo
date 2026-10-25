# SIM-TR-PHI-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
With noise sigma 2: do the TR0 constructivist and essentialist patterns hold?

## Phase operationalization tested
PHI Transcendence = mystical experience: common core vs construction (P102).

## Sources this run draws on
P102 (Jones & Gellman, 'Mysticism', Stanford Encyclopedia of Philosophy, first published 11 Nov 2004, substantive revision 4 Sep 2026; read in full in TR0; SEP copyright, short phrases only): perennialism / essentialism vs constructivism; Katz's argument (A) + (B) -> (C); 'we can never get to the experiences themselves'; Deikman's deautomatization; thin and thick descriptions; post-experiential interpretation shaped by culture.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | w = 1, no noise, no scheme, no overlay gives correlation 1 |
| H1 | hypothesis | noise sigma 2: strong constructivism with independent schemes still gives |r| < 0.03 |
| H2 | hypothesis | noise sigma 2: under essentialism correlation still rises with deautomatization (d 0 < 0.4 < 0.8) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-PHI-A",
 "iteration": 3,
 "kind": "core_construct",
 "seed": 40603,
 "T": 6,
 "M": 10,
 "F": 40,
 "reps": 200,
 "d_values": [
  0.0,
  0.4,
  0.8
 ],
 "scenarios": {
  "constructivist_indep": {
   "w": 0.0,
   "h": 0.0,
   "lam": 1.0,
   "sigma": 2.0
  },
  "essentialist": {
   "w": 0.5,
   "h": 0.0,
   "lam": 1.0,
   "sigma": 2.0
  }
 },
 "hyps": [
  [
   "noise sigma 2: strong constructivism with independent schemes still gives |r| < 0.03",
   "all(abs(v) < 0.03 for v in o['scenarios']['constructivist_indep'].values())"
  ],
  [
   "noise sigma 2: under essentialism correlation still rises with deautomatization (d 0 < 0.4 < 0.8)",
   "o['scenarios']['essentialist']['0.0'] < o['scenarios']['essentialist']['0.4'] < o['scenarios']['essentialist']['0.8']"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
