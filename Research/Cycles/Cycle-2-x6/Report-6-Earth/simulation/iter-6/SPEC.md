# SIM-R6-C2 - iteration 6 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Consolidation: do the iteration 1-2 conclusions (unbounded erodes, constrained recovers) hold across death rate gamma and heat-transfer q?

## Refinement from previous iteration
Generalises iterations 1-2 over the parameters that in Cycle 1 limited the base model (regulation in 63% of configurations).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| RB1 | hypothesis | constrained keeps >= 0.8x band in >= 80% of settings |
| RB2 | hypothesis | unbounded keeps >= 0.8x band in <= 20% of settings |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our own re-implementation of the published designs from their verbal descriptions (W01 full text; W02, W03 abstracts only). Parable model; no claim about the real Earth. steps 1000 for run time.

## Command
`python sim_r6.py iter-6` (run from `Report-6-Earth/simulation/`)
