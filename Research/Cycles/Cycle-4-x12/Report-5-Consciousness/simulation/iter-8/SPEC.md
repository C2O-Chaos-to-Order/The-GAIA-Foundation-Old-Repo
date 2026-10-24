# SIM-R5-C4 - iteration 8 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Can sparse sampling (1%) still tell 'slightly subcritical' (0.98) from 'critical' (0.999)?

## Refinement from previous iteration
Two m values, five seeds each.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H8 | hypothesis | non-overlapping estimates |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-8` (run from `Report-5-Consciousness/simulation/`)
