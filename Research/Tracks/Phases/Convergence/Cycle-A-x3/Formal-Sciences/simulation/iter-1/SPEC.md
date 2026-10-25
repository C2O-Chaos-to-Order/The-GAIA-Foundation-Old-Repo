# SIM-CV-FOR-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P74's ZFEL null as a Markov chain: with P_loss 0.005 and P_gain set for S = 0.201, is the equilibrium 0.201, the second eigenvalue 1 - P_gain - P_loss, and the proportion at 682 steps from S0 = 0.3878 the analytic value?

## Phase operationalization tested
FOR Convergence = convergence of a Markov chain to equilibrium (P73), here P74's two-state chain.

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains. P74 (Berger, Stoilova, Varney, Abrams, Miglietta, Cartwright & Oakley 2026, 'Adaptive molecular convergence is pervasive across deep time and largely decoupled from phenotypic convergence', PNAS 123:e2616248123, PMC13438476, CC BY; read in full in CVA, SI not read): ZFEL null as a two-state Markov chain, S = P_gain/(P_loss + P_gain), chance overlap S^2; S0 = 0.3878, S = 0.201 (~4%); 86 medusozoans, 'n = 3,570 species pairs'; 50 samples of 100 pairs = 247,500 quartets (236,070 after excluding overlaps); '4,755,188 possible nonoverlapping quartets'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | P74's two-state chain: E(1) = 0.201 within 1e-9 |
| H2 | hypothesis | second eigenvalue = 1 - P_gain - P_loss within 1e-12 |
| H3 | hypothesis | V_682(1) equals S + (S0 - S) lambda2^682 within 1e-9 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. P_loss 0.005 is the agent's choice. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-A",
 "iteration": 1,
 "kind": "markov_converge",
 "seed": 30201,
 "T": [
  [
   0.9987421777221527,
   0.0012578222778473092
  ],
  [
   0.005,
   0.995
  ]
 ],
 "V0": [
  0.6122000000000001,
  0.3878
 ],
 "report_n": [
  100,
  682
 ],
 "n_max": 700,
 "hyps": [
  [
   "P74's two-state chain: E(1) = 0.201 within 1e-9",
   "abs(o['E'][1]-0.201) < 1e-9"
  ],
  [
   "second eigenvalue = 1 - P_gain - P_loss within 1e-12",
   "abs(o['lambda2']-0.9937421777221527) < 1e-10"
  ],
  [
   "V_682(1) equals S + (S0 - S) lambda2^682 within 1e-9",
   "abs(o['V']['682'][1]-(0.201+(0.3878-0.201)*0.9937421777221527**682)) < 1e-9"
  ]
 ]
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
