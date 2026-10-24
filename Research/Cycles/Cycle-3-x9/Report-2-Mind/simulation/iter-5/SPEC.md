# SIM-R2-C3 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Model recovery with the combined parametric + delay design, generators at defaults.

## Refinement from previous iteration
Uses the designs of iterations 2 and 4.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | >= 80% recovery at noise 0.1 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-5` (run from `Report-2-Mind/simulation/`)
