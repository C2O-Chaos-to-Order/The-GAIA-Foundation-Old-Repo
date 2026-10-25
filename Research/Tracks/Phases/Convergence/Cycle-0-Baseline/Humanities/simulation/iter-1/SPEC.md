# SIM-CV-HUM-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P71's statistics: do Table 2's BIC values follow from AIC and df (n 1138), do its LR chi-squares and p values follow from AIC differences, do Table 3's z and p follow from beta/SE, and do the printed percentages and counts add up?

## Phase operationalization tested
HUM Convergence = phonetic convergence (accommodation): speakers shifting toward an interlocutor's variant (P71).

## Sources this run draws on
P71 (Sabev, Yuen, Andreeva & Moebius 2026, phonetic accommodation of German -ig, Front Psychol, PMC13585743, CC BY; read in full in CV0): 1138 trials after excluding 21 of 1159; Table 2 model selection (df, AIC, BIC, chi2, p for M0-M9); Table 3 final GLMM (beta, SE, z, p); 301/563 shadowing, 157/575 interaction.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival function at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | every printed BIC equals AIC + df (ln 1138 - 2) within 0.05 |
| H2 | hypothesis | every printed LR chi-square equals the AIC-implied value within 0.05 and every printed p within 0.002 of the recomputed p |
| H3 | hypothesis | every printed z within 0.1 of beta/SE and printed p within 0.002 of 2(1 - Phi(|z|)) |
| H4 | hypothesis | printed percentages within 0.1 and sums exact |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic arithmetic audit; tolerances (BIC 0.05; chi2 0.05; p 0.002; z 0.1; % 0.1) set before the smoke test. Inputs are rounded to 2 decimals, so recomputed p values carry rounding error. Foreknowledge: a hand check before running found no errors.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-0",
 "iteration": 1,
 "kind": "glmm_audit",
 "seed": 29501,
 "n_obs": 1138,
 "models": [
  [
   "M0",
   8,
   898.39,
   938.69
  ],
  [
   "M1",
   18,
   848.36,
   939.03
  ],
  [
   "M2",
   13,
   841.93,
   907.41
  ],
  [
   "M3",
   12,
   840.23,
   900.68
  ],
  [
   "M4",
   13,
   835.41,
   900.89
  ],
  [
   "M5",
   14,
   837.13,
   907.65
  ],
  [
   "M6",
   14,
   836.77,
   907.28
  ],
  [
   "M7",
   17,
   839.27,
   924.9
  ],
  [
   "M8",
   17,
   835.5,
   921.13
  ],
  [
   "M9",
   14,
   829.93,
   900.45
  ]
 ],
 "comparisons": [
  [
   "M1",
   "M0",
   70.03,
   0.0
  ],
  [
   "M1",
   "M2",
   3.56,
   0.6141
  ],
  [
   "M2",
   "M3",
   0.31,
   0.5797
  ],
  [
   "M4",
   "M3",
   6.82,
   0.009
  ],
  [
   "M5",
   "M4",
   0.28,
   0.6
  ],
  [
   "M6",
   "M4",
   0.64,
   0.4229
  ],
  [
   "M7",
   "M4",
   4.14,
   0.3878
  ],
  [
   "M8",
   "M4",
   7.91,
   0.095
  ],
  [
   "M9",
   "M4",
   7.48,
   0.0062
  ]
 ],
 "coefs": [
  [
   "Intercept",
   -2.13,
   0.68,
   -3.14,
   0.0017
  ],
  [
   "order",
   0.47,
   0.1,
   4.67,
   0.0
  ],
  [
   "task",
   1.77,
   0.45,
   3.95,
   0.0001
  ],
  [
   "frequency",
   0.27,
   0.25,
   1.06,
   0.2882
  ],
  [
   "gender",
   -4.02,
   1.35,
   -2.97,
   0.003
  ],
  [
   "direction",
   -1.87,
   1.32,
   -1.42,
   0.1567
  ],
  [
   "task:frequency",
   1.68,
   0.52,
   3.25,
   0.0012
  ],
  [
   "task:gender",
   1.86,
   0.9,
   2.07,
   0.0388
  ],
  [
   "frequency:gender",
   -0.86,
   0.51,
   -1.7,
   0.0901
  ],
  [
   "task:direction",
   -3.92,
   0.58,
   -6.73,
   0.0
  ],
  [
   "gender:direction",
   -5.75,
   2.68,
   -2.14,
   0.0323
  ],
  [
   "task:frequency:gender",
   2.6,
   1.03,
   2.53,
   0.0115
  ]
 ],
 "percents": {
  "shadowing": [
   301,
   563,
   53.5
  ],
  "interaction": [
   157,
   575,
   27.3
  ],
  "overall": [
   458,
   1138,
   40.2
  ]
 },
 "sums": {
  "accommodated": [
   [
    301,
    157
   ],
   458
  ],
  "trials": [
   [
    563,
    575
   ],
   1138
  ],
  "after_exclusion": [
   [
    1159,
    -21
   ],
   1138
  ],
  "participants": [
   [
    30,
    31,
    -19
   ],
   42
  ]
 },
 "hyps": [
  [
   "every printed BIC equals AIC + df (ln 1138 - 2) within 0.05",
   "all(abs(v['diff'])<0.05 for v in o['bic'].values())"
  ],
  [
   "every printed LR chi-square equals the AIC-implied value within 0.05 and every printed p within 0.002 of the recomputed p",
   "all(abs(v['chi2_diff'])<0.05 and abs(v['p']-v['printed_p'])<0.002 for v in o['lr'].values())"
  ],
  [
   "every printed z within 0.1 of beta/SE and printed p within 0.002 of 2(1 - Phi(|z|))",
   "all(abs(v['z_diff'])<0.1 and abs(v['p_from_printed_z']-v['printed_p'])<0.002 for v in o['coefs'].values())"
  ],
  [
   "printed percentages within 0.1 and sums exact",
   "all(abs(v['diff'])<0.1 for v in o['percents'].values()) and all(v['computed']==v['printed'] for v in o['sums'].values())"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
