# Divergence in the Natural Sciences — Cycle-0-Baseline (DV0)

Phase report: Divergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
In biology, divergence is well operationalized (genomic differentiation, Fst, branching descent) and strongly evidenced; the open questions are about mechanism (selection vs drift, timing).

## Claims (ledger: `claims/claims.csv`)
- **DV0-NAT-01** [E] In a speciation continuum of hybridizing races and incipient species of Heliconius erato-clade butterflies, genomic divergence increases with ecological and reproductive isolation, both at the red colour-pattern locus and at genomic regions unlinked to colour pattern. *Operationalization:* Divergence = genomic differentiation between populations along a speciation continuum. *Sources:* P01. *Limits:* 2.2 Mb of the H. erato genome only; a handful of population pairs; continuum stages are proxies for speciation stages, not a time series.
- **DV0-NAT-04** [E] Darwin's 1837-1838 notebook states that 'organized beings represent a tree irregularly branched', and the text beside an early sketch concerns genealogical distance between descendants of a common ancestor, where Darwin would later locate his principle of divergence of characteristics. *Operationalization:* Divergence = branching descent from a common ancestor (Darwin's principle of divergence). *Sources:* P02. *Limits:* Reported through a history-of-science article; the notebook itself was not read here.
- **DV0-NAT-02** [P] The same study infers that divergence may accumulate early in the speciation process and that limited gene flow cannot account for the high divergence between the incipient species H. erato and H. himera. *Operationalization:* Divergence with gene flow (divergence proceeding despite exchange). *Sources:* P01. *Limits:* Inference from one incipient-species pair; alternative histories (e.g. older isolation) are not excluded by the data shown.
- **DV0-NAT-03** [P] In a neutral two-deme Wright-Fisher model (N = 100, 400 loci), drift alone raised Fst to 0.385 after 200 generations (heterozygosity decay matched theory within 5%), whereas symmetric migration with Nm = 1 held Fst at 0.056: gene flow strongly restrains neutral divergence. *Operationalization:* Divergence = Fst growth between demes. *Sources:* SIM-DV-NAT-0/iter-1#V1;SIM-DV-NAT-0/iter-1#H1;SIM-DV-NAT-0/iter-1#H2. *Limits:* Toy neutral model; the H1 threshold was moved from 0.5 to 0.25 after a pre-spec smoke test (disclosed in the SPEC). Selection, which drives the colour-locus divergence in P01, is absent.

## Simulations (SIM-DV-NAT-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 2/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `7badc7b2` | Divergence as population differentiation: do two demes diverge (Fst rises) under drift alone, and does gene flow hold divergence back? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: P01 gives the empirical anchor (genomic divergence rises with isolation along a speciation continuum); P02 gives Darwin's own 'irregularly branched' tree. The adaptive-radiation query returned mostly radiotherapy papers (noise) and nothing was used from it.

## Unresolved
- Selection-driven divergence (colour locus) is not modelled; the baseline sim is neutral.
- Cell differentiation (developmental divergence) and physical bifurcation are not yet covered.
