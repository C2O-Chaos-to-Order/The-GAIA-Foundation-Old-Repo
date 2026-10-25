# SIM-TR-APP-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P106: do Table 1's dose conditions add to the reported observation counts?

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
| H1 | hypothesis | P106 Table 1: the 5D-ASC dose conditions of the included samples add to the 14 observations the text reports |
| H2 | hypothesis | the MEQ30 (11) and 11-ASC (10) observation counts match Table 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Counting Table 1's listed dosages for included samples (agent's reading). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 6,
 "kind": "arith_audit",
 "seed": 42406,
 "items": [
  {
   "name": "obs_5DASC",
   "expr": "1+4+2+3+1+1+1",
   "printed": 14
  },
  {
   "name": "samples_5DASC",
   "expr": "1+1+1+1+1+2",
   "printed": 7
  },
  {
   "name": "obs_11ASC_4scales",
   "expr": "1+1+1+1+2+1+3",
   "printed": 10
  },
  {
   "name": "obs_MEQ30",
   "expr": "3+1+4+3",
   "printed": 11
  },
  {
   "name": "studies_table1",
   "expr": "17",
   "printed": 17
  }
 ],
 "hyps": [
  [
   "P106 Table 1: the 5D-ASC dose conditions of the included samples add to the 14 observations the text reports",
   "o['items']['obs_5DASC']['diff'] == 0"
  ],
  [
   "the MEQ30 (11) and 11-ASC (10) observation counts match Table 1",
   "o['items']['obs_MEQ30']['diff'] == 0 and o['items']['obs_11ASC_4scales']['diff'] == 0"
  ]
 ]
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
