# SIM-AS-APP-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P91 Tables 1-2: counts sum to group sizes and match percentages?

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91).

## Sources this run draws on
P91 (Zhao, Zhao, Ma, Liu, Chen & Sha 2024, 'Dynamics in the prevalence and clinical manifestations of acute mountain sickness of different ascent protocols during high altitudes exposure', Front Public Health 12:1472935, PMC11617577, CC BY; read in full in ASA): 770 young lowland men, fast (air, n 424) vs slow (bus over 2 days, n 346) ascent to 3650 m, then 4400 m (717 reached); Tables 1-2 counts and p-values; adjusted OR fast vs slow 1.52 at 3650 m and 0.67 at 4400 m; propensity-matched 272 + 272 (Table 5).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P91 Table 1 (3650 m) counts sum to the group sizes and percentages match counts within 0.1 |
| H2 | hypothesis | P91 Table 2 (4400 m) counts sum and match percentages within 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-B",
 "iteration": 6,
 "kind": "arith_audit",
 "seed": 36406,
 "items": [
  {
   "name": "T1_Han_pct",
   "expr": "100*226/251",
   "printed": 90.0
  },
  {
   "name": "T1_Tibetan_pct",
   "expr": "100*2/251",
   "printed": 0.8
  },
  {
   "name": "T1_Others_pct",
   "expr": "100*23/251",
   "printed": 9.2
  },
  {
   "name": "T1_nat_sum",
   "expr": "226+2+23",
   "printed": 251
  },
  {
   "name": "T1_smoke_sum",
   "expr": "66+59+126",
   "printed": 251
  },
  {
   "name": "T1_neg_nat_sum",
   "expr": "469+12+38",
   "printed": 519
  },
  {
   "name": "T2_neg_nat_sum",
   "expr": "394+12+34",
   "printed": 440
  },
  {
   "name": "T2_smoke_sum_pos",
   "expr": "71+60+146",
   "printed": 277
  },
  {
   "name": "T2_smoke_pct_non",
   "expr": "100*71/277",
   "printed": 25.0
  }
 ],
 "hyps": [
  [
   "P91 Table 1 (3650 m) counts sum to the group sizes and percentages match counts within 0.1",
   "all(abs(o['items'][k]['diff']) <= 0.1 for k in ['T1_Han_pct','T1_Tibetan_pct','T1_Others_pct','T1_nat_sum','T1_smoke_sum','T1_neg_nat_sum'])"
  ],
  [
   "P91 Table 2 (4400 m) counts sum and match percentages within 0.1",
   "all(abs(o['items'][k]['diff']) <= 0.1 for k in ['T2_neg_nat_sum','T2_smoke_sum_pos','T2_smoke_pct_non'])"
  ]
 ]
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
