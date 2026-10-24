# SIM-R7-C4 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Connectivity under Established links only.

## Refinement from previous iteration
Graph check with L28.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | R2 joins another report |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens placement is a keyword rule by the same agent. Report 7's own C4 claims are excluded from inputs.

## Command
`python sim_r7.py iter-5` (run from `Report-7-Unified/simulation/`)
