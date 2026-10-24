# SIM-R4-C2 - iteration 3 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
W09: with causally ordered mediators there are many decompositions. Does summing separately estimated single-mediator PMs (as a reader might do with S12 Table 4) overstate the joint PM?

## Refinement from previous iteration
Adds a second mediator to the iteration 1-2 design.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V3 | validation | independent mediators: sum = joint |
| V3b | validation | joint PM within 0.02 of truth |
| H2 | hypothesis | c12 = 0.6: sum overstates joint by >= 0.10 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic linear-Gaussian (and one logistic) data with known truth; illustrates estimator behaviour only. Does not re-analyse S12 or any cohort, and says nothing about whether religious practice causes health effects. S12 itself did not sum its proportions; the 65% is our arithmetic, used only to show why such sums should not be read as a joint share.

## Command
`python sim_r4.py iter-3` (run from `Report-4-Spirit/simulation/`)
