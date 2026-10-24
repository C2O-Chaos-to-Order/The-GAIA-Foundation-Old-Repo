# SIM-R5-C1 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Backward-masking toy: near threshold, is late activity bimodal (all-or-none) in the bistable unit and absent in the weak unit? (an ignition-style signature, V19 GNW).

## Refinement from previous iteration
Reads `../iter-1/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| K1 | hypothesis | strong unit: near-threshold late activity bimodal (BC > 0.555) |
| K2 | hypothesis | weak unit never ignites |
| K3 | validation | longer stimulus does not reduce ignition probability |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Mask amplitude 1.5 chosen in development so that thresholds fall inside the grid (disclosed).

## Command
`python sim_r5.py iter-2` (run from `Report-5-Consciousness/simulation/`)
