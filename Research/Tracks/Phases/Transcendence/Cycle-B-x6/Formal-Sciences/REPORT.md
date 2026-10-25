# Transcendence in the Formal Sciences — Cycle-B-x6 (TRB)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: lookahead small and linear in bases 3, 7, 10, 16; base-3 Liouville check under-designed.

## Claims (ledger: `claims/claims.csv`)
- **TRB-FOR-01** [E] P98 defines (b, t)-sane numbers (the base-b expansion's lookahead is bounded by t) and proves that a real number is not a Liouville number if and only if it is (b, ct)-sane with a linear witness, so non-Liouville numbers, including all algebraic irrationals and e, can be converted between bases with linear lookahead (Theorem 1's bound r = ceil(log b/log a) t(n) digits read). Liouville numbers, the first explicitly constructed transcendental numbers, are exactly those with super-linear lookahead; Proposition 3 constructs numbers sane for t but not for slightly smaller t. Known irrationality-measure bounds include mu(pi) <= 7.60630852. *Operationalization:* FOR Transcendence = transcendental and Liouville numbers. *Sources:* P98. *Limits:* Results are about computational complexity of base change; finite-digit checks cannot verify them. Notation slip: a bit count printed as (1 + floor(a)) where floor(log a) is meant.
- **TRB-FOR-02** [E] In exact arithmetic, truncations of Liouville's constant sum 10^-(i!) meet |L - p/q| < q^-c for every c = 1..5 (first at n = c terms); over 150 base-10 digits the lookahead d_n of sqrt(2) - 1 and e - 2 stays at most 2n, while Liouville's constant reaches d_n/n = 6 (d_120 = 720). P98 Proposition 3's number with t(n) = 2 + n^2 in base 2 (blocks at 3, 11, 123, 15131) is (2, t+1)-sane for n <= 130 and fails (2, t-1)-sanity at n = 3, 11, 123. Schoolbook conversion of the first 60 decimal digits read 201 (sqrt 2) and 200 (e) binary digits, within 4 x max d_n = 244. *Operationalization:* FOR Transcendence = Liouville numbers and base-change lookahead. *Sources:* SIM-TR-FOR-0/iter-1#V1;SIM-TR-FOR-0/iter-1#H1;SIM-TR-FOR-0/iter-1#H2;SIM-TR-FOR-0/iter-1#H3;SIM-TR-FOR-0/iter-1#H4;SIM-TR-FOR-0/iter-1#H5. *Limits:* Finite checks of proved statements; d_n and the read count are the agent's operationalisations.
- **TRB-FOR-03** [E] Over 200 base-10 digits the lookahead of sqrt(2), cbrt(2), the golden ratio, e and pi exceeded n by at most 4 digits (d_n/n at most 2.5, at n = 1-2), as expected for non-Liouville numbers (P98): all algebraic irrationals and e, and pi with irrationality measure at most 7.6. *Operationalization:* FOR Transcendence = lookahead of classical constants. *Sources:* SIM-TR-FOR-A/iter-1#V1;SIM-TR-FOR-A/iter-1#H1;SIM-TR-FOR-A/iter-1#H2. *Limits:* Finite digits; the bound concerns the agent's d_n, not P98's formal witness.
- **TRB-FOR-04** [E] In base 2 over 400 digits, sqrt(2) and pi exceeded n by 9 digits somewhere and e by 8, so the pre-registered bound n + 8 was not supported for sqrt(2) and pi (a threshold set too tight; still linear). P98's Proposition 3 number had lookahead 15008 digits beyond n at n = 123 in base 2 and d_n/n of 37 at n = 123 in base 10; Liouville's constant reached d_n/n = 6 at n = 120 in base 10: super-linear lookahead in both bases. *Operationalization:* FOR Transcendence = Liouville-type lookahead across bases. *Sources:* SIM-TR-FOR-A/iter-2#V1;SIM-TR-FOR-A/iter-2#H1;SIM-TR-FOR-A/iter-2#H2;SIM-TR-FOR-A/iter-3#V1;SIM-TR-FOR-A/iter-3#H1;SIM-TR-FOR-A/iter-3#H2. *Limits:* Finite digits; one pre-registered threshold was not supported.
- **TRB-FOR-05** [E] In bases 3, 7, 10 and 16 the lookahead of sqrt(2), cbrt(2), the golden ratio, e and pi stayed within n + 6 digits (base 10 up to 400 digits: n + 4; base 16: n + 3; base 3: n + 6), and the maximal excess kept recurring late (after n = 100 for three of five constants in base 10: sqrt(2), cbrt(2) and the golden ratio). One pre-registered check was not supported: in base 3 neither Liouville's constant nor the Proposition 3 number reached d_n/n = 5 within 150 digits, because their large gaps lie beyond 150 base-3 digits (a design choice that was too short). *Operationalization:* FOR Transcendence = lookahead across bases. *Sources:* SIM-TR-FOR-B/iter-1#V1;SIM-TR-FOR-B/iter-1#H1;SIM-TR-FOR-B/iter-2#V1;SIM-TR-FOR-B/iter-2#H1;SIM-TR-FOR-B/iter-3#V1;SIM-TR-FOR-B/iter-3#H1;SIM-TR-FOR-B/iter-4#V1;SIM-TR-FOR-B/iter-4#H1;SIM-TR-FOR-B/iter-5#V1;SIM-TR-FOR-B/iter-5#H1;SIM-TR-FOR-B/iter-6#V1;SIM-TR-FOR-B/iter-6#H1. *Limits:* Finite digits; one design error disclosed.

## Simulations (SIM-TR-FOR-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 5/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `49937c5a` | Base 3, 250 digits: d_n <= n + 9 for sqrt(2), e, pi? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `55e1c422` | Base 16, 100 digits: d_n <= n + 4? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `78ef91e9` | Base 10, 400 digits: d_n <= n + 6 for sqrt(2), e, pi? | V1 Pass; H1 Supported; R1 Reported |
| 4 | `97010c16` | Base 3: do Liouville's constant and the Proposition 3 number reach d_n/n >= 5 within 150 digits? | V1 Pass; H1 Not supported; R1 Reported |
| 5 | `b26f00c5` | Base 7, 200 digits: d_n <= n + 8 for cbrt(2) and the golden ratio? | V1 Pass; H1 Supported; R1 Reported |
| 6 | `af133c6f` | Base 10, 400 digits: is the maximal excess d_n - n attained after n = 100 for at least three of five constants? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: TRB-FOR-05: base 3: excess at most 6.
- Pass 2: TRB-FOR-05 (base 16, iteration 2): excess at most 3.
- Pass 3: TRB-FOR-05 (base 10, 400 digits, iteration 3): excess at most 4.
- Pass 4: TRB-FOR-05 (iteration 4): Liouville-type numbers not super-linear within 150 base-3 digits (design too short; not supported).
- Pass 5: TRB-FOR-05 (base 7, iteration 5): excess at most 4.
- Pass 6: TRB-FOR-05 (iteration 6): maximal excess late for three of five constants.

## Unresolved
- Classical transcendence proofs (Hermite, Lindemann) not sourced.
- Liouville-type numbers in base 3 need more than 150 digits.
