# SIM-R2-C3 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Delay signature: does an interval between pre-exposure and conditioning separate the accounts?

## Refinement from previous iteration
Adds empty delay steps.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | KF LI drops >= 50% with delay; PH changes < 5% |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-4` (run from `Report-2-Mind/simulation/`)
