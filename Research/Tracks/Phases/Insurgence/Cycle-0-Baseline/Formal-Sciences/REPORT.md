# Insurgence in the Formal Sciences — Cycle-0-Baseline (IN0)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: insurgence as a phase transition, the sudden appearance of a giant component at mean degree 1 (P27); P27's printed experiment reproduces.

## Claims (ledger: `claims/claims.csv`)
- **IN0-FOR-01** [E] In sparse Erdős–Rényi graphs with mean degree c, components are small when c < 1 (expected size of a random node's component about 1/(1-c)) and a giant component holding a positive fraction s of nodes appears when c > 1, with s = 1 - exp(-cs); P27 calls this a phase transition, 'a qualitative change in response to a small variation in a quantitative parameter'. *Operationalization:* FOR Insurgence = sudden emergence of a giant connected component at a critical mean degree. *Sources:* P27. *Limits:* P27 presents the giant-component result informally (proof referred elsewhere); lecture notes, licence not stated.
- **IN0-FOR-02** [P] P27's subcritical experiment reproduced: at c = 0.8 the mean component size was 4.69 (SE 0.26) against theory 5.00 and P27's printed 5.45 (both within 4 SE). With 50,000 nodes the largest component held 0.5% of nodes at c = 0.9, 3.1% at c = 1.0, 16.5% at 1.1 and 58.5% at 1.5 (theory 58.3%), within 0.02 of s = 1 - exp(-cs) for c >= 1.2. *Operationalization:* FOR Insurgence = giant component emergence. *Sources:* SIM-IN-FOR-0/iter-1#V1;SIM-IN-FOR-0/iter-1#H1;SIM-IN-FOR-0/iter-1#H2;SIM-IN-FOR-0/iter-1#H3. *Limits:* Finite n blurs the transition at c = 1; ten graphs per c.

## Simulations (SIM-IN-FOR-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 3/3)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `d5104b3f` | Emergence of the giant component in sparse Erdos-Renyi graphs (P27): reproduce P27's subcritical experiment (n 5000, c 0.8, 1000 samples, printed mean 5.45 vs theory 5.00) and the largest-component fraction against s = 1 - exp(-cs) across c = 0.5-1.5. | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Giant-component emergence sourced (IN0-FOR-01); P27's printed experiment checked (IN0-FOR-02).

## Unresolved
- Percolation and other phase-transition senses unsourced; P27 is lecture notes with no stated licence.
