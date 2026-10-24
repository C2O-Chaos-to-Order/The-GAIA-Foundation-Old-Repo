# SIM-R1-C4 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check: imported Cycle-3 code and the new interpolated metric.

## Refinement from previous iteration
New simulation for the carried item 'R1 continuous re-induction metric' (C3-R1-06).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | C3 ratio 7.0 reproduced |
| V2 | validation | t* in (need-1, need] |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop (Cycle-2/3 session model, imported unchanged from Cycle 3); linear interpolation between daily values is our choice; W05 anchors are pooled heuristics. Nothing fitted to human data.

## Command
`python sim_r1.py iter-1` (run from `Report-1-Body/simulation/`)
