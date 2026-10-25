# SIM-AS-APP-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P95 Table 2 CI symmetry on the log scale

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
| H1 | hypothesis | each P95 Table 2 RR equals the geometric mean of its CI within 0.02 (log-symmetric CIs) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Rounding to 2 decimals. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-C",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 37403,
 "items": [
  {
   "name": "T2_gm_1",
   "expr": "sqrt(1.25*1.73)",
   "printed": 1.47
  },
  {
   "name": "T2_gm_2",
   "expr": "sqrt(1.42*2.51)",
   "printed": 1.89
  },
  {
   "name": "T2_gm_3",
   "expr": "sqrt(1.12*1.4)",
   "printed": 1.25
  },
  {
   "name": "T2_gm_4",
   "expr": "sqrt(1.44*1.78)",
   "printed": 1.6
  },
  {
   "name": "T2_gm_5",
   "expr": "sqrt(1.26*1.45)",
   "printed": 1.35
  },
  {
   "name": "T2_gm_6",
   "expr": "sqrt(1.18*1.71)",
   "printed": 1.42
  },
  {
   "name": "T2_gm_7",
   "expr": "sqrt(1.52*2.09)",
   "printed": 1.78
  },
  {
   "name": "T2_gm_8",
   "expr": "sqrt(2.01*2.75)",
   "printed": 2.35
  },
  {
   "name": "T2_gm_9",
   "expr": "sqrt(1.27*1.84)",
   "printed": 1.53
  },
  {
   "name": "T2_gm_10",
   "expr": "sqrt(1.69*2.41)",
   "printed": 2.02
  },
  {
   "name": "T2_gm_11",
   "expr": "sqrt(1.02*1.3)",
   "printed": 1.15
  },
  {
   "name": "T2_gm_12",
   "expr": "sqrt(1.25*1.48)",
   "printed": 1.36
  },
  {
   "name": "T2_gm_13",
   "expr": "sqrt(0.84*0.99)",
   "printed": 0.91
  },
  {
   "name": "T2_gm_14",
   "expr": "sqrt(0.67*0.9)",
   "printed": 0.78
  },
  {
   "name": "T2_gm_15",
   "expr": "sqrt(0.87*0.99)",
   "printed": 0.93
  }
 ],
 "hyps": [
  [
   "each P95 Table 2 RR equals the geometric mean of its CI within 0.02 (log-symmetric CIs)",
   "all(abs(v['diff']) <= 0.02 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
