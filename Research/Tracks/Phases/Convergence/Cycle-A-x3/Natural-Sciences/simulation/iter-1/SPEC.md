# SIM-CV-NAT-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P74's ZFEL null model of molecular convergence: does a simulated two-state chain for 9194 loci in two lineages follow the analytic chance overlap S(t)^2 from S0^2 = 0.150 to S^2 = 0.040, and do P74's printed pair and quartet counts follow from 86 species and its sampling scheme?

## Phase operationalization tested
NAT Convergence (competing reading, now sourced) = convergent evolution: independent lineages acquiring the same molecular changes; P74's null for chance convergence.

## Sources this run draws on
P74 (Berger, Stoilova, Varney, Abrams, Miglietta, Cartwright & Oakley 2026, 'Adaptive molecular convergence is pervasive across deep time and largely decoupled from phenotypic convergence', PNAS 123:e2616248123, PMC13438476, CC BY; read in full in CVA, SI not read): ZFEL null as a two-state Markov chain, S = P_gain/(P_loss + P_gain), chance overlap S^2; S0 = 0.3878, S = 0.201 (~4%); 86 medusozoans, 'n = 3,570 species pairs'; 50 samples of 100 pairs = 247,500 quartets (236,070 after excluding overlaps); '4,755,188 possible nonoverlapping quartets'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | two-state chain stationary probability equals P74 Eq. 1 |
| H1 | hypothesis | simulated chance overlap within max(4 SE, 0.001) of the analytic S(t)^2 at every time and P_loss |
| H2 | hypothesis | steady-state overlap S^2 within 0.002 of P74's '~4%' |
| H3 | hypothesis | with P_loss 0.02 the overlap at 682 My is within 0.001 of S^2 (steady state reached) |
| H4 | hypothesis | 86 species give P74's printed 3,570 species pairs |
| H5 | hypothesis | 50 samples of 100 pairs give P74's 247,500 quartets |
| H6 | hypothesis | expected species-disjoint quartets in the sample (86 species) within 0.5% of P74's 236,070 |
| H7 | hypothesis | P74's 4,755,188 'possible nonoverlapping quartets' equals the count of species-disjoint pairs of pairs for 85 or 86 species |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Stochastic (10 replicates per P_loss). P_loss values are the agent's (P74 uses 'varying rates of loss' not given in the main text); P_gain is set so the steady state is P74's S = 0.201. Time steps are My. Foreknowledge from arithmetic before writing: C(86, 2) = 3655, not 3,570 (C(85, 2) = 3,570), and the species-disjoint pair-of-pairs counts for 85 or 86 species are about 6.2 and 6.5 million, not 4,755,188. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-NAT-A",
 "iteration": 1,
 "kind": "zfel_null",
 "seed": 30101,
 "n_loci": 9194,
 "S0": 0.3878,
 "S": 0.201,
 "P_loss": [
  0.002,
  0.005,
  0.02
 ],
 "t_report": [
  0,
  100,
  300,
  682
 ],
 "reps": 10,
 "combinatorics": {
  "n_species": [
   85,
   86
  ],
  "samples": 50,
  "pairs_per_sample": 100
 },
 "hyps": [
  [
   "simulated chance overlap within max(4 SE, 0.001) of the analytic S(t)^2 at every time and P_loss",
   "all(abs(r['sim_mean'][t]-r['analytic'][t]) <= max(4*r['sim_se'][t], 1e-3) for r in o['runs'].values() for t in r['analytic'])"
  ],
  [
   "steady-state overlap S^2 within 0.002 of P74's '~4%'",
   "abs(o['S_sq']-0.04) < 0.002"
  ],
  [
   "with P_loss 0.02 the overlap at 682 My is within 0.001 of S^2 (steady state reached)",
   "abs(o['runs']['Ploss0.02']['analytic']['682']-o['S_sq']) < 0.001"
  ],
  [
   "86 species give P74's printed 3,570 species pairs",
   "o['combinatorics']['by_n']['86']['pairs'] == 3570"
  ],
  [
   "50 samples of 100 pairs give P74's 247,500 quartets",
   "o['combinatorics']['sampled_quartets'] == 247500"
  ],
  [
   "expected species-disjoint quartets in the sample (86 species) within 0.5% of P74's 236,070",
   "abs(o['combinatorics']['by_n']['86']['expected_disjoint_in_sample']/236070-1) < 0.005"
  ],
  [
   "P74's 4,755,188 'possible nonoverlapping quartets' equals the count of species-disjoint pairs of pairs for 85 or 86 species",
   "any(v['disjoint_pair_of_pairs'] == 4755188 for v in o['combinatorics']['by_n'].values())"
  ]
 ]
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
