# SIM-AL-SOC-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Study 1: do the printed standardized paths to prosocial behaviour (fusion .25, efficacy .16, empathy .33) follow from P61's printed correlation matrix?

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
| H1 | hypothesis | betas within 0.02 of printed |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Correlations printed to two decimals, so betas carry rounding error of about 0.01. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-C",
 "iteration": 1,
 "kind": "summary_audit",
 "seed": 27301,
 "hyps": [
  [
   "betas within 0.02 of printed",
   "o['regression']['max_diff'] < 0.02"
  ]
 ],
 "regression": {
  "names": [
   "F",
   "E",
   "M",
   "Y"
  ],
  "R": [
   [
    1,
    0.75,
    0.13,
    0.4
   ],
   [
    0.75,
    1,
    0.11,
    0.37
   ],
   [
    0.13,
    0.11,
    1,
    0.38
   ],
   [
    0.4,
    0.37,
    0.38,
    1
   ]
  ],
  "y": "Y",
  "x": [
   "F",
   "E",
   "M"
  ],
  "printed": {
   "F": 0.25,
   "E": 0.16,
   "M": 0.33
  }
 }
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
