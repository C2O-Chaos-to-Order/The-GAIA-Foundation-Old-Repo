# SIM-R1-C4 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Does the answer depend on the re-induction threshold?

## Refinement from previous iteration
Three thresholds.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | meets both at all three |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop (Cycle-2/3 session model, imported unchanged from Cycle 3); linear interpolation between daily values is our choice; W05 anchors are pooled heuristics. Nothing fitted to human data.

## Command
`python sim_r1.py iter-6` (run from `Report-1-Body/simulation/`)
