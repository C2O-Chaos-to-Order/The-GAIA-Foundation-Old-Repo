# SIM-TR-APP-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P103: do printed means, SDs and t imply valid pre-post correlations and consistent signs?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P103 (Kim & Ahn 2021, 'Development and application of a self-transcendence enhancement program for the well-being of elderly women living alone in Korea', Korean J Women Health Nurs 27:128-140, PMC9334186, CC BY 4.0; read in full in TRA): single-group pre-post, 40 recruited, 34 completed; Reed's Self-Transcendence Scale; Table 2 characteristics (N 34); Table 3 pre/post means, SDs, paired t and one-tailed p; a priori n 32 (d .45, one-sided, power .80); reasons for discontinuation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P103: printed means, SDs and t imply pre-post correlations within [-1, 1] for all eight outcomes |
| H2 | hypothesis | t has the sign of (post - pre) for all eight |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-B",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 41401,
 "items": [
  {
   "name": "dz_SelfTranscendence",
   "expr": "8.78/sqrt(34)"
  },
  {
   "name": "r_SelfTranscendence",
   "expr": "(7.47**2+7.82**2-(abs(48.91-43.26)*sqrt(34)/abs(8.78))**2)/(2*7.47*7.82)"
  },
  {
   "name": "sign_SelfTranscendence",
   "expr": "((48.91)-(43.26))*(8.78)"
  },
  {
   "name": "dz_SpiritualWB",
   "expr": "8.3/sqrt(34)"
  },
  {
   "name": "r_SpiritualWB",
   "expr": "(8.09**2+7.82**2-(abs(64.29-56.52)*sqrt(34)/abs(8.3))**2)/(2*8.09*7.82)"
  },
  {
   "name": "sign_SpiritualWB",
   "expr": "((64.29)-(56.52))*(8.3)"
  },
  {
   "name": "dz_ReligiousSWB",
   "expr": "1.79/sqrt(34)"
  },
  {
   "name": "r_ReligiousSWB",
   "expr": "(7.76**2+7.52**2-(abs(29.7-27.76)*sqrt(34)/abs(1.79))**2)/(2*7.76*7.52)"
  },
  {
   "name": "sign_ReligiousSWB",
   "expr": "((29.7)-(27.76))*(1.79)"
  },
  {
   "name": "dz_ExistentialSWB",
   "expr": "6.75/sqrt(34)"
  },
  {
   "name": "r_ExistentialSWB",
   "expr": "(5.95**2+4.95**2-(abs(34.58-29.55)*sqrt(34)/abs(6.75))**2)/(2*5.95*4.95)"
  },
  {
   "name": "sign_ExistentialSWB",
   "expr": "((34.58)-(29.55))*(6.75)"
  },
  {
   "name": "dz_Depression",
   "expr": "-7.59/sqrt(34)"
  },
  {
   "name": "r_Depression",
   "expr": "(1.83**2+1.49**2-(abs(7.0-8.73)*sqrt(34)/abs(-7.59))**2)/(2*1.83*1.49)"
  },
  {
   "name": "sign_Depression",
   "expr": "((7.0)-(8.73))*(-7.59)"
  },
  {
   "name": "dz_LifeSatisfaction",
   "expr": "1.72/sqrt(34)"
  },
  {
   "name": "r_LifeSatisfaction",
   "expr": "(4.66**2+4.87**2-(abs(14.97-14.14)*sqrt(34)/abs(1.72))**2)/(2*4.66*4.87)"
  },
  {
   "name": "sign_LifeSatisfaction",
   "expr": "((14.97)-(14.14))*(1.72)"
  },
  {
   "name": "dz_PositiveAffect",
   "expr": "3.77/sqrt(34)"
  },
  {
   "name": "r_PositiveAffect",
   "expr": "(7.42**2+6.91**2-(abs(32.0-30.41)*sqrt(34)/abs(3.77))**2)/(2*7.42*6.91)"
  },
  {
   "name": "sign_PositiveAffect",
   "expr": "((32.0)-(30.41))*(3.77)"
  },
  {
   "name": "dz_NegativeAffect",
   "expr": "-6.15/sqrt(34)"
  },
  {
   "name": "r_NegativeAffect",
   "expr": "(4.86**2+4.47**2-(abs(30.26-34.11)*sqrt(34)/abs(-6.15))**2)/(2*4.86*4.47)"
  },
  {
   "name": "sign_NegativeAffect",
   "expr": "((30.26)-(34.11))*(-6.15)"
  }
 ],
 "hyps": [
  [
   "P103: printed means, SDs and t imply pre-post correlations within [-1, 1] for all eight outcomes",
   "all(-1 <= v['value'] <= 1 for k, v in o['items'].items() if k.startswith('r_'))"
  ],
  [
   "t has the sign of (post - pre) for all eight",
   "all(v['value'] > 0 for k, v in o['items'].items() if k.startswith('sign_'))"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
