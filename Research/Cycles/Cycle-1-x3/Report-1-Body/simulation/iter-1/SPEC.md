# SIM-R1-C1 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Map the controller-gain space of the C0 toy loop (step load D=1, plant leak kl=0.1) and record the best-peak gain pair for iteration 2.

## Refinement from previous iteration
First iteration of this cycle (builds on the Cycle-0 baseline simulation).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| G1 | validation | P-only cells match the analytic residual D/(kl+kp) within 1% |
| G2 | validation | every stable PI cell returns to set point (|tail mean| < 0.02) |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Gain grid only; no delay, no noise.

## Command
`python sim_r1.py iter-1` (run from `Report-1-Body/simulation/`)
