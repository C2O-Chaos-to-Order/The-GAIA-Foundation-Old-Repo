# Insurgence in the Formal Sciences — Cycle-B-x6 (INB)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: the critical window is now sourced (P36) and reproduced up to n = 10^6 (exponents 0.64-0.69); earlier results replicate.

## Claims (ledger: `claims/claims.csv`)
- **INB-FOR-01** [E] In sparse Erdős–Rényi graphs with mean degree c, components are small when c < 1 (expected size of a random node's component about 1/(1-c)) and a giant component holding a positive fraction s of nodes appears when c > 1, with s = 1 - exp(-cs); P27 calls this a phase transition, 'a qualitative change in response to a small variation in a quantitative parameter'. *Operationalization:* FOR Insurgence = sudden emergence of a giant connected component at a critical mean degree. *Sources:* P27. *Limits:* P27 presents the giant-component result informally (proof referred elsewhere); lecture notes, licence not stated.
- **INB-FOR-06** [E] For the Erdős–Rényi graph G(n, p) in the critical window p = 1/n + lambda n^(-4/3), the largest components have size of order n^(2/3) (Theta(n^(2/3))), and Aldous (1997) gives the limit of the rescaled component sizes via a Brownian motion with parabolic drift. *Operationalization:* FOR Insurgence = the critical window. *Sources:* P36. *Limits:* Lecture slides, no licence stated; proof not given in P36. This now sources the n^(2/3) law used unsourced in INA-FOR-03.
- **INB-FOR-02** [P] P27's subcritical experiment reproduced: at c = 0.8 the mean component size was 4.69 (SE 0.26) against theory 5.00 and P27's printed 5.45 (both within 4 SE). With 50,000 nodes the largest component held 0.5% of nodes at c = 0.9, 3.1% at c = 1.0, 16.5% at 1.1 and 58.5% at 1.5 (theory 58.3%), within 0.02 of s = 1 - exp(-cs) for c >= 1.2. *Operationalization:* FOR Insurgence = giant component emergence. *Sources:* SIM-IN-FOR-0/iter-1#V1;SIM-IN-FOR-0/iter-1#H1;SIM-IN-FOR-0/iter-1#H2;SIM-IN-FOR-0/iter-1#H3. *Limits:* Finite n blurs the transition at c = 1; ten graphs per c.
- **INB-FOR-03** [P] At the critical mean degree c = 1 the largest component held 75.7, 409 and 2,092 nodes for n = 1,000, 10,000 and 100,000 (fractions 7.6%, 4.1%, 2.1%); its growth exponent was 0.72, within 0.1 of the standard n^(2/3) law: at the threshold itself no giant component exists yet, only a slowly widening critical cluster. *Operationalization:* FOR Insurgence = the critical window of the transition. *Sources:* SIM-IN-FOR-A/iter-1#V1;SIM-IN-FOR-A/iter-1#H1. *Limits:* The n^(2/3) law is stated from the agent's knowledge, not from a source read in this track; the fitted 0.72 is above 2/3 (finite-size effects).
- **INB-FOR-04** [P] Poisson(c) branching processes (P27's approximation for component sizes) reached 1,000 individuals in 17.2%, 58.6%, 79.5% and 93.9% of 5,000 runs for c = 1.1, 1.5, 2 and 3, each within 4 SE (+0.01) of s = 1 - exp(-cs) (17.6%, 58.3%, 79.7%, 94.0%): the same equation fixes the giant-component fraction and the chance that one lineage escapes extinction. *Operationalization:* FOR Insurgence = a lineage escaping extinction. *Sources:* SIM-IN-FOR-A/iter-2#V1;SIM-IN-FOR-A/iter-2#H1. *Limits:* Reaching K = 1000 is a proxy for survival.
- **INB-FOR-05** [P] Replication at n = 200,000: the subcritical mean component size at c = 0.8 was 4.97 (SE 0.30; theory 5.00, P27's printed 5.45 within 4 SE), and the largest component held 0.2% of nodes at c = 0.9, 1.5% at 1.0, 18.0% at 1.1 (theory 17.6%) and 58.6% at 1.5 (theory 58.3%), within 0.02 of s from c = 1.1 upward; the transition is sharper than at n = 50,000 (IN0-FOR-02: 16.5% at 1.1). *Operationalization:* FOR Insurgence = giant-component emergence (replication). *Sources:* SIM-IN-FOR-A/iter-3#V1;SIM-IN-FOR-A/iter-3#H1;SIM-IN-FOR-A/iter-3#H2;SIM-IN-FOR-A/iter-3#H3. *Limits:* Five graphs per c.
- **INB-FOR-07** [P] Over n = 1,000 to 1,000,000 the largest component grew with exponents 0.687 (lambda = 0), 0.672 (lambda = +1) and 0.636 (lambda = -1), all within 0.1 of 2/3 (INA's 0.72 used only n up to 100,000); rescaled sizes L/n^(2/3) stayed of order one (about 0.5 to 2.2), larger for larger lambda. *Operationalization:* FOR Insurgence = critical window (simulation). *Sources:* SIM-IN-FOR-B/iter-1#V1;SIM-IN-FOR-B/iter-1#H1;SIM-IN-FOR-B/iter-2#V1;SIM-IN-FOR-B/iter-2#H1;SIM-IN-FOR-B/iter-3#V1;SIM-IN-FOR-B/iter-3#H1. *Limits:* Ten graphs per n; rescaled sizes fluctuate strongly, as expected for a random limit.
- **INB-FOR-08** [P] Replications held: lineages reaching 10,000 individuals at c = 1.05, 1.1, 1.5 (9.1%, 18.1%, 58.0%) matched s (9.3%, 17.6%, 58.2%); at n = 100,000 the giant component was within 0.02 of s from c = 1.1, and the subcritical mean (4.58, SE 0.27) again bracketed theory 5.00 and P27's printed 5.45 within 4 SE. *Operationalization:* FOR Insurgence = giant component and survival (replications). *Sources:* SIM-IN-FOR-B/iter-4#V1;SIM-IN-FOR-B/iter-4#H1;SIM-IN-FOR-B/iter-5#V1;SIM-IN-FOR-B/iter-5#H1;SIM-IN-FOR-B/iter-5#H2;SIM-IN-FOR-B/iter-5#H3;SIM-IN-FOR-B/iter-6#V1;SIM-IN-FOR-B/iter-6#H1. *Limits:* Replications on new seeds.

## Simulations (SIM-IN-FOR-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 8/8)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `e534b823` | The critical window (P36): with c = 1 + lambda n^(-1/3), lambda = 0, is the largest component ~ n^(2/3) over n = 10^3 to 10^6? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `c5fefb9d` | Inside the window, lambda = +1 (P36): does the largest component still scale like n^(2/3)? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `a7228bda` | Inside the window, lambda = -1 (P36). | V1 Pass; H1 Supported; R1 Reported |
| 4 | `3c305a28` | Finite-K bias near c = 1 (FOR x6): share of Poisson(c) lineages reaching K = 10,000 for c = 1.05, 1.1, 1.5. | V1 Pass; H1 Supported; R1 Reported |
| 5 | `c0986747` | Replication of IN0-FOR-02 (n = 100,000, 5 graphs per c) on a new seed. | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 6 | `fe43e388` | Replication of INA-FOR-04 on a new seed (K = 1000). | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: INB-FOR-06: the n^(2/3) critical-window law sourced (was unsourced in INA).
- Pass 2: INB-FOR-07: exponents 0.64-0.69 over n up to 10^6 for lambda = -1, 0, +1.
- Pass 3: Added nothing: lambda = -1 run folded into INB-FOR-07.
- Pass 4: INB-FOR-08 (part): finite-K bias near c = 1 small at K = 10,000.
- Pass 5: Added nothing: replication of IN0-FOR-02 (folded into INB-FOR-08).
- Pass 6: Added nothing: replication of INA-FOR-04 (folded into INB-FOR-08).

## Unresolved
- Aldous limit not reproduced; P36 is slides without licence.
