# SIM-R7-C3 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Label-error sensitivity of the Established links.

## Refinement from previous iteration
Random E->P flips.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | median downgraded share <= 0.5 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens hand coding is by the same agent that wrote the keyword rule.

## Command
`python sim_r7.py iter-4` (run from `Report-7-Unified/simulation/`)
