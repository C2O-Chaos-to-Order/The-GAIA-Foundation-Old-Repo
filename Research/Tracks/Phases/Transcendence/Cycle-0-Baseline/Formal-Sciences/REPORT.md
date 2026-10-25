# Transcendence in the Formal Sciences — Cycle-0-Baseline (TR0)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: transcendental and Liouville numbers (P98); non-Liouville numbers have linear base-change lookahead, Liouville's constant does not.

## Claims (ledger: `claims/claims.csv`)
- **TR0-FOR-01** [E] P98 defines (b, t)-sane numbers (the base-b expansion's lookahead is bounded by t) and proves that a real number is not a Liouville number if and only if it is (b, ct)-sane with a linear witness, so non-Liouville numbers, including all algebraic irrationals and e, can be converted between bases with linear lookahead (Theorem 1's bound r = ceil(log b/log a) t(n) digits read). Liouville numbers, the first explicitly constructed transcendental numbers, are exactly those with super-linear lookahead; Proposition 3 constructs numbers sane for t but not for slightly smaller t. Known irrationality-measure bounds include mu(pi) <= 7.60630852. *Operationalization:* FOR Transcendence = transcendental and Liouville numbers. *Sources:* P98. *Limits:* Results are about computational complexity of base change; finite-digit checks cannot verify them. Notation slip: a bit count printed as (1 + floor(a)) where floor(log a) is meant.
- **TR0-FOR-02** [E] In exact arithmetic, truncations of Liouville's constant sum 10^-(i!) meet |L - p/q| < q^-c for every c = 1..5 (first at n = c terms); over 150 base-10 digits the lookahead d_n of sqrt(2) - 1 and e - 2 stays at most 2n, while Liouville's constant reaches d_n/n = 6 (d_120 = 720). P98 Proposition 3's number with t(n) = 2 + n^2 in base 2 (blocks at 3, 11, 123, 15131) is (2, t+1)-sane for n <= 130 and fails (2, t-1)-sanity at n = 3, 11, 123. Schoolbook conversion of the first 60 decimal digits read 201 (sqrt 2) and 200 (e) binary digits, within 4 x max d_n = 244. *Operationalization:* FOR Transcendence = Liouville numbers and base-change lookahead. *Sources:* SIM-TR-FOR-0/iter-1#V1;SIM-TR-FOR-0/iter-1#H1;SIM-TR-FOR-0/iter-1#H2;SIM-TR-FOR-0/iter-1#H3;SIM-TR-FOR-0/iter-1#H4;SIM-TR-FOR-0/iter-1#H5. *Limits:* Finite checks of proved statements; d_n and the read count are the agent's operationalisations.

## Simulations (SIM-TR-FOR-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 5/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `01bd85cf` | P98's notions in exact arithmetic: do truncations of Liouville's constant meet the Liouville condition for c = 1..5, is the base-10 lookahead of sqrt(2) and e linear with small slope while Liouville's constant's is not, does Proposition 3's construction behave as stated (t(n) = 2 + n^2, base 2), and does schoolbook base 2 -> 10 conversion respect Theorem 1's read bound? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; H5 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Sanity, Liouville numbers and base-change complexity sourced (TR0-FOR-01); Liouville condition, linear vs super-linear lookahead, Proposition 3 and the read bound verified in exact arithmetic (TR0-FOR-02).

## Unresolved
- Classical transcendence proofs (Hermite, Lindemann, Gelfond-Schneider) not sourced (PMC 0 hits; arXiv timed out).
- Finite-digit checks cannot establish sanity or Liouville-ness.
