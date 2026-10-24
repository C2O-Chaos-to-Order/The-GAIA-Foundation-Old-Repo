# SIM-R1-C2 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
R6 analogue (cross-link L01): if the body's set point itself adapts toward the prevailing temperature (like daisies adapting their optimum in SIM-R6-C2), does regulation erode when unbounded and recover when bounded?

## Refinement from previous iteration
Carries the bounded gain from iteration 3 forward in the record; tests the structural parallel suggested by the R6 Cycle-2 results.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H4 | hypothesis | unbounded set-point adaptation raises the sustained peak >= 50% |
| H4b | hypothesis | bounded (<= 0.25) keeps it within 20% |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own; units are arbitrary deviation units per minute-step. W04/W05 give only qualitative anchors (direction, a 1:2 decay heuristic, an 8-12x re-induction ratio for HR and Tc). Nothing here is fitted to human data. Set-point adaptation is a modelling device, not a claim that human set points drift this way.

## Command
`python sim_r1.py iter-4` (run from `Report-1-Body/simulation/`)
