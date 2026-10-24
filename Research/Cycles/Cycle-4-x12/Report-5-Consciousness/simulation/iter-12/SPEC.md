# SIM-R5-C4 - iteration 12 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Negative control: destroy temporal order.

## Refinement from previous iteration
Shuffles bins.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H12 | hypothesis | shuffled max|r_k| < 0.05; original within 0.03 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Generic Poisson branching process (Y01's model class), not a brain model; binomial subsampling; seeded. Avalanche exponent by a simple continuous-approximation MLE (s_min = 1). Nothing fitted to recordings.

## Command
`python sim_r5.py iter-12` (run from `Report-5-Consciousness/simulation/`)
