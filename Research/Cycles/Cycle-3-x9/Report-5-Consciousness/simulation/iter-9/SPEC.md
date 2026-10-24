# SIM-R5-C3 - iteration 9 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consolidation: replicate iteration 2 with new seeds.

## Refinement from previous iteration
Replication.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H9 | hypothesis | >= 8/9 settings |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy modular Kuramoto network (4 modules, between-module coupling 0.2 x within); PCI-like and susceptibility are analogues of empirical measures, not the measures themselves. No claim about consciousness follows from toy behaviour.

## Command
`python sim_r5.py iter-9` (run from `Report-5-Consciousness/simulation/`)
