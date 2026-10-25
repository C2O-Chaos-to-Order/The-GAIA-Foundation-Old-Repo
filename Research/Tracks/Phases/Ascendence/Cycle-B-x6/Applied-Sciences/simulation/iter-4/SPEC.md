# SIM-AS-APP-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P91 Table 5 symptom p-values (fast vs slow cohort): reproduce?

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
| H1 | hypothesis | P91 Table 5 p-values printed '<0.001' are below 0.001 when recomputed (GI, insomnia, fatigue, dyspnoea at 3650 m; headache at 4400 m) |
| H2 | hypothesis | dizziness at 4400 m: p within 0.005 of the printed 0.010 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pearson chi-square without continuity correction. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-B",
 "iteration": 4,
 "kind": "arith_audit",
 "seed": 36404,
 "items": [
  {
   "name": "P3_GI",
   "expr": "chi2_2x2(71, 201, 37, 235)",
   "printed": 0.001
  },
  {
   "name": "P3_insomnia",
   "expr": "chi2_2x2(95, 177, 52, 220)",
   "printed": 0.001
  },
  {
   "name": "P3_fatigue",
   "expr": "chi2_2x2(169, 103, 101, 171)",
   "printed": 0.001
  },
  {
   "name": "P4_headache",
   "expr": "chi2_2x2(109, 163, 151, 121)",
   "printed": 0.001
  },
  {
   "name": "P4_dizziness",
   "expr": "chi2_2x2(128, 144, 158, 114)",
   "printed": 0.01
  },
  {
   "name": "P3_dyspnea",
   "expr": "chi2_2x2(95, 177, 23, 249)",
   "printed": 0.001
  }
 ],
 "hyps": [
  [
   "P91 Table 5 p-values printed '<0.001' are below 0.001 when recomputed (GI, insomnia, fatigue, dyspnoea at 3650 m; headache at 4400 m)",
   "all(o['items'][k]['value'] < 0.001 for k in ['P3_GI','P3_insomnia','P3_fatigue','P4_headache','P3_dyspnea'])"
  ],
  [
   "dizziness at 4400 m: p within 0.005 of the printed 0.010",
   "abs(o['items']['P4_dizziness']['diff']) <= 0.005"
  ]
 ]
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
