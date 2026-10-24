# SIM-R4-C2 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Violate the mediator-outcome no-confounding assumption with an unmeasured U and measure the bias in PM.

## Refinement from previous iteration
Uses the estimator validated in iteration 1.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V2 | validation | removing U's contribution recovers truth |
| H1 | hypothesis | u = 0.3 biases PM by >= 25% relative |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic linear-Gaussian (and one logistic) data with known truth; illustrates estimator behaviour only. Does not re-analyse S12 or any cohort, and says nothing about whether religious practice causes health effects.

## Command
`python sim_r4.py iter-2` (run from `Report-4-Spirit/simulation/`)
