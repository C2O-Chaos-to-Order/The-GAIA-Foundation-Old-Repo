# SIM-R2-C3 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Sensitivity: how much of the KF parameter space shows the delay signature?

## Refinement from previous iteration
Grid sensitivity of iteration 4.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H7 | hypothesis | delay drop >= 0.1 in >= 70% of grid |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-7` (run from `Report-2-Mind/simulation/`)
