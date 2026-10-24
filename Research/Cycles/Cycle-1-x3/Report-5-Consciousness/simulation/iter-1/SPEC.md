# SIM-R5-C1 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Phase diagram of the C0 ignition unit over recurrence w and threshold theta: where is it bistable?

## Refinement from previous iteration
First iteration of this cycle (builds on the Cycle-0 baseline simulation).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| P1 | validation | simulated bistability matches the fixed-point count in every cell |
| P2 | validation | C0 weak (w=2) monostable, strong (w=8) bistable |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Single rate unit.

## Command
`python sim_r5.py iter-1` (run from `Report-5-Consciousness/simulation/`)
