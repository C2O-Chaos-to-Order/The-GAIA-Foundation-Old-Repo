# SIM-AS-HUM-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P92 rating and articulation arithmetic

## Phase operationalization tested
HUM Ascendence = rising intonation (uptalk; P89, P92) and the spread of a minority rising variant.

## Sources this run draws on
P92 (Calhoun & White 2025, 'What Makes Iconic Pitch Associations "Natural": The Effect of Age on Affective Meanings of Uptalk and Creak', Lang Speech 68:606-632, PMC12365360, CC BY-NC; read in full in ASB): matched-guise ratings of uptalk, creak and neutral NZ English by 60 listeners (71 collected), 7,200 ratings; Table 4 ANOVA; mean ratings by age; Tables 2-3 F0 and articulation rate.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P92: 7200 ratings = 120 per listener = 15 scales x 8 items |
| H2 | hypothesis | P92: creaky stimuli are slower than uptalk stimuli relative to neutral (articulation rate) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-HUM-D",
 "iteration": 12,
 "kind": "arith_audit",
 "seed": 38512,
 "items": [
  {
   "name": "ratings_per_listener",
   "expr": "7200/60",
   "printed": 120
  },
  {
   "name": "items_per_listener",
   "expr": "15*8",
   "printed": 120
  },
  {
   "name": "F0_uptalk_peak_mean",
   "expr": "(293+312+338)/3"
  },
  {
   "name": "artic_uptalk_minus_neutral",
   "expr": "5.21-5.42"
  },
  {
   "name": "artic_creaky_minus_neutral",
   "expr": "5.04-5.42"
  }
 ],
 "hyps": [
  [
   "P92: 7200 ratings = 120 per listener = 15 scales x 8 items",
   "o['items']['ratings_per_listener']['diff'] == 0 and o['items']['items_per_listener']['diff'] == 0"
  ],
  [
   "P92: creaky stimuli are slower than uptalk stimuli relative to neutral (articulation rate)",
   "o['items']['artic_creaky_minus_neutral']['value'] < o['items']['artic_uptalk_minus_neutral']['value']"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-12` (run from `Humanities/simulation/`)
