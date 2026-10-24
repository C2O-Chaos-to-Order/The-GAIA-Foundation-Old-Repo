# Convergence in the Formal Sciences — Cycle-A-x3 (CVA)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P74's null is a P73 chain; a non-regular chain can still converge; the Wielandt bound is tight but rarely reached at random; a stubborn agent fixes the consensus.

## Claims (ledger: `claims/claims.csv`)
- **CVA-FOR-01** [E] A Markov chain is regular if some power of its transition matrix has only positive entries, which needs checking only up to the power (n - 1)^2 + 1; a regular chain converges to a unique equilibrium E with ET = E whatever the initial distribution (BestTV/CableCast: (.2, .8) gives .36/.64, .408/.592, .4224/.5776, then 3/7, 4/7); regularity is sufficient, not necessary, for ET = E to have a solution. *Operationalization:* FOR Convergence = convergence of a Markov chain to equilibrium. *Sources:* P73. *Limits:* Introductory textbook; it states the (n - 1)^2 + 1 bound as 'a theorem' without proof or name. Slips: B is first printed with entries 3 and 7 for .3 and .7; 'Best RV'; Example 2's transition matrix is not in the page text, so 13/55, 3/11, 27/55 cannot be checked.
- **CVA-FOR-02** [E] P73's printed iterates and E = (3/7, 4/7) reproduce exactly; the error shrinks as 0.3^n (second eigenvalue 0.3; error after 20 steps below 1e-9); A is regular at power 2 (A^2 = [[.40, .60], [.24, .76]]) and B never; the Wielandt matrix attains (n - 1)^2 + 1 exactly for n = 3-6, so P73's bound is tight; the periodic chain [[0, 1], [1, 0]] has E = (.5, .5) solving ET = E yet V_n oscillates, so Method 2 finds an equilibrium that is not a limit; DeGroot averaging with the same matrix reached consensus 4/7, the E-weighted mean of the initial opinions. *Operationalization:* FOR Convergence = convergence to equilibrium and consensus. *Sources:* SIM-CV-FOR-0/iter-1#V1;SIM-CV-FOR-0/iter-1#H1;SIM-CV-FOR-0/iter-1#H2;SIM-CV-FOR-0/iter-1#H3;SIM-CV-FOR-0/iter-1#H4;SIM-CV-FOR-0/iter-1#H5;SIM-CV-FOR-0/iter-1#H6. *Limits:* The Wielandt matrix, periodic chain and DeGroot reading are standard theory added by the agent, not in P73.
- **CVA-FOR-03** [E] P74's null locus is a two-state Markov chain of P73's kind: with P_loss 0.005 and P_gain 0.00126 the equilibrium is exactly 0.201, the second eigenvalue is 1 - P_gain - P_loss = 0.99374, and from S0 = 0.3878 the share of ones after 682 steps is 0.2036, the analytic value; with this slow rate the chain is still 0.003 above equilibrium at P74's oldest time point. *Operationalization:* FOR Convergence = Markov-chain convergence (shared with NAT). *Sources:* SIM-CV-FOR-A/iter-1#V1;SIM-CV-FOR-A/iter-1#H1;SIM-CV-FOR-A/iter-1#H2;SIM-CV-FOR-A/iter-1#H3. *Limits:* P_loss is the agent's choice.
- **CVA-FOR-04** [E] P73's matrix B is not regular, yet both starts (0.2, 0.8) and (0.9, 0.1) converge to (1, 0), illustrating P73's 'sufficient, not necessary'; the Wielandt matrix needs exactly (n - 1)^2 + 1 = 37, 50 and 65 powers for n = 7, 8, 9; among 2000 random primitive patterns per size the largest exponents were 5, 10, 14, 13, 13 for n = 3-7 against bounds 5, 10, 17, 26, 37, so the bound is reached at random only for n <= 4. *Operationalization:* FOR Convergence = when chains converge. *Sources:* SIM-CV-FOR-A/iter-2#V1;SIM-CV-FOR-A/iter-2#H1;SIM-CV-FOR-A/iter-2#H2;SIM-CV-FOR-A/iter-2#H3;SIM-CV-FOR-A/iter-2#H4. *Limits:* Random patterns at density 0.3 only.
- **CVA-FOR-05** [E] In a four-agent DeGroot chain where agent 1 keeps its own opinion, all opinions converged to agent 1's initial 0.9 (spread 0), and the chain's limit is (1, 0, 0, 0) from both starts: a fully stubborn agent determines the consensus. *Operationalization:* FOR Convergence = consensus with a stubborn agent. *Sources:* SIM-CV-FOR-A/iter-3#V1;SIM-CV-FOR-A/iter-3#H1;SIM-CV-FOR-A/iter-3#H2. *Limits:* Network chosen by the agent.

## Simulations (SIM-CV-FOR-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 9/9)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `d287b912` | P74's ZFEL null as a Markov chain: with P_loss 0.005 and P_gain set for S = 0.201, is the equilibrium 0.201, the second eigenvalue 1 - P_gain - P_loss, and the proportion at 682 steps from S0 = 0.3878 the analytic value? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 2 | `78f38dc0` | P73 says regularity is sufficient, not necessary: does P73's non-regular B still converge to a unique limit from two starts, does the Wielandt matrix attain (n - 1)^2 + 1 for n = 7-9, and do 2000 random primitive 0/1 patterns per size (n = 3-7) stay within (and for n >= 5 below) the bound? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; R1 Reported |
| 3 | `d28e7046` | DeGroot consensus with a stubborn agent: in a four-agent chain where agent 1 keeps its opinion, does everyone converge to agent 1's initial opinion, and is the chain's limit (1, 0, 0, 0) from both starts? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: CVA-FOR-03: P74's null as a P73-type chain; slow loss rates leave it short of equilibrium at 682 My.
- Pass 2: CVA-FOR-04: non-regular B still converges; Wielandt bound tight for n = 7-9 and rarely reached at random.
- Pass 3: CVA-FOR-05: a stubborn agent fixes the DeGroot consensus.

## Unresolved
- Mixing-time bounds (Levin & Peres, cited in P74) not sourced.
- Convergence rate on general networks unsourced.
