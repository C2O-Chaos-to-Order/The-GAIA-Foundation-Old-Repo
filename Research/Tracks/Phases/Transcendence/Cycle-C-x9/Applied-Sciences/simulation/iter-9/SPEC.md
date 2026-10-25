# SIM-TR-APP-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106: fitted challenging-experience scores at 300 ug/kg below 30%?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA). TRC adds P106's psilocybin dose-response meta-regression.

## Sources this run draws on
P106 (Hirschfeld & Schmidt 2021, 'Dose-response relationships of psilocybin-induced subjective experiences in humans', J Psychopharmacol 35:384-397, PMC8058832, CC BY 4.0; read in full in TRC): linear RVE meta-regression of 5D-ASC, 11-ASC, MEQ30 and HRS ratings on oral psilocybin dose (ug/kg) in healthy participants from the Altered States Database; Table 2 intercepts, slopes, SEs, t (df), p, Tau^2, I^2; 'complete mystical experience' (>60% on all four MEQ30 factors) expected at about 350 ug/kg and above.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9 |
| H1 | hypothesis | P106: at 300 ug/kg the fitted challenging-experience scores (Dread of Ego Dissolution, Anxiety) stay below 30% of maximum |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 9,
 "kind": "arith_audit",
 "seed": 42409,
 "items": [
  {
   "name": "slope_ratio_Oceanic_Dread",
   "expr": "0.127/0.092"
  },
  {
   "name": "pct300_Oceanic",
   "expr": "4.0+0.127*300"
  },
  {
   "name": "pct300_Dread",
   "expr": "-2.2+0.092*300"
  },
  {
   "name": "pct300_Anxiety",
   "expr": "-0.5+0.029*300"
  }
 ],
 "hyps": [
  [
   "P106: at 300 ug/kg the fitted challenging-experience scores (Dread of Ego Dissolution, Anxiety) stay below 30% of maximum",
   "o['items']['pct300_Dread']['value'] < 30 and o['items']['pct300_Anxiety']['value'] < 30"
  ]
 ]
}
```

## Command
`python sim_app.py iter-9` (run from `Applied-Sciences/simulation/`)
