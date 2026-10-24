# SIM-AL-NAT-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Tertiary two-state (TTS) model with P53's approximate values (L 1e6, l_T 200, l_R 0.3, K_t 0.02, K_r 5): does adding tertiary pre-equilibria inside each quaternary state keep non-cooperative binding within states while giving a maximal Hill slope near 2.8?

## Phase operationalization tested
NAT Allegiance = cooperative binding with tertiary and quaternary switches (TTS).

## Sources this run draws on
P53 (Eaton 2022, 'A retrospective on statistical mechanical models for hemoglobin allostery', J Chem Phys 157:184104, CC BY; read in full in ALA): MWC partition function Eq. (4), TTS Eq. (13), Fig. 3 and Fig. 5 parameter values; both quaternary states bind non-cooperatively. P46 (read in full in AL0): Hb Hill n = 2.8.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | end slopes within 0.05 of 1 |
| H2 | hypothesis | max slope within 0.5 of 2.8 |
| H3 | hypothesis | max slope varies by > 0.1 over L = 1e5, 1e6, 1e7 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Eq. (13)'s fraction layout is lost in the extracted text; the agent reads the T term as (L / l_T^4)[...]^4 (disclosed). Smoke foreknowledge: max slope 2.55, all checks passed.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-A",
 "iteration": 2,
 "kind": "mwc_binding",
 "seed": 25102,
 "model": "TTS",
 "params": {
  "l_T": 200,
  "l_R": 0.3,
  "K_t": 0.02,
  "K_r": 5.0
 },
 "L": 1000000.0,
 "L_values": [
  100000.0,
  1000000.0,
  10000000.0
 ],
 "n_ref": 2.8,
 "tol_n": 0.5
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
