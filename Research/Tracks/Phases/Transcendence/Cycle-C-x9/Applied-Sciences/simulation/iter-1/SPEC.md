# SIM-TR-APP-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106 Table 2 (5D-ASC, 11-ASC): does each t equal slope/SE?

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
| H1 | hypothesis | P106 Table 2 (5D-ASC and 11-ASC): every printed t equals slope/SE within rounding (0.0005/SE + 0.05) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic; rounding tolerance 0.0005/SE + 0.05. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 42401,
 "items": [
  {
   "name": "t_AuditoryAlt",
   "expr": "0.044/0.0062",
   "printed": 7.1
  },
  {
   "name": "tol_AuditoryAlt",
   "expr": "0.0005/0.0062 + 0.05 + 1e-9"
  },
  {
   "name": "t_OceanicB",
   "expr": "0.127/0.0388",
   "printed": 3.3
  },
  {
   "name": "tol_OceanicB",
   "expr": "0.0005/0.0388 + 0.05 + 1e-9"
  },
  {
   "name": "t_DreadEgo",
   "expr": "0.092/0.0093",
   "printed": 9.8
  },
  {
   "name": "tol_DreadEgo",
   "expr": "0.0005/0.0093 + 0.05 + 1e-9"
  },
  {
   "name": "t_VigilanceRed",
   "expr": "0.098/0.0252",
   "printed": 3.9
  },
  {
   "name": "tol_VigilanceRed",
   "expr": "0.0005/0.0252 + 0.05 + 1e-9"
  },
  {
   "name": "t_VisionaryR",
   "expr": "0.151/0.039",
   "printed": 3.9
  },
  {
   "name": "tol_VisionaryR",
   "expr": "0.0005/0.039 + 0.05 + 1e-9"
  },
  {
   "name": "t_Anxiety",
   "expr": "0.029/0.0203",
   "printed": 1.4
  },
  {
   "name": "tol_Anxiety",
   "expr": "0.0005/0.0203 + 0.05 + 1e-9"
  },
  {
   "name": "t_AVSynesthesia",
   "expr": "0.061/0.0692",
   "printed": 0.9
  },
  {
   "name": "tol_AVSynesthesia",
   "expr": "0.0005/0.0692 + 0.05 + 1e-9"
  },
  {
   "name": "t_Blissful",
   "expr": "0.117/0.0352",
   "printed": 3.3
  },
  {
   "name": "tol_Blissful",
   "expr": "0.0005/0.0352 + 0.05 + 1e-9"
  },
  {
   "name": "t_ComplexImag",
   "expr": "0.117/0.0796",
   "printed": 1.5
  },
  {
   "name": "tol_ComplexImag",
   "expr": "0.0005/0.0796 + 0.05 + 1e-9"
  },
  {
   "name": "t_ChangedMeaning",
   "expr": "-0.01/0.0432",
   "printed": -0.2
  },
  {
   "name": "tol_ChangedMeaning",
   "expr": "0.0005/0.0432 + 0.05 + 1e-9"
  },
  {
   "name": "t_Disembodiment",
   "expr": "0.067/0.0611",
   "printed": 1.1
  },
  {
   "name": "tol_Disembodiment",
   "expr": "0.0005/0.0611 + 0.05 + 1e-9"
  },
  {
   "name": "t_ElementaryImag",
   "expr": "0.111/0.127",
   "printed": 0.9
  },
  {
   "name": "tol_ElementaryImag",
   "expr": "0.0005/0.127 + 0.05 + 1e-9"
  },
  {
   "name": "t_Unity",
   "expr": "0.099/0.0103",
   "printed": 9.6
  },
  {
   "name": "tol_Unity",
   "expr": "0.0005/0.0103 + 0.05 + 1e-9"
  },
  {
   "name": "t_Insight",
   "expr": "0.095/0.0172",
   "printed": 5.5
  },
  {
   "name": "tol_Insight",
   "expr": "0.0005/0.0172 + 0.05 + 1e-9"
  },
  {
   "name": "t_ImpairedCtrl",
   "expr": "-0.007/0.0089",
   "printed": -0.7
  },
  {
   "name": "tol_ImpairedCtrl",
   "expr": "0.0005/0.0089 + 0.05 + 1e-9"
  },
  {
   "name": "t_Spiritual",
   "expr": "0.132/0.0632",
   "printed": 2.1
  },
  {
   "name": "tol_Spiritual",
   "expr": "0.0005/0.0632 + 0.05 + 1e-9"
  }
 ],
 "hyps": [
  [
   "P106 Table 2 (5D-ASC and 11-ASC): every printed t equals slope/SE within rounding (0.0005/SE + 0.05)",
   "all(abs(o['items']['t_'+k[4:]]['diff']) <= o['items'][k]['value'] for k in o['items'] if k.startswith('tol_'))"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
