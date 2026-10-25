# SIM-AS-APP-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P88's counterfactual as a curve: for 1-5 ascent days (2978 m), does P(moderate or severe) fall every day for four profiles, is a smoker's 1-day risk below a non-smoker's 3-day risk, and is the baseline 1-day risk above 0.8 and 5-day below 0.4?

## Phase operationalization tested
APP Ascendence = ascent rate and AMS (P88).

## Sources this run draws on
P88 (Poudel et al. 2022, ascent rate and AMS severity, Mustang district hospital, PLoS One, PMC9612449, CC BY; read in full in AS0 incl. peer-review history): N 105, AMS 74%; chi-square and t statistics; Table 2 Bayesian ordered logit (model 4: cut points -0.97, 1.48; ascent rate (km/day) 1.14; peak and residence altitude (log) -0.02, -0.08; age 31-60 0.68; smoking -1.82); response levels None, Mild, Moderate or Severe; Fig 2 counterfactual 'odds ... increase twofold (2.069)', abstract 'risk ... twice'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P(moderate or severe) falls with every extra ascent day (1-5) in all four profiles |
| H2 | hypothesis | a smoker's 1-day risk is below a non-smoker's 3-day risk (smoking -1.82 vs two extra days) |
| H3 | hypothesis | the baseline 1-day risk exceeds 0.8 and the 5-day risk is below 0.4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Point estimates, natural logs; profiles: middle-aged male baseline, smoker, age 0-30, age 61-85. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-A",
 "iteration": 2,
 "kind": "arith_audit",
 "seed": 35402,
 "items": [
  {
   "name": "P_base_1d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/1) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*0)))"
  },
  {
   "name": "P_base_2d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/2) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*0)))"
  },
  {
   "name": "P_base_3d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*0)))"
  },
  {
   "name": "P_base_4d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/4) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*0)))"
  },
  {
   "name": "P_base_5d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/5) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*0)))"
  },
  {
   "name": "P_smoker_1d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/1) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*1)))"
  },
  {
   "name": "P_smoker_2d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/2) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*1)))"
  },
  {
   "name": "P_smoker_3d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*1)))"
  },
  {
   "name": "P_smoker_4d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/4) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*1)))"
  },
  {
   "name": "P_smoker_5d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/5) - 0.02*log(3800) - 0.08*log(542) + 0.68 - 1.82*1)))"
  },
  {
   "name": "P_age0_30_1d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/1) - 0.02*log(3800) - 0.08*log(542) + 0.0 - 1.82*0)))"
  },
  {
   "name": "P_age0_30_2d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/2) - 0.02*log(3800) - 0.08*log(542) + 0.0 - 1.82*0)))"
  },
  {
   "name": "P_age0_30_3d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + 0.0 - 1.82*0)))"
  },
  {
   "name": "P_age0_30_4d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/4) - 0.02*log(3800) - 0.08*log(542) + 0.0 - 1.82*0)))"
  },
  {
   "name": "P_age0_30_5d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/5) - 0.02*log(3800) - 0.08*log(542) + 0.0 - 1.82*0)))"
  },
  {
   "name": "P_age61_85_1d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/1) - 0.02*log(3800) - 0.08*log(542) + -0.79 - 1.82*0)))"
  },
  {
   "name": "P_age61_85_2d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/2) - 0.02*log(3800) - 0.08*log(542) + -0.79 - 1.82*0)))"
  },
  {
   "name": "P_age61_85_3d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + -0.79 - 1.82*0)))"
  },
  {
   "name": "P_age61_85_4d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/4) - 0.02*log(3800) - 0.08*log(542) + -0.79 - 1.82*0)))"
  },
  {
   "name": "P_age61_85_5d",
   "expr": "(1-logistic(1.48-(1.14*(2.978/5) - 0.02*log(3800) - 0.08*log(542) + -0.79 - 1.82*0)))"
  }
 ],
 "hyps": [
  [
   "P(moderate or severe) falls with every extra ascent day (1-5) in all four profiles",
   "all(o['items'][f'P_{g}_{d}d']['value'] > o['items'][f'P_{g}_{d+1}d']['value'] for g in ['base','smoker','age0_30','age61_85'] for d in range(1, 5))"
  ],
  [
   "a smoker's 1-day risk is below a non-smoker's 3-day risk (smoking -1.82 vs two extra days)",
   "o['items']['P_smoker_1d']['value'] < o['items']['P_base_3d']['value']"
  ],
  [
   "the baseline 1-day risk exceeds 0.8 and the 5-day risk is below 0.4",
   "o['items']['P_base_1d']['value'] > 0.8 and o['items']['P_base_5d']['value'] < 0.4"
  ]
 ]
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
