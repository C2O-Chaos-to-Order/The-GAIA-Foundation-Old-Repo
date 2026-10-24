# SIM-R2-C3 - iteration 9 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consolidation: replicate iteration 6 with a new seed and twice the replicates.

## Refinement from previous iteration
Replication only.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H9 | hypothesis | |diff| <= 0.05 from iteration 6 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-9` (run from `Report-2-Mind/simulation/`)
