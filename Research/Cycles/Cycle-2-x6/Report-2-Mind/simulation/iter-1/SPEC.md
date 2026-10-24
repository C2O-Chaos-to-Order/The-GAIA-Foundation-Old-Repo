# SIM-R2-C2 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Carried agenda (C1 R2): Rescorla-Wagner cannot produce latent inhibition (LI); test whether a Pearce-Hall-type hybrid and a Kalman-filter (Bayesian) learner produce BOTH LI and blocking.

## Refinement from previous iteration
Cycle 1 found RW blocking but no LI. This iteration adds the Bayesian learner suggested by W06.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | RW converges to lambda |
| V2 | validation | RW LI index = 0 |
| V3 | validation | RW blocking >= 0.8 |
| H_PH | hypothesis | PH: LI >= 0.2 and blocking >= 0.5 |
| H_KF | hypothesis | KF: LI >= 0.2 and blocking >= 0.5 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook model forms implemented by us; the PH variant is the common hybrid (delta rule x associability), not the original 1980 equations. No animal or human data are fitted; LI/blocking thresholds are our own pre-registered bars.

## Command
`python sim_r2.py iter-1` (run from `Report-2-Mind/simulation/`)
