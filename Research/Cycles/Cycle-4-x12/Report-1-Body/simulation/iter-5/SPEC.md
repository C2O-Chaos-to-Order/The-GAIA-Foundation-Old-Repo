# SIM-R1-C4 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Sensitivity: +-20% one at a time (C3: 2.2 to 11.3).

## Refinement from previous iteration
Continuous metric.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | all in [6,14] |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop (Cycle-2/3 session model, imported unchanged from Cycle 3); linear interpolation between daily values is our choice; W05 anchors are pooled heuristics. Nothing fitted to human data.

## Command
`python sim_r1.py iter-5` (run from `Report-1-Body/simulation/`)
