# SIM-TR-APP-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P108: do Fisher r-to-z statistics (ego-dissolution) reproduce?

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
| H1 | hypothesis | P108: Fisher r-to-z statistics for ego-dissolution vs well-being across classes reproduce within 0.05 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
z = (atanh r1 - atanh r2)/sqrt(1/(n1-3) + 1/(n2-3)). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-D",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 43403,
 "items": [
  {
   "name": "z_edi_psy_coc",
   "expr": "(np.arctanh(0.392)-np.arctanh(0.103))/sqrt(1/(1043-3)+1/(377-3))",
   "printed": 5.15
  },
  {
   "name": "z_edi_psy_alc",
   "expr": "(np.arctanh(0.392)-np.arctanh(0.084))/sqrt(1/(1043-3)+1/(408-3))",
   "printed": 5.63
  },
  {
   "name": "z_edi_coc_alc",
   "expr": "(np.arctanh(0.103)-np.arctanh(0.084))/sqrt(1/(377-3)+1/(408-3))",
   "printed": 0.267
  }
 ],
 "hyps": [
  [
   "P108: Fisher r-to-z statistics for ego-dissolution vs well-being across classes reproduce within 0.05",
   "all(abs(v['diff']) <= 0.05 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
