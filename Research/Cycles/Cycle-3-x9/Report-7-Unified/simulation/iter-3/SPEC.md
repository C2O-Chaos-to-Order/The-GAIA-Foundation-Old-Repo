# SIM-R7-C3 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Does the essential-claim rule change the Cycle-2 downgrades (starting from the Cycle-1 labels)?

## Refinement from previous iteration
Compares strict vs essential rules.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | >= 1 of L04/L08/L16 restored |
| H3r | reporting | rule differences |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens hand coding is by the same agent that wrote the keyword rule.

## Command
`python sim_r7.py iter-3` (run from `Report-7-Unified/simulation/`)
