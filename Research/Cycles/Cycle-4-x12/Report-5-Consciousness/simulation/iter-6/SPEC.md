# SIM-R5-C4 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Avalanche statistics under subsampling (Y02).

## Refinement from previous iteration
Separation of time scales (h = 0.01) so avalanches are defined.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | exponent shifts by > 0.2 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings. Exponent MLE is crude and ignores cut-offs.

## Command
`python sim_r5.py iter-6` (run from `Report-5-Consciousness/simulation/`)
