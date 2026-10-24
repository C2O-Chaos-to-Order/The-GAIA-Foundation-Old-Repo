# SIM-R1-C3 - iteration 8 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Second distinguishing prediction: do savings accumulate over repeated acclimation/decay cycles (e.g. seasons)?

## Refinement from previous iteration
Repeats the 14 HA / 14 decay protocol three times from the decayed state.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H8 | hypothesis | days to 95% re-induction fall across cycles |
| H8r | reporting | slow share after each decay |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data.

## Command
`python sim_r1.py iter-8` (run from `Report-1-Body/simulation/`)
