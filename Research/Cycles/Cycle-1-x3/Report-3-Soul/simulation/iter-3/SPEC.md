# SIM-R3-C1 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Widen (C15 Jain jiva, V40) and report what is stable instead of a single partition: co-clustering frequencies across codings x metrics x linkages x k.

## Refinement from previous iteration
Reads `../iter-2/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| E1 | validation | coding matrix complete and every row sourced |
| E3 | hypothesis | no universal attribute |
| K1 | reporting | base-partition recurrence |
| K2 | hypothesis | at least one pair co-clusters in >= 80% of draws |
| K3 | reporting | C15 stable partners |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Consensus is descriptive of our coding, not of the traditions.

## Command
`python sim_r3.py iter-3` (run from `Report-3-Soul/simulation/`)
