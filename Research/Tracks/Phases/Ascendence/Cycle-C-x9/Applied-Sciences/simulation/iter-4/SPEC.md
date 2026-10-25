# SIM-AS-APP-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P95 stated prevalence range vs Table 1

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
| H1 | hypothesis | P95's stated range 5.5%-83% matches Table 1's minimum and maximum |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-C",
 "iteration": 4,
 "kind": "arith_audit",
 "seed": 37404,
 "items": [
  {
   "name": "T1_max_prev",
   "expr": "max([73,26,63,70,60.46,38.89,62,28.57,11,32,40,40,43,83,81.18,66.7,41,35,43.4,68,69.2,67,67,45.1,50,20,52.4,35.5,60,43,62.2,55.8,60.8,5.5,74,40.4,45,63,84,66,36,23.1,21.9,58,47,50,56,52,20.3,81.8,72,69,28.6,17,34,51,47.1,58.3])",
   "printed": 83
  },
  {
   "name": "T1_min_prev",
   "expr": "min([73,26,63,70,60.46,38.89,62,28.57,11,32,40,40,43,83,81.18,66.7,41,35,43.4,68,69.2,67,67,45.1,50,20,52.4,35.5,60,43,62.2,55.8,60.8,5.5,74,40.4,45,63,84,66,36,23.1,21.9,58,47,50,56,52,20.3,81.8,72,69,28.6,17,34,51,47.1,58.3])",
   "printed": 5.5
  }
 ],
 "hyps": [
  [
   "P95's stated range 5.5%-83% matches Table 1's minimum and maximum",
   "o['items']['T1_max_prev']['diff'] == 0 and o['items']['T1_min_prev']['diff'] == 0"
  ]
 ]
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
