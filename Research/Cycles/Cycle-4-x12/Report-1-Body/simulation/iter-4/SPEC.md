# SIM-R1-C4 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Robustness of the selected setting to day-to-day load noise (C3: 1 of 20 seeds).

## Refinement from previous iteration
Continuous metric.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | >= 80% of seeds in [8,12] |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop (Cycle-2/3 session model, imported unchanged from Cycle 3); linear interpolation between daily values is our choice; W05 anchors are pooled heuristics. Nothing fitted to human data.

## Command
`python sim_r1.py iter-4` (run from `Report-1-Body/simulation/`)
