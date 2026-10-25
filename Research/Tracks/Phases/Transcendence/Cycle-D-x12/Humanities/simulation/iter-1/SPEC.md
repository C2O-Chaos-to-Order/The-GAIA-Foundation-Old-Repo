# SIM-TR-HUM-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
n 10: t 4.0 BF01 below 1/10?

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
| H1 | hypothesis | n 10: t 4.0 gives BF01 below 1/10 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
JZS. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-D",
 "iteration": 1,
 "kind": "jzs_bf_audit",
 "seed": 43501,
 "items": [
  {
   "name": "t3.0",
   "t": 3.0,
   "n": 10
  },
  {
   "name": "t4.0",
   "t": 4.0,
   "n": 10
  },
  {
   "name": "t5.0",
   "t": 5.0,
   "n": 10
  }
 ],
 "scales": [
  0.707
 ],
 "hyps": [
  [
   "n 10: t 4.0 gives BF01 below 1/10",
   "o['items']['t4.0']['0.707']['BF01'] < 0.1"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
