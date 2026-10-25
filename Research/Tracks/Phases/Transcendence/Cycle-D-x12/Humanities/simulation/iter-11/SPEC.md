# SIM-TR-HUM-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
n 34, t 2.0: does BF01 rise with prior width?

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
| H1 | hypothesis | n 34, t 2.0: BF01 rises with prior width across 0.354-1.414 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
JZS. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-D",
 "iteration": 11,
 "kind": "jzs_bf_audit",
 "seed": 43511,
 "items": [
  {
   "name": "t2.0",
   "t": 2.0,
   "n": 34
  },
  {
   "name": "t2.5",
   "t": 2.5,
   "n": 34
  }
 ],
 "scales": [
  0.354,
  0.707,
  1.0,
  1.414
 ],
 "hyps": [
  [
   "n 34, t 2.0: BF01 rises with prior width across 0.354-1.414",
   "(lambda d: d['0.354']['BF01'] < d['0.707']['BF01'] < d['1.0']['BF01'] < d['1.414']['BF01'])(o['items']['t2.0'])"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-11` (run from `Humanities/simulation/`)
