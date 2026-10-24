# SIM-AL-NAT-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
With P64's c = K_T/K_R = 0.0144, the MWC optimum is L = 1/c^2 = 4,823: is the maximal slope there higher than at P64's fitted L = 10^5?

## Phase operationalization tested
NAT Allegiance = fitted MWC cooperativity (P64).

## Sources this run draws on
P64 (Henry, Harper, Glass, Metaferia, Louis & Eaton 2021, 'MWC allosteric model explains unusual hemoglobin-oxygen binding curves from sickle cell drug binding', Biophys J 120:2543-2551, PMC8390878, CC BY; read in full in ALD): Table 1 fitted MWC parameters for normal red cells at 37 C: L 75,000-160,000, K_T 3.5 mM^-1 (p50 = 160 torr), K_R 240 mM^-1 (p50 = 2.3 torr), L_X (drug bound) 20; measured p50 about 37 torr in the authors' buffer. P53 (Eaton 2022, read in full in ALA): MWC Eq. (4), TTS Eq. (13) and approximate values. P46 (read in full in AL0): Hb n = 2.8.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | end slopes 1 |
| H2 | hypothesis | max slope within 0.5 of 2.8 |
| H3 | hypothesis | max slope varies by > 0.1 over L |
| H4 | hypothesis | slope at L 4823 exceeds slope at L 1e5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's derivation (ALB: slope peaks at L c^2 = 1). A first attempt crashed on a dictionary key ('4823' vs '4823.0') before producing results; the expression was corrected to use the main curve (L = 4823) and the run restarted (disclosed).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Optional extra hypotheses H4+ use the mwc_binding 'hyps' extension added in ALD (smoke-tested at seed 99).

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-D",
 "iteration": 4,
 "kind": "mwc_binding",
 "seed": 28104,
 "model": "MWC",
 "params": {
  "K_T": 0.00625,
  "K_R": 0.4347826086956522
 },
 "L": 4823,
 "L_values": [
  4823,
  100000.0
 ],
 "n_ref": 2.8,
 "tol_n": 0.5,
 "hyps": [
  [
   "slope at L 4823 exceeds slope at L 1e5",
   "o['main']['slope_max'] > o['by_L']['100000.0']['slope_max']"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-4` (run from `Natural-Sciences/simulation/`)
