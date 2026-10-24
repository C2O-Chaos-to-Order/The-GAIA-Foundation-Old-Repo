# SIM-AL-SOC-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P61 re-audit: with the printed correlations, does a model without empathy reproduce the fusion path within 0.02 of .25 (empathy's path is the largest, .33)?

## Phase operationalization tested
SOC Allegiance = robustness of the 'bright side' paths (P61).

## Sources this run draws on
P61 (Shen et al. 2026, 'The bright side of identity fusion', Behav Sci, PMC13603169, CC BY; read in full in ALC): Study 1 (N = 609) correlations and standardized paths; Study 2 (N = 72, 24 per group) pre/post means and SDs, F values, Tukey-labelled differences with CIs, G*Power N 66; mediation shares.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | fusion path within 0.02 of .25 without empathy |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's model-dropping variant.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-D",
 "iteration": 4,
 "kind": "summary_audit",
 "seed": 28304,
 "hyps": [
  [
   "fusion path within 0.02 of .25 without empathy",
   "abs(o['regression']['beta']['F'] - 0.25) < 0.02"
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
   "E"
  ],
  "printed": {
   "F": 0.25,
   "E": 0.16
  }
 }
}
```

## Command
`python sim_soc.py iter-4` (run from `Social-Sciences/simulation/`)
