# SIM-R7-C3 - iteration 7 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Carried item 'two-coder lens placement': keyword rule vs hand coding on a seeded 40-claim sample.

## Refinement from previous iteration
Hand coding (data/lens_hand_coding.csv) was made from wordings with the codebook (data/LENS_CODEBOOK.md) before this run.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V4 | validation | sample reproducible |
| H7 | hypothesis | mean kappa >= 0.41 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Bookkeeping and graph checks on our own records; they test consistency, not any claim about the world. Lens hand coding is by the same agent that wrote the keyword rule.

## Command
`python sim_r7.py iter-7` (run from `Report-7-Unified/simulation/`)
