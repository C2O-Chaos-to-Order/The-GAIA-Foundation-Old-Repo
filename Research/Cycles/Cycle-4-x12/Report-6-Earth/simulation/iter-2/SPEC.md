# SIM-R6-C4 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Does the constrained variant reach the published L_max once the range is not truncated?

## Refinement from previous iteration
L1 = 2.6.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | L_max within 0.1 of 2.32 |
| H2r | reporting | L_est, total life |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
W03 (Lenton & Lovelock 2000) still not open access: the constrained-adaptation cost form is ours (W01 s6.3 verbal description), so agreement with the published row is calibration, not reproduction. Equations/constants from W01; seed floor 0.001 (not stated in W01). Daisyworld is a parable; nothing about a literal soul or heart of the Earth.

## Command
`python sim_r6.py iter-2` (run from `Report-6-Earth/simulation/`)
