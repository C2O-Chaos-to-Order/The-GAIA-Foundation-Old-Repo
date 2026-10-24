# SIM-R6-C2 - iteration 4 SPEC

Written before execution. Params: `params.json` (hashed in EXECUTION_RECORD.json).

## Purpose
A second, band-independent regulation metric: damping ratio = mean |dTe/dL| lifeless / with life inside the habitable band.

## Refinement from previous iteration
Iterations 1-3 used only band width; this guards against a metric artefact.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| DM0 | validation | no-adaptation damping ratio > 1 |
| DM1 | reporting | damping per case |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported - a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Our own re-implementation of the published designs from their verbal descriptions (W01 full text; W02, W03 abstracts only). Parable model; no claim about the real Earth. W01's 'mean damping' is defined differently; numbers are not comparable.

## Command
`python sim_r6.py iter-4` (run from `Report-6-Earth/simulation/`)
