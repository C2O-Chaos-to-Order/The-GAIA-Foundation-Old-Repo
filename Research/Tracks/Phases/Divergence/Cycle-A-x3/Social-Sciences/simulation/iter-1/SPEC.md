# SIM-DV-SOC-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Independent re-implementation of P03's event model: do stochastic external events sustain high opinion conflict where bounded confidence alone does not, and does P03's Eq. 6 predict the levels?

## Phase operationalization tested
SOC Divergence = sustained polarisation (conflict = SD of opinions) under homophily and external events (P03).

## Sources this run draws on
P03 (Condie & Condie 2021; re-read in full in this cycle): SIEM rules, certainty allocation, event parameters, Eq. 6 Delta O = 0.75(1 - eps)[0.44 + Es (Ef Ed)^0.08].

## Refinement from previous iteration
New run family (DV0 used the noise-free Deffuant model; P03's event mechanism was listed as unmodelled).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | certainty mean 0.5 within 4 SE |
| H1 | hypothesis | no events: conflict within 0.1 of Eq. 6 |
| H2 | hypothesis | events: within 0.1 of Eq. 6 |
| H3 | hypothesis | events add > 0.1 conflict |
| R1 | reporting | per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Not P03's code: k = 4 links per step is our choice (P03 varies k; its default was not stated in the text read); certainty drift interpreted as symmetric; random directed partner draws instead of an undirected random network. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-A",
 "iteration": 1,
 "kind": "siem",
 "seed": 15301,
 "agents": 490,
 "k": 4,
 "eps": 0.2,
 "T": 1000,
 "t0": 500,
 "reps": 5,
 "Ef": 0.05,
 "Ed": 10,
 "Es": 0.6,
 "cdrift": 0.1,
 "tol_se": 4,
 "h_tol": 0.1,
 "h3": 0.1
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
