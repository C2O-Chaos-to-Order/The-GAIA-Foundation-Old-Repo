# SIM-R2-C3 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check: copied learning rules reproduce Cycle 2; empty delay steps are inert for weights.

## Refinement from previous iteration
New simulation for carried item 'R2 discriminating LI datasets'.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C2 LI indices |
| V2 | validation | delay steps leave weights unchanged |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Textbook-form learning rules (Mackintosh form simplified by us); delay is modelled only as uncertainty growth in KF (tau2 per empty step); no animal data are fitted because no open-access parametric LI dataset was found.

## Command
`python sim_r2.py iter-1` (run from `Report-2-Mind/simulation/`)
