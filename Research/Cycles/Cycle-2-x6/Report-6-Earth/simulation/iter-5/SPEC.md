# SIM-R6-C2 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Test W01's statement (citing Stocker 1995, not read) that mutation of the trait extends regulation: k albedo types with neighbour mutation.

## Refinement from previous iteration
Moves from adaptation of the response (iters 1-4) to evolution of the effect trait (albedo).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| M0 | validation | 2-type, no-mutation multi() equals two-daisy width within 0.02 |
| M1 | hypothesis | max width for k>2 >= 1.1x two-type |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our own re-implementation of the published designs from their verbal descriptions (W01 full text; W02, W03 abstracts only). Parable model; no claim about the real Earth. steps reduced to 1000 for run time (equilibration checked by M0 against the 1000-step two-daisy model).

## Command
`python sim_r6.py iter-5` (run from `Report-6-Earth/simulation/`)
