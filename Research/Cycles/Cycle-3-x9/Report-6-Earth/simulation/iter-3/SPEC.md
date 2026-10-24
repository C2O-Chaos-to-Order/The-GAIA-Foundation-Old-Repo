# SIM-R6-C3 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Reproduce the neutral-daisy control and test our reading of 'total life'.

## Refinement from previous iteration
Adds the control row.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H3 | hypothesis | neutral 0.74-1.11 |
| H3b | hypothesis | total life within 10% |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Equations and constants from W01 (full text). The seed floor (minimum cover allowing germination) is not stated in W01 (we use 0.001; tested in iteration 4). Our 'total life' and 'slope ratio' metrics are our readings, not W01's definitions. The constrained-adaptation cost form is ours (W03 not open access). Daisyworld is a parable.

## Command
`python sim_r6.py iter-3` (run from `Report-6-Earth/simulation/`)
