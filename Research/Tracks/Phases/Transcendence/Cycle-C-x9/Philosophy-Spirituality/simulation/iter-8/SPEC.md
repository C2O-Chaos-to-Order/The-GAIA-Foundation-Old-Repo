# SIM-TR-PHI-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Core/construct toy with 3 traditions and heritage 0.5: agreement > 0.15?

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
| H1 | hypothesis | 3 traditions, heritage 0.5: cross-tradition correlation at d 0 > 0.15 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-PHI-C",
 "iteration": 8,
 "kind": "core_construct",
 "seed": 42608,
 "T": 3,
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
   "h": 0.5,
   "lam": 1.0,
   "sigma": 1.0
  }
 },
 "hyps": [
  [
   "3 traditions, heritage 0.5: cross-tradition correlation at d 0 > 0.15",
   "o['scenarios']['constructivist_heritage']['0.0'] > 0.15"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-8` (run from `Philosophy-Spirituality/simulation/`)
