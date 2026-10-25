# SIM-TR-HUM-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P103 with Cauchy scale 1: do life satisfaction and religious well-being still give BF01 > 1/3?

## Phase operationalization tested
HUM Transcendence = the sublime and self-transcendence from nature vs art (P101).

## Sources this run draws on
P103 (Kim & Ahn 2021, 'Development and application of a self-transcendence enhancement program for the well-being of elderly women living alone in Korea', Korean J Women Health Nurs 27:128-140, PMC9334186, CC BY 4.0; read in full in TRA): single-group pre-post, 40 recruited, 34 completed; Reed's Self-Transcendence Scale; Table 2 characteristics (N 34); Table 3 pre/post means, SDs, paired t and one-tailed p; a priori n 32 (d .45, one-sided, power .80); reasons for discontinuation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the JZS mixing density integrates to 1 |
| H1 | hypothesis | P103 with a wider prior (scale 1): life satisfaction and religious well-being still give BF01 > 1/3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
JZS default family. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-B",
 "iteration": 1,
 "kind": "jzs_bf_audit",
 "seed": 41501,
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
  1.0
 ],
 "hyps": [
  [
   "P103 with a wider prior (scale 1): life satisfaction and religious well-being still give BF01 > 1/3",
   "o['items']['LifeSatisfaction']['1.0']['BF01'] > 1/3 and o['items']['ReligiousSWB']['1.0']['BF01'] > 1/3"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
