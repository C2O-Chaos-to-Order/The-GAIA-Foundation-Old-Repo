# SIM-R1-C2 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consolidation: does the iteration-1 acquisition result replicate across 20 seeds of day-to-day load noise?

## Refinement from previous iteration
Replicates H1 with the noise model introduced in iteration 5.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | reduction >= 30% in every seed |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own; units are arbitrary deviation units per minute-step. W04/W05 give only qualitative anchors (direction, a 1:2 decay heuristic, an 8-12x re-induction ratio for HR and Tc). Nothing here is fitted to human data. Unbounded learner as in iteration 1.

## Command
`python sim_r1.py iter-6` (run from `Report-1-Body/simulation/`)
