# SIM-AS-HUM-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P92: residual df, age differences by condition, F p-values

## Phase operationalization tested
HUM Ascendence = rising intonation (uptalk; P89, P92) and the spread of a minority rising variant.

## Sources this run draws on
P92 (Calhoun & White 2025, 'What Makes Iconic Pitch Associations "Natural": The Effect of Age on Affective Meanings of Uptalk and Creak', Lang Speech 68:606-632, PMC12365360, CC BY-NC; read in full in ASB): matched-guise ratings of uptalk, creak and neutral NZ English by 60 listeners (71 collected), 7,200 ratings; Table 4 ANOVA; mean ratings by age; Tables 2-3 F0 and articulation rate.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P92's residual df (7076) equals 7200 - 1 - the fixed-effect df (47) |
| H2 | hypothesis | by mean ratings, the age-group difference is largest for creak (P92: age differences 'especially for creak') |
| H3 | hypothesis | age:condition and scale:condition F values give p below 1e-10 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit; F p-values via scipy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-HUM-C",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 37501,
 "items": [
  {
   "name": "resid_df_fixed_only",
   "expr": "7200-1-(1+7+2+7+2+14+14)",
   "printed": 7076
  },
  {
   "name": "age_diff_neutral",
   "expr": "56.1-53.7"
  },
  {
   "name": "age_diff_creak",
   "expr": "53.5-50.2"
  },
  {
   "name": "age_diff_uptalk",
   "expr": "43.6-38"
  },
  {
   "name": "p_age_cond",
   "expr": "float(__import__('scipy.stats', fromlist=['f']).f.sf(47.65, 2, 7076))"
  },
  {
   "name": "p_scale_cond",
   "expr": "float(__import__('scipy.stats', fromlist=['f']).f.sf(10.05, 14, 7076))"
  }
 ],
 "hyps": [
  [
   "P92's residual df (7076) equals 7200 - 1 - the fixed-effect df (47)",
   "o['items']['resid_df_fixed_only']['diff'] == 0"
  ],
  [
   "by mean ratings, the age-group difference is largest for creak (P92: age differences 'especially for creak')",
   "o['items']['age_diff_creak']['value'] > max(o['items']['age_diff_uptalk']['value'], o['items']['age_diff_neutral']['value'])"
  ],
  [
   "age:condition and scale:condition F values give p below 1e-10",
   "o['items']['p_age_cond']['value'] < 1e-10 and o['items']['p_scale_cond']['value'] < 1e-10"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
