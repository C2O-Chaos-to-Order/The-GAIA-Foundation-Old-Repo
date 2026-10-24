# SIM-AL-NAT-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Voxelotor-bound haemoglobin in P64 has L_X = 20: with the same K values, is the curve nearly non-cooperative (maximal slope below 1.3) and left-shifted (P50 below 5 torr)?

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
| H4 | hypothesis | maximal slope below 1.3 |
| H5 | hypothesis | P50 below 5 torr |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's reading: drug assumed not to change K_T, K_R (P64's assumption).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Optional extra hypotheses H4+ use the mwc_binding 'hyps' extension added in ALD (smoke-tested at seed 99).

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-D",
 "iteration": 2,
 "kind": "mwc_binding",
 "seed": 28102,
 "model": "MWC",
 "params": {
  "K_T": 0.00625,
  "K_R": 0.4347826086956522
 },
 "L": 20,
 "L_values": [
  10,
  20,
  40
 ],
 "n_ref": 2.8,
 "tol_n": 0.5,
 "hyps": [
  [
   "maximal slope below 1.3",
   "o['main']['slope_max'] < 1.3"
  ],
  [
   "P50 below 5 torr",
   "o['main']['P50'] < 5"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
