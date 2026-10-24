# SIM-R1-C2 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Add a learned, anticipatory (feedforward) term to the Cycle-1 bounded feedback loop and test whether 14 days of daily exposure lower the peak (direction per W04).

## Refinement from previous iteration
Carries the Cycle-1 agenda item 'bounded/learning feedforward' (C1 R1 T3 Not supported: a fixed feedforward gain did not robustly help).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no load: T stays at T0 |
| V2 | validation | P-control steady state = d/(a+Kp) |
| H1 | hypothesis | peak reduced >= 30% by day 14 |
| H1b | reporting | days to half adaptation |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own; units are arbitrary deviation units per minute-step. W04/W05 give only qualitative anchors (direction, a 1:2 decay heuristic, an 8-12x re-induction ratio for HR and Tc). Nothing here is fitted to human data.

## Command
`python sim_r1.py iter-1` (run from `Report-1-Body/simulation/`)
