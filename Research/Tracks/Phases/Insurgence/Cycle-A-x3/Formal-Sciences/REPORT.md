# Insurgence in the Formal Sciences — Cycle-A-x3 (INA)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: at c = 1 the largest cluster grows sub-linearly (n^0.72 measured); the branching-process survival s = 1 - exp(-cs) is confirmed; the transition sharpens at n = 200,000.

## Claims (ledger: `claims/claims.csv`)
- **INA-FOR-01** [E] In sparse Erdős–Rényi graphs with mean degree c, components are small when c < 1 (expected size of a random node's component about 1/(1-c)) and a giant component holding a positive fraction s of nodes appears when c > 1, with s = 1 - exp(-cs); P27 calls this a phase transition, 'a qualitative change in response to a small variation in a quantitative parameter'. *Operationalization:* FOR Insurgence = sudden emergence of a giant connected component at a critical mean degree. *Sources:* P27. *Limits:* P27 presents the giant-component result informally (proof referred elsewhere); lecture notes, licence not stated.
- **INA-FOR-02** [P] P27's subcritical experiment reproduced: at c = 0.8 the mean component size was 4.69 (SE 0.26) against theory 5.00 and P27's printed 5.45 (both within 4 SE). With 50,000 nodes the largest component held 0.5% of nodes at c = 0.9, 3.1% at c = 1.0, 16.5% at 1.1 and 58.5% at 1.5 (theory 58.3%), within 0.02 of s = 1 - exp(-cs) for c >= 1.2. *Operationalization:* FOR Insurgence = giant component emergence. *Sources:* SIM-IN-FOR-0/iter-1#V1;SIM-IN-FOR-0/iter-1#H1;SIM-IN-FOR-0/iter-1#H2;SIM-IN-FOR-0/iter-1#H3. *Limits:* Finite n blurs the transition at c = 1; ten graphs per c.
- **INA-FOR-03** [P] At the critical mean degree c = 1 the largest component held 75.7, 409 and 2,092 nodes for n = 1,000, 10,000 and 100,000 (fractions 7.6%, 4.1%, 2.1%); its growth exponent was 0.72, within 0.1 of the standard n^(2/3) law: at the threshold itself no giant component exists yet, only a slowly widening critical cluster. *Operationalization:* FOR Insurgence = the critical window of the transition. *Sources:* SIM-IN-FOR-A/iter-1#V1;SIM-IN-FOR-A/iter-1#H1. *Limits:* The n^(2/3) law is stated from the agent's knowledge, not from a source read in this track; the fitted 0.72 is above 2/3 (finite-size effects).
- **INA-FOR-04** [P] Poisson(c) branching processes (P27's approximation for component sizes) reached 1,000 individuals in 17.2%, 58.6%, 79.5% and 93.9% of 5,000 runs for c = 1.1, 1.5, 2 and 3, each within 4 SE (+0.01) of s = 1 - exp(-cs) (17.6%, 58.3%, 79.7%, 94.0%): the same equation fixes the giant-component fraction and the chance that one lineage escapes extinction. *Operationalization:* FOR Insurgence = a lineage escaping extinction. *Sources:* SIM-IN-FOR-A/iter-2#V1;SIM-IN-FOR-A/iter-2#H1. *Limits:* Reaching K = 1000 is a proxy for survival.
- **INA-FOR-05** [P] Replication at n = 200,000: the subcritical mean component size at c = 0.8 was 4.97 (SE 0.30; theory 5.00, P27's printed 5.45 within 4 SE), and the largest component held 0.2% of nodes at c = 0.9, 1.5% at 1.0, 18.0% at 1.1 (theory 17.6%) and 58.6% at 1.5 (theory 58.3%), within 0.02 of s from c = 1.1 upward; the transition is sharper than at n = 50,000 (IN0-FOR-02: 16.5% at 1.1). *Operationalization:* FOR Insurgence = giant-component emergence (replication). *Sources:* SIM-IN-FOR-A/iter-3#V1;SIM-IN-FOR-A/iter-3#H1;SIM-IN-FOR-A/iter-3#H2;SIM-IN-FOR-A/iter-3#H3. *Limits:* Five graphs per c.

## Simulations (SIM-IN-FOR-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 5/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `bab43400` | Size of the largest component at the critical point c = 1 (FOR pass 2): does it grow like n^(2/3) for n = 1,000, 10,000, 100,000? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `21050847` | Branching-process approximation (FOR pass 2; P27 Definition 2.4): does the share of Poisson(c) Galton-Watson processes reaching 1,000 individuals match s = 1 - exp(-cs) for c = 1.1, 1.5, 2, 3? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `cc92f555` | Replication at larger n (FOR pass 3): repeat IN0's giant-component run with n = 200,000 (5 graphs per c) and a fresh subcritical sample; is the largest-component fraction within 0.02 of s from c = 1.1 upward? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: INA-FOR-03: at c = 1 the largest component grows like n^0.72 (standard law n^(2/3), stated from the agent's knowledge, not a source).
- Pass 2: INA-FOR-04: branching-process survival matches s = 1 - exp(-cs) for c = 1.1-3 (P27's approximation).
- Pass 3: INA-FOR-05: replication of IN0-FOR-02 at n = 200,000; sharper transition. No new source.

## Unresolved
- n^(2/3) critical-window law not sourced; fitted exponent 0.72.
- P27 lecture notes, licence not stated.
