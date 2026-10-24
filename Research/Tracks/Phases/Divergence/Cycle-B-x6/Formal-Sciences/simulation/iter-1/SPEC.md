# SIM-DV-FOR-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Check P16's likelihood reading of KL divergence: for data from p, -(1/n) log L(c|q) approaches D(p||q) (Eq. A2) for a six-sided 'die'.

## Phase operationalization tested
FOR Divergence = statistical divergence D(p||q) as the large-sample average log-likelihood penalty of the model q (P16).

## Sources this run draws on
P16 (Shlens 2014, arXiv:1404.2000, read in full in DVB): Eq. 2 and Appendix Eq. A2; Stirling approximation good for n > O(100).

## Refinement from previous iteration
DVA ran KL with no readable source; this iteration tests the source's stated relation.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | LR rate within 4 SE of D at every n |
| H1 | hypothesis | Eq. A2 within 0.01 nats at n = 1e5 |
| H2 | hypothesis | error decreases with n |
| R1 | reporting | by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One random (p, q) pair from Dirichlet(1); natural logs (nats) not bits. The 0.01 nat bound was chosen by the agent from the (K-1)/2 log n / n Stirling-order term, before running. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-B",
 "iteration": 1,
 "kind": "kl_likelihood",
 "seed": 16201,
 "K": 6,
 "conc": 1.0,
 "n_values": [
  100,
  1000,
  10000,
  100000
 ],
 "reps": 200,
 "tol_se": 4,
 "h1": 0.01
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
