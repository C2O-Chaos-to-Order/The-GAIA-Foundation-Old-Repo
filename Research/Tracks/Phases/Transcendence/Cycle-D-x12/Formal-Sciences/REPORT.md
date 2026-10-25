# Transcendence in the Formal Sciences — Cycle-D-x12 (TRD)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x12: base-dependence reading predicted 10 of 12 outcomes; the two misses are a mis-set threshold.

## Claims (ledger: `claims/claims.csv`)
- **TRD-FOR-01** [E] P98 defines (b, t)-sane numbers (the base-b expansion's lookahead is bounded by t) and proves that a real number is not a Liouville number if and only if it is (b, ct)-sane with a linear witness, so non-Liouville numbers, including all algebraic irrationals and e, can be converted between bases with linear lookahead (Theorem 1's bound r = ceil(log b/log a) t(n) digits read). Liouville numbers, the first explicitly constructed transcendental numbers, are exactly those with super-linear lookahead; Proposition 3 constructs numbers sane for t but not for slightly smaller t. Known irrationality-measure bounds include mu(pi) <= 7.60630852. *Operationalization:* FOR Transcendence = transcendental and Liouville numbers. *Sources:* P98. *Limits:* Results are about computational complexity of base change; finite-digit checks cannot verify them. Notation slip: a bit count printed as (1 + floor(a)) where floor(log a) is meant.
- **TRD-FOR-02** [E] In exact arithmetic, truncations of Liouville's constant sum 10^-(i!) meet |L - p/q| < q^-c for every c = 1..5 (first at n = c terms); over 150 base-10 digits the lookahead d_n of sqrt(2) - 1 and e - 2 stays at most 2n, while Liouville's constant reaches d_n/n = 6 (d_120 = 720). P98 Proposition 3's number with t(n) = 2 + n^2 in base 2 (blocks at 3, 11, 123, 15131) is (2, t+1)-sane for n <= 130 and fails (2, t-1)-sanity at n = 3, 11, 123. Schoolbook conversion of the first 60 decimal digits read 201 (sqrt 2) and 200 (e) binary digits, within 4 x max d_n = 244. *Operationalization:* FOR Transcendence = Liouville numbers and base-change lookahead. *Sources:* SIM-TR-FOR-0/iter-1#V1;SIM-TR-FOR-0/iter-1#H1;SIM-TR-FOR-0/iter-1#H2;SIM-TR-FOR-0/iter-1#H3;SIM-TR-FOR-0/iter-1#H4;SIM-TR-FOR-0/iter-1#H5. *Limits:* Finite checks of proved statements; d_n and the read count are the agent's operationalisations.
- **TRD-FOR-03** [E] Over 200 base-10 digits the lookahead of sqrt(2), cbrt(2), the golden ratio, e and pi exceeded n by at most 4 digits (d_n/n at most 2.5, at n = 1-2), as expected for non-Liouville numbers (P98): all algebraic irrationals and e, and pi with irrationality measure at most 7.6. *Operationalization:* FOR Transcendence = lookahead of classical constants. *Sources:* SIM-TR-FOR-A/iter-1#V1;SIM-TR-FOR-A/iter-1#H1;SIM-TR-FOR-A/iter-1#H2. *Limits:* Finite digits; the bound concerns the agent's d_n, not P98's formal witness.
- **TRD-FOR-04** [E] In base 2 over 400 digits, sqrt(2) and pi exceeded n by 9 digits somewhere and e by 8, so the pre-registered bound n + 8 was not supported for sqrt(2) and pi (a threshold set too tight; still linear). P98's Proposition 3 number had lookahead 15008 digits beyond n at n = 123 in base 2 and d_n/n of 37 at n = 123 in base 10; Liouville's constant reached d_n/n = 6 at n = 120 in base 10: super-linear lookahead in both bases. *Operationalization:* FOR Transcendence = Liouville-type lookahead across bases. *Sources:* SIM-TR-FOR-A/iter-2#V1;SIM-TR-FOR-A/iter-2#H1;SIM-TR-FOR-A/iter-2#H2;SIM-TR-FOR-A/iter-3#V1;SIM-TR-FOR-A/iter-3#H1;SIM-TR-FOR-A/iter-3#H2. *Limits:* Finite digits; one pre-registered threshold was not supported.
- **TRD-FOR-05** [E] In bases 3, 7, 10 and 16 the lookahead of sqrt(2), cbrt(2), the golden ratio, e and pi stayed within n + 6 digits (base 10 up to 400 digits: n + 4; base 16: n + 3; base 3: n + 6), and the maximal excess kept recurring late (after n = 100 for three of five constants in base 10: sqrt(2), cbrt(2) and the golden ratio). One pre-registered check was not supported: in base 3 neither Liouville's constant nor the Proposition 3 number reached d_n/n = 5 within 150 digits, which TRB attributed to too few digits; TRC withdraws that attribution (the failure persists at 600 digits; see TRC-FOR-06). *Operationalization:* FOR Transcendence = lookahead across bases. *Sources:* SIM-TR-FOR-B/iter-1#V1;SIM-TR-FOR-B/iter-1#H1;SIM-TR-FOR-B/iter-2#V1;SIM-TR-FOR-B/iter-2#H1;SIM-TR-FOR-B/iter-3#V1;SIM-TR-FOR-B/iter-3#H1;SIM-TR-FOR-B/iter-4#V1;SIM-TR-FOR-B/iter-4#H1;SIM-TR-FOR-B/iter-5#V1;SIM-TR-FOR-B/iter-5#H1;SIM-TR-FOR-B/iter-6#V1;SIM-TR-FOR-B/iter-6#H1. *Limits:* Finite digits; TRB's 'design error' attribution withdrawn in TRC.
- **TRD-FOR-06** [E] Liouville's constant and P98's Proposition 3 number do not show super-linear lookahead in base 3 even at 600 digits (maximal d_n/n 3.5 and 2.0) or in base 7 at 400 digits (2.0 and 3.0), so TRB's attribution of the base-3 failure to too few digits is not supported (pre-registered checks not supported in both runs). The agent's reading: this lookahead measures closeness to base-b fractions, and Liouville's constant is built from decimal fractions and the Proposition 3 number from binary ones, so super-linear lookahead is expected only in bases related to 10 or 2. *Operationalization:* FOR Transcendence = base dependence of lookahead. *Sources:* SIM-TR-FOR-C/iter-1#V1;SIM-TR-FOR-C/iter-1#H1;SIM-TR-FOR-C/iter-7#V1;SIM-TR-FOR-C/iter-7#H1. *Limits:* The reading is the agent's (P98 not re-read in TRC); only bases 3 and 7 tried.
- **TRD-FOR-07** [E] For sqrt(2), cbrt(2), the golden ratio, e and pi the excess d_n - n stayed small in bases 2 (at most 11 over 800 digits), 5 (5), 12 (4) and 20 (3), but in base 10 the pre-registered bound n + 6 is not supported over 800 digits: pi's excess reaches 7 at n = 761. Maximal excesses keep appearing late (after n = 200 for pi and the golden ratio in base 10). *Operationalization:* FOR Transcendence = lookahead across bases. *Sources:* SIM-TR-FOR-C/iter-2#V1;SIM-TR-FOR-C/iter-2#H1;SIM-TR-FOR-C/iter-3#V1;SIM-TR-FOR-C/iter-3#H1;SIM-TR-FOR-C/iter-4#V1;SIM-TR-FOR-C/iter-4#H1;SIM-TR-FOR-C/iter-5#V1;SIM-TR-FOR-C/iter-5#H1;SIM-TR-FOR-C/iter-6#V1;SIM-TR-FOR-C/iter-6#H1;SIM-TR-FOR-C/iter-8#V1;SIM-TR-FOR-C/iter-8#H1;SIM-TR-FOR-C/iter-9#V1;SIM-TR-FOR-C/iter-9#H1. *Limits:* Finite digits; pi's late excess is consistent with the run of six 9s near decimal 762 (not sourced here).
- **TRD-FOR-09** [E] Classical constants keep small excesses: base 16 (400 digits) at most 3, base 8 (300) at most 4, base 3 (400) at most 7, and base 10 over 1000 digits at most 7 (pi at n = 761, as over 800 digits). *Operationalization:* FOR Transcendence = lookahead across bases. *Sources:* SIM-TR-FOR-D/iter-7#V1;SIM-TR-FOR-D/iter-7#H1;SIM-TR-FOR-D/iter-8#V1;SIM-TR-FOR-D/iter-8#H1;SIM-TR-FOR-D/iter-9#V1;SIM-TR-FOR-D/iter-9#H1;SIM-TR-FOR-D/iter-10#V1;SIM-TR-FOR-D/iter-10#H1. *Limits:* Finite digits.
- **TRD-FOR-08** [P] TRC's reading (lookahead tracks closeness to base-b fractions) predicted the base pattern: the Proposition 3 number is super-linear in bases 4 (maximal d_n/n 122) and 6 (47.6) but not 9 (2.0), and Liouville's constant stays linear in bases 2, 5 and 15 (maximal excess 10, 5, 3) but jumps in bases 20 and 30 (excess 434 and 368 at n = 120). The pre-registered threshold d_n/n >= 5 is not supported in bases 20 and 30 (4.62 and 4.07), because a 720-decimal-digit gap spans fewer base-20 or base-30 digits; the threshold, not the pattern, was mis-set. *Operationalization:* FOR Transcendence = base dependence of lookahead. *Sources:* SIM-TR-FOR-D/iter-1#V1;SIM-TR-FOR-D/iter-1#H1;SIM-TR-FOR-D/iter-2#V1;SIM-TR-FOR-D/iter-2#H1;SIM-TR-FOR-D/iter-3#V1;SIM-TR-FOR-D/iter-3#H1;SIM-TR-FOR-D/iter-4#V1;SIM-TR-FOR-D/iter-4#H1;SIM-TR-FOR-D/iter-5#V1;SIM-TR-FOR-D/iter-5#H1;SIM-TR-FOR-D/iter-6#V1;SIM-TR-FOR-D/iter-6#H1;SIM-TR-FOR-D/iter-11#V1;SIM-TR-FOR-D/iter-11#H1;SIM-TR-FOR-D/iter-12#V1;SIM-TR-FOR-D/iter-12#H1. *Limits:* Agent's reading, not taken from P98; finite digits.

## Simulations (SIM-TR-FOR-D; 12 iteration(s), spec-first; validation 12/12, hypotheses supported 10/12)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `f7fb0569` | Liouville's constant in base 20 (contains 2 and 5): super-linear (d_n/n >= 5)? | V1 Pass; H1 Not supported; R1 Reported |
| 2 | `1612f1e3` | Liouville's constant in base 5: stays below 5? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `e1b294fd` | Liouville's constant in base 2: stays below 5? | V1 Pass; H1 Supported; R1 Reported |
| 4 | `40d2f925` | Proposition 3 number in base 4: super-linear? | V1 Pass; H1 Supported; R1 Reported |
| 5 | `9f7899af` | Proposition 3 number in base 6: super-linear? | V1 Pass; H1 Supported; R1 Reported |
| 6 | `02d73a8c` | Proposition 3 number in base 9: stays below 5? | V1 Pass; H1 Supported; R1 Reported |
| 7 | `64eadf3a` | Base 16, 400 digits: d_n <= n + 6? | V1 Pass; H1 Supported; R1 Reported |
| 8 | `0026a532` | Base 8, 300 digits: d_n <= n + 6? | V1 Pass; H1 Supported; R1 Reported |
| 9 | `bc05f645` | Base 10, 1000 digits: d_n <= n + 8? | V1 Pass; H1 Supported; R1 Reported |
| 10 | `166a669c` | Base 3, 400 digits: d_n <= n + 9? | V1 Pass; H1 Supported; R1 Reported |
| 11 | `1b42003b` | Liouville's constant in base 30: super-linear? | V1 Pass; H1 Not supported; R1 Reported |
| 12 | `cd4ba428` | Liouville's constant in base 15: stays below 5? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (12; details `research/PASSES.md`)
- Pass 1: TRD-FOR-08: Liouville base 20 jumps (excess 434) but ratio 4.62 < 5 (not supported).
- Pass 2: TRD-FOR-08 (base 5, iteration 2): linear.
- Pass 3: TRD-FOR-08 (base 2, iteration 3): linear.
- Pass 4: TRD-FOR-08 (Proposition 3, base 4, iteration 4): ratio 122.
- Pass 5: TRD-FOR-08 (base 6, iteration 5): 47.6.
- Pass 6: TRD-FOR-08 (base 9, iteration 6): linear.
- Pass 7: TRD-FOR-09: base 16 excess at most 3.
- Pass 8: TRD-FOR-09 (base 8, iteration 8): at most 4.
- Pass 9: TRD-FOR-09 (base 10, 1000 digits, iteration 9): at most 7.
- Pass 10: TRD-FOR-09 (base 3, iteration 10): at most 7.
- Pass 11: TRD-FOR-08 (base 30, iteration 11): excess 368, ratio 4.07 (not supported).
- Pass 12: TRD-FOR-08 (base 15, iteration 12): linear.

## Unresolved
- Base-dependence reading is the agent's; a proof or source not found.
- Classical transcendence proofs not sourced.
