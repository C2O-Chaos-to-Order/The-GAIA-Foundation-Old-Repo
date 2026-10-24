# SIM-R6-C3 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code checks of the published energy balance and growth function.

## Refinement from previous iteration
New simulation for carried item 'R6 Lenton & Lovelock published equations' (Cycle 2 re-implemented the design from verbal descriptions).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | dead-planet energy balance |
| V2 | validation | growth function zeros/peak |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Equations and constants from W01 (full text). The seed floor (minimum cover allowing germination) is not stated in W01 (we use 0.001; tested in iteration 4). Our 'total life' and 'slope ratio' metrics are our readings, not W01's definitions. The constrained-adaptation cost form is ours (W03 not open access). Daisyworld is a parable.

## Command
`python sim_r6.py iter-1` (run from `Report-6-Earth/simulation/`)
