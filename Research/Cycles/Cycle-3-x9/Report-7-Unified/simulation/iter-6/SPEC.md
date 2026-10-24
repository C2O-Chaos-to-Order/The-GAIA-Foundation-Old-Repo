# SIM-R7-C3 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Did Cycle 3 fill empty Being x Lens cells?

## Refinement from previous iteration
Targeted searches in passes 3/8 aimed at empty cells.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | >= 3 of 6 EMPTY cells populated |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens hand coding is by the same agent that wrote the keyword rule.

## Command
`python sim_r7.py iter-6` (run from `Report-7-Unified/simulation/`)
