# SIM-TR-FOR-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Base 10, 400 digits: is the maximal excess d_n - n attained after n = 100 for at least three of five constants?

## Phase operationalization tested
FOR Transcendence = transcendental / Liouville numbers and base-change lookahead (P98).

## Sources this run draws on
P98 (Jakobsen & Simonsen 2020, 'Liouville Numbers and the Computational Complexity of Changing Bases', CiE 2020, LNCS 12098, PMC7309484, Springer, PMC COVID-19 collection reuse terms; read in full in TR0): (b, t)-sanity; Lemma: x is not a Liouville number iff it is (b, ct)-sane for some c; algebraic numbers and e have finite irrationality measure; Theorem 1 conversion bound r = ceil(log b / log a) t(n); Proposition 3 construction x = sum b^-(t^j(1)); mu(pi) <= 7.60630852; Liouville's constant sum 10^-(i!).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Machin's formula in integer arithmetic gives pi = 3.14159265358979... |
| H1 | hypothesis | base 10, 400 digits: the excess d_n - n is attained after n = 100 for at least three of the five constants (no sign of the excess dying out) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Exact arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-FOR-B",
 "iteration": 6,
 "kind": "lookahead_set",
 "seed": 41206,
 "digits": 400,
 "base": 10,
 "numbers": [
  "sqrt2",
  "cbrt2",
  "phi",
  "e",
  "pi"
 ],
 "hyps": [
  [
   "base 10, 400 digits: the excess d_n - n is attained after n = 100 for at least three of the five constants (no sign of the excess dying out)",
   "sum(1 for k in ['sqrt2','cbrt2','phi','e','pi'] if o['by_number'][k]['argmax_excess'] > 100) >= 3"
  ]
 ]
}
```

## Command
`python sim_for.py iter-6` (run from `Formal-Sciences/simulation/`)
