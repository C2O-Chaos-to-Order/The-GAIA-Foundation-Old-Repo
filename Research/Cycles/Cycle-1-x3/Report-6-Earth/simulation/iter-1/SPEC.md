# SIM-R6-C1 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Is Daisyworld regulation robust to death rate, heat-transfer parameter q and albedo contrast?

## Refinement from previous iteration
First iteration of this cycle (builds on the Cycle-0 baseline simulation).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| D0 | validation | lifeless planet matches analytic radiative balance |
| D1 | hypothesis | regulation (>= 2x lifeless band) in >= 80% of configurations |
| D2 | reporting | failing configurations |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Parable model.

## Command
`python sim_r6.py iter-1` (run from `Report-6-Earth/simulation/`)
