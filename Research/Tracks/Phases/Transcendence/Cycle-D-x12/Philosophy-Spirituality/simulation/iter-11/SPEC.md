# SIM-TR-PHI-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Heritage 0.9: agreement above 0.40?

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
| H1 | hypothesis | heritage 0.9: agreement above the h 0.5 value 0.40 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-PHI-D",
 "iteration": 11,
 "kind": "core_construct",
 "seed": 43611,
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
  "constructivist_heritage": {
   "w": 0.0,
   "h": 0.9,
   "lam": 1.0,
   "sigma": 1.0
  }
 },
 "hyps": [
  [
   "heritage 0.9: agreement above the h 0.5 value 0.40",
   "o['scenarios']['constructivist_heritage']['0.0'] > 0.40"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-11` (run from `Philosophy-Spirituality/simulation/`)
