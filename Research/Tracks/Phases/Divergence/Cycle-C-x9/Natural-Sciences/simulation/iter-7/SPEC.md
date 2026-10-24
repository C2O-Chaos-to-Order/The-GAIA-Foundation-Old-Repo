# SIM-DV-NAT-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Noisier pitchfork (sigma 0.2) with the DVB bias grid: does more noise weaken the bias that decides fates?

## Phase operationalization tested
NAT Divergence = cell-fate split at a pitchfork (P10 metaphor; P22 normal form).

## Sources this run draws on
P10 (read in full in DVA); P22 (read in full in DVC) for the supercritical pitchfork form.

## Refinement from previous iteration
DVB iteration 6 used sigma 0.1; only sigma and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | bias 0: fraction 0.5 within 4 binomial SE |
| V2 | validation | mean |x| within 10% of sqrt(a1) |
| H1 | hypothesis | largest bias: > 0.9 in one valley |
| R1 | reporting | fractions |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-C",
 "iteration": 7,
 "kind": "pitchfork_landscape",
 "seed": 17107,
 "cells": 2000,
 "dt": 0.01,
 "T": 20,
 "a0": -1.0,
 "a1": 1.0,
 "sigma": 0.2,
 "biases": [
  0.0,
  0.005,
  0.01,
  0.02
 ],
 "tol_se": 4,
 "h1": 0.9
}
```

## Command
`python sim_nat.py iter-7` (run from `Natural-Sciences/simulation/`)
