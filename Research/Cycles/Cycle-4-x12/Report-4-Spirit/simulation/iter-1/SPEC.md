# SIM-R4-C4 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Code check: null cohort and U-stratified recovery of a known effect.

## Refinement from previous iteration
New simulation for the carried item 'R4 negative-control designs' (Y03, Y04).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | null ORs ~1 |
| V2 | validation | stratified OR = exp(-0.5) |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Synthetic cohorts with one binary unmeasured confounder and logistic outcomes; crude 2x2 odds ratios. Real negative controls are never perfect (Y03); the design numbers are illustrations, not estimates for any study.

## Command
`python sim_r4.py iter-1` (run from `Report-4-Spirit/simulation/`)
