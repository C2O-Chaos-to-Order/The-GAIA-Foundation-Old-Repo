# SIM-R2-C3 - iteration 8 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Challenge: does a third, Mackintosh-type account break recovery?

## Refinement from previous iteration
Three-way recovery, off-grid.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H8 | hypothesis | >= 70% three-way recovery at noise 0.1 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-8` (run from `Report-2-Mind/simulation/`)
