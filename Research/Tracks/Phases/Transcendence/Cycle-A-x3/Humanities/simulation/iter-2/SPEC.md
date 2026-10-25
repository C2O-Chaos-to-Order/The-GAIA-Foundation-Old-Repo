# SIM-TR-HUM-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Prior sensitivity: do the vastness and danger conclusions hold for Cauchy scales 0.5, 1 and 1.414?

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
| H1 | hypothesis | vastness BF01 stays above 1/3 for Cauchy scales 0.5, 1 and 1.414 |
| H2 | hypothesis | existential danger BF01 stays below 1/100 for all three scales |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iter-1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-A",
 "iteration": 2,
 "kind": "jzs_bf_audit",
 "seed": 40502,
 "items": [
  {
   "name": "ConceptualComplexity",
   "t": -1.932,
   "n": 50,
   "printed_BF01": 1.171
  },
  {
   "name": "ExistentialDanger",
   "t": -5.72,
   "n": 50,
   "printed_BF01": 3.961e-05
  },
  {
   "name": "Vastness",
   "t": -2.041,
   "n": 50,
   "printed_BF01": 0.968
  }
 ],
 "scales": [
  0.5,
  1.0,
  1.414
 ],
 "hyps": [
  [
   "vastness BF01 stays above 1/3 for Cauchy scales 0.5, 1 and 1.414",
   "all(v['BF01'] > 1/3 for v in o['items']['Vastness'].values())"
  ],
  [
   "existential danger BF01 stays below 1/100 for all three scales",
   "all(v['BF01'] < 0.01 for v in o['items']['ExistentialDanger'].values())"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
