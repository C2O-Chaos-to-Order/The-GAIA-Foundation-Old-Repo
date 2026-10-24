# SIM-DV-PHI-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Branching paired with merging as a formal skeleton for 'procession with reversion' (P07) and 'return' (P18): is multiplicity bounded, and does the mean-field estimate match?

## Phase operationalization tested
PHI Divergence = differentiation from unity to multiplicity paired with a return movement (P07 abiding-procession-reversion; P08 Bergson's two-way movement; P18 Laozi ch. 42 and reversal). Formal skeleton only.

## Sources this run draws on
P07 (Kalligas, SEP 'Plotinus', re-read in full in DVB); P08 (re-read in full); P18 (Chan, SEP 'Laozi', read at cited passages). No source states this model; it is the agent's formal analogue, not a reading of any tradition.

## Refinement from previous iteration
New run family (DVA used pure branching only).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Yule control within 4 SE |
| V2 | validation | stationary mean within 4 SE of exact |
| H1 | hypothesis | mean-field within 10% |
| R1 | reporting | means |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Exchangeable groups, constant rates, T = 30 assumed long enough for stationarity (V2 checks this). Says nothing about Plotinus, Bergson or the Laozi. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-B",
 "iteration": 1,
 "kind": "split_merge",
 "seed": 16601,
 "lam": 1.0,
 "mu": 0.1,
 "Ty": 3.0,
 "reps_y": 2000,
 "T": 30.0,
 "reps": 2000,
 "tol_se": 4
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
