# SIM-R2-C2 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Identifiability under more noise.

## Refinement from previous iteration
Extends iteration 4 to noise 0.1 and 0.2.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| MR_0.1 | hypothesis | diagnostic accuracy >= 0.8 |
| MG_0.1 | hypothesis | gain >= 0.2 |
| MR_0.2 | hypothesis | diagnostic accuracy >= 0.8 |
| MG_0.2 | hypothesis | gain >= 0.2 |
| MR_r | reporting | confusion matrices |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook model forms implemented by us; the PH variant is the common hybrid (delta rule x associability), not the original 1980 equations. No animal or human data are fitted; LI/blocking thresholds are our own pre-registered bars.

## Command
`python sim_r2.py iter-5` (run from `Report-2-Mind/simulation/`)
