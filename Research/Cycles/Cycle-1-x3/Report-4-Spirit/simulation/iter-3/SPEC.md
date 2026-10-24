# SIM-R4-C1 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
What do the sibling fixed-effects and instrument designs of V16/V17 buy? Simulate known truth (beta = -0.1) under family-only confounding, individual confounding, and an instrument that violates exclusion.

## Refinement from previous iteration
Reads `../iter-2/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| S1 | validation | family-only confounding: sibling FE unbiased, naive biased |
| S2 | validation | individual confounding biases sibling FE |
| S3 | validation | valid instrument recovers beta |
| S4 | validation | exclusion violation biases IV |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Linear-Gaussian design simulation; validates the logic of the designs, not V16/V17's data.

## Command
`python sim_r4.py iter-3` (run from `Report-4-Spirit/simulation/`)
