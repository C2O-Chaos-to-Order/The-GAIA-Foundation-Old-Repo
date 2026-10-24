# SIM-R1-C2 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Decay and re-induction: calibrate the forgetting rate to W05's '1 day of HA is lost following 2 days of HAD', then TEST whether the same simple learner reproduces W05's 'HRA was 8-12 times faster than HAD'.

## Refinement from previous iteration
Uses the learning rate of iteration 1 unchanged; iteration 1 established acquisition.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| C1cal | reporting | fitted forgetting rate |
| H2 | hypothesis | re-induction/decay rate ratio in [8, 12] |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy loop of our own; units are arbitrary deviation units per minute-step. W04/W05 give only qualitative anchors (direction, a 1:2 decay heuristic, an 8-12x re-induction ratio for HR and Tc). Nothing here is fitted to human data. The rate definitions (% of adaptation per day) follow W05's %Decay formula in spirit; W05 pools heterogeneous studies.

## Command
`python sim_r1.py iter-2` (run from `Report-1-Body/simulation/`)
