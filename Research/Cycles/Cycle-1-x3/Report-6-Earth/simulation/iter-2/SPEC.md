# SIM-R6-C1 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Toy test related to the Darwinization critique (V23-V25, V39): if daisies adapt their optimum temperature to local conditions, does planetary regulation survive? Unbounded and bounded adaptation.

## Refinement from previous iteration
Reads `../iter-1/outputs/results.json`.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| A0 | validation | rate 0 reproduces non-adapting run |
| A1 | hypothesis | regulation survives unbounded adaptation |
| A_bounded_5/10 | hypothesis | regulation survives bounded adaptation |
| A2 | reporting | optimum drift |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our own toy; not a reproduction of published adaptive-Daisyworld studies.

## Command
`python sim_r6.py iter-2` (run from `Report-6-Earth/simulation/`)
