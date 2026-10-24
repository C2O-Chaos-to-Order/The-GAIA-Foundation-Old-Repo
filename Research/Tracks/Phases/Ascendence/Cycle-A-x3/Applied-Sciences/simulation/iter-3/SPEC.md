# SIM-AS-APP-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P91's printed statistics: do totals, univariate odds ratios and chi-square p-values follow from its counts, do audited percentages match counts, and does the 4400 m AMS percentage use the 717 who reached 4400 m?

## Phase operationalization tested
APP Ascendence = ascent protocol and AMS (P91).

## Sources this run draws on
P91 (Zhao, Zhao, Ma, Liu, Chen & Sha 2024, 'Dynamics in the prevalence and clinical manifestations of acute mountain sickness of different ascent protocols during high altitudes exposure', Front Public Health 12:1472935, PMC11617577, CC BY; read in full in ASA): 770 young lowland men, fast (air, n 424) vs slow (bus over 2 days, n 346) ascent to 3650 m, then 4400 m (717 reached); Tables 1-2 counts and p-values; adjusted OR fast vs slow 1.52 at 3650 m and 0.67 at 4400 m; propensity-matched 272 + 272 (Table 5).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | cohort and table totals add up (424, 346, 717) |
| H2 | hypothesis | the univariate odds ratios follow from Tables 1-2 counts within 0.01 |
| H3 | hypothesis | the six printed chi-square p-values reproduce within 0.005 (Pearson, no continuity correction) |
| H4 | hypothesis | the audited Table 2 and Table 5 percentages match their counts within 0.1 points |
| H5 | hypothesis | the 4400 m AMS percentage (36.0%) uses the 717 subjects who reached 4400 m |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit (Pearson chi-square without continuity correction; P91 does not say which). Foreknowledge from reading: the agent noticed while reading that 277 is 36.0% of 770, not of 717, and some Table 5 percentages differ from count/272. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-A",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 35403,
 "items": [
  {
   "name": "T1_fast_total",
   "expr": "155+269",
   "printed": 424
  },
  {
   "name": "T1_slow_total",
   "expr": "96+250",
   "printed": 346
  },
  {
   "name": "T2_total",
   "expr": "277+440",
   "printed": 717
  },
  {
   "name": "pct_AMS_4400_old_of717",
   "expr": "100*277/717",
   "printed": 36.0
  },
  {
   "name": "pct_AMS_4400_old_of770",
   "expr": "100*277/770",
   "printed": 36.0
  },
  {
   "name": "T1_uni_OR_old",
   "expr": "(155/96)/(269/250)",
   "printed": 1.5
  },
  {
   "name": "T2_uni_OR_old",
   "expr": "(140/137)/(263/177)",
   "printed": 0.69
  },
  {
   "name": "T1_uni_OR_new",
   "expr": "(137/85)/(287/261)",
   "printed": 1.47
  },
  {
   "name": "T2_uni_OR_new",
   "expr": "(126/131)/(277/183)",
   "printed": 0.64
  },
  {
   "name": "T1_ascent_p_old",
   "expr": "chi2_2x2(155, 96, 269, 250)",
   "printed": 0.009
  },
  {
   "name": "T2_ascent_p_old",
   "expr": "chi2_2x2(140, 137, 263, 177)",
   "printed": 0.015
  },
  {
   "name": "T5_3650_old_p",
   "expr": "chi2_2x2(103, 169, 72, 200)",
   "printed": 0.004
  },
  {
   "name": "T5_4400_old_p",
   "expr": "chi2_2x2(97, 175, 121, 151)",
   "printed": 0.036
  },
  {
   "name": "T5_3650_new_p",
   "expr": "chi2_2x2(88, 184, 63, 209)",
   "printed": 0.017
  },
  {
   "name": "T5_4400_new_p",
   "expr": "chi2_2x2(88, 184, 115, 157)",
   "printed": 0.017
  },
  {
   "name": "T5_fatigue_slow4400_pct",
   "expr": "100*150/272",
   "printed": 50.3
  },
  {
   "name": "T5_palpitation_slow3650_pct",
   "expr": "100*30/272",
   "printed": 8.7
  },
  {
   "name": "T5_dyspnea_slow4400_pct",
   "expr": "100*92/272",
   "printed": 33.5
  },
  {
   "name": "T2_others_pct",
   "expr": "100*23/277",
   "printed": 9.4
  },
  {
   "name": "T2_nationality_sum",
   "expr": "249+2+23",
   "printed": 277
  }
 ],
 "hyps": [
  [
   "cohort and table totals add up (424, 346, 717)",
   "all(o['items'][k]['diff'] == 0 for k in ['T1_fast_total','T1_slow_total','T2_total'])"
  ],
  [
   "the univariate odds ratios follow from Tables 1-2 counts within 0.01",
   "all(abs(o['items'][k]['diff']) <= 0.01 for k in ['T1_uni_OR_old','T2_uni_OR_old','T1_uni_OR_new','T2_uni_OR_new'])"
  ],
  [
   "the six printed chi-square p-values reproduce within 0.005 (Pearson, no continuity correction)",
   "all(abs(o['items'][k]['diff']) <= 0.005 for k in ['T1_ascent_p_old','T2_ascent_p_old','T5_3650_old_p','T5_4400_old_p','T5_3650_new_p','T5_4400_new_p'])"
  ],
  [
   "the audited Table 2 and Table 5 percentages match their counts within 0.1 points",
   "all(abs(o['items'][k]['diff']) <= 0.1 for k in ['T5_fatigue_slow4400_pct','T5_palpitation_slow3650_pct','T5_dyspnea_slow4400_pct','T2_others_pct'])"
  ],
  [
   "the 4400 m AMS percentage (36.0%) uses the 717 subjects who reached 4400 m",
   "abs(o['items']['pct_AMS_4400_old_of717']['diff']) <= 0.1"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
