# SIM-AS-APP-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P88 model comparison and residence altitude: is model 4's WAIC gain over model 3 below one SE, and does a 1400 m residence change the 1-day risk by < 0.02?

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91).

## Sources this run draws on
P88 (Poudel et al. 2022, ascent rate and AMS severity, Mustang district hospital, PLoS One, PMC9612449, CC BY; read in full in AS0 incl. peer-review history): N 105, AMS 74%; chi-square and t statistics; Table 2 Bayesian ordered logit (model 4: cut points -0.97, 1.48; ascent rate (km/day) 1.14; peak and residence altitude (log) -0.02, -0.08; age 31-60 0.68; smoking -1.82); response levels None, Mild, Moderate or Severe; Fig 2 counterfactual 'odds ... increase twofold (2.069)', abstract 'risk ... twice'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | model 4's WAIC advantage over model 3 is smaller than 1 SE of model 4's WAIC (the extra comorbidity term is not clearly better) |
| H2 | hypothesis | a Kathmandu-altitude residence (1400 m) changes the 1-day risk by less than 0.02 (residence coefficient -0.08 on ln m) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Point estimates; natural logs. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-B",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 36403,
 "items": [
  {
   "name": "WAIC_m1_m4",
   "expr": "227.06-218.59"
  },
  {
   "name": "WAIC_m3_m4",
   "expr": "219.35-218.59"
  },
  {
   "name": "WAIC_m3_m4_over_SE4",
   "expr": "(219.35-218.59)/12.24"
  },
  {
   "name": "P_base_1d_res1400",
   "expr": "1-logistic(1.48-(1.14*2.978-0.02*log(3800)-0.08*log(1400)+0.68))"
  },
  {
   "name": "P_base_3d_res1400",
   "expr": "1-logistic(1.48-(1.14*2.978/3-0.02*log(3800)-0.08*log(1400)+0.68))"
  }
 ],
 "hyps": [
  [
   "model 4's WAIC advantage over model 3 is smaller than 1 SE of model 4's WAIC (the extra comorbidity term is not clearly better)",
   "o['items']['WAIC_m3_m4_over_SE4']['value'] < 1"
  ],
  [
   "a Kathmandu-altitude residence (1400 m) changes the 1-day risk by less than 0.02 (residence coefficient -0.08 on ln m)",
   "abs(o['items']['P_base_1d_res1400']['value'] - 0.872855) < 0.02"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
