# SIM-R1-C4 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Re-run Cycle 3's pre-declared coarse grid with the continuous metric.

## Refinement from previous iteration
Same 144 settings as C3 iteration 2; selects the setting meeting both anchors with ratio closest to 10 (fallback: C3 selection).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | >= 1 of 144 meets both |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop (Cycle-2/3 session model, imported unchanged from Cycle 3); linear interpolation between daily values is our choice; W05 anchors are pooled heuristics. Nothing fitted to human data.

## Command
`python sim_r1.py iter-2` (run from `Report-1-Body/simulation/`)
