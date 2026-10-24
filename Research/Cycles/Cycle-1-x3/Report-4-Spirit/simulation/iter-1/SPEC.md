# SIM-R4-C1 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Recompute E-values for every attendance-health estimate read in full (S12, V12, V13) plus the abstract-only meta-analysis (T08), and check against the E-values the papers report.

## Refinement from previous iteration
First iteration of this cycle (builds on the Cycle-0 baseline simulation).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V0 | validation | E-value formula reproduces the S14 worked example |
| V_* | validation | recomputed E-values match V12 (2.04) and V13 (5.70, 2.35) |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
E-values bound confounding; they do not detect it.

## Command
`python sim_r4.py iter-1` (run from `Report-4-Spirit/simulation/`)
