# SIM-R5-C3 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Criticality link (X12): does the PCI-like peak sit where a criticality proxy peaks?

## Refinement from previous iteration
Adds synchrony susceptibility N*var(r).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H6 | hypothesis | argmax within one step |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Toy modular Kuramoto network (4 modules, between-module coupling 0.2 x within); PCI-like and susceptibility are analogues of empirical measures, not the measures themselves. No claim about consciousness follows from toy behaviour.

## Command
`python sim_r5.py iter-6` (run from `Report-5-Consciousness/simulation/`)
