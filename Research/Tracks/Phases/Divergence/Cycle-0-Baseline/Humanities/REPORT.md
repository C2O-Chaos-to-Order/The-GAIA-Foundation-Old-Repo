# Divergence in the Humanities — Cycle-0-Baseline (DV0)

Phase report: Divergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
In the humanities, divergence of languages and of images of descent is documented, and the measurement method visibly shapes the result.

## Claims (ledger: `claims/claims.csv`)
- **DV0-HUM-01** [E] For the Andic branch of East Caucasian, geographic distances correlate with linguistic divergence across several alternative phylogenies, and qualitative classifications fit geography better than cognacy-based phylogenies. *Operationalization:* Divergence = genealogical distance between languages. *Sources:* P06. *Limits:* One small language group; correlation, not mechanism.
- **DV0-HUM-03** [E] Historians disagree about the image of divergence in Darwin: some argue the Origin diagram has the structure not of a tree but of a coral, and P02 argues the sketches had a heuristic function and became more abstract diagrams over time. *Operationalization:* Divergence images: tree vs coral vs seaweed. *Sources:* P02. *Limits:* One historiographical article's survey.
- **DV0-HUM-02** [P] The authors interpret the better geographic fit of qualitative classifications as possible implicit geographic bias, so that how linguistic divergence is measured (cognacy vs expert classification) can change what it appears to show. *Operationalization:* Measurement-dependence of 'divergence'. *Sources:* P06. *Limits:* An interpretation offered by the authors; not tested against an independent benchmark.
- **DV0-HUM-04** [P] In a formal lexical-replacement model, a constant-rate shared-cognate estimate recovered a 3,000-year split without bias when rates were equal across meanings, but underestimated it by 16% when rates varied (gamma shape 1). *Operationalization:* Divergence time from shared cognates. *Sources:* SIM-DV-HUM-0/iter-1#V1;SIM-DV-HUM-0/iter-1#V2;SIM-DV-HUM-0/iter-1#H1. *Limits:* Formal check of a dating method; parameters illustrative; borrowing and chance resemblance ignored.

## Simulations (SIM-DV-HUM-0; 1 iteration(s), spec-first; validation 2/2, hypotheses supported 1/1)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `42d14e2b` | Divergence as language splitting: how well does a constant-rate shared-cognate estimate recover split time, with and without rate heterogeneity? | V1 Pass; V2 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: P06 shows that the measured divergence between languages depends on the classification method; P02 records the tree-vs-coral debate over Darwin's divergence image. No source on glottochronology itself was read yet (the HUM simulation's rate value is illustrative).

## Unresolved
- No glottochronology/lexicostatistics source read; the HUM sim rate is illustrative.
- Textual (manuscript) and artistic divergence not yet covered.
