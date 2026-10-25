# SIM-TR-APP-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106 Table 2: do CI widths follow from SE and df?

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
| H1 | hypothesis | P106 Table 2: every 95% CI half-width / SE is within 10% of the t critical value at the printed df |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
t quantile at the printed df. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 4,
 "kind": "arith_audit",
 "seed": 42404,
 "items": [
  {
   "name": "tcritimp_AuditoryAlt",
   "expr": "(0.081-0.006)/(2*0.0062)"
  },
  {
   "name": "tcrit_AuditoryAlt",
   "expr": "t_q(0.975, 1.5)"
  },
  {
   "name": "tcritimp_OceanicB",
   "expr": "(0.249-0.005)/(2*0.0388)"
  },
  {
   "name": "tcrit_OceanicB",
   "expr": "t_q(0.975, 3.1)"
  },
  {
   "name": "tcritimp_DreadEgo",
   "expr": "(0.122-0.062)/(2*0.0093)"
  },
  {
   "name": "tcrit_DreadEgo",
   "expr": "t_q(0.975, 3.0)"
  },
  {
   "name": "tcritimp_VigilanceRed",
   "expr": "(0.211--0.015)/(2*0.0252)"
  },
  {
   "name": "tcrit_VigilanceRed",
   "expr": "t_q(0.975, 1.9)"
  },
  {
   "name": "tcritimp_VisionaryR",
   "expr": "(0.269-0.032)/(2*0.039)"
  },
  {
   "name": "tcrit_VisionaryR",
   "expr": "t_q(0.975, 3.3)"
  },
  {
   "name": "tcritimp_Anxiety",
   "expr": "(0.179--0.121)/(2*0.0203)"
  },
  {
   "name": "tcrit_Anxiety",
   "expr": "t_q(0.975, 1.3)"
  },
  {
   "name": "tcritimp_AVSynesthesia",
   "expr": "(0.571--0.449)/(2*0.0692)"
  },
  {
   "name": "tcrit_AVSynesthesia",
   "expr": "t_q(0.975, 1.3)"
  },
  {
   "name": "tcritimp_Blissful",
   "expr": "(0.324--0.091)/(2*0.0352)"
  },
  {
   "name": "tcrit_Blissful",
   "expr": "t_q(0.975, 1.5)"
  },
  {
   "name": "tcritimp_ComplexImag",
   "expr": "(0.713--0.48)/(2*0.0796)"
  },
  {
   "name": "tcrit_ComplexImag",
   "expr": "t_q(0.975, 1.3)"
  },
  {
   "name": "tcritimp_ChangedMeaning",
   "expr": "(0.332--0.352)/(2*0.0432)"
  },
  {
   "name": "tcrit_ChangedMeaning",
   "expr": "t_q(0.975, 1.3)"
  },
  {
   "name": "tcritimp_Disembodiment",
   "expr": "(0.536--0.401)/(2*0.0611)"
  },
  {
   "name": "tcrit_Disembodiment",
   "expr": "t_q(0.975, 1.3)"
  },
  {
   "name": "tcritimp_ElementaryImag",
   "expr": "(1.09--0.873)/(2*0.127)"
  },
  {
   "name": "tcrit_ElementaryImag",
   "expr": "t_q(0.975, 1.3)"
  },
  {
   "name": "tcritimp_Unity",
   "expr": "(0.16-0.038)/(2*0.0103)"
  },
  {
   "name": "tcrit_Unity",
   "expr": "t_q(0.975, 1.5)"
  },
  {
   "name": "tcritimp_Insight",
   "expr": "(0.197--0.006)/(2*0.0172)"
  },
  {
   "name": "tcrit_Insight",
   "expr": "t_q(0.975, 1.5)"
  },
  {
   "name": "tcritimp_ImpairedCtrl",
   "expr": "(0.07--0.093)/(2*0.0089)"
  },
  {
   "name": "tcrit_ImpairedCtrl",
   "expr": "t_q(0.975, 1.2)"
  },
  {
   "name": "tcritimp_Spiritual",
   "expr": "(0.488--0.224)/(2*0.0632)"
  },
  {
   "name": "tcrit_Spiritual",
   "expr": "t_q(0.975, 1.6)"
  },
  {
   "name": "tcritimp_Ineffability",
   "expr": "(0.166--0.02)/(2*0.0243)"
  },
  {
   "name": "tcrit_Ineffability",
   "expr": "t_q(0.975, 2.3)"
  },
  {
   "name": "tcritimp_Mystical",
   "expr": "(0.183--0.021)/(2*0.0264)"
  },
  {
   "name": "tcrit_Mystical",
   "expr": "t_q(0.975, 2.3)"
  },
  {
   "name": "tcritimp_PositiveMood",
   "expr": "(0.15--0.034)/(2*0.0239)"
  },
  {
   "name": "tcrit_PositiveMood",
   "expr": "t_q(0.975, 2.3)"
  },
  {
   "name": "tcritimp_TranscTimeSpace",
   "expr": "(0.175-0.002)/(2*0.0227)"
  },
  {
   "name": "tcrit_TranscTimeSpace",
   "expr": "t_q(0.975, 2.3)"
  }
 ],
 "hyps": [
  [
   "P106 Table 2: every 95% CI half-width / SE is within 10% of the t critical value at the printed df",
   "all(abs(o['items']['tcritimp_'+k[6:]]['value'] / o['items'][k]['value'] - 1) <= 0.10 for k in o['items'] if k.startswith('tcrit_'))"
  ]
 ]
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
