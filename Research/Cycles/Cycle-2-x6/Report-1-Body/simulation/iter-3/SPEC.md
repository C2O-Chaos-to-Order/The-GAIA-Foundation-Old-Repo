# SIM-R1-C2 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Cost of anticipation: when the cue arrives but the load does not, a learned feedforward cools below the set point. Can a bound on the learned gain keep that harm small while keeping most of the benefit?

## Refinement from previous iteration
Iteration 1 learned without bound; this iteration adds the 'bounded' half of the agenda item.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | some bound: undershoot <= 0.2 and >= 70% of unbounded benefit |
| H3r | reporting | unbounded undershoot |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own; units are arbitrary deviation units per minute-step. W04/W05 give only qualitative anchors (direction, a 1:2 decay heuristic, an 8-12x re-induction ratio for HR and Tc). Nothing here is fitted to human data.

## Command
`python sim_r1.py iter-3` (run from `Report-1-Body/simulation/`)
