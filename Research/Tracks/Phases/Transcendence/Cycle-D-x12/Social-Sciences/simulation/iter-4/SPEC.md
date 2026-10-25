# SIM-TR-SOC-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P108: is the sample mostly male and mostly experienced users, as stated?

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
| H1 | hypothesis | P108: over half the subjects had used psychedelics on over 10 occasions, and most were male |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-D",
 "iteration": 4,
 "kind": "arith_audit",
 "seed": 43304,
 "items": [
  {
   "name": "share_psy_gt10",
   "expr": "(69+69+87+68+67)/691"
  },
  {
   "name": "share_male",
   "expr": "1-238/691"
  }
 ],
 "hyps": [
  [
   "P108: over half the subjects had used psychedelics on over 10 occasions, and most were male",
   "o['items']['share_psy_gt10']['value'] > 0.5 and o['items']['share_male']['value'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-4` (run from `Social-Sciences/simulation/`)
