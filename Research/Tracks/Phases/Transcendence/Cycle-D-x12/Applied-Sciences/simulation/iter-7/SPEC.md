# SIM-TR-APP-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P108: do R^2 values agree roughly with the rhos?

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
| H1 | hypothesis | P108: intensity-EDI R^2 values imply Pearson r within 0.1 of the printed Spearman rho (0.577, 0.279, 0.334) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pearson vs Spearman; tolerance 0.1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-D",
 "iteration": 7,
 "kind": "arith_audit",
 "seed": 43407,
 "items": [
  {
   "name": "r_from_R2_psy",
   "expr": "sqrt(0.328)"
  },
  {
   "name": "r_from_R2_coc",
   "expr": "sqrt(0.078)"
  },
  {
   "name": "r_from_R2_alc",
   "expr": "sqrt(0.084)"
  }
 ],
 "hyps": [
  [
   "P108: intensity-EDI R^2 values imply Pearson r within 0.1 of the printed Spearman rho (0.577, 0.279, 0.334)",
   "abs(o['items']['r_from_R2_psy']['value']-0.577) <= 0.1 and abs(o['items']['r_from_R2_coc']['value']-0.279) <= 0.1 and abs(o['items']['r_from_R2_alc']['value']-0.334) <= 0.1"
  ]
 ]
}
```

## Command
`python sim_app.py iter-7` (run from `Applied-Sciences/simulation/`)
