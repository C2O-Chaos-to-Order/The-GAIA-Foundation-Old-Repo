# SIM-R7-C4 - iteration 12 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Gate inputs across Cycle 4.

## Refinement from previous iteration
Reads execution records only.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H12 | hypothesis | all validation pass |
| G0 | reporting | gate inputs |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens placement is a keyword rule by the same agent. Report 7's own C4 claims are excluded from inputs.

## Command
`python sim_r7.py iter-12` (run from `Report-7-Unified/simulation/`)
