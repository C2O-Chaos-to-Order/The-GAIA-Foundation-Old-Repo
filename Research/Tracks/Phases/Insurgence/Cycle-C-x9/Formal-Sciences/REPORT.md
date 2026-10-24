# Insurgence in the Formal Sciences — Cycle-C-x9 (INC)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x9: no new source; the critical-window scaling holds across lambda = -4..+4 with finite-size drift; the rest are replications.

## Claims (ledger: `claims/claims.csv`)
- **INC-FOR-01** [E] In sparse Erdős–Rényi graphs with mean degree c, components are small when c < 1 (expected size of a random node's component about 1/(1-c)) and a giant component holding a positive fraction s of nodes appears when c > 1, with s = 1 - exp(-cs); P27 calls this a phase transition, 'a qualitative change in response to a small variation in a quantitative parameter'. *Operationalization:* FOR Insurgence = sudden emergence of a giant connected component at a critical mean degree. *Sources:* P27. *Limits:* P27 presents the giant-component result informally (proof referred elsewhere); lecture notes, licence not stated.
- **INC-FOR-06** [E] For the Erdős–Rényi graph G(n, p) in the critical window p = 1/n + lambda n^(-4/3), the largest components have size of order n^(2/3) (Theta(n^(2/3))), and Aldous (1997) gives the limit of the rescaled component sizes via a Brownian motion with parabolic drift. *Operationalization:* FOR Insurgence = the critical window. *Sources:* P36. *Limits:* Lecture slides, no licence stated; proof not given in P36. This now sources the n^(2/3) law used unsourced in INA-FOR-03.
- **INC-FOR-02** [P] P27's subcritical experiment reproduced: at c = 0.8 the mean component size was 4.69 (SE 0.26) against theory 5.00 and P27's printed 5.45 (both within 4 SE). With 50,000 nodes the largest component held 0.5% of nodes at c = 0.9, 3.1% at c = 1.0, 16.5% at 1.1 and 58.5% at 1.5 (theory 58.3%), within 0.02 of s = 1 - exp(-cs) for c >= 1.2. *Operationalization:* FOR Insurgence = giant component emergence. *Sources:* SIM-IN-FOR-0/iter-1#V1;SIM-IN-FOR-0/iter-1#H1;SIM-IN-FOR-0/iter-1#H2;SIM-IN-FOR-0/iter-1#H3. *Limits:* Finite n blurs the transition at c = 1; ten graphs per c.
- **INC-FOR-03** [P] At the critical mean degree c = 1 the largest component held 75.7, 409 and 2,092 nodes for n = 1,000, 10,000 and 100,000 (fractions 7.6%, 4.1%, 2.1%); its growth exponent was 0.72, within 0.1 of the standard n^(2/3) law: at the threshold itself no giant component exists yet, only a slowly widening critical cluster. *Operationalization:* FOR Insurgence = the critical window of the transition. *Sources:* SIM-IN-FOR-A/iter-1#V1;SIM-IN-FOR-A/iter-1#H1. *Limits:* The n^(2/3) law is stated from the agent's knowledge, not from a source read in this track; the fitted 0.72 is above 2/3 (finite-size effects).
- **INC-FOR-04** [P] Poisson(c) branching processes (P27's approximation for component sizes) reached 1,000 individuals in 17.2%, 58.6%, 79.5% and 93.9% of 5,000 runs for c = 1.1, 1.5, 2 and 3, each within 4 SE (+0.01) of s = 1 - exp(-cs) (17.6%, 58.3%, 79.7%, 94.0%): the same equation fixes the giant-component fraction and the chance that one lineage escapes extinction. *Operationalization:* FOR Insurgence = a lineage escaping extinction. *Sources:* SIM-IN-FOR-A/iter-2#V1;SIM-IN-FOR-A/iter-2#H1. *Limits:* Reaching K = 1000 is a proxy for survival.
- **INC-FOR-05** [P] Replication at n = 200,000: the subcritical mean component size at c = 0.8 was 4.97 (SE 0.30; theory 5.00, P27's printed 5.45 within 4 SE), and the largest component held 0.2% of nodes at c = 0.9, 1.5% at 1.0, 18.0% at 1.1 (theory 17.6%) and 58.6% at 1.5 (theory 58.3%), within 0.02 of s from c = 1.1 upward; the transition is sharper than at n = 50,000 (IN0-FOR-02: 16.5% at 1.1). *Operationalization:* FOR Insurgence = giant-component emergence (replication). *Sources:* SIM-IN-FOR-A/iter-3#V1;SIM-IN-FOR-A/iter-3#H1;SIM-IN-FOR-A/iter-3#H2;SIM-IN-FOR-A/iter-3#H3. *Limits:* Five graphs per c.
- **INC-FOR-07** [P] Over n = 1,000 to 1,000,000 the largest component grew with exponents 0.687 (lambda = 0), 0.672 (lambda = +1) and 0.636 (lambda = -1), all within 0.1 of 2/3 (INA's 0.72 used only n up to 100,000); rescaled sizes L/n^(2/3) stayed of order one (about 0.5 to 2.2), larger for larger lambda. *Operationalization:* FOR Insurgence = critical window (simulation). *Sources:* SIM-IN-FOR-B/iter-1#V1;SIM-IN-FOR-B/iter-1#H1;SIM-IN-FOR-B/iter-2#V1;SIM-IN-FOR-B/iter-2#H1;SIM-IN-FOR-B/iter-3#V1;SIM-IN-FOR-B/iter-3#H1. *Limits:* Ten graphs per n; rescaled sizes fluctuate strongly, as expected for a random limit.
- **INC-FOR-08** [P] Replications held: lineages reaching 10,000 individuals at c = 1.05, 1.1, 1.5 (9.1%, 18.1%, 58.0%) matched s (9.3%, 17.6%, 58.2%); at n = 100,000 the giant component was within 0.02 of s from c = 1.1, and the subcritical mean (4.58, SE 0.27) again bracketed theory 5.00 and P27's printed 5.45 within 4 SE. *Operationalization:* FOR Insurgence = giant component and survival (replications). *Sources:* SIM-IN-FOR-B/iter-4#V1;SIM-IN-FOR-B/iter-4#H1;SIM-IN-FOR-B/iter-5#V1;SIM-IN-FOR-B/iter-5#H1;SIM-IN-FOR-B/iter-5#H2;SIM-IN-FOR-B/iter-5#H3;SIM-IN-FOR-B/iter-6#V1;SIM-IN-FOR-B/iter-6#H1. *Limits:* Replications on new seeds.
- **INC-FOR-09** [P] The n^(2/3) scaling of the largest component (P36: for any fixed lambda in p = 1/n + lambda n^(-4/3)) held within 0.1 for lambda = -4, -2, 0, +2, +4 up to n = 10^6, but the rescaled size L/n^(2/3) still drifted with n for lambda = +2 (2.8 to 4.3) and +4 (5.2 to 7.3): at these sizes the window is only approximately scale-free. *Operationalization:* FOR Insurgence = the critical window across lambda. *Sources:* SIM-IN-FOR-C/iter-1#V1;SIM-IN-FOR-C/iter-1#H1;SIM-IN-FOR-C/iter-2#V1;SIM-IN-FOR-C/iter-2#H1;SIM-IN-FOR-C/iter-3#V1;SIM-IN-FOR-C/iter-3#H1;SIM-IN-FOR-C/iter-4#V1;SIM-IN-FOR-C/iter-4#H1;SIM-IN-FOR-C/iter-5#V1;SIM-IN-FOR-C/iter-5#H1. *Limits:* 10 graphs per n; no new source (P36 reused). Aldous's limit law not tested.
- **INC-FOR-10** [P] Replications: lineage survival at K = 10,000 within tolerance of s even at c = 1.02 (3.7% vs 3.9%) and c = 1.05 (9.4% vs 9.4%); giant component and K = 1,000 survival replicated on third seeds. Nothing new. *Operationalization:* FOR Insurgence = lineage survival (replications). *Sources:* SIM-IN-FOR-C/iter-6#V1;SIM-IN-FOR-C/iter-6#H1;SIM-IN-FOR-C/iter-7#V1;SIM-IN-FOR-C/iter-7#H1;SIM-IN-FOR-C/iter-8#V1;SIM-IN-FOR-C/iter-8#H1;SIM-IN-FOR-C/iter-8#H2;SIM-IN-FOR-C/iter-8#H3;SIM-IN-FOR-C/iter-9#V1;SIM-IN-FOR-C/iter-9#H1. *Limits:* Replications only.

## Simulations (SIM-IN-FOR-C; 9 iteration(s), spec-first; validation 9/9, hypotheses supported 11/11)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `e3999dbe` | Replication of INB-FOR iter-1 (critical window, lambda = 0) on a new seed. | V1 Pass; H1 Supported; R1 Reported |
| 2 | `2bb225be` | Critical window at lambda = +2 (P36: Theta(n^(2/3)) for any fixed lambda). | V1 Pass; H1 Supported; R1 Reported |
| 3 | `e1bf7a3f` | Critical window at lambda = -2. | V1 Pass; H1 Supported; R1 Reported |
| 4 | `40094b48` | Critical window at lambda = +4 (edge of the window at small n). | V1 Pass; H1 Supported; R1 Reported |
| 5 | `c5a97672` | Critical window at lambda = -4. | V1 Pass; H1 Supported; R1 Reported |
| 6 | `43b63072` | Replication of INB-FOR iter-4 (finite-K bias, K = 10,000) on a new seed. | V1 Pass; H1 Supported; R1 Reported |
| 7 | `cf338081` | Lineage survival very close to criticality: c = 1.02, 1.05 with K = 10,000. | V1 Pass; H1 Supported; R1 Reported |
| 8 | `8ddb881f` | Replication of IN0-FOR-02 giant component on a third seed. | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 9 | `90bccaac` | Replication of INA-FOR-04 (K = 1000) on a third seed. | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (9; details `research/PASSES.md`)
- Pass 1: Added nothing: no FOR source search was run this cycle (search time went to the NAT, SOC, APP, HUM and PHI gaps); replication of INB-FOR iter-1.
- Pass 2: INC-FOR-09: the n^(2/3) law across lambda = -4..+4, with drift of the rescaled size at positive lambda.
- Pass 3: Added nothing: folded into INC-FOR-09.
- Pass 4: Added nothing: folded into INC-FOR-09.
- Pass 5: Added nothing: folded into INC-FOR-09.
- Pass 6: Added nothing: replication (INC-FOR-10).
- Pass 7: Added nothing: c = 1.02 agrees with theory; folded into INC-FOR-10.
- Pass 8: Added nothing: replication.
- Pass 9: Added nothing: replication.

## Unresolved
- No new FOR source; Aldous's limit law still untested.
