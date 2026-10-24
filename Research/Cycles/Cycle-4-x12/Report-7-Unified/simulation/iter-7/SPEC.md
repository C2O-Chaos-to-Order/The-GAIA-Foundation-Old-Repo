# SIM-R7-C4 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Lens placement of the new Cycle-4 claims.

## Refinement from previous iteration
Keyword rule v1.0.1.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H7 | hypothesis | >= 50% placed |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens placement is a keyword rule by the same agent. Report 7's own C4 claims are excluded from inputs.

## Command
`python sim_r7.py iter-7` (run from `Report-7-Unified/simulation/`)
