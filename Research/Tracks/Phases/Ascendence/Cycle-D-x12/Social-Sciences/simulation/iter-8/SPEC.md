# SIM-AS-SOC-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P96 arithmetic

## Phase operationalization tested
SOC Ascendence = upward and total intergenerational mobility (P87; P93 for women's educational mobility). ASD adds P96's US rank-based relative and absolute mobility.

## Sources this run draws on
P96 (Song, Massey, Rolf, Ferrie, Rothbaum & Xie 2020, 'Long-term decline in intergenerational mobility in the United States since the 1850s', PNAS 117:251-258, PMC6955340, CC BY-NC-ND; read in full in ASD, SI Appendix not read): father-son occupational rank-rank correlations rising from about 0.17 (1830 cohort) to 0.27 (1900) and 0.32 (1980); absolute upward mobility (>= 7.5 points on a 0-100 rank scale of 70 occupations) rising before 1900 and falling after 1940; the role of the farm-to-factory shift.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P96's 'average increase of 0.01 in every 10 y', '165 y' and '16 cohorts' follow from its endpoints |
| H2 | hypothesis | most of the rise in rank-rank correlation (0.17 to 0.32) happened by the 1900 cohort (0.27): share above one half |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-D",
 "iteration": 8,
 "kind": "arith_audit",
 "seed": 38308,
 "items": [
  {
   "name": "corr_rise_per_decade",
   "expr": "(0.32-0.17)/15",
   "printed": 0.01
  },
  {
   "name": "years_1850_2015",
   "expr": "2015-1850",
   "printed": 165
  },
  {
   "name": "cohorts_1830_1980",
   "expr": "(1980-1830)/10+1",
   "printed": 16
  },
  {
   "name": "farm_pop_rise",
   "expr": "32.5/4.9"
  },
  {
   "name": "farm_share_fall",
   "expr": "57-13"
  },
  {
   "name": "threshold_in_ranks",
   "expr": "7.5*69/100"
  },
  {
   "name": "pre1900_share_of_rise",
   "expr": "(0.27-0.17)/(0.32-0.17)"
  }
 ],
 "hyps": [
  [
   "P96's 'average increase of 0.01 in every 10 y', '165 y' and '16 cohorts' follow from its endpoints",
   "abs(o['items']['corr_rise_per_decade']['diff']) <= 0.0005 and o['items']['years_1850_2015']['diff'] == 0 and o['items']['cohorts_1830_1980']['diff'] == 0"
  ],
  [
   "most of the rise in rank-rank correlation (0.17 to 0.32) happened by the 1900 cohort (0.27): share above one half",
   "o['items']['pre1900_share_of_rise']['value'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-8` (run from `Social-Sciences/simulation/`)
