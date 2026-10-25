# Transcendence in the Formal Sciences — Cycle-A-x3 (TRA)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: classical constants have small linear lookahead in bases 10 and 2; Liouville-type numbers are super-linear in both.

## Claims (ledger: `claims/claims.csv`)
- **TRA-FOR-01** [E] P98 defines (b, t)-sane numbers (the base-b expansion's lookahead is bounded by t) and proves that a real number is not a Liouville number if and only if it is (b, ct)-sane with a linear witness, so non-Liouville numbers, including all algebraic irrationals and e, can be converted between bases with linear lookahead (Theorem 1's bound r = ceil(log b/log a) t(n) digits read). Liouville numbers, the first explicitly constructed transcendental numbers, are exactly those with super-linear lookahead; Proposition 3 constructs numbers sane for t but not for slightly smaller t. Known irrationality-measure bounds include mu(pi) <= 7.60630852. *Operationalization:* FOR Transcendence = transcendental and Liouville numbers. *Sources:* P98. *Limits:* Results are about computational complexity of base change; finite-digit checks cannot verify them. Notation slip: a bit count printed as (1 + floor(a)) where floor(log a) is meant.
- **TRA-FOR-02** [E] In exact arithmetic, truncations of Liouville's constant sum 10^-(i!) meet |L - p/q| < q^-c for every c = 1..5 (first at n = c terms); over 150 base-10 digits the lookahead d_n of sqrt(2) - 1 and e - 2 stays at most 2n, while Liouville's constant reaches d_n/n = 6 (d_120 = 720). P98 Proposition 3's number with t(n) = 2 + n^2 in base 2 (blocks at 3, 11, 123, 15131) is (2, t+1)-sane for n <= 130 and fails (2, t-1)-sanity at n = 3, 11, 123. Schoolbook conversion of the first 60 decimal digits read 201 (sqrt 2) and 200 (e) binary digits, within 4 x max d_n = 244. *Operationalization:* FOR Transcendence = Liouville numbers and base-change lookahead. *Sources:* SIM-TR-FOR-0/iter-1#V1;SIM-TR-FOR-0/iter-1#H1;SIM-TR-FOR-0/iter-1#H2;SIM-TR-FOR-0/iter-1#H3;SIM-TR-FOR-0/iter-1#H4;SIM-TR-FOR-0/iter-1#H5. *Limits:* Finite checks of proved statements; d_n and the read count are the agent's operationalisations.
- **TRA-FOR-03** [E] Over 200 base-10 digits the lookahead of sqrt(2), cbrt(2), the golden ratio, e and pi exceeded n by at most 4 digits (d_n/n at most 2.5, at n = 1-2), as expected for non-Liouville numbers (P98): all algebraic irrationals and e, and pi with irrationality measure at most 7.6. *Operationalization:* FOR Transcendence = lookahead of classical constants. *Sources:* SIM-TR-FOR-A/iter-1#V1;SIM-TR-FOR-A/iter-1#H1;SIM-TR-FOR-A/iter-1#H2. *Limits:* Finite digits; the bound concerns the agent's d_n, not P98's formal witness.
- **TRA-FOR-04** [E] In base 2 over 400 digits, sqrt(2) and pi exceeded n by 9 digits somewhere and e by 8, so the pre-registered bound n + 8 was not supported for sqrt(2) and pi (a threshold set too tight; still linear). P98's Proposition 3 number had lookahead 15008 digits beyond n at n = 123 in base 2 and d_n/n of 37 at n = 123 in base 10; Liouville's constant reached d_n/n = 6 at n = 120 in base 10: super-linear lookahead in both bases. *Operationalization:* FOR Transcendence = Liouville-type lookahead across bases. *Sources:* SIM-TR-FOR-A/iter-2#V1;SIM-TR-FOR-A/iter-2#H1;SIM-TR-FOR-A/iter-2#H2;SIM-TR-FOR-A/iter-3#V1;SIM-TR-FOR-A/iter-3#H1;SIM-TR-FOR-A/iter-3#H2. *Limits:* Finite digits; one pre-registered threshold was not supported.

## Simulations (SIM-TR-FOR-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 5/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `b7350d8a` | Base-10 lookahead over 200 digits for sqrt(2), cbrt(2), the golden ratio, e and pi: is it n + at most 5 and d_n/n <= 3? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `0e62c13c` | Base-2 lookahead over 400 digits: d_n <= n + 8 for sqrt(2), e, pi; super-linear for P98's Proposition 3 number? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |
| 3 | `294af3e0` | Base-10 lookahead of Liouville's constant and of the Proposition 3 number: d_n/n >= 6 and >= 5 within 150 digits? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: TRA-FOR-03: classical constants have lookahead n + at most 4 in base 10.
- Pass 2: TRA-FOR-04: base 2: n + 9 for sqrt(2) and pi (threshold too tight); Proposition 3 number super-linear.
- Pass 3: TRA-FOR-04 (base 10, iteration 3): Liouville's constant and the Proposition 3 number super-linear.

## Unresolved
- Classical transcendence proofs (Hermite, Lindemann) not sourced (PMC 0 hits; arXiv timed out).
- Base-2 bound n + 8 too tight for sqrt(2) and pi over 400 digits; longer expansions not checked.
