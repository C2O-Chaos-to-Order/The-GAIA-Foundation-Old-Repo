# SIM-R4-C2 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Carried agenda (C1 R4: mediation designs). Baseline: under the no-unmeasured-confounding assumption S12 states, the product-of-coefficients method recovers the indirect effect and proportion mediated (PM).

## Refinement from previous iteration
First iteration; establishes the estimator is correct before stressing it.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | indirect effect within 3 SE |
| V1b | validation | PM within 0.02 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic linear-Gaussian (and one logistic) data with known truth; illustrates estimator behaviour only. Does not re-analyse S12 or any cohort, and says nothing about whether religious practice causes health effects.

## Command
`python sim_r4.py iter-1` (run from `Report-4-Spirit/simulation/`)
