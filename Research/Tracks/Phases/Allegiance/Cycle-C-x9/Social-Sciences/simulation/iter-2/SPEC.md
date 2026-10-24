# SIM-AL-SOC-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Study 2 post-test: does the F follow from the printed means and SDs, and do Tukey HSD comparisons support P61's 'social > personal' and 'social > control'?

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
| H1 | hypothesis | F within 0.05 of 5.94 |
| H2 | hypothesis | social vs personal significant by Tukey HSD |
| H3 | hypothesis | social vs control significant by Tukey HSD |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Group 0 = social, 1 = personal, 2 = control (P61's order). Foreknowledge by hand arithmetic while reading: Tukey HSD about 2.69 > the 2.54 social-personal difference, so H2 expected not supported; the smoke test (seed 99) also ran this configuration.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-C",
 "iteration": 2,
 "kind": "summary_audit",
 "seed": 27302,
 "hyps": [
  [
   "F within 0.05 of 5.94",
   "abs(o['anova']['diff']) < 0.05"
  ],
  [
   "social vs personal significant by Tukey HSD",
   "o['anova']['tukey']['pairs']['0-1']['sig']"
  ],
  [
   "social vs control significant by Tukey HSD",
   "o['anova']['tukey']['pairs']['0-2']['sig']"
  ]
 ],
 "anova": {
  "means": [
   38.21,
   35.67,
   34.42
  ],
  "sds": [
   4.23,
   3.6,
   3.8
  ],
  "n": [
   24,
   24,
   24
  ],
  "printed_F": 5.94,
  "tukey": [
   [
    0,
    1
   ],
   [
    0,
    2
   ],
   [
    1,
    2
   ]
  ]
 }
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
