# SIM-AS-APP-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P88: is the 1-day/3-day risk ratio larger for a middle-aged smoker than a non-smoker?

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91).

## Sources this run draws on
P88 (Poudel et al. 2022, ascent rate and AMS severity, Mustang district hospital, PLoS One, PMC9612449, CC BY; read in full in AS0 incl. peer-review history): N 105, AMS 74%; chi-square and t statistics; Table 2 Bayesian ordered logit (model 4: cut points -0.97, 1.48; ascent rate (km/day) 1.14; peak and residence altitude (log) -0.02, -0.08; age 31-60 0.68; smoking -1.82); response levels None, Mild, Moderate or Severe; Fig 2 counterfactual 'odds ... increase twofold (2.069)', abstract 'risk ... twice'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | IPF reproduces both margins within 1e-9 |
| H1 | hypothesis | middle-aged smoker (age 0.68 + smoking -1.82 as one constant): the 1-day/3-day risk ratio is larger than for the non-smoker (point value 2.095) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Age and smoking combined into one constant (0.68 - 1.82); V1 compares with the ASA-APP iteration-2 point value (5.0782); the V1 text says 'AS0 audit value'. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-B",
 "iteration": 5,
 "kind": "ordlogit_mc",
 "seed": 36405,
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
   -1.14,
   0.0
  ]
 },
 "gain_km": 2.978,
 "peak_m": 3800,
 "res_m": 542,
 "days": [
  3
 ],
 "v1_point": 5.0782,
 "hyps": [
  [
   "middle-aged smoker (age 0.68 + smoking -1.82 as one constant): the 1-day/3-day risk ratio is larger than for the non-smoker (point value 2.095)",
   "o['by_days']['3']['point_rr'] > 2.0953"
  ]
 ]
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
