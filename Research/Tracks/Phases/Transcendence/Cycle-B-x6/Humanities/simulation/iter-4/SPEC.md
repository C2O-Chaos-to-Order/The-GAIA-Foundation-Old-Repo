# SIM-TR-HUM-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
n 34 (P103's size): does t 2.0 give BF01 > 1/3?

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
| H1 | hypothesis | n 34 (P103): t 2.0 gives BF01 > 1/3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
JZS. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-B",
 "iteration": 4,
 "kind": "jzs_bf_audit",
 "seed": 41504,
 "items": [
  {
   "name": "t2.0",
   "t": 2.0,
   "n": 34
  },
  {
   "name": "t2.25",
   "t": 2.25,
   "n": 34
  },
  {
   "name": "t2.5",
   "t": 2.5,
   "n": 34
  },
  {
   "name": "t2.75",
   "t": 2.75,
   "n": 34
  },
  {
   "name": "t3.0",
   "t": 3.0,
   "n": 34
  },
  {
   "name": "t3.5",
   "t": 3.5,
   "n": 34
  }
 ],
 "scales": [
  0.707
 ],
 "hyps": [
  [
   "n 34 (P103): t 2.0 gives BF01 > 1/3",
   "o['items']['t2.0']['0.707']['BF01'] > 1/3"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-4` (run from `Humanities/simulation/`)
