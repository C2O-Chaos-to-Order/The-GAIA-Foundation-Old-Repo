# SIM-CV-FOR-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P74's two-state null chain in mixing-time terms: is t_mix(1/4) = 186 steps (agent arithmetic before the run), and is the chain within 0.02 of stationarity at 682 My?

## Phase operationalization tested
FOR Convergence = mixing time (shared with NAT's convergent-evolution reading).

## Sources this run draws on
P74 (Berger, Stoilova, Varney, Abrams, Miglietta, Cartwright & Oakley 2026, 'Adaptive molecular convergence is pervasive across deep time and largely decoupled from phenotypic convergence', PNAS 123:e2616248123, PMC13438476, CC BY; read in full in CVA, SI not read): ZFEL null as a two-state Markov chain, S = P_gain/(P_loss + P_gain), chance overlap S^2; S0 = 0.3878, S = 0.201 (~4%); 86 medusozoans, 'n = 3,570 species pairs'; 50 samples of 100 pairs = 247,500 quartets (236,070 after excluding overlaps); '4,755,188 possible nonoverlapping quartets'. P78 (Wikipedia contributors, 'Markov chain mixing time', English Wikipedia, revision 1323553013 of 22 November 2025, CC BY-SA 4.0; read in full in CVB): t_mix(eps) = min{t : max_x max_A |Pr(X_t in A | X_0 = x) - pi(A)| <= eps}; changing eps < 1/2 changes t_mix by a constant factor, eps = 1/4 by convention; 'This is the sense in which Dave Bayer and Persi Diaconis (1992) proved that the number of riffle shuffles needed to mix an ordinary 52 card deck is 7'; growth 1.5 log2 n.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | a chain whose rows equal pi has d(1) = 0 |
| H1 | hypothesis | P74's two-state chain: t_mix(1/4) = ceil(log(0.25/max pi)/log lambda2) = 186 (agent arithmetic before the run) |
| H2 | hypothesis | at 682 My the P74 chain is within 0.02 of stationarity in total variation |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. P_loss 0.005 as in CVA (agent's). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-B",
 "iteration": 4,
 "kind": "mixing_time",
 "seed": 31204,
 "chains": {
  "P74": [
   [
    0.9987421777221527,
    0.0012578222778473092
   ],
   [
    0.005,
    0.995
   ]
  ]
 },
 "eps_values": [
  0.25,
  0.01
 ],
 "report_t": [
  100,
  682
 ],
 "t_max": 5000,
 "hyps": [
  [
   "P74's two-state chain: t_mix(1/4) = ceil(log(0.25/max pi)/log lambda2) = 186 (agent arithmetic before the run)",
   "o['chains']['P74']['tmix']['0.25'] == 186"
  ],
  [
   "at 682 My the P74 chain is within 0.02 of stationarity in total variation",
   "o['chains']['P74']['d_at']['682'] < 0.02"
  ]
 ]
}
```

## Command
`python sim_for.py iter-4` (run from `Formal-Sciences/simulation/`)
