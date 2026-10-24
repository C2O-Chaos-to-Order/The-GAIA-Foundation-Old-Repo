# SIM-R5-C3 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check against Cycle 2.

## Refinement from previous iteration
New simulation for carried item 'R5 perturbation scaled with network size'.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C2 it6 N=40 seed 1 |
| V2 | validation | no kick -> 0 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy modular Kuramoto network (4 modules, between-module coupling 0.2 x within); PCI-like and susceptibility are analogues of empirical measures, not the measures themselves. No claim about consciousness follows from toy behaviour.

## Command
`python sim_r5.py iter-1` (run from `Report-5-Consciousness/simulation/`)
