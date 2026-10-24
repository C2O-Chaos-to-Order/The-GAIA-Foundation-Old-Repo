# SIM-R3-C2 - iteration 2 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
Uncertainty of the agreement estimate: bootstrap CI and Krippendorff's alpha (W08).

## Refinement from previous iteration
Adds interval estimates to iteration 1's point estimate.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| H2 | hypothesis | CI lower bound >= 0.41 |
| H2r | reporting | Krippendorff's alpha |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Coder A and coder B are the same research agent; B used a written codebook (research/pass-5/CODEBOOK.md), required a quoted passage per cell and did not view A's values while coding. This is codebook re-coding (intra-rater) reliability, NOT inter-rater reliability. Agreement concerns descriptions of doctrines only.

## Command
`python sim_r3.py iter-2` (run from `Report-3-Soul/simulation/`)
