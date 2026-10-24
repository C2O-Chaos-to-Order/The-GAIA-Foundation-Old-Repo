# SIM-R7-C3 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Apply the strict rule to the Cycle-3 ledger and register (27 links incl. L25-L27).

## Refinement from previous iteration
Cycle-3 data.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | no E link downgraded |
| V3 | validation | all basis claims resolve |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens hand coding is by the same agent that wrote the keyword rule.

## Command
`python sim_r7.py iter-2` (run from `Report-7-Unified/simulation/`)
