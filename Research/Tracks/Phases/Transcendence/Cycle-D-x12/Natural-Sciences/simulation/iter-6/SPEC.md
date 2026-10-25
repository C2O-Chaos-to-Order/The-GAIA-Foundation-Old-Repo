# SIM-TR-NAT-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Small reverse asymmetry (c_i 0.12): never switching optimal?

## Phase operationalization tested
NAT Transcendence = an evolutionary transition in individuality; fitness decoupling vs tradeoff breaking (P97). TRB adds P104's ratcheting against reversion.

## Sources this run draws on
P104 (Libby, Conlin, Kerr & Ratcliff 2016, 'Stabilizing multicellularity through ratcheting', Phil Trans R Soc B 371:20150444, PMC4958938, CC BY 4.0; read in full in TRB): I and G cells, environments E_I and E_G; type 1 ratcheting (fitness trade-offs, Tables 1-3) and type 2 (lower switch rate p); eq. 2.2 special case c = 2: I_t + G_t = 2(2 - p)^(t-1) G_0; Fig. 5a: c_g = c_i = 0.1, n_i = n_g = 10 gives optimal p about 0.2, c_g > c_i gives p < 1e-6; equations 2.1-2.3 not present in the extracted text.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the reconstructed model reproduces P104's printed special case or pure-strategy limit |
| H1 | hypothesis | small reverse asymmetry (c_i 0.12 > c_g 0.1): never switching optimal (as TRC found for c_i 0.1 > c_g 0.05) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iter-1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-NAT-D",
 "iteration": 6,
 "kind": "ratchet_switch",
 "seed": 43106,
 "mode": "fluct",
 "n_g": 10,
 "n_i": 10,
 "c_g": 0.1,
 "c_i_list": [
  0.12
 ],
 "logp_min": -8,
 "n_grid": 400,
 "hyps": [
  [
   "small reverse asymmetry (c_i 0.12 > c_g 0.1): never switching optimal (as TRC found for c_i 0.1 > c_g 0.05)",
   "o['by_c']['0.12']['p_opt'] < 1e-6"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
