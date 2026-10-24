# SIM-R6-C4 - iteration 10 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Calibration against the published row (disclosed as calibration).

## Refinement from previous iteration
k x R grid.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H10 | hypothesis | best err <= 0.05 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
W03 (Lenton & Lovelock 2000) still not open access: the constrained-adaptation cost form is ours (W01 s6.3 verbal description), so agreement with the published row is calibration, not reproduction. Equations/constants from W01; seed floor 0.001 (not stated in W01). Daisyworld is a parable; nothing about a literal soul or heart of the Earth.

## Command
`python sim_r6.py iter-10` (run from `Report-6-Earth/simulation/`)
