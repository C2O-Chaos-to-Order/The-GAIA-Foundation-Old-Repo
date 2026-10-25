# SIM-TR-FOR-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Base-10 lookahead over 200 digits for sqrt(2), cbrt(2), the golden ratio, e and pi: is it n + at most 5 and d_n/n <= 3?

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
| H1 | hypothesis | base 10, 200 digits: lookahead exceeds n by at most 5 digits (d_n <= n + 5) for sqrt(2), cbrt(2), the golden ratio, e and pi |
| H2 | hypothesis | base 10: max d_n/n <= 3 for all five (a small linear witness, as for non-Liouville numbers) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Exact arithmetic; d_n is the agent's operationalisation; finite digits cannot prove sanity. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-FOR-A",
 "iteration": 1,
 "kind": "lookahead_set",
 "seed": 40201,
 "digits": 200,
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
   "base 10, 200 digits: lookahead exceeds n by at most 5 digits (d_n <= n + 5) for sqrt(2), cbrt(2), the golden ratio, e and pi",
   "all(o['by_number'][k]['max_excess'] <= 5 for k in ['sqrt2','cbrt2','phi','e','pi'])"
  ],
  [
   "base 10: max d_n/n <= 3 for all five (a small linear witness, as for non-Liouville numbers)",
   "all(o['by_number'][k]['max_ratio'] <= 3 for k in ['sqrt2','cbrt2','phi','e','pi'])"
  ]
 ]
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
