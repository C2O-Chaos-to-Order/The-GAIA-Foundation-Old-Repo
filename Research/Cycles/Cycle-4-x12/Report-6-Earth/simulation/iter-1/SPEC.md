# SIM-R6-C4 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code checks: vectorised copy reproduces Cycle 3; extending the range leaves the original model unchanged.

## Refinement from previous iteration
New for Cycle 4: Cycle 3 stopped at L = 1.7, which truncated the constrained run (carried item 'W03 equations' still blocked).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | reproduces C3 |
| V2 | validation | range-extension inert for original |
| C0 | reporting | C3 edge |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
W03 (Lenton & Lovelock 2000) still not open access: the constrained-adaptation cost form is ours (W01 s6.3 verbal description), so agreement with the published row is calibration, not reproduction. Equations/constants from W01; seed floor 0.001 (not stated in W01). Daisyworld is a parable; nothing about a literal soul or heart of the Earth.

## Command
`python sim_r6.py iter-1` (run from `Report-6-Earth/simulation/`)
