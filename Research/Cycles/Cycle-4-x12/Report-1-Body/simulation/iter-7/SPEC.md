# SIM-R1-C4 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Third anchor not used for selection: W05's ~2.5% decay per day.

## Refinement from previous iteration
Out-of-sample check of the selected setting.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H7 | hypothesis | 1.5-3.5%/day |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop (Cycle-2/3 session model, imported unchanged from Cycle 3); linear interpolation between daily values is our choice; W05 anchors are pooled heuristics. Nothing fitted to human data.

## Command
`python sim_r1.py iter-7` (run from `Report-1-Body/simulation/`)
