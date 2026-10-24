# SIM-R2-C2 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Dose-response: does LI grow with the number of pre-exposures in PH and KF?

## Refinement from previous iteration
Iterations 1-2 used a single pre-exposure length.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| D_PH | hypothesis | Spearman >= 0.9 |
| D_KF | hypothesis | Spearman >= 0.9 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook model forms implemented by us; the PH variant is the common hybrid (delta rule x associability), not the original 1980 equations. No animal or human data are fitted; LI/blocking thresholds are our own pre-registered bars.

## Command
`python sim_r2.py iter-3` (run from `Report-2-Mind/simulation/`)
