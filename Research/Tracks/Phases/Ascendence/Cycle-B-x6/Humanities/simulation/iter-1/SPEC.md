# SIM-AS-HUM-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P92's printed numbers: listener counts, rating total, age means, ANOVA mean squares, implied residual MS, F p-values and articulation means

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
| H1 | hypothesis | P92's listener counts, rating total, age-group means and articulation means follow from its printed numbers within rounding (0.06) |
| H2 | hypothesis | Table 4 mean squares equal SumSq/df within 1 |
| H3 | hypothesis | the F values imply one residual mean square (within 2 between the condition and three-way rows) |
| H4 | hypothesis | printed p-values for age:scale and the three-way term reproduce within 20% relative |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic audit; F p-values via scipy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-HUM-B",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 36501,
 "items": [
  {
   "name": "listeners_after_exclusions",
   "expr": "71-(2+1+4+2+1+1)",
   "printed": 60
  },
  {
   "name": "listener_groups_sum",
   "expr": "15+15+10+20",
   "printed": 60
  },
  {
   "name": "ratings_total",
   "expr": "60*15*8",
   "printed": 7200
  },
  {
   "name": "neutral_mean_from_ages",
   "expr": "(53.7+56.1)/2",
   "printed": 54.9
  },
  {
   "name": "creak_mean_from_ages",
   "expr": "(50.2+53.5)/2",
   "printed": 51.8
  },
  {
   "name": "uptalk_mean_from_ages",
   "expr": "(43.6+38)/2",
   "printed": 40.8
  },
  {
   "name": "MS_scale",
   "expr": "29706/7",
   "printed": 4244
  },
  {
   "name": "MS_condition",
   "expr": "260654/2",
   "printed": 130327
  },
  {
   "name": "MS_age_scale",
   "expr": "5988/7",
   "printed": 855
  },
  {
   "name": "MS_age_cond",
   "expr": "25927/2",
   "printed": 12963
  },
  {
   "name": "MS_scale_cond",
   "expr": "38270/14",
   "printed": 2734
  },
  {
   "name": "MS_3way",
   "expr": "10991/14",
   "printed": 785
  },
  {
   "name": "resid_MS_from_condition",
   "expr": "130327/479.1"
  },
  {
   "name": "resid_MS_from_3way",
   "expr": "785/2.89"
  },
  {
   "name": "p_age_scale",
   "expr": "float(__import__('scipy.stats', fromlist=['f']).f.sf(3.14, 7, 7076))",
   "printed": 0.00256
  },
  {
   "name": "p_3way",
   "expr": "float(__import__('scipy.stats', fromlist=['f']).f.sf(2.89, 14, 7076))",
   "printed": 0.00023
  },
  {
   "name": "artic_neutral",
   "expr": "(5.01+5.56+5.69)/3",
   "printed": 5.42
  },
  {
   "name": "artic_creaky",
   "expr": "(4.54+4.98+5.60)/3",
   "printed": 5.04
  },
  {
   "name": "artic_uptalk",
   "expr": "(4.89+5.35+5.40)/3",
   "printed": 5.21
  },
  {
   "name": "artic_S1",
   "expr": "(5.01+4.54+4.89)/3",
   "printed": 4.81
  }
 ],
 "hyps": [
  [
   "P92's listener counts, rating total, age-group means and articulation means follow from its printed numbers within rounding (0.06)",
   "all(abs(o['items'][k]['diff']) <= 0.06 for k in ['listeners_after_exclusions','listener_groups_sum','ratings_total','neutral_mean_from_ages','creak_mean_from_ages','uptalk_mean_from_ages','artic_neutral','artic_creaky','artic_uptalk','artic_S1'])"
  ],
  [
   "Table 4 mean squares equal SumSq/df within 1",
   "all(abs(o['items'][k]['diff']) <= 1 for k in ['MS_scale','MS_condition','MS_age_scale','MS_age_cond','MS_scale_cond','MS_3way'])"
  ],
  [
   "the F values imply one residual mean square (within 2 between the condition and three-way rows)",
   "abs(o['items']['resid_MS_from_condition']['value'] - o['items']['resid_MS_from_3way']['value']) <= 2"
  ],
  [
   "printed p-values for age:scale and the three-way term reproduce within 20% relative",
   "abs(o['items']['p_age_scale']['diff']) <= 0.2*0.00256 and abs(o['items']['p_3way']['diff']) <= 0.2*0.00023"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
