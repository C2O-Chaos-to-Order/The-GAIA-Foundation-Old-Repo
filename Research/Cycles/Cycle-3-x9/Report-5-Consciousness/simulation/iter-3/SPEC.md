# SIM-R5-C3 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Do larger networks keep the peak?

## Refinement from previous iteration
Extends sizes.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | peak at N=96, 128 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy modular Kuramoto network (4 modules, between-module coupling 0.2 x within); PCI-like and susceptibility are analogues of empirical measures, not the measures themselves. No claim about consciousness follows from toy behaviour.

## Command
`python sim_r5.py iter-3` (run from `Report-5-Consciousness/simulation/`)
