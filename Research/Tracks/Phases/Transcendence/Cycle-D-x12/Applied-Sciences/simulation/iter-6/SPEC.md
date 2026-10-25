# SIM-TR-APP-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P108: does every bootstrap CI contain its rho?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA). TRD adds P108's ego-dissolution measure.

## Sources this run draws on
P108 (Nour, Evans, Nutt & Carhart-Harris 2016, 'Ego-Dissolution and Psychedelics: Validation of the Ego-Dissolution Inventory (EDI)', Front Hum Neurosci 10:269, PMC4906025, CC BY 4.0; read in full in TRD): anonymous online survey, 691 subjects, 1828 drug experiences (1043 psychedelic, 377 cocaine, 408 alcohol); 16 items form two factors (8-item EDI, alpha 0.93; ego-inflation, alpha 0.91); EDI correlates with a 7-item MEQ unitive measure (rho 0.735) and with psychedelic dose (rho 0.371); Table 2 demographics; Spearman rhos, bootstrap CIs, Fisher r-to-z, dependent-correlation t-tests, Bonferroni p < 0.008.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9 |
| H1 | hypothesis | P108: every printed bootstrap 95% CI contains its rho |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-D",
 "iteration": 6,
 "kind": "arith_audit",
 "seed": 43406,
 "items": [
  {
   "name": "in_ci_unit_edi",
   "expr": "int(0.704 <= 0.735 <= 0.763)"
  },
  {
   "name": "in_ci_unit_inf",
   "expr": "int(0.219 <= 0.274 <= 0.332)"
  },
  {
   "name": "in_ci_psy_dose_edi",
   "expr": "int(0.317 <= 0.371 <= 0.427)"
  },
  {
   "name": "in_ci_psy_dose_inf",
   "expr": "int(0.003 <= 0.063 <= 0.127)"
  },
  {
   "name": "in_ci_coc_dose_inf",
   "expr": "int(0.39 <= 0.385 <= 0.477)"
  },
  {
   "name": "in_ci_coc_dose_edi",
   "expr": "int(0.012 <= 0.115 <= 0.211)"
  },
  {
   "name": "in_ci_alc_dose_edi",
   "expr": "int(-0.15 <= -0.055 <= 0.048)"
  },
  {
   "name": "in_ci_alc_dose_inf",
   "expr": "int(-0.148 <= -0.054 <= 0.037)"
  },
  {
   "name": "in_ci_psy_int_edi",
   "expr": "int(0.529 <= 0.577 <= 0.621)"
  },
  {
   "name": "in_ci_psy_int_inf",
   "expr": "int(0.04 <= 0.099 <= 0.159)"
  },
  {
   "name": "in_ci_coc_int_inf",
   "expr": "int(0.464 <= 0.545 <= 0.625)"
  },
  {
   "name": "in_ci_alc_int_inf",
   "expr": "int(0.41 <= 0.502 <= 0.582)"
  },
  {
   "name": "in_ci_coc_int_edi",
   "expr": "int(0.18 <= 0.279 <= 0.378)"
  },
  {
   "name": "in_ci_alc_int_edi",
   "expr": "int(0.237 <= 0.334 <= 0.421)"
  },
  {
   "name": "in_ci_psy_wb_edi",
   "expr": "int(0.342 <= 0.392 <= 0.442)"
  },
  {
   "name": "in_ci_coc_wb_edi",
   "expr": "int(-0.006 <= 0.103 <= 0.204)"
  },
  {
   "name": "in_ci_alc_wb_edi",
   "expr": "int(-0.009 <= 0.084 <= 0.181)"
  },
  {
   "name": "in_ci_psy_wb_inf",
   "expr": "int(0.135 <= 0.198 <= 0.263)"
  },
  {
   "name": "in_ci_coc_wb_inf",
   "expr": "int(-0.198 <= -0.083 <= 0.027)"
  },
  {
   "name": "in_ci_alc_wb_inf",
   "expr": "int(-0.216 <= -0.112 <= -0.014)"
  }
 ],
 "hyps": [
  [
   "P108: every printed bootstrap 95% CI contains its rho",
   "all(v['value'] == 1 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
