# SIM-R1-C3 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Could a realistic study design tell the two memories apart? Model recovery with peak temperatures on 9 test days.

## Refinement from previous iteration
Adds measurement noise and BIC model selection.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | >= 80% recovery at 5% noise |
| H5r | reporting | recovery at 10%, 20% |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data. Generating parameters lie on the fitting grid, which flatters recovery.

## Command
`python sim_r1.py iter-5` (run from `Report-1-Body/simulation/`)
