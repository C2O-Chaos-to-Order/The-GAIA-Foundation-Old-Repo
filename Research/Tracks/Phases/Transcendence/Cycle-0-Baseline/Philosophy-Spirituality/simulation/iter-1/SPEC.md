# SIM-TR-PHI-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
A toy of the essentialism / strong-constructivism debate P102 reports: without a common core, are cross-tradition reports uncorrelated (or correlated only via shared heritage); with a core, does deautomatization raise agreement and do thick interpretive overlays lower it?

## Phase operationalization tested
PHI Transcendence = mystical experience said to transcend concepts and traditions (a 'common core'), versus the constructivist view that experience is shaped by tradition (P102).

## Sources this run draws on
P102 (Jones & Gellman, 'Mysticism', Stanford Encyclopedia of Philosophy, first published 11 Nov 2004, substantive revision 4 Sep 2026; read in full in TR0; SEP copyright, short phrases only): perennialism / essentialism vs constructivism; Katz's argument (A) + (B) -> (C); 'we can never get to the experiences themselves'; Deikman's deautomatization; thin and thick descriptions; post-experiential interpretation shaped by culture.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | w = 1, no noise, no scheme, no overlay gives cross-tradition correlation 1 |
| H1 | hypothesis | strong constructivism with pervasively different schemes (Katz's (A) and (B)): cross-tradition report correlation |r| < 0.03 at every training level |
| H2 | hypothesis | strong constructivism with a shared heritage component (h 0.5): cross-tradition correlation > 0.15 without any common core (d 0) |
| H3 | hypothesis | essentialism (w 0.5): cross-tradition correlation rises with deautomatization (d 0 < 0.4 < 0.8) |
| H4 | hypothesis | strong constructivism with heritage: training does not raise agreement (r at d 0.8 below r at d 0) |
| H5 | hypothesis | a thick interpretive overlay masks a core: essentialist thin reports (lam 0) agree more across traditions than thick ones (lam 1) at d 0 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical: a formal toy, not a test of mysticism or of P102. T 6 traditions, M 10 mystics each, F 40 features, 200 replicates; all parameters are the agent's choices. 'Experience' and 'report' are vectors, which already presupposes commensurability.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-PHI-0",
 "iteration": 1,
 "kind": "core_construct",
 "seed": 39601,
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
   "sigma": 1.0
  },
  "constructivist_heritage": {
   "w": 0.0,
   "h": 0.5,
   "lam": 1.0,
   "sigma": 1.0
  },
  "essentialist": {
   "w": 0.5,
   "h": 0.0,
   "lam": 1.0,
   "sigma": 1.0
  },
  "essentialist_thin": {
   "w": 0.5,
   "h": 0.0,
   "lam": 0.0,
   "sigma": 1.0
  }
 },
 "hyps": [
  [
   "strong constructivism with pervasively different schemes (Katz's (A) and (B)): cross-tradition report correlation |r| < 0.03 at every training level",
   "all(abs(v) < 0.03 for v in o['scenarios']['constructivist_indep'].values())"
  ],
  [
   "strong constructivism with a shared heritage component (h 0.5): cross-tradition correlation > 0.15 without any common core (d 0)",
   "o['scenarios']['constructivist_heritage']['0.0'] > 0.15"
  ],
  [
   "essentialism (w 0.5): cross-tradition correlation rises with deautomatization (d 0 < 0.4 < 0.8)",
   "o['scenarios']['essentialist']['0.0'] < o['scenarios']['essentialist']['0.4'] < o['scenarios']['essentialist']['0.8']"
  ],
  [
   "strong constructivism with heritage: training does not raise agreement (r at d 0.8 below r at d 0)",
   "o['scenarios']['constructivist_heritage']['0.8'] < o['scenarios']['constructivist_heritage']['0.0']"
  ],
  [
   "a thick interpretive overlay masks a core: essentialist thin reports (lam 0) agree more across traditions than thick ones (lam 1) at d 0",
   "o['scenarios']['essentialist_thin']['0.0'] > o['scenarios']['essentialist']['0.0']"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
