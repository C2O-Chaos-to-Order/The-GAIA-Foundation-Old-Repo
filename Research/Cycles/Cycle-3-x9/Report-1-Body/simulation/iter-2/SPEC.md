# SIM-R1-C3 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Can a fast-plus-slow memory meet BOTH W05 anchors (about 1 HA day lost per 2 decay days, and 8-12x faster re-induction) that a single state could not?

## Refinement from previous iteration
Adds the slow state; pre-declared 192-setting grid.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | some setting meets both anchors |
| H2r | reporting | selected setting and ratio range |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own (Cycle-2 session model unchanged); one 'day' is one learning step. The two-state form is borrowed from motor adaptation (X22), not from thermal physiology; W05 anchors are pooled heuristics. Nothing is fitted to human data.

## Command
`python sim_r1.py iter-2` (run from `Report-1-Body/simulation/`)
