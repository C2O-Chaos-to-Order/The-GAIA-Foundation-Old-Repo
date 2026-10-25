# SIM-AS-APP-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P88 model: residence altitude

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91). ASC adds P95's meta-analysis.

## Sources this run draws on
P88 (Poudel et al. 2022, ascent rate and AMS severity, Mustang district hospital, PLoS One, PMC9612449, CC BY; read in full in AS0 incl. peer-review history): N 105, AMS 74%; chi-square and t statistics; Table 2 Bayesian ordered logit (model 4: cut points -0.97, 1.48; ascent rate (km/day) 1.14; peak and residence altitude (log) -0.02, -0.08; age 31-60 0.68; smoking -1.82); response levels None, Mild, Moderate or Severe; Fig 2 counterfactual 'odds ... increase twofold (2.069)', abstract 'risk ... twice'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P88 model: residence at 2500 m vs 1 m lowers the 1-day risk by more than 0.05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Point estimates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-D",
 "iteration": 11,
 "kind": "arith_audit",
 "seed": 38411,
 "items": [
  {
   "name": "P_base_1d_res0",
   "expr": "1-logistic(1.48-(1.14*2.978-0.02*log(3800)-0.08*log(1)+0.68))"
  },
  {
   "name": "P_base_1d_res2500",
   "expr": "1-logistic(1.48-(1.14*2.978-0.02*log(3800)-0.08*log(2500)+0.68))"
  }
 ],
 "hyps": [
  [
   "P88 model: residence at 2500 m vs 1 m lowers the 1-day risk by more than 0.05",
   "o['items']['P_base_1d_res0']['value'] - o['items']['P_base_1d_res2500']['value'] > 0.05"
  ]
 ]
}
```

## Command
`python sim_app.py iter-11` (run from `Applied-Sciences/simulation/`)
