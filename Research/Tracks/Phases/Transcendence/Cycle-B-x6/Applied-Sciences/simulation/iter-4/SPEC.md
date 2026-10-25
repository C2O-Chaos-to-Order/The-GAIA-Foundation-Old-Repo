# SIM-TR-APP-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
19 raters, 12-14 agreeing: are their modified kappas below 'excellent'?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P100 (Pena-Gayo, Gonzalez-Chorda, Cervera-Gasch, Mena-Tudela 2018, Spanish Reed Self-Transcendence Scale, Rev Lat Am Enfermagem, PMC6293607, CC BY 4.0; read in full in TR0): 19 experts; I-CVI, Pc, modified kappa, S-CVI; N 116 (138 recruited, 22 incomplete); EFA (Bartlett, KMO) and CFA (chi-square, df, RMSEA, SRMR) of 1-4 factor models; Table 2 sociodemographics.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | binomial probabilities sum to 1 |
| H1 | hypothesis | 19 raters: with 14 agreeing (I-CVI 0.74) the modified kappa is below 0.74, i.e. 'good' rather than 'excellent' |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
400,000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-B",
 "iteration": 4,
 "kind": "cvi_chance_mc",
 "seed": 41404,
 "N": 19,
 "A_list": [
  12,
  13,
  14
 ],
 "reps": 400000,
 "hyps": [
  [
   "19 raters: with 14 agreeing (I-CVI 0.74) the modified kappa is below 0.74, i.e. 'good' rather than 'excellent'",
   "o['by_A']['14']['kappa'] < 0.74"
  ]
 ]
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
