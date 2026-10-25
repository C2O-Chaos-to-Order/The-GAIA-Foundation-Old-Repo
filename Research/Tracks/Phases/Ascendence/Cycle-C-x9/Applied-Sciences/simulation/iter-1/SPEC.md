# SIM-AS-APP-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P95 Table 1: do sample sizes sum to 2,705?

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
| H1 | hypothesis | P95 Table 1 sample sizes sum to the stated 2,705 participants |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's transcription of 58 rows. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-C",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 37401,
 "items": [
  {
   "name": "T1_rows",
   "expr": "58",
   "printed": 58
  },
  {
   "name": "T1_n_sum",
   "expr": "103+50+35+20+43+18+29+42+19+170+50+50+43+12+77+44+135+20+30+19+13+15+12+51+20+20+21+31+20+14+37+86+102+54+19+109+22+42+16+42+102+13+164+19+20+10+12+21+64+11+11+42+65+104+119+59+102+12",
   "printed": 2705
  }
 ],
 "hyps": [
  [
   "P95 Table 1 sample sizes sum to the stated 2,705 participants",
   "o['items']['T1_n_sum']['diff'] == 0"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
