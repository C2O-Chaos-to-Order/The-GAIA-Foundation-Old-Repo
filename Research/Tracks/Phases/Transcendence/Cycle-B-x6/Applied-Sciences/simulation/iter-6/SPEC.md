# SIM-TR-APP-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P100's RMSEA with N rather than N - 1: still reproduced?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P100 (Pena-Gayo, Gonzalez-Chorda, Cervera-Gasch, Mena-Tudela 2018, Spanish Reed Self-Transcendence Scale, Rev Lat Am Enfermagem, PMC6293607, CC BY 4.0; read in full in TR0): 19 experts; I-CVI, Pc, modified kappa, S-CVI; N 116 (138 recruited, 22 incomplete); EFA (Bartlett, KMO) and CFA (chi-square, df, RMSEA, SRMR) of 1-4 factor models; Table 2 sociodemographics.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P100's RMSEA also reproduces within 0.001 with N instead of N - 1 in the denominator (the convention does not matter at N 116) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-B",
 "iteration": 6,
 "kind": "arith_audit",
 "seed": 41406,
 "items": [
  {
   "name": "rmsea_N_4f",
   "expr": "sqrt(max(111.537-84,0)/(84*116))",
   "printed": 0.053
  },
  {
   "name": "rmsea_N_3f",
   "expr": "sqrt(max(111.673-87,0)/(87*116))",
   "printed": 0.049
  },
  {
   "name": "rmsea_N_2f",
   "expr": "sqrt(max(117.577-89,0)/(89*116))",
   "printed": 0.053
  },
  {
   "name": "rmsea_N_1f",
   "expr": "sqrt(max(152.377-90,0)/(90*116))",
   "printed": 0.077
  }
 ],
 "hyps": [
  [
   "P100's RMSEA also reproduces within 0.001 with N instead of N - 1 in the denominator (the convention does not matter at N 116)",
   "all(abs(v['diff']) <= 0.001 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
