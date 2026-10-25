# SIM-TR-APP-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P103 with a small effect (d .30): power at 34 completers?

## Phase operationalization tested
APP Transcendence = self-transcendence measured and promoted in nursing (P100; P103 added in TRA).

## Sources this run draws on
P103 (Kim & Ahn 2021, 'Development and application of a self-transcendence enhancement program for the well-being of elderly women living alone in Korea', Korean J Women Health Nurs 27:128-140, PMC9334186, CC BY 4.0; read in full in TRA): single-group pre-post, 40 recruited, 34 completed; Reed's Self-Transcendence Scale; Table 2 characteristics (N 34); Table 3 pre/post means, SDs, paired t and one-tailed p; a priori n 32 (d .45, one-sided, power .80); reasons for discontinuation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 with 1 df equals 0.05 within 1e-9 |
| H1 | hypothesis | P103's design with a small effect (d .30): power at 34 completers below 0.80 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Noncentral t, one-sided. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-APP-C",
 "iteration": 8,
 "kind": "arith_audit",
 "seed": 42408,
 "items": [
  {
   "name": "pow_d30_n34",
   "expr": "nct_pow1(0.30*sqrt(34), 33)"
  },
  {
   "name": "pow_d30_n70",
   "expr": "nct_pow1(0.30*sqrt(70), 69)"
  },
  {
   "name": "n_for_80_d30",
   "expr": "min(n for n in range(5, 400) if nct_pow1(0.30*sqrt(n), n-1) >= 0.80)"
  }
 ],
 "hyps": [
  [
   "P103's design with a small effect (d .30): power at 34 completers below 0.80",
   "o['items']['pow_d30_n34']['value'] < 0.80"
  ]
 ]
}
```

## Command
`python sim_app.py iter-8` (run from `Applied-Sciences/simulation/`)
