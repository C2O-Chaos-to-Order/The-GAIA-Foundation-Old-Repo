# Divergence in the Philosophy Spirituality — Cycle-0-Baseline (DV0)

Phase report: Divergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
In philosophy, divergence is a named principle (Bergson) and a structural motif (Plotinian procession); mapping both onto one GAIA phase is interpretation (PS).

## Claims (ledger: `claims/claims.csv`)
- **DV0-PHI-01** [E] Bergson held that if the original vital impulse is common to all life, there must also be a principle of divergence and differentiation explaining evolution, and that the successive bifurcations of life organise into two great opposite tendencies, instinct and intelligence, which remain inseparable tendencies rather than self-contained states. *Operationalization:* Divergence = differentiation of tendencies from a common impulse. *Sources:* P08. *Limits:* Reports a philosophical position, not its truth.
- **DV0-PHI-02** [E] In Plotinus, the 'theory of the two activities' is the cornerstone of the so-called process of 'emanation', by which the principles of reality other than the first come to be constituted. *Operationalization:* Divergence = procession of the many from the One. *Sources:* P07. *Limits:* The SEP entry itself flags 'emanation' as a conventional label ('so-called').
- **DV0-PHI-03** [PS] Plotinian procession and Bergsonian divergence are both 'one-to-many' accounts but differ in kind: one derives a hierarchy of principles from a first principle, the other derives diverging life tendencies from a common impulse in time; treating both as one 'Divergence phase' is an interpretive mapping, not a shared mechanism. *Operationalization:* Divergence as a cross-tradition philosophical category. *Sources:* P07;P08. *Limits:* Interpretation by this report; other readings (e.g. Bergson's criticism of finalism) are not yet compared.
- **DV0-PHI-04** [H] A Chinese restaurant process started from a single group produced on average 7.88 branches for n = 1,000 (alpha = 1) with a dominant branch holding 61% on average; the validation check (within 5% of the analytic 7.49) failed at 5.2%, so the run is not a validated result. *Operationalization:* Divergence = one-to-many branching (formal skeleton). *Sources:* SIM-DV-PHI-0/iter-1#V1;SIM-DV-PHI-0/iter-1#H1. *Limits:* V1 Fail is attributed to an under-tolerant check (no Monte Carlo tolerance; 300 replicates give SE about 0.14), supported by an out-of-record diagnostic with 3,000 replicates (7.52); recorded, not re-run; fixed tolerance planned for x3. Formal skeleton only: models no tradition.

## Simulations (SIM-DV-PHI-0; 1 iteration(s), spec-first; validation 0/1, hypotheses supported 1/1)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `1b088ab9` | Divergence as 'one becoming many': formal properties of a branching process that starts from a single group. | V1 Fail; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: P08 supplies an explicit philosophical 'principle of divergence and differentiation'; P07 the Plotinian procession from the One. The schism query returned nothing usable on religious divergence (Added nothing for spirituality proper: theological/denominational divergence is open for x3).

## Unresolved
- Religious/denominational divergence not yet sourced.
- Non-Western accounts of differentiation from a source (e.g. Daoist or Vedantic cosmogonies) not yet covered.
