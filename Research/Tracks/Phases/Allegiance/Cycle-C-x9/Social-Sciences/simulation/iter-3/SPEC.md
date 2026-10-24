# SIM-AL-SOC-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Study 2 pre-test: does F 0.73 follow from the printed pre-test means and SDs (groups equivalent at baseline)?

## Phase operationalization tested
SOC Allegiance = auditing a 'bright side of fusion' study from its printed summaries (P61).

## Sources this run draws on
P61 (Shen et al. 2026, 'The bright side of identity fusion', Behav Sci, PMC13603169, CC BY; read in full in ALC): Study 1 (N = 609) correlations and standardized paths; Study 2 (N = 72, 24 per group) pre/post means and SDs, F values, Tukey-labelled differences with CIs, G*Power N 66; mediation shares.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | F within 0.05 of 0.73 |
| H2 | hypothesis | F below the 5% critical value 3.13 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-C",
 "iteration": 3,
 "kind": "summary_audit",
 "seed": 27303,
 "hyps": [
  [
   "F within 0.05 of 0.73",
   "abs(o['anova']['diff']) < 0.05"
  ],
  [
   "F below the 5% critical value 3.13",
   "o['anova']['F'] < 3.13"
  ]
 ],
 "anova": {
  "means": [
   35.5,
   34.21,
   35.38
  ],
  "sds": [
   4.16,
   3.96,
   4.12
  ],
  "n": [
   24,
   24,
   24
  ],
  "printed_F": 0.73
 }
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
