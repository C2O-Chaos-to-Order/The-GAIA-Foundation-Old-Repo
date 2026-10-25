# SIM-AS-APP-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P95 Table 2 participant counts vs 2,705

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
| H1 | hypothesis | no P95 Table 2 factor has more participants than the 2,705 in the meta-analysis |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-C",
 "iteration": 2,
 "kind": "arith_audit",
 "seed": 37402,
 "items": [
  {
   "name": "T2_n_1",
   "expr": "425"
  },
  {
   "name": "T2_n_2",
   "expr": "120"
  },
  {
   "name": "T2_n_3",
   "expr": "1180"
  },
  {
   "name": "T2_n_4",
   "expr": "1270"
  },
  {
   "name": "T2_n_5",
   "expr": "2550"
  },
  {
   "name": "T2_n_6",
   "expr": "430"
  },
  {
   "name": "T2_n_7",
   "expr": "692"
  },
  {
   "name": "T2_n_8",
   "expr": "1012"
  },
  {
   "name": "T2_n_9",
   "expr": "692"
  },
  {
   "name": "T2_n_10",
   "expr": "1012"
  },
  {
   "name": "T2_n_11",
   "expr": "2895"
  },
  {
   "name": "T2_n_12",
   "expr": "1023"
  },
  {
   "name": "T2_n_13",
   "expr": "1842"
  },
  {
   "name": "T2_n_14",
   "expr": "428"
  },
  {
   "name": "T2_n_15",
   "expr": "2250"
  }
 ],
 "hyps": [
  [
   "no P95 Table 2 factor has more participants than the 2,705 in the meta-analysis",
   "all(v['value'] <= 2705 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
