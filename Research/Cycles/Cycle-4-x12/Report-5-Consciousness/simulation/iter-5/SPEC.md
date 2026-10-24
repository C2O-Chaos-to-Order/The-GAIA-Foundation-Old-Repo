# SIM-R5-C4 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Near-critical, sparse sampling (m 0.99, alpha 0.01): how long must recordings be?

## Refinement from previous iteration
Varies recording length.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | mean |err| < 0.01 at T = 1e5 |
| H5r | reporting | error by T |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-5` (run from `Report-5-Consciousness/simulation/`)
