# SIM-TR-APP-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106: at what dose do the fitted lines put all four MEQ30 factors above 60%?

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
| H1 | hypothesis | P106: the dose at which all four MEQ30 factors exceed 60% (fitted lines) is between 300 and 400 ug/kg ('approximately 350 ug/kg') |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on the fitted lines; extrapolation not checked. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 5,
 "kind": "arith_audit",
 "seed": 42405,
 "items": [
  {
   "name": "dose60_Ineffability",
   "expr": "(60-48.2)/0.073"
  },
  {
   "name": "dose60_Mystical",
   "expr": "(60-32.9)/0.081"
  },
  {
   "name": "dose60_PositiveMood",
   "expr": "(60-49.8)/0.058"
  },
  {
   "name": "dose60_TranscTimeSpace",
   "expr": "(60-32.2)/0.090"
  },
  {
   "name": "dose60_all_four",
   "expr": "max((60-48.2)/0.073,(60-32.9)/0.081,(60-49.8)/0.058,(60-32.2)/0.090)"
  }
 ],
 "hyps": [
  [
   "P106: the dose at which all four MEQ30 factors exceed 60% (fitted lines) is between 300 and 400 ug/kg ('approximately 350 ug/kg')",
   "300 <= o['items']['dose60_all_four']['value'] <= 400"
  ]
 ]
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
