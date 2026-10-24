# SIM-AL-SOC-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Prosocial outcome: if the printed CIs (4.83 [3.25, 6.42], 4.04 [2.46, 5.63]) are Tukey intervals, is the implied F within 10% of the printed 30.67, and does eta squared .47 follow from F(2, 69)?

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
| H1 | hypothesis | implied F within 10% of 30.67 |
| H2 | hypothesis | eta squared within 0.005 of .47 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge by hand while reading: implied MSW about 5.25 and F about 30.7; eta squared 61.34/130.34 = 0.47.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-C",
 "iteration": 4,
 "kind": "summary_audit",
 "seed": 27304,
 "hyps": [
  [
   "implied F within 10% of 30.67",
   "abs(o['tukey_ci']['implied_F'] / 30.67 - 1) < 0.1"
  ],
  [
   "eta squared within 0.005 of .47",
   "abs(o['eta2']['eta2'] - 0.47) < 0.005"
  ]
 ],
 "tukey_ci": {
  "k": 3,
  "n": 24,
  "df": 69,
  "diffs": [
   4.83,
   4.04
  ],
  "cis": {
   "a": [
    3.25,
    6.42
   ],
   "b": [
    2.46,
    5.63
   ]
  },
  "printed_F": 30.67
 },
 "eta2": {
  "F": 30.67,
  "df1": 2,
  "df2": 69,
  "printed": 0.47
 }
}
```

## Command
`python sim_soc.py iter-4` (run from `Social-Sciences/simulation/`)
