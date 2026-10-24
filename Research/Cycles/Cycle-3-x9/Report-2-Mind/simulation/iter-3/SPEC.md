# SIM-R2-C3 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Context specificity: LI in animals is attenuated by a context change; do the models reproduce that with context as a cue?

## Refinement from previous iteration
Adds a context cue present during pre-exposure.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | context change attenuates LI >= 50% in PH and KF |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-3` (run from `Report-2-Mind/simulation/`)
