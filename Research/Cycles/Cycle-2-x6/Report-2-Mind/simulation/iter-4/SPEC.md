# SIM-R2-C2 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Identifiability: if data came from one model, can a fit tell which? Model recovery with an acquisition-only design vs a diagnostic design (acquisition + LI + blocking).

## Refinement from previous iteration
Iterations 1-3 showed where the models differ qualitatively; this tests whether those differences are recoverable from noisy data.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| MR_0.05 | hypothesis | diagnostic accuracy >= 0.8 |
| MG_0.05 | hypothesis | diagnostic beats acquisition-only by >= 0.2 |
| MR_r | reporting | confusion matrices |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook model forms implemented by us; the PH variant is the common hybrid (delta rule x associability), not the original 1980 equations. No animal or human data are fitted; LI/blocking thresholds are our own pre-registered bars. Generating parameters are drawn from the same grid used for fitting (optimistic).

## Command
`python sim_r2.py iter-4` (run from `Report-2-Mind/simulation/`)
