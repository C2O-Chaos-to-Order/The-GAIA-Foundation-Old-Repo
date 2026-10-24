# SIM-R1-C3 - iteration 9 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consolidation: replicate the iteration-2 answer on an independent, finer grid.

## Refinement from previous iteration
Different grid points from iteration 2 (none shared).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H9 | hypothesis | finer grid also has settings meeting both anchors |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data.

## Command
`python sim_r1.py iter-9` (run from `Report-1-Body/simulation/`)
