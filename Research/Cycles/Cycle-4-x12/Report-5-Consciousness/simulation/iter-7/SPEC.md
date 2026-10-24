# SIM-R5-C4 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Y02's 'driven' regime: with more input, avalanches merge; does MR still work?

## Refinement from previous iteration
Varies input h.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H7 | hypothesis | at h = 10 empty bins < 1% and MR within 0.03 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-7` (run from `Report-5-Consciousness/simulation/`)
