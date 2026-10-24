# SIM-R5-C3 - iteration 5 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Sensitivity to the response binarisation threshold.

## Refinement from previous iteration
Threshold grid.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H5 | hypothesis | peak for >= 3/4 thresholds |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy modular Kuramoto network (4 modules, between-module coupling 0.2 x within); PCI-like and susceptibility are analogues of empirical measures, not the measures themselves. No claim about consciousness follows from toy behaviour.

## Command
`python sim_r5.py iter-5` (run from `Report-5-Consciousness/simulation/`)
