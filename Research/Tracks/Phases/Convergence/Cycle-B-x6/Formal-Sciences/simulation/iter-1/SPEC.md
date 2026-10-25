# SIM-CV-FOR-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P78's riffle-shuffle statement: computed exactly (Gilbert-Shannon-Reeds model, rising sequences), is t_mix(1/4) = 7 for 52 cards, is d(7) < 1/2, and is d(k) non-increasing?

## Phase operationalization tested
FOR Convergence = convergence to stationarity measured by mixing time (P78).

## Sources this run draws on
P78 (Wikipedia contributors, 'Markov chain mixing time', English Wikipedia, revision 1323553013 of 22 November 2025, CC BY-SA 4.0; read in full in CVB): t_mix(eps) = min{t : max_x max_A |Pr(X_t in A | X_0 = x) - pi(A)| <= eps}; changing eps < 1/2 changes t_mix by a constant factor, eps = 1/4 by convention; 'This is the sense in which Dave Bayer and Persi Diaconis (1992) proved that the number of riffle shuffles needed to mix an ordinary 52 card deck is 7'; growth 1.5 log2 n.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | a chain whose rows equal pi has d(1) = 0 |
| H1 | hypothesis | P78: 7 riffle shuffles mix 52 cards in the t_mix(1/4) sense (t_mix(1/4) = 7) |
| H2 | hypothesis | d(7) < 1/2 for 52 cards (t_mix(1/2) <= 7) |
| H3 | hypothesis | d(k) is non-increasing in k (k = 0-12) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic exact arithmetic (Python fractions). The rising-sequence formula is the agent's implementation of the Bayer-Diaconis result P78 cites (the 1992 paper was not read). Foreknowledge: the agent recalled d(7) ~ 0.33 for 52 cards before writing, so H1 was expected not supported (disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-B",
 "iteration": 1,
 "kind": "mixing_time",
 "seed": 31201,
 "riffle": {
  "n_cards": [
   52
  ],
  "k_max": 12
 },
 "eps_values": [
  0.25,
  0.5,
  0.1
 ],
 "hyps": [
  [
   "P78: 7 riffle shuffles mix 52 cards in the t_mix(1/4) sense (t_mix(1/4) = 7)",
   "o['riffle']['52']['tmix']['0.25'] == 7"
  ],
  [
   "d(7) < 1/2 for 52 cards (t_mix(1/2) <= 7)",
   "o['riffle']['52']['d']['7'] < 0.5"
  ],
  [
   "d(k) is non-increasing in k (k = 0-12)",
   "all(o['riffle']['52']['d'][str(k+1)] <= o['riffle']['52']['d'][str(k)] for k in range(12))"
  ]
 ]
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
