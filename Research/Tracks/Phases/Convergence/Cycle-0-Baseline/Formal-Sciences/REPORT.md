# Convergence in the Formal Sciences — Cycle-0-Baseline (CV0)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: convergence of regular Markov chains (P73); examples reproduce, the (n - 1)^2 + 1 bound is tight, and a periodic chain shows an equilibrium that is not a limit.

## Claims (ledger: `claims/claims.csv`)
- **CV0-FOR-01** [E] A Markov chain is regular if some power of its transition matrix has only positive entries, which needs checking only up to the power (n - 1)^2 + 1; a regular chain converges to a unique equilibrium E with ET = E whatever the initial distribution (BestTV/CableCast: (.2, .8) gives .36/.64, .408/.592, .4224/.5776, then 3/7, 4/7); regularity is sufficient, not necessary, for ET = E to have a solution. *Operationalization:* FOR Convergence = convergence of a Markov chain to equilibrium. *Sources:* P73. *Limits:* Introductory textbook; it states the (n - 1)^2 + 1 bound as 'a theorem' without proof or name. Slips: B is first printed with entries 3 and 7 for .3 and .7; 'Best RV'; Example 2's transition matrix is not in the page text, so 13/55, 3/11, 27/55 cannot be checked.
- **CV0-FOR-02** [E] P73's printed iterates and E = (3/7, 4/7) reproduce exactly; the error shrinks as 0.3^n (second eigenvalue 0.3; error after 20 steps below 1e-9); A is regular at power 2 (A^2 = [[.40, .60], [.24, .76]]) and B never; the Wielandt matrix attains (n - 1)^2 + 1 exactly for n = 3-6, so P73's bound is tight; the periodic chain [[0, 1], [1, 0]] has E = (.5, .5) solving ET = E yet V_n oscillates, so Method 2 finds an equilibrium that is not a limit; DeGroot averaging with the same matrix reached consensus 4/7, the E-weighted mean of the initial opinions. *Operationalization:* FOR Convergence = convergence to equilibrium and consensus. *Sources:* SIM-CV-FOR-0/iter-1#V1;SIM-CV-FOR-0/iter-1#H1;SIM-CV-FOR-0/iter-1#H2;SIM-CV-FOR-0/iter-1#H3;SIM-CV-FOR-0/iter-1#H4;SIM-CV-FOR-0/iter-1#H5;SIM-CV-FOR-0/iter-1#H6. *Limits:* The Wielandt matrix, periodic chain and DeGroot reading are standard theory added by the agent, not in P73.

## Simulations (SIM-CV-FOR-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 6/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `16e244e7` | P73's regular Markov chains: do the printed iterates and equilibrium of the BestTV/CableCast example reproduce, does the error shrink as |lambda2|^n, are A regular and B not, does the Wielandt matrix attain P73's bound (n - 1)^2 + 1, does a periodic chain have a solution of ET = E without converging, and does DeGroot averaging reach an E-weighted consensus? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; H5 Supported; H6 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Regular chains, equilibrium and the (n - 1)^2 + 1 bound sourced (CV0-FOR-01); examples reproduced, bound shown tight, periodic counter-case and DeGroot consensus (CV0-FOR-02).

## Unresolved
- P73 Example 2's matrix is absent from the page text (13/55, 3/11, 27/55 unchecked).
- Convergence rates for consensus on general networks (algebraic connectivity) unsourced.
