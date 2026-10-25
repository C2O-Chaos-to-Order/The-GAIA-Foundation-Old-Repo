# SIM-TR-HUM-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
n 50, ultrawide prior: t 2.5 BF01 above 1/3?

## Phase operationalization tested
HUM Transcendence = the sublime and self-transcendence from nature vs art (P101).

## Sources this run draws on
P101 (Chirico, Clewis, Yaden & Gaggioli 2021, 'Nature versus art as elicitors of the sublime: A virtual reality study', PLoS One, PMC7984734, CC BY 4.0; read in full in TR0): within-subject VR, n 50 (39 women); eight sublime dimensions (incl. self-transcendence, vastness, existential danger); Table 2 means, SDs, t(49), p, Cohen's d, BF01; text calls vastness and danger 'strong evidence for H 1'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the JZS mixing density integrates to 1 |
| H1 | hypothesis | n 50 with an ultrawide prior (scale 1.414): t 2.5 gives BF01 above 1/3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
JZS. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-C",
 "iteration": 4,
 "kind": "jzs_bf_audit",
 "seed": 42504,
 "items": [
  {
   "name": "t2.0",
   "t": 2.0,
   "n": 50
  },
  {
   "name": "t2.25",
   "t": 2.25,
   "n": 50
  },
  {
   "name": "t2.5",
   "t": 2.5,
   "n": 50
  },
  {
   "name": "t2.75",
   "t": 2.75,
   "n": 50
  },
  {
   "name": "t3.0",
   "t": 3.0,
   "n": 50
  },
  {
   "name": "t3.5",
   "t": 3.5,
   "n": 50
  }
 ],
 "scales": [
  1.414
 ],
 "hyps": [
  [
   "n 50 with an ultrawide prior (scale 1.414): t 2.5 gives BF01 above 1/3",
   "o['items']['t2.5']['1.414']['BF01'] > 1/3"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-4` (run from `Humanities/simulation/`)
