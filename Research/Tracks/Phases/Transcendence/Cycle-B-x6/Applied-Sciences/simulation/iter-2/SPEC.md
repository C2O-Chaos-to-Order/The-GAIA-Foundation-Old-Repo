# SIM-TR-APP-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P103: post hoc power at observed t, and design power at d .45 with 34 completers?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P103 (Kim & Ahn 2021, 'Development and application of a self-transcendence enhancement program for the well-being of elderly women living alone in Korea', Korean J Women Health Nurs 27:128-140, PMC9334186, CC BY 4.0; read in full in TRA): single-group pre-post, 40 recruited, 34 completed; Reed's Self-Transcendence Scale; Table 2 characteristics (N 34); Table 3 pre/post means, SDs, paired t and one-tailed p; a priori n 32 (d .45, one-sided, power .80); reasons for discontinuation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | the design power at d .45 with the 34 completers is still at least .80 (P103 planned 32) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Noncentral t, one-sided, df 33. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-B",
 "iteration": 2,
 "kind": "arith_audit",
 "seed": 41402,
 "items": [
  {
   "name": "pow_SelfTranscendence",
   "expr": "nct_pow1(abs(8.78), 33)"
  },
  {
   "name": "pow_SpiritualWB",
   "expr": "nct_pow1(abs(8.3), 33)"
  },
  {
   "name": "pow_ReligiousSWB",
   "expr": "nct_pow1(abs(1.79), 33)"
  },
  {
   "name": "pow_ExistentialSWB",
   "expr": "nct_pow1(abs(6.75), 33)"
  },
  {
   "name": "pow_Depression",
   "expr": "nct_pow1(abs(-7.59), 33)"
  },
  {
   "name": "pow_LifeSatisfaction",
   "expr": "nct_pow1(abs(1.72), 33)"
  },
  {
   "name": "pow_PositiveAffect",
   "expr": "nct_pow1(abs(3.77), 33)"
  },
  {
   "name": "pow_NegativeAffect",
   "expr": "nct_pow1(abs(-6.15), 33)"
  },
  {
   "name": "pow_design_d45_n34",
   "expr": "nct_pow1(0.45*sqrt(34), 33)"
  }
 ],
 "hyps": [
  [
   "the design power at d .45 with the 34 completers is still at least .80 (P103 planned 32)",
   "o['items']['pow_design_d45_n34']['value'] >= 0.80"
  ]
 ]
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
