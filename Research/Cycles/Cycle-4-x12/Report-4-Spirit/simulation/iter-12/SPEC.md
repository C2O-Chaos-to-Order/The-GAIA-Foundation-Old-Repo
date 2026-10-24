# SIM-R4-C4 - iteration 12 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consolidation: confounding plus a true effect.

## Refinement from previous iteration
Combines iterations 2 and 4.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H12 | hypothesis | flag and correct |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic cohorts with one binary unmeasured confounder and logistic outcomes; crude 2x2 odds ratios. Real negative controls are never perfect (Y03); the design numbers are illustrations, not estimates for any study.

## Command
`python sim_r4.py iter-12` (run from `Report-4-Spirit/simulation/`)
