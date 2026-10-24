# SIM-R3-C4 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check; counts of uncertain cells and cluster sizes.

## Refinement from previous iteration
New for Cycle 4: stability (not reliability) of the typology; independent human coding remains impossible for this agent and is disclosed.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C3 labels |
| V2 | validation | ARI toys |
| C0 | reporting | uncertain cells, sizes |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
No independent human coder (carried item) - this agent cannot recruit one; disclosed and still open. All codings are by the same research agent; stability of coding A is NOT reliability of coding A. 15 conceptions is a small sample for clustering. Describes descriptions of doctrines, not whether a soul exists.

## Command
`python sim_r3.py iter-1` (run from `Report-3-Soul/simulation/`)
