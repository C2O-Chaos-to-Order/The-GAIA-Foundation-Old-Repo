# SIM-R5-C4 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Does the MR estimator recover m under the same subsampling?

## Refinement from previous iteration
Adds MR (k = 1..40).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | |MR - m| < 0.02 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-3` (run from `Report-5-Consciousness/simulation/`)
