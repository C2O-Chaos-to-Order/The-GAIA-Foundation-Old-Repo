# SIM-R1-C3 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Distinguishing prediction: does decay slow down with longer absence more in the two-state model than in a single exponential?

## Refinement from previous iteration
Uses the iteration-2 selection and the Cycle-2 single-state calibration (lam 0.025).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | deceleration ratio lower by >= 0.1 for two-state |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data. Primary decay studies at 12 and 26 days exist but were not read in full (not open access).

## Command
`python sim_r1.py iter-4` (run from `Report-1-Body/simulation/`)
