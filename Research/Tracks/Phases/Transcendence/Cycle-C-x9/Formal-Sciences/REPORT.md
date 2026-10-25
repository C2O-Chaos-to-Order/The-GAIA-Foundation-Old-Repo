# Transcendence in the Formal Sciences — Cycle-C-x9 (TRC)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x9: Liouville-type lookahead is base dependent; TRB's attribution withdrawn; pi's excess reaches 7 at 800 decimal digits.

## Claims (ledger: `claims/claims.csv`)
- **TRC-FOR-01** [E] P98 defines (b, t)-sane numbers (the base-b expansion's lookahead is bounded by t) and proves that a real number is not a Liouville number if and only if it is (b, ct)-sane with a linear witness, so non-Liouville numbers, including all algebraic irrationals and e, can be converted between bases with linear lookahead (Theorem 1's bound r = ceil(log b/log a) t(n) digits read). Liouville numbers, the first explicitly constructed transcendental numbers, are exactly those with super-linear lookahead; Proposition 3 constructs numbers sane for t but not for slightly smaller t. Known irrationality-measure bounds include mu(pi) <= 7.60630852. *Operationalization:* FOR Transcendence = transcendental and Liouville numbers. *Sources:* P98. *Limits:* Results are about computational complexity of base change; finite-digit checks cannot verify them. Notation slip: a bit count printed as (1 + floor(a)) where floor(log a) is meant.
- **TRC-FOR-02** [E] In exact arithmetic, truncations of Liouville's constant sum 10^-(i!) meet |L - p/q| < q^-c for every c = 1..5 (first at n = c terms); over 150 base-10 digits the lookahead d_n of sqrt(2) - 1 and e - 2 stays at most 2n, while Liouville's constant reaches d_n/n = 6 (d_120 = 720). P98 Proposition 3's number with t(n) = 2 + n^2 in base 2 (blocks at 3, 11, 123, 15131) is (2, t+1)-sane for n <= 130 and fails (2, t-1)-sanity at n = 3, 11, 123. Schoolbook conversion of the first 60 decimal digits read 201 (sqrt 2) and 200 (e) binary digits, within 4 x max d_n = 244. *Operationalization:* FOR Transcendence = Liouville numbers and base-change lookahead. *Sources:* SIM-TR-FOR-0/iter-1#V1;SIM-TR-FOR-0/iter-1#H1;SIM-TR-FOR-0/iter-1#H2;SIM-TR-FOR-0/iter-1#H3;SIM-TR-FOR-0/iter-1#H4;SIM-TR-FOR-0/iter-1#H5. *Limits:* Finite checks of proved statements; d_n and the read count are the agent's operationalisations.
- **TRC-FOR-03** [E] Over 200 base-10 digits the lookahead of sqrt(2), cbrt(2), the golden ratio, e and pi exceeded n by at most 4 digits (d_n/n at most 2.5, at n = 1-2), as expected for non-Liouville numbers (P98): all algebraic irrationals and e, and pi with irrationality measure at most 7.6. *Operationalization:* FOR Transcendence = lookahead of classical constants. *Sources:* SIM-TR-FOR-A/iter-1#V1;SIM-TR-FOR-A/iter-1#H1;SIM-TR-FOR-A/iter-1#H2. *Limits:* Finite digits; the bound concerns the agent's d_n, not P98's formal witness.
- **TRC-FOR-04** [E] In base 2 over 400 digits, sqrt(2) and pi exceeded n by 9 digits somewhere and e by 8, so the pre-registered bound n + 8 was not supported for sqrt(2) and pi (a threshold set too tight; still linear). P98's Proposition 3 number had lookahead 15008 digits beyond n at n = 123 in base 2 and d_n/n of 37 at n = 123 in base 10; Liouville's constant reached d_n/n = 6 at n = 120 in base 10: super-linear lookahead in both bases. *Operationalization:* FOR Transcendence = Liouville-type lookahead across bases. *Sources:* SIM-TR-FOR-A/iter-2#V1;SIM-TR-FOR-A/iter-2#H1;SIM-TR-FOR-A/iter-2#H2;SIM-TR-FOR-A/iter-3#V1;SIM-TR-FOR-A/iter-3#H1;SIM-TR-FOR-A/iter-3#H2. *Limits:* Finite digits; one pre-registered threshold was not supported.
- **TRC-FOR-05** [E] In bases 3, 7, 10 and 16 the lookahead of sqrt(2), cbrt(2), the golden ratio, e and pi stayed within n + 6 digits (base 10 up to 400 digits: n + 4; base 16: n + 3; base 3: n + 6), and the maximal excess kept recurring late (after n = 100 for three of five constants in base 10: sqrt(2), cbrt(2) and the golden ratio). One pre-registered check was not supported: in base 3 neither Liouville's constant nor the Proposition 3 number reached d_n/n = 5 within 150 digits, which TRB attributed to too few digits; TRC withdraws that attribution (the failure persists at 600 digits; see TRC-FOR-06). *Operationalization:* FOR Transcendence = lookahead across bases. *Sources:* SIM-TR-FOR-B/iter-1#V1;SIM-TR-FOR-B/iter-1#H1;SIM-TR-FOR-B/iter-2#V1;SIM-TR-FOR-B/iter-2#H1;SIM-TR-FOR-B/iter-3#V1;SIM-TR-FOR-B/iter-3#H1;SIM-TR-FOR-B/iter-4#V1;SIM-TR-FOR-B/iter-4#H1;SIM-TR-FOR-B/iter-5#V1;SIM-TR-FOR-B/iter-5#H1;SIM-TR-FOR-B/iter-6#V1;SIM-TR-FOR-B/iter-6#H1. *Limits:* Finite digits; TRB's 'design error' attribution withdrawn in TRC.
- **TRC-FOR-06** [E] Liouville's constant and P98's Proposition 3 number do not show super-linear lookahead in base 3 even at 600 digits (maximal d_n/n 3.5 and 2.0) or in base 7 at 400 digits (2.0 and 3.0), so TRB's attribution of the base-3 failure to too few digits is not supported (pre-registered checks not supported in both runs). The agent's reading: this lookahead measures closeness to base-b fractions, and Liouville's constant is built from decimal fractions and the Proposition 3 number from binary ones, so super-linear lookahead is expected only in bases related to 10 or 2. *Operationalization:* FOR Transcendence = base dependence of lookahead. *Sources:* SIM-TR-FOR-C/iter-1#V1;SIM-TR-FOR-C/iter-1#H1;SIM-TR-FOR-C/iter-7#V1;SIM-TR-FOR-C/iter-7#H1. *Limits:* The reading is the agent's (P98 not re-read in TRC); only bases 3 and 7 tried.
- **TRC-FOR-07** [E] For sqrt(2), cbrt(2), the golden ratio, e and pi the excess d_n - n stayed small in bases 2 (at most 11 over 800 digits), 5 (5), 12 (4) and 20 (3), but in base 10 the pre-registered bound n + 6 is not supported over 800 digits: pi's excess reaches 7 at n = 761. Maximal excesses keep appearing late (after n = 200 for pi and the golden ratio in base 10). *Operationalization:* FOR Transcendence = lookahead across bases. *Sources:* SIM-TR-FOR-C/iter-2#V1;SIM-TR-FOR-C/iter-2#H1;SIM-TR-FOR-C/iter-3#V1;SIM-TR-FOR-C/iter-3#H1;SIM-TR-FOR-C/iter-4#V1;SIM-TR-FOR-C/iter-4#H1;SIM-TR-FOR-C/iter-5#V1;SIM-TR-FOR-C/iter-5#H1;SIM-TR-FOR-C/iter-6#V1;SIM-TR-FOR-C/iter-6#H1;SIM-TR-FOR-C/iter-8#V1;SIM-TR-FOR-C/iter-8#H1;SIM-TR-FOR-C/iter-9#V1;SIM-TR-FOR-C/iter-9#H1. *Limits:* Finite digits; pi's late excess is consistent with the run of six 9s near decimal 762 (not sourced here).

## Simulations (SIM-TR-FOR-C; 9 iteration(s), spec-first; validation 9/9, hypotheses supported 6/9)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `b265498d` | Base 3, 600 digits: do the Liouville-type numbers reach d_n/n >= 5 (TRB attributed its failure to too few digits)? | V1 Pass; H1 Not supported; R1 Reported |
| 2 | `df38111b` | Base 2, 800 digits: d_n <= n + 12 for sqrt(2), e, pi? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `287742fd` | Base 5, 300 digits: d_n <= n + 8? | V1 Pass; H1 Supported; R1 Reported |
| 4 | `607fb14d` | Base 12, 200 digits: d_n <= n + 6? | V1 Pass; H1 Supported; R1 Reported |
| 5 | `ab58001e` | Base 10, 800 digits: d_n <= n + 6 for sqrt(2), e, pi? | V1 Pass; H1 Not supported; R1 Reported |
| 6 | `ecf5119d` | Base 20, 150 digits: d_n <= n + 4? | V1 Pass; H1 Supported; R1 Reported |
| 7 | `4b576700` | Base 7, 400 digits: do the Liouville-type numbers reach d_n/n >= 5? | V1 Pass; H1 Not supported; R1 Reported |
| 8 | `9474814e` | Base 10, 400 digits: d_n <= n + 6 for cbrt(2) and the golden ratio? | V1 Pass; H1 Supported; R1 Reported |
| 9 | `ca2798e1` | Base 10, 800 digits: maximal excess after n = 200 for at least two of five constants? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (9; details `research/PASSES.md`)
- Pass 1: TRC-FOR-06: base 3 at 600 digits still not super-linear; TRB attribution withdrawn.
- Pass 2: TRC-FOR-07 (base 2, iteration 2): excess at most 11.
- Pass 3: TRC-FOR-07 (base 5, iteration 3): at most 5.
- Pass 4: TRC-FOR-07 (base 12, iteration 4): at most 4.
- Pass 5: TRC-FOR-07 (base 10, 800 digits, iteration 5): pi reaches 7 at n 761 (not supported).
- Pass 6: TRC-FOR-07 (base 20, iteration 6): at most 3.
- Pass 7: TRC-FOR-06 (base 7, iteration 7): not super-linear.
- Pass 8: TRC-FOR-07 (cbrt(2), golden ratio, iteration 8): at most 4.
- Pass 9: TRC-FOR-07 (iteration 9): late maxima for pi and the golden ratio.

## Unresolved
- Base dependence of Liouville-type lookahead is the agent's reading; P98 not re-read.
- Classical transcendence proofs not sourced.
