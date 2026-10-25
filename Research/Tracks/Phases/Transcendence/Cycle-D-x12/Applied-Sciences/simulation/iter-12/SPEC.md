# SIM-TR-APP-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106: dose at which all MEQ30 factors exceed 50%?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P106 (Hirschfeld & Schmidt 2021, 'Dose-response relationships of psilocybin-induced subjective experiences in humans', J Psychopharmacol 35:384-397, PMC8058832, CC BY 4.0; read in full in TRC): linear RVE meta-regression of 5D-ASC, 11-ASC, MEQ30 and HRS ratings on oral psilocybin dose (ug/kg) in healthy participants from the Altered States Database; Table 2 intercepts, slopes, SEs, t (df), p, Tau^2, I^2; 'complete mystical experience' (>60% on all four MEQ30 factors) expected at about 350 ug/kg and above.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9 |
| H1 | hypothesis | P106's fitted lines put all four MEQ30 factors above 50% below 250 ug/kg |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on fitted lines. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-D",
 "iteration": 12,
 "kind": "arith_audit",
 "seed": 43412,
 "items": [
  {
   "name": "dose50_all_four",
   "expr": "max((50-48.2)/0.073,(50-32.9)/0.081,(50-49.8)/0.058,(50-32.2)/0.090)"
  }
 ],
 "hyps": [
  [
   "P106's fitted lines put all four MEQ30 factors above 50% below 250 ug/kg",
   "o['items']['dose50_all_four']['value'] < 250"
  ]
 ]
}
```

## Command
`python sim_app.py iter-12` (run from `Applied-Sciences/simulation/`)
