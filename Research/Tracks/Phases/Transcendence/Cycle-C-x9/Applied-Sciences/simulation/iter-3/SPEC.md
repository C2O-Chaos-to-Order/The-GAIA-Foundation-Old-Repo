# SIM-TR-APP-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106 Table 2: do printed p-values follow from t and df?

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
| H1 | hypothesis | P106 Table 2: every printed p is within 0.02 of the two-sided t p-value at slope/SE and the printed df |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-sided t; fractional Satterthwaite df as printed. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 3,
 "kind": "arith_audit",
 "seed": 42403,
 "items": [
  {
   "name": "p_AuditoryAlt",
   "expr": "t_p2(0.044/0.0062, 1.5)",
   "printed": 0.04
  },
  {
   "name": "p_OceanicB",
   "expr": "t_p2(0.127/0.0388, 3.1)",
   "printed": 0.045
  },
  {
   "name": "p_DreadEgo",
   "expr": "t_p2(0.092/0.0093, 3.0)",
   "printed": 0.002
  },
  {
   "name": "p_VigilanceRed",
   "expr": "t_p2(0.098/0.0252, 1.9)",
   "printed": 0.065
  },
  {
   "name": "p_VisionaryR",
   "expr": "t_p2(0.151/0.039, 3.3)",
   "printed": 0.026
  },
  {
   "name": "p_Anxiety",
   "expr": "t_p2(0.029/0.0203, 1.3)",
   "printed": 0.348
  },
  {
   "name": "p_AVSynesthesia",
   "expr": "t_p2(0.061/0.0692, 1.3)",
   "printed": 0.51
  },
  {
   "name": "p_Blissful",
   "expr": "t_p2(0.117/0.0352, 1.5)",
   "printed": 0.115
  },
  {
   "name": "p_ComplexImag",
   "expr": "t_p2(0.117/0.0796, 1.3)",
   "printed": 0.338
  },
  {
   "name": "p_ChangedMeaning",
   "expr": "t_p2(-0.01/0.0432, 1.3)",
   "printed": 0.85
  },
  {
   "name": "p_Disembodiment",
   "expr": "t_p2(0.067/0.0611, 1.3)",
   "printed": 0.435
  },
  {
   "name": "p_ElementaryImag",
   "expr": "t_p2(0.111/0.127, 1.3)",
   "printed": 0.517
  },
  {
   "name": "p_Unity",
   "expr": "t_p2(0.099/0.0103, 1.5)",
   "printed": 0.025
  },
  {
   "name": "p_Insight",
   "expr": "t_p2(0.095/0.0172, 1.5)",
   "printed": 0.055
  },
  {
   "name": "p_ImpairedCtrl",
   "expr": "t_p2(-0.007/0.0089, 1.2)",
   "printed": 0.579
  },
  {
   "name": "p_Spiritual",
   "expr": "t_p2(0.132/0.0632, 1.6)",
   "printed": 0.205
  },
  {
   "name": "p_Ineffability",
   "expr": "t_p2(0.073/0.0243, 2.3)",
   "printed": 0.081
  },
  {
   "name": "p_Mystical",
   "expr": "t_p2(0.081/0.0264, 2.3)",
   "printed": 0.078
  },
  {
   "name": "p_PositiveMood",
   "expr": "t_p2(0.058/0.0239, 2.3)",
   "printed": 0.122
  },
  {
   "name": "p_TranscTimeSpace",
   "expr": "t_p2(0.09/0.0227, 2.3)",
   "printed": 0.048
  }
 ],
 "hyps": [
  [
   "P106 Table 2: every printed p is within 0.02 of the two-sided t p-value at slope/SE and the printed df",
   "all(abs(v['diff']) <= 0.02 for v in o['items'].values())"
  ]
 ]
}
```

## Command
`python sim_app.py iter-3` (run from `Applied-Sciences/simulation/`)
