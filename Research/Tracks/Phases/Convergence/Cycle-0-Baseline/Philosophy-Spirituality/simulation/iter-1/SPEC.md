# SIM-CV-PHI-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Peirce's convergence of inquiry (P72) as a toy: do Bayesian inquirers with different full-support priors converge (disagreement < 0.02 after 5000 shared observations, monotonically shrinking), does a dogmatic prior excluding the truth stay away from it, and do observationally equivalent hypotheses ('buried secrets') keep their prior disagreement?

## Phase operationalization tested
PHI Convergence = Peirce's convergence of inquiry: 'the opinion which is fated to be ultimately agreed to by all who investigate' (P72).

## Sources this run draws on
P72 (Capps, 'The Pragmatic Theory of Truth', Stanford Encyclopedia of Philosophy, first published 21 Mar 2019, substantive revision 22 May 2023; read in full in CV0): Peirce 1878 'The opinion which is fated to be ultimately agreed to by all who investigate'; Peirce 1901 'ideal limit towards which endless investigation would tend'; 'buried secrets' objection; Misak 'never in a position to judge'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | conjugate Beta posterior mean equals a numerical grid posterior |
| H1 | hypothesis | full-support agents disagree by < 0.02 after 5000 observations |
| H2 | hypothesis | disagreement shrinks monotonically over checkpoints |
| H3 | hypothesis | the dogmatic agent ends at 0.4 (its closest support), at least 0.15 from the truth |
| H4 | hypothesis | observationally equivalent hypotheses: posterior-odds spread equals prior spread (8.9) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical: a formal toy of a philosophical thesis, not a test of it. Priors (including a confident wrong prior Beta(200, 800)) are the agent's choices. Bernoulli truth 0.6.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-0",
 "iteration": 1,
 "kind": "bayes_merge",
 "seed": 29601,
 "theta": 0.6,
 "n_obs": 5000,
 "checkpoints": [
  10,
  100,
  1000,
  5000
 ],
 "beta_priors": {
  "sceptic": [
   1,
   20
  ],
  "flat": [
   1,
   1
  ],
  "enthusiast": [
   20,
   1
  ],
  "confident_wrong": [
   200,
   800
  ]
 },
 "dogmatic_support": [
  0.2,
  0.3,
  0.4
 ],
 "equivalent_prior_odds": {
  "A": 0.1,
  "B": 1.0,
  "C": 9.0
 },
 "hyps": [
  [
   "full-support agents disagree by < 0.02 after 5000 observations",
   "o['spread']['5000']<0.02"
  ],
  [
   "disagreement shrinks monotonically over checkpoints",
   "all(o['spread'][a]>o['spread'][b] for a,b in [('10','100'),('100','1000'),('1000','5000')])"
  ],
  [
   "the dogmatic agent ends at 0.4 (its closest support), at least 0.15 from the truth",
   "o['dogmatic']['mode']==0.4 and abs(o['dogmatic']['mean_end']-0.6)>=0.15"
  ],
  [
   "observationally equivalent hypotheses: posterior-odds spread equals prior spread (8.9)",
   "abs(o['buried']['spread']-8.9)<1e-9"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
