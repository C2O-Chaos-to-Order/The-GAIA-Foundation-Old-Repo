# SIM-TR-APP-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106 Table 2 (MEQ30): as iter-1.

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
| H1 | hypothesis | P106 Table 2 (MEQ30): every printed t equals slope/SE within rounding |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iter-1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 2,
 "kind": "arith_audit",
 "seed": 42402,
 "items": [
  {
   "name": "t_Ineffability",
   "expr": "0.073/0.0243",
   "printed": 3.0
  },
  {
   "name": "tol_Ineffability",
   "expr": "0.0005/0.0243 + 0.05 + 1e-9"
  },
  {
   "name": "t_Mystical",
   "expr": "0.081/0.0264",
   "printed": 3.1
  },
  {
   "name": "tol_Mystical",
   "expr": "0.0005/0.0264 + 0.05 + 1e-9"
  },
  {
   "name": "t_PositiveMood",
   "expr": "0.058/0.0239",
   "printed": 2.4
  },
  {
   "name": "tol_PositiveMood",
   "expr": "0.0005/0.0239 + 0.05 + 1e-9"
  },
  {
   "name": "t_TranscTimeSpace",
   "expr": "0.09/0.0227",
   "printed": 3.9
  },
  {
   "name": "tol_TranscTimeSpace",
   "expr": "0.0005/0.0227 + 0.05 + 1e-9"
  }
 ],
 "hyps": [
  [
   "P106 Table 2 (MEQ30): every printed t equals slope/SE within rounding",
   "all(abs(o['items']['t_'+k[4:]]['diff']) <= o['items'][k]['value'] for k in o['items'] if k.startswith('tol_'))"
  ]
 ]
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
