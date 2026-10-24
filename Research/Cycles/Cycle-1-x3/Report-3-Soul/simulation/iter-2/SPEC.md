# SIM-R3-C1 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Alternative clustering methods and k, with silhouette as a structure-strength measure.

## Refinement from previous iteration
Reads `../iter-1/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| E1 | validation | coding matrix complete and every row sourced |
| E3 | hypothesis | no universal attribute |
| M1 | hypothesis | alternative linkages agree with average linkage at k=4 (median ARI >= 0.8) |
| M2 | reporting | best silhouette (< 0.25 = weak structure) |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Ward on binary data is a heuristic.

## Command
`python sim_r3.py iter-2` (run from `Report-3-Soul/simulation/`)
