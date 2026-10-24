# SIM-R2-C2 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Are the iteration-1 results properties of the models or of the default parameters? Sweep each model's parameter grid.

## Refinement from previous iteration
Generalises iteration 1 over parameters.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| S1 | validation | RW never shows LI |
| S2 | hypothesis | PH both phenomena in >= 50% of grid |
| S3 | hypothesis | KF both in >= 50% of grid |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook model forms implemented by us; the PH variant is the common hybrid (delta rule x associability), not the original 1980 equations. No animal or human data are fitted; LI/blocking thresholds are our own pre-registered bars.

## Command
`python sim_r2.py iter-2` (run from `Report-2-Mind/simulation/`)
