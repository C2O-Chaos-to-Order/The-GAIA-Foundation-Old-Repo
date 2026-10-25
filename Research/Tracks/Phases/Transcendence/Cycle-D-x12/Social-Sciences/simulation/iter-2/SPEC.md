# SIM-TR-SOC-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P108 Table 2: do the percentages follow from counts?

## Phase operationalization tested
SOC Transcendence = self-transcendence values and prosocial orientation (P99). TRD adds P108's ego-dissolution measure.

## Sources this run draws on
P108 (Nour, Evans, Nutt & Carhart-Harris 2016, 'Ego-Dissolution and Psychedelics: Validation of the Ego-Dissolution Inventory (EDI)', Front Hum Neurosci 10:269, PMC4906025, CC BY 4.0; read in full in TRD): anonymous online survey, 691 subjects, 1828 drug experiences (1043 psychedelic, 377 cocaine, 408 alcohol); 16 items form two factors (8-item EDI, alpha 0.93; ego-inflation, alpha 0.91); EDI correlates with a 7-item MEQ unitive measure (rho 0.735) and with psychedelic dose (rho 0.371); Table 2 demographics; Spearman rhos, bootstrap CIs, Fisher r-to-z, dependent-correlation t-tests, Bonferroni p < 0.008.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9 |
| H1 | hypothesis | P108 Table 2: every printed percentage equals count/691 to two decimals (within 0.01) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-D",
 "iteration": 2,
 "kind": "arith_audit",
 "seed": 43302,
 "items": [
  {
   "name": "edu_noqual",
   "expr": "round(100*2/691, 2)",
   "printed": 0.29
  },
  {
   "name": "edu_gcse",
   "expr": "round(100*29/691, 2)",
   "printed": 4.2
  },
  {
   "name": "edu_hs",
   "expr": "round(100*68/691, 2)",
   "printed": 9.84
  },
  {
   "name": "edu_someuni",
   "expr": "round(100*168/691, 2)",
   "printed": 24.31
  },
  {
   "name": "edu_ba",
   "expr": "round(100*229/691, 2)",
   "printed": 33.14
  },
  {
   "name": "edu_pg",
   "expr": "round(100*195/691, 2)",
   "printed": 28.22
  },
  {
   "name": "ps_never",
   "expr": "round(100*107/691, 2)",
   "printed": 15.48
  },
  {
   "name": "ps_once",
   "expr": "round(100*26/691, 2)",
   "printed": 3.76
  },
  {
   "name": "ps_2_5",
   "expr": "round(100*106/691, 2)",
   "printed": 15.34
  },
  {
   "name": "ps_6_10",
   "expr": "round(100*92/691, 2)",
   "printed": 13.31
  },
  {
   "name": "ps_11_15",
   "expr": "round(100*69/691, 2)",
   "printed": 9.99
  },
  {
   "name": "ps_16_25",
   "expr": "round(100*69/691, 2)",
   "printed": 9.99
  },
  {
   "name": "ps_26_50",
   "expr": "round(100*87/691, 2)",
   "printed": 12.59
  },
  {
   "name": "ps_51_100",
   "expr": "round(100*68/691, 2)",
   "printed": 9.84
  },
  {
   "name": "ps_gt100",
   "expr": "round(100*67/691, 2)",
   "printed": 9.7
  },
  {
   "name": "co_never",
   "expr": "round(100*236/691, 2)",
   "printed": 34.15
  },
  {
   "name": "co_once",
   "expr": "round(100*70/691, 2)",
   "printed": 10.13
  },
  {
   "name": "co_2_5",
   "expr": "round(100*106/691, 2)",
   "printed": 15.34
  },
  {
   "name": "co_6_10",
   "expr": "round(100*59/691, 2)",
   "printed": 8.54
  },
  {
   "name": "co_11_15",
   "expr": "round(100*35/691, 2)",
   "printed": 5.07
  },
  {
   "name": "co_16_25",
   "expr": "round(100*45/691, 2)",
   "printed": 6.51
  },
  {
   "name": "co_26_50",
   "expr": "round(100*42/691, 2)",
   "printed": 6.08
  },
  {
   "name": "co_51_100",
   "expr": "round(100*47/691, 2)",
   "printed": 6.8
  },
  {
   "name": "co_gt100",
   "expr": "round(100*51/691, 2)",
   "printed": 7.38
  },
  {
   "name": "al_0",
   "expr": "round(100*191/691, 2)",
   "printed": 27.64
  },
  {
   "name": "al_1_6",
   "expr": "round(100*213/691, 2)",
   "printed": 30.82
  },
  {
   "name": "al_7_12",
   "expr": "round(100*123/691, 2)",
   "printed": 17.8
  },
  {
   "name": "al_13_18",
   "expr": "round(100*58/691, 2)",
   "printed": 8.39
  },
  {
   "name": "al_19_24",
   "expr": "round(100*38/691, 2)",
   "printed": 5.5
  },
  {
   "name": "al_25_30",
   "expr": "round(100*19/691, 2)",
   "printed": 2.75
  },
  {
   "name": "al_31_36",
   "expr": "round(100*17/691, 2)",
   "printed": 2.46
  },
  {
   "name": "al_37_42",
   "expr": "round(100*8/691, 2)",
   "printed": 1.16
  },
  {
   "name": "al_43_48",
   "expr": "round(100*7/691, 2)",
   "printed": 1.01
  },
  {
   "name": "al_49_54",
   "expr": "round(100*6/691, 2)",
   "printed": 0.89
  },
  {
   "name": "al_55_60",
   "expr": "round(100*4/691, 2)",
   "printed": 0.58
  },
  {
   "name": "al_gt60",
   "expr": "round(100*7/691, 2)",
   "printed": 1.01
  },
  {
   "name": "female",
   "expr": "round(100*238/691, 2)",
   "printed": 34.44
  }
 ],
 "hyps": [
  [
   "P108 Table 2: every printed percentage equals count/691 to two decimals (within 0.01)",
   "all(abs(v['diff']) <= 0.01 + 1e-9 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
