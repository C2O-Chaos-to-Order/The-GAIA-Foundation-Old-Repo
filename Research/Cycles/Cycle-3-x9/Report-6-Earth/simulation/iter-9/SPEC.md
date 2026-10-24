# SIM-R6-C3 - iteration 9 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Numerical robustness of the reproduction (iteration 2).

## Refinement from previous iteration
Halved Euler step.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H9 | hypothesis | change <= 0.01 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Equations and constants from W01 (full text). The seed floor (minimum cover allowing germination) is not stated in W01 (we use 0.001; tested in iteration 4). Our 'total life' and 'slope ratio' metrics are our readings, not W01's definitions. The constrained-adaptation cost form is ours (W03 not open access). Daisyworld is a parable.

## Command
`python sim_r6.py iter-9` (run from `Report-6-Earth/simulation/`)
