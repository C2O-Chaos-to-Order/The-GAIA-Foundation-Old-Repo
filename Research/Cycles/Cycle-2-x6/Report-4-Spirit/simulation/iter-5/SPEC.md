# SIM-R4-C2 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Inference: at a realistic sample size, does the usual (Sobel) 95% CI keep its coverage, and how much does moderate unmeasured M-Y confounding destroy it?

## Refinement from previous iteration
Turns the iteration-2 bias into a statement about confidence intervals.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V4 | validation | coverage in [0.90, 0.99] without confounding |
| H4 | hypothesis | u = 0.3: coverage < 0.5 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic linear-Gaussian (and one logistic) data with known truth; illustrates estimator behaviour only. Does not re-analyse S12 or any cohort, and says nothing about whether religious practice causes health effects.

## Command
`python sim_r4.py iter-5` (run from `Report-4-Spirit/simulation/`)
