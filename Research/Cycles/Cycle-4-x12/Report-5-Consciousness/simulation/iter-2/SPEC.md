# SIM-R5-C4 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Replicate Y01's central claim: conventional estimation underestimates m under subsampling.

## Refinement from previous iteration
Adds binomial subsampling (alpha 0.1).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | underestimate by > 0.1 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-2` (run from `Report-5-Consciousness/simulation/`)
