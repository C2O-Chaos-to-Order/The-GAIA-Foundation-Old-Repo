# SIM-TR-FOR-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P98's notions in exact arithmetic: do truncations of Liouville's constant meet the Liouville condition for c = 1..5, is the base-10 lookahead of sqrt(2) and e linear with small slope while Liouville's constant's is not, does Proposition 3's construction behave as stated (t(n) = 2 + n^2, base 2), and does schoolbook base 2 -> 10 conversion respect Theorem 1's read bound?

## Phase operationalization tested
FOR Transcendence = transcendental numbers (not roots of any integer polynomial); Liouville numbers as the first explicit examples (P98).

## Sources this run draws on
P98 (Jakobsen & Simonsen 2020, 'Liouville Numbers and the Computational Complexity of Changing Bases', CiE 2020, LNCS 12098, PMC7309484, Springer, PMC COVID-19 collection reuse terms; read in full in TR0): (b, t)-sanity; Lemma: x is not a Liouville number iff it is (b, ct)-sane for some c; algebraic numbers and e have finite irrationality measure; Theorem 1 conversion bound r = ceil(log b / log a) t(n); Proposition 3 construction x = sum b^-(t^j(1)); mu(pi) <= 7.60630852; Liouville's constant sum 10^-(i!).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | 10^-1 + 10^-2 + 10^-6 = 0.110001 exactly |
| H1 | hypothesis | Liouville's constant meets |L - p/q| < q^-c with q >= 2 for every c = 1..5 using its own truncations (n <= 5 terms) |
| H2 | hypothesis | sqrt(2) - 1 and e - 2 have small linear lookahead in base 10 over 150 digits: max d_n/n <= 3 (consistent with finite irrationality measure, P98 Lemmas 1-2) |
| H3 | hypothesis | Liouville's constant has lookahead outgrowing small linear witnesses: max d_n/n >= 5 within 150 digits |
| H4 | hypothesis | P98 Proposition 3 with t(n) = 2 + n^2 in base 2: x is (2, t+1)-sane for n <= 130 and fails (2, t-1)-sanity at n = 3, 11 and 123 |
| H5 | hypothesis | schoolbook conversion base 2 -> base 10 (first 60 digits) reads no more than ceil(log 10/log 2) x max d_n = 4 x max d_n binary digits (P98 Theorem 1's r) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Exact rational arithmetic; sqrt(2) to 400 digits, e from 320 series terms, Liouville's constant to 6 terms (720 digits; the 7th term is 10^-5040). d_n is the agent's operationalisation: smallest j with 10^-j <= distance from x to the nearest n-digit fraction. 'Read count' is the agent's schoolbook comparison, not P98's algorithm. Finite-digit checks cannot prove sanity or Liouville-ness. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-FOR-0",
 "iteration": 1,
 "kind": "liouville_sanity",
 "seed": 39201,
 "digits": 150,
 "prec": 400,
 "L_terms": 6,
 "e_terms": 320,
 "c_max": 5,
 "prop3_nmax": 130,
 "conv_n": 60,
 "hyps": [
  [
   "Liouville's constant meets |L - p/q| < q^-c with q >= 2 for every c = 1..5 using its own truncations (n <= 5 terms)",
   "all(o['liouville_first_n'][str(c)] is not None for c in [1,2,3,4,5])"
  ],
  [
   "sqrt(2) - 1 and e - 2 have small linear lookahead in base 10 over 150 digits: max d_n/n <= 3 (consistent with finite irrationality measure, P98 Lemmas 1-2)",
   "o['max_dn_over_n']['sqrt2'] <= 3 and o['max_dn_over_n']['e'] <= 3"
  ],
  [
   "Liouville's constant has lookahead outgrowing small linear witnesses: max d_n/n >= 5 within 150 digits",
   "o['max_dn_over_n']['liouville'] >= 5"
  ],
  [
   "P98 Proposition 3 with t(n) = 2 + n^2 in base 2: x is (2, t+1)-sane for n <= 130 and fails (2, t-1)-sanity at n = 3, 11 and 123",
   "o['prop3_sane_with_t_plus_1'] and all(o['prop3_not_sane_t_minus_1_at_z'].values()) and len(o['prop3_not_sane_t_minus_1_at_z']) == 3"
  ],
  [
   "schoolbook conversion base 2 -> base 10 (first 60 digits) reads no more than ceil(log 10/log 2) x max d_n = 4 x max d_n binary digits (P98 Theorem 1's r)",
   "o['reads_base2_for_base10']['sqrt2'] <= 4*o['max_dn_first_conv_n']['sqrt2'] and o['reads_base2_for_base10']['e'] <= 4*o['max_dn_first_conv_n']['e']"
  ]
 ]
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
