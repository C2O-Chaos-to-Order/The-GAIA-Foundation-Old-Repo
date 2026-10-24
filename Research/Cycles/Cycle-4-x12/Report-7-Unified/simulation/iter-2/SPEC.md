# SIM-R7-C4 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Strict rule on the Cycle-4 register (28 links).

## Refinement from previous iteration
Cycle-4 data.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | no E link downgraded |
| V3 | validation | basis resolves |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens placement is a keyword rule by the same agent. Report 7's own C4 claims are excluded from inputs.

## Command
`python sim_r7.py iter-2` (run from `Report-7-Unified/simulation/`)
