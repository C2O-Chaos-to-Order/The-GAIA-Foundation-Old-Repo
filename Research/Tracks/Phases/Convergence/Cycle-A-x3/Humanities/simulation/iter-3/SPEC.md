# SIM-CV-HUM-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P71's Table 1 counts, questionnaire shares and in-text chi-squares: do they add up and recompute, and are the subgroup questionnaire percentages consistent with the overall 82.1%?

## Phase operationalization tested
HUM Convergence = auditing a convergence study.

## Sources this run draws on
P71 (Sabev, Yuen, Andreeva & Moebius 2026, phonetic accommodation of German -ig, Front Psychol, PMC13585743, CC BY; read in full in CV0): 1138 trials after excluding 21 of 1159; Table 2 model selection (df, AIC, BIC, chi2, p for M0-M9); Table 3 final GLMM (beta, SE, z, p); 301/563 shadowing, 157/575 interaction.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival function at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P71 Table 1 rows and totals and the questionnaire shares (82.1 + 14.8 + 3.1) add up exactly |
| H2 | hypothesis | in-text chi-square p values within 0.002 of recomputed |
| H3 | hypothesis | every overall-vs-subgroup questionnaire percentage implies a mixing weight in [0, 1] |
| H4 | hypothesis | implied P->F weight within 0.05 of Table 1's session share 46/61 (exploratory; questionnaire counts not reported) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. The questionnaire's response counts are not reported, so the mixing weights are only checked for consistency; H4 compares with Table 1 session shares as an exploratory proxy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-A",
 "iteration": 3,
 "kind": "glmm_audit",
 "seed": 30503,
 "sums": {
  "shadowing_female": [
   [
    17,
    4
   ],
   21
  ],
  "shadowing_male": [
   [
    6,
    3
   ],
   9
  ],
  "shadowing_PF": [
   [
    17,
    6
   ],
   23
  ],
  "shadowing_FP": [
   [
    4,
    3
   ],
   7
  ],
  "shadowing_total": [
   [
    23,
    7
   ],
   30
  ],
  "interaction_female": [
   [
    16,
    4
   ],
   20
  ],
  "interaction_male": [
   [
    7,
    4
   ],
   11
  ],
  "interaction_PF": [
   [
    16,
    7
   ],
   23
  ],
  "interaction_FP": [
   [
    4,
    4
   ],
   8
  ],
  "interaction_total": [
   [
    23,
    8
   ],
   31
  ],
  "questionnaire_tenths": [
   [
    821,
    148,
    31
   ],
   1000
  ]
 },
 "chi2_text": {
  "frequency_x_direction": [
   0.63,
   1,
   0.4277
  ],
  "M4_vs_M3_text": [
   6.82,
   1,
   0.009
  ]
 },
 "mix": {
  "frequency": [
   82.1,
   86.5,
   77.3
  ],
  "direction_PF": [
   82.1,
   81.5,
   84.7
  ],
  "gender_female": [
   82.1,
   81.0,
   84.6
  ]
 },
 "hyps": [
  [
   "P71 Table 1 rows and totals and the questionnaire shares (82.1 + 14.8 + 3.1) add up exactly",
   "all(v['computed'] == v['printed'] for v in o['sums'].values())"
  ],
  [
   "in-text chi-square p values within 0.002 of recomputed",
   "all(abs(v['diff']) < 0.002 for v in o['chi2_text'].values())"
  ],
  [
   "every overall-vs-subgroup questionnaire percentage implies a mixing weight in [0, 1]",
   "all(0 <= v['implied_w'] <= 1 for v in o['mix'].values())"
  ],
  [
   "implied P->F weight within 0.05 of Table 1's session share 46/61 (exploratory; questionnaire counts not reported)",
   "abs(o['mix']['direction_PF']['implied_w']-46/61) < 0.05"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
