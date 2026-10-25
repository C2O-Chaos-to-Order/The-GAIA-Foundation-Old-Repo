# SIM-TR-HUM-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Do default JZS Bayes factors (Cauchy 0.707) recomputed from P101's t and n 50 reproduce Table 2's BF01, and what do they say about vastness and danger?

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
| H1 | hypothesis | default JZS BF01 (Cauchy scale 0.707) from t and n 50 is within 10% of Table 2's printed BF01 for all eight dimensions |
| H2 | hypothesis | recomputed vastness BF01 is above 1/3 (not strong evidence for a difference) |
| H3 | hypothesis | recomputed existential-danger BF01 is below 1/100 (extreme evidence for a difference) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Rouder et al. 2009 one-sample formula applied to paired differences; JASP default scale assumed (P101 does not state it). Foreknowledge: the agent noticed while reading that 1/0.968 = 1.033. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-HUM-A",
 "iteration": 1,
 "kind": "jzs_bf_audit",
 "seed": 40501,
 "items": [
  {
   "name": "Rarity",
   "t": 0.253,
   "n": 50,
   "printed_BF01": 6.304
  },
  {
   "name": "BeautyPerception",
   "t": -0.03,
   "n": 50,
   "printed_BF01": 6.479
  },
  {
   "name": "SelfTranscendence",
   "t": -0.355,
   "n": 50,
   "printed_BF01": 6.121
  },
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
  },
  {
   "name": "NeedToShare",
   "t": -1.821,
   "n": 50,
   "printed_BF01": 1.411
  },
  {
   "name": "ExistentialSafety",
   "t": 1.948,
   "n": 50,
   "printed_BF01": 1.14
  }
 ],
 "scales": [
  0.707
 ],
 "hyps": [
  [
   "default JZS BF01 (Cauchy scale 0.707) from t and n 50 is within 10% of Table 2's printed BF01 for all eight dimensions",
   "all(0.9 <= v['0.707']['ratio_to_printed'] <= 1.1 for v in o['items'].values())"
  ],
  [
   "recomputed vastness BF01 is above 1/3 (not strong evidence for a difference)",
   "o['items']['Vastness']['0.707']['BF01'] > 1/3"
  ],
  [
   "recomputed existential-danger BF01 is below 1/100 (extreme evidence for a difference)",
   "o['items']['ExistentialDanger']['0.707']['BF01'] < 0.01"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
