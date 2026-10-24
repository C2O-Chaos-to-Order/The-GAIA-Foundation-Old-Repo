# SIM-R1-C1 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Add sensor/effector delay (the main way real feedback fails) and parameter uncertainty. The iteration-1 best-peak gains are added to the PI delay scan (adaptive refinement).

## Refinement from previous iteration
Reads `../iter-1/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| D1 | validation | numeric critical delay for P-only control matches arccos(-a/k)/sqrt(k^2-a^2) within 5% |
| D2 | reporting | PI critical delay by gain pair, including the iteration-1 best pair |
| M1 | hypothesis | with feedback present, adding feedforward does not reduce the fraction of runs that restore the set point |
| M2 | hypothesis | median peak ratio (FB+FF)/FB < 1 across parameter uncertainty |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Linear toy; uniform parameter ranges are our assumption.

## Command
`python sim_r1.py iter-2` (run from `Report-1-Body/simulation/`)
