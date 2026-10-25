# SIM-TR-HUM-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Bayes factors for P103's paired changes (n 34): strong for self-transcendence, not for life satisfaction?

## Phase operationalization tested
HUM Transcendence = the sublime and self-transcendence from nature vs art (P101). Cross-field: P103 (APP).

## Sources this run draws on
P103 (Kim & Ahn 2021, 'Development and application of a self-transcendence enhancement program for the well-being of elderly women living alone in Korea', Korean J Women Health Nurs 27:128-140, PMC9334186, CC BY 4.0; read in full in TRA): single-group pre-post, 40 recruited, 34 completed; Reed's Self-Transcendence Scale; Table 2 characteristics (N 34); Table 3 pre/post means, SDs, paired t and one-tailed p; a priori n 32 (d .45, one-sided, power .80); reasons for discontinuation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the JZS mixing density integrates to 1 |
| H1 | hypothesis | P103 (n 34): self-transcendence change t 8.78 gives BF01 < 1/100 |
| H2 | hypothesis | P103: life satisfaction t 1.72 gives BF01 > 1/3 (not evidence for a change; printed p .470 one-tailed) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-sided JZS default; P103 reports one-tailed p. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-A",
 "iteration": 3,
 "kind": "jzs_bf_audit",
 "seed": 40503,
 "items": [
  {
   "name": "SelfTranscendence",
   "t": 8.78,
   "n": 34
  },
  {
   "name": "SpiritualWB",
   "t": 8.3,
   "n": 34
  },
  {
   "name": "ReligiousSWB",
   "t": 1.79,
   "n": 34
  },
  {
   "name": "ExistentialSWB",
   "t": 6.75,
   "n": 34
  },
  {
   "name": "Depression",
   "t": -7.59,
   "n": 34
  },
  {
   "name": "LifeSatisfaction",
   "t": 1.72,
   "n": 34
  },
  {
   "name": "PositiveAffect",
   "t": 3.77,
   "n": 34
  },
  {
   "name": "NegativeAffect",
   "t": -6.15,
   "n": 34
  }
 ],
 "scales": [
  0.707
 ],
 "hyps": [
  [
   "P103 (n 34): self-transcendence change t 8.78 gives BF01 < 1/100",
   "o['items']['SelfTranscendence']['0.707']['BF01'] < 0.01"
  ],
  [
   "P103: life satisfaction t 1.72 gives BF01 > 1/3 (not evidence for a change; printed p .470 one-tailed)",
   "o['items']['LifeSatisfaction']['0.707']['BF01'] > 1/3"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
