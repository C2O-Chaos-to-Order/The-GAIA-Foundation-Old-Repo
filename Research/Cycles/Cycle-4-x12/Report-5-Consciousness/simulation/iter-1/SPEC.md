# SIM-R5-C4 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check for the new measure: PAR stationary mean and full-sampling estimator.

## Refinement from previous iteration
New simulation for the carried item 'R5 better criticality measure (avalanches)'; replaces Cycle-3's network peak measure for this question.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean = h/(1-m) within 2% |
| V2 | validation | conventional = m within 0.01 at full sampling |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-1` (run from `Report-5-Consciousness/simulation/`)
