# SIM-R5-C4 - iteration 11 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Replication of iteration 4 with new seeds.

## Refinement from previous iteration
Seeds 500+.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H11 | hypothesis | >= 90% of cells |err| < 0.03 |
| H11r | reporting | conventional at alpha 0.01 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-11` (run from `Report-5-Consciousness/simulation/`)
