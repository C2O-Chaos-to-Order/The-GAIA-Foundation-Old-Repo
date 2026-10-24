# SIM-R1-C3 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Robustness of the selected setting to day-to-day load noise.

## Refinement from previous iteration
Same noise model as SIM-R1-C2 iteration 5/6.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | ratio in [8,12] in >= 80% of seeds |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data.

## Command
`python sim_r1.py iter-6` (run from `Report-1-Body/simulation/`)
