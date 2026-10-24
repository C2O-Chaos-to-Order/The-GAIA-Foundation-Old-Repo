# SIM-AL-SOC-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Study 1 mediation shares: do the printed percentages equal part/total, and do the parts sum to the total?

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
| H1 | hypothesis | percentages within 0.05 points of part/total |
| H2 | hypothesis | parts sum to total within 0.005 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge from reading: 0.06 + 0.02 + 0.12 = 0.20 versus total 0.21.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-C",
 "iteration": 6,
 "kind": "summary_audit",
 "seed": 27306,
 "hyps": [
  [
   "percentages within 0.05 points of part/total",
   "o['shares']['study1']['max_pct_diff'] < 0.05"
  ],
  [
   "parts sum to total within 0.005",
   "abs(o['shares']['study1']['sum_parts'] - o['shares']['study1']['total']) < 0.005"
  ]
 ],
 "shares": {
  "study1": {
   "parts": {
    "efficacy": 0.06,
    "empathy": 0.02,
    "direct": 0.12
   },
   "total": 0.21,
   "printed_pct": {
    "efficacy": 28.57,
    "empathy": 9.52,
    "direct": 57.14
   }
  }
 }
}
```

## Command
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
