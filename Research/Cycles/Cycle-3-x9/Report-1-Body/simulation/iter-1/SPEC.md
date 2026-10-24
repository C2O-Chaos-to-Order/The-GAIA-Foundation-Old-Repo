# SIM-R1-C3 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check before new work: the copied Cycle-2 session model and single-state learner must reproduce the Cycle-2 result, and the new two-state code must collapse to it.

## Refinement from previous iteration
New simulation for the carried item 'R1 two-timescale acclimation memory' (C2-R1-04: a single state gave only 2.1x).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C2 it2 ratio |
| V2 | validation | two-state with B_s=0 equals single-state |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data.

## Command
`python sim_r1.py iter-1` (run from `Report-1-Body/simulation/`)
