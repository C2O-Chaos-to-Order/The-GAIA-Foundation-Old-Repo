# SIM-AL-NAT-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
MWC model with P53's approximate haemoglobin values (K_T 0.001, K_R 1 per Torr, L 5e5): is binding non-cooperative within each quaternary state but cooperative overall, with end slopes 1, a maximal Hill slope near P46's 2.8, and a maximal slope that changes when only L changes?

## Phase operationalization tested
NAT Allegiance = cooperative binding through a shared conformational switch (MWC).

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
| H3 | hypothesis | max slope varies by > 0.1 over L = 5e4, 5e5, 5e6 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
P53's values are approximate ('~'); P46's 2.8 is a fit to real Hb, not to MWC. Smoke foreknowledge (seed 99): max slope 3.64 (H2 not supported) and spread over these L values below 0.1 (H3 not supported); a first smoke failed V1 from numerical error at y near 0 or 1, fixed by restricting V1 to 1e-6 < y < 1 - 1e-6 (code fix, no threshold change). Thresholds kept as written before the smoke.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-A",
 "iteration": 1,
 "kind": "mwc_binding",
 "seed": 25101,
 "model": "MWC",
 "params": {
  "K_T": 0.001,
  "K_R": 1.0
 },
 "L": 500000.0,
 "L_values": [
  50000.0,
  500000.0,
  5000000.0
 ],
 "n_ref": 2.8,
 "tol_n": 0.5
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
