# SIM-R3-C2 - iteration 1 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Carried agenda (C1 R3: inter-rater coding). Agreement between the C1 coding (A) and a codebook re-coding (B) of a seeded random sample of 48 of the 180 cells (4 per attribute).

## Refinement from previous iteration
Cycle 1 had a single coder; this adds a second, codebook-based, evidence-quoted coding.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| K0 | validation | sample reproducible from seed |
| K00 | validation | kappa implementation check |
| H1 | hypothesis | kappa >= 0.61 |
| H1r | reporting | disagreements |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder A and coder B are the same research agent; B used a written codebook (research/pass-5/CODEBOOK.md), required a quoted passage per cell and did not view A's values while coding. This is codebook re-coding (intra-rater) reliability, NOT inter-rater reliability. Agreement concerns descriptions of doctrines only.

## Command
`python sim_r3.py iter-1` (run from `Report-3-Soul/simulation/`)
