# SIM-AS-APP-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Cross-source: P91 and P88 ascent risk ratios vs P95's rapid-ascent RR

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91). ASC adds P95's meta-analysis.

## Sources this run draws on
P95 (Liu, Tan, Ren, Bai, Yong, Gao, Ba & Gongga 2026, 'Prevalence and risk factors for AMS: A systematic review and meta-analysis', PLoS One, PMC13068236, CC BY; read in full in ASC): 58 observational studies (stated n 2,705), pooled AMS prevalence 48.25% (95% CI 42.58-53.96), Table 1 study list, Table 2 GRADE risk ratios incl. rapid ascent (<6 h) RR 1.60 (1.44-1.78). P91 (Zhao, Zhao, Ma, Liu, Chen & Sha 2024, 'Dynamics in the prevalence and clinical manifestations of acute mountain sickness of different ascent protocols during high altitudes exposure', Front Public Health 12:1472935, PMC11617577, CC BY; read in full in ASA): 770 young lowland men, fast (air, n 424) vs slow (bus over 2 days, n 346) ascent to 3650 m, then 4400 m (717 reached); Tables 1-2 counts and p-values; adjusted OR fast vs slow 1.52 at 3650 m and 0.67 at 4400 m; propensity-matched 272 + 272 (Table 5). P88 (Poudel et al. 2022, ascent rate and AMS severity, Mustang district hospital, PLoS One, PMC9612449, CC BY; read in full in AS0 incl. peer-review history): N 105, AMS 74%; chi-square and t statistics; Table 2 Bayesian ordered logit (model 4: cut points -0.97, 1.48; ascent rate (km/day) 1.14; peak and residence altitude (log) -0.02, -0.08; age 31-60 0.68; smoking -1.82); response levels None, Mild, Moderate or Severe; Fig 2 counterfactual 'odds ... increase twofold (2.069)', abstract 'risk ... twice'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P91's matched first-stage risk ratio (fast vs slow, 37.9% / 26.5%) lies inside P95's CI for rapid ascent (1.44-1.78) |
| H2 | hypothesis | P88's 1-day/3-day risk ratio (2.069) exceeds P95's upper CI limit for rapid ascent (1.78) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Different exposure definitions (agent's comparison). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-C",
 "iteration": 8,
 "kind": "arith_audit",
 "seed": 37408,
 "items": [
  {
   "name": "P91_matched_RR_3650",
   "expr": "37.9/26.5"
  },
  {
   "name": "P88_RR_1v3",
   "expr": "2.069"
  }
 ],
 "hyps": [
  [
   "P91's matched first-stage risk ratio (fast vs slow, 37.9% / 26.5%) lies inside P95's CI for rapid ascent (1.44-1.78)",
   "1.44 <= o['items']['P91_matched_RR_3650']['value'] <= 1.78"
  ],
  [
   "P88's 1-day/3-day risk ratio (2.069) exceeds P95's upper CI limit for rapid ascent (1.78)",
   "o['items']['P88_RR_1v3']['value'] > 1.78"
  ]
 ]
}
```

## Command
`python sim_app.py iter-8` (run from `Applied-Sciences/simulation/`)
