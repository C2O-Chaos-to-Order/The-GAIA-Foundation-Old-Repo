# SIM-R1-C3 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Mechanism check: is the re-induction advantage carried by the slow state's retention?

## Refinement from previous iteration
Varies A_s around the iteration-2 selection.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | ratio rises monotonically with A_s (Spearman >= 0.9) |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data.

## Command
`python sim_r1.py iter-3` (run from `Report-1-Body/simulation/`)
