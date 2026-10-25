# SIM-AS-APP-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P95 Table 2 recommendation counts

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
| H1 | hypothesis | of P95's 15 graded factors, strong recommendations (5: rapid ascent, HR moderate and marked, SpO2 marked, AMS history) are fewer than half |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's hand count of Table 2 entered as constants. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-D",
 "iteration": 12,
 "kind": "arith_audit",
 "seed": 38412,
 "items": [
  {
   "name": "strong_recs",
   "expr": "5"
  },
  {
   "name": "moderate_or_high",
   "expr": "8"
  }
 ],
 "hyps": [
  [
   "of P95's 15 graded factors, strong recommendations (5: rapid ascent, HR moderate and marked, SpO2 marked, AMS history) are fewer than half",
   "o['items']['strong_recs']['value'] < 7.5"
  ]
 ]
}
```

## Command
`python sim_app.py iter-12` (run from `Applied-Sciences/simulation/`)
