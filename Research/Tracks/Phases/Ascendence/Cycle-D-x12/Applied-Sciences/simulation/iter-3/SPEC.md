# SIM-AS-APP-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P88 model 1 vs 10 days

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91). ASC adds P95's meta-analysis.

## Sources this run draws on
P88 (Poudel et al. 2022, ascent rate and AMS severity, Mustang district hospital, PLoS One, PMC9612449, CC BY; read in full in AS0 incl. peer-review history): N 105, AMS 74%; chi-square and t statistics; Table 2 Bayesian ordered logit (model 4: cut points -0.97, 1.48; ascent rate (km/day) 1.14; peak and residence altitude (log) -0.02, -0.08; age 31-60 0.68; smoking -1.82); response levels None, Mild, Moderate or Severe; Fig 2 counterfactual 'odds ... increase twofold (2.069)', abstract 'risk ... twice'. P95 (Liu, Tan, Ren, Bai, Yong, Gao, Ba & Gongga 2026, 'Prevalence and risk factors for AMS: A systematic review and meta-analysis', PLoS One, PMC13068236, CC BY; read in full in ASC): 58 observational studies (stated n 2,705), pooled AMS prevalence 48.25% (95% CI 42.58-53.96), Table 1 study list, Table 2 GRADE risk ratios incl. rapid ascent (<6 h) RR 1.60 (1.44-1.78).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | IPF reproduces both margins within 1e-9 |
| H1 | hypothesis | P88 model: 1-day vs 10-day (about 300 m/day, P95's recommended pace) risk ratio (point) above 3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As above; 10 days is the agent's reading of 300 m/day for a 2978 m gain. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-D",
 "iteration": 3,
 "kind": "ordlogit_mc",
 "seed": 38403,
 "draws": 200000,
 "coef": {
  "c2": [
   1.48,
   0.0
  ],
  "rate": [
   1.14,
   0.4
  ],
  "peak": [
   -0.02,
   0.0
  ],
  "res": [
   -0.08,
   0.0
  ],
  "age": [
   0.68,
   0.0
  ]
 },
 "gain_km": 2.978,
 "peak_m": 3800,
 "res_m": 542,
 "days": [
  10
 ],
 "v1_point": 3.5722,
 "hyps": [
  [
   "P88 model: 1-day vs 10-day (about 300 m/day, P95's recommended pace) risk ratio (point) above 3",
   "o['by_days']['10']['point_rr'] > 3"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
