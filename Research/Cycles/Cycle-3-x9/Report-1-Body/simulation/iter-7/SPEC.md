# SIM-R1-C3 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Sensitivity analysis: one-at-a-time +-20% perturbation of the four memory parameters and two loop parameters.

## Refinement from previous iteration
Sensitivity of the iteration-2 selection.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H7 | hypothesis | ratio stays in [6,14] for every perturbation |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data. A_f, A_s capped at 1.

## Command
`python sim_r1.py iter-7` (run from `Report-1-Body/simulation/`)
