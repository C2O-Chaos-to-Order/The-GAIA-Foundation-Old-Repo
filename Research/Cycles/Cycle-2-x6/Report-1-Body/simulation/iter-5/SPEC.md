# SIM-R1-C2 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Robustness of bounded learning feedforward over learning rate, feedback gain and effector capacity, with 20% day-to-day load noise.

## Refinement from previous iteration
Uses the safe bound selected in iteration 3 (carried via iteration 4).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | >= 20% reduction and undershoot <= 0.2 in >= 80% of settings |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own; units are arbitrary deviation units per minute-step. W04/W05 give only qualitative anchors (direction, a 1:2 decay heuristic, an 8-12x re-induction ratio for HR and Tc). Nothing here is fitted to human data.

## Command
`python sim_r1.py iter-5` (run from `Report-1-Body/simulation/`)
