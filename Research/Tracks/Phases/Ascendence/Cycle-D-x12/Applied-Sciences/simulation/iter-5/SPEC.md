# SIM-AS-APP-D - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P95 Table 2: CI width vs group size

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91). ASC adds P95's meta-analysis.

## Sources this run draws on
P95 (Liu, Tan, Ren, Bai, Yong, Gao, Ba & Gongga 2026, 'Prevalence and risk factors for AMS: A systematic review and meta-analysis', PLoS One, PMC13068236, CC BY; read in full in ASC): 58 observational studies (stated n 2,705), pooled AMS prevalence 48.25% (95% CI 42.58-53.96), Table 1 study list, Table 2 GRADE risk ratios incl. rapid ascent (<6 h) RR 1.60 (1.44-1.78).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P95 Table 2: the widest log-CI belongs to the smallest group (extreme altitude, n 120) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-D",
 "iteration": 5,
 "kind": "arith_audit",
 "seed": 38405,
 "items": [
  {
   "name": "logw_1_n425",
   "expr": "log(1.73)-log(1.25)"
  },
  {
   "name": "logw_2_n120",
   "expr": "log(2.51)-log(1.42)"
  },
  {
   "name": "logw_3_n1180",
   "expr": "log(1.4)-log(1.12)"
  },
  {
   "name": "logw_4_n1270",
   "expr": "log(1.78)-log(1.44)"
  },
  {
   "name": "logw_5_n2550",
   "expr": "log(1.45)-log(1.26)"
  },
  {
   "name": "logw_6_n430",
   "expr": "log(1.71)-log(1.18)"
  },
  {
   "name": "logw_7_n692",
   "expr": "log(2.09)-log(1.52)"
  },
  {
   "name": "logw_8_n1012",
   "expr": "log(2.75)-log(2.01)"
  },
  {
   "name": "logw_9_n692",
   "expr": "log(1.84)-log(1.27)"
  },
  {
   "name": "logw_10_n1012",
   "expr": "log(2.41)-log(1.69)"
  },
  {
   "name": "logw_11_n2895",
   "expr": "log(1.3)-log(1.02)"
  },
  {
   "name": "logw_12_n1023",
   "expr": "log(1.48)-log(1.25)"
  },
  {
   "name": "logw_13_n1842",
   "expr": "log(0.99)-log(0.84)"
  },
  {
   "name": "logw_14_n428",
   "expr": "log(0.9)-log(0.67)"
  },
  {
   "name": "logw_15_n2250",
   "expr": "log(0.99)-log(0.87)"
  }
 ],
 "hyps": [
  [
   "P95 Table 2: the widest log-CI belongs to the smallest group (extreme altitude, n 120)",
   "max(o['items'], key=lambda k: o['items'][k]['value']) == 'logw_2_n120'"
  ]
 ]
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
