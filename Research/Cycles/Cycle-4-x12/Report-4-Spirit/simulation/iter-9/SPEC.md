# SIM-R4-C4 - iteration 9 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Rare outcomes, as for cause-specific mortality.

## Refinement from previous iteration
Outcome prevalence 2%.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H9 | hypothesis | power >= 80% |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic cohorts with one binary unmeasured confounder and logistic outcomes; crude 2x2 odds ratios. Real negative controls are never perfect (Y03); the design numbers are illustrations, not estimates for any study.

## Command
`python sim_r4.py iter-9` (run from `Report-4-Spirit/simulation/`)
