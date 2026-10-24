# SIM-AL-NAT-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same with one tenth of P55's noise (A = 0.025): do the constants become identifiable, and does the end-versus-middle pattern appear?

## Phase operationalization tested
NAT Allegiance = identifiability at low noise.

## Sources this run draws on
P55 (Benndorf & Schulz 2023, 'Identifiability of equilibrium constants for receptors with two to five binding sites', J Gen Physiol 155:e202313423, CC BY-NC-SA; read in full in ALB): noise model Eq. 9, seven concentrations x five points, end parameters less precise, counts Eqs. 20-21.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | end constants less precise than middle ones |
| H2 | hypothesis | max Hill slope CV < 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's application of P55's noise and design to a single Adair curve (P55 fits many mutant curves jointly). Smoke foreknowledge (seed 99, 100 reps): constants very poorly determined (SD of log10 K 1.7-3.9) with the middle ones worst (H1 not supported), maximal Hill slope well determined (H2 supported).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-NAT-B",
 "iteration": 2,
 "kind": "adair_identify",
 "seed": 26102,
 "A": 0.025,
 "n_conc": 7,
 "K_true": [
  0.02,
  0.05,
  0.2,
  2.0
 ],
 "n_rep": 5,
 "reps": 300
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
