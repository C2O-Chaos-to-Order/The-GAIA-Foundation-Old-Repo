# SIM-R5-C3 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Redo the failed Cycle-2 robustness test (C2-R5-05) with the perturbation scaled to one module.

## Refinement from previous iteration
Kick = N/4 units instead of a fixed 10.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | peak in >= 80% of settings |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy modular Kuramoto network (4 modules, between-module coupling 0.2 x within); PCI-like and susceptibility are analogues of empirical measures, not the measures themselves. No claim about consciousness follows from toy behaviour.

## Command
`python sim_r5.py iter-2` (run from `Report-5-Consciousness/simulation/`)
