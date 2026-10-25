# SIM-AS-APP-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P88's ordered-logit results: do exp(B) give the printed odds ratios, do percentages give whole counts, do the printed test statistics give the stated p-values, and does model 4 reproduce the 2.069 counterfactual for a 1-day vs 3-day Pokhara-Muktinath ascent, and as which quantity (risk ratio or odds ratio)?

## Phase operationalization tested
APP Ascendence = physical ascent to altitude; ascent rate (km/day) as a risk factor for acute mountain sickness (P88).

## Sources this run draws on
P88 (Poudel et al. 2022, ascent rate and AMS severity, Mustang district hospital, PLoS One, PMC9612449, CC BY; read in full in AS0 incl. peer-review history): N 105, AMS 74%; chi-square and t statistics; Table 2 Bayesian ordered logit (model 4: cut points -0.97, 1.48; ascent rate (km/day) 1.14; peak and residence altitude (log) -0.02, -0.08; age 31-60 0.68; smoking -1.82); response levels None, Mild, Moderate or Severe; Fig 2 counterfactual 'odds ... increase twofold (2.069)', abstract 'risk ... twice'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | odds ratios exp(B) reproduce the printed 3.13 and 0.16 within 0.01 |
| H2 | hypothesis | the severity percentages give whole counts that add up: 74.3% of 105 and 61.5/35.9/2.6% of 78 each within 0.1 of an integer, summing to 78 |
| H3 | hypothesis | the printed test statistics give p-values consistent with the text (age < 0.05; smoking within 0.001 of 0.015; alcohol < 0.001; SpO2 t within 0.001 of 0.224) |
| H4 | hypothesis | model-4 point estimates (natural logs) give a moderate/severe risk ratio within 0.05 of the printed 2.069 (1-day vs 3-day Pokhara-Muktinath) |
| H5 | hypothesis | P88's wording 'odds ... increase twofold (2.069)' holds as an odds ratio: point-estimate odds ratio within 0.5 of 2.069 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. Counterfactual from posterior point estimates (P88 averages over the posterior, so a small gap is expected); natural logs assumed for '(Log)' (log10 also reported); convention logit P(Y <= k) = c_k - eta; 2978 m gain over 1 vs 3 days; baseline as in P88's Fig 2 caption (male, 31-60, no comorbidity, non-smoker, no alcohol, 542 m residence, 3800 m peak). Foreknowledge: hand computation before running (risk ratio about 2.09, odds ratio about 9.6).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-0",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 34401,
 "items": [
  {
   "name": "OR_ascent",
   "expr": "exp(1.14)",
   "printed": 3.13
  },
  {
   "name": "OR_smoking",
   "expr": "exp(-1.82)",
   "printed": 0.16
  },
  {
   "name": "AMS_cases",
   "expr": "0.743*105",
   "printed": 78
  },
  {
   "name": "mild_n",
   "expr": "0.615*78",
   "printed": 48
  },
  {
   "name": "moderate_n",
   "expr": "0.359*78",
   "printed": 28
  },
  {
   "name": "severe_n",
   "expr": "0.026*78",
   "printed": 2
  },
  {
   "name": "p_age",
   "expr": "chi2_sf(10.17, 4)",
   "printed": 0.05
  },
  {
   "name": "p_smoking",
   "expr": "chi2_sf(8.33, 2)",
   "printed": 0.015
  },
  {
   "name": "p_alcohol",
   "expr": "chi2_sf(18.79, 2)",
   "printed": 0.001
  },
  {
   "name": "p_spo2_t",
   "expr": "t_p2(1.222, 103)",
   "printed": 0.224
  },
  {
   "name": "P_modsev_1day_ln",
   "expr": "(1-logistic(1.48-(1.14*2.978 - 0.02*log(3800) - 0.08*log(542) + 0.68)))"
  },
  {
   "name": "P_modsev_3day_ln",
   "expr": "(1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + 0.68)))"
  },
  {
   "name": "risk_ratio_ln",
   "expr": "(1-logistic(1.48-(1.14*2.978 - 0.02*log(3800) - 0.08*log(542) + 0.68)))/(1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + 0.68)))",
   "printed": 2.069
  },
  {
   "name": "odds_ratio_ln",
   "expr": "((1-logistic(1.48-(1.14*2.978 - 0.02*log(3800) - 0.08*log(542) + 0.68)))/(1-(1-logistic(1.48-(1.14*2.978 - 0.02*log(3800) - 0.08*log(542) + 0.68)))))/((1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + 0.68)))/(1-(1-logistic(1.48-(1.14*(2.978/3) - 0.02*log(3800) - 0.08*log(542) + 0.68)))))",
   "printed": 2.069
  },
  {
   "name": "risk_ratio_log10",
   "expr": "(1-logistic(1.48-(1.14*2.978 - 0.02*np.log10(3800) - 0.08*np.log10(542) + 0.68)))/(1-logistic(1.48-(1.14*(2.978/3) - 0.02*np.log10(3800) - 0.08*np.log10(542) + 0.68)))",
   "printed": 2.069
  },
  {
   "name": "odds_ratio_closed_form",
   "expr": "exp(1.14*(2.978-2.978/3))"
  }
 ],
 "hyps": [
  [
   "odds ratios exp(B) reproduce the printed 3.13 and 0.16 within 0.01",
   "abs(o['items']['OR_ascent']['diff']) <= 0.01 and abs(o['items']['OR_smoking']['diff']) <= 0.01"
  ],
  [
   "the severity percentages give whole counts that add up: 74.3% of 105 and 61.5/35.9/2.6% of 78 each within 0.1 of an integer, summing to 78",
   "all(abs(o['items'][k]['value']-round(o['items'][k]['value'])) <= 0.1 for k in ['AMS_cases','mild_n','moderate_n','severe_n']) and sum(round(o['items'][k]['value']) for k in ['mild_n','moderate_n','severe_n']) == 78"
  ],
  [
   "the printed test statistics give p-values consistent with the text (age < 0.05; smoking within 0.001 of 0.015; alcohol < 0.001; SpO2 t within 0.001 of 0.224)",
   "o['items']['p_age']['value'] < 0.05 and abs(o['items']['p_smoking']['diff']) <= 0.001 and o['items']['p_alcohol']['value'] < 0.001 and abs(o['items']['p_spo2_t']['diff']) <= 0.001"
  ],
  [
   "model-4 point estimates (natural logs) give a moderate/severe risk ratio within 0.05 of the printed 2.069 (1-day vs 3-day Pokhara-Muktinath)",
   "abs(o['items']['risk_ratio_ln']['diff']) <= 0.05"
  ],
  [
   "P88's wording 'odds ... increase twofold (2.069)' holds as an odds ratio: point-estimate odds ratio within 0.5 of 2.069",
   "abs(o['items']['odds_ratio_ln']['diff']) <= 0.5"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
