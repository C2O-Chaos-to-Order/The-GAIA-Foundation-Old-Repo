# Divergence — operationalizations and competing definitions

Status: Proposed working definitions for the GAIA Phase axis (Research/README.md §9.3, §12 Q1, Q4). Each field keeps its own meaning; no single cross-field definition is assumed. Competing definitions are recorded, not resolved. Sources: see the cycle registers (P-numbers); "unsourced" means named here but not yet backed by a source read in this track.

| field | working operationalization (this track) | competing or neighbouring definitions | sourced? |
|---|---|---|---|
| Natural sciences | genetic/genomic differentiation between populations (e.g. Fst) along a speciation continuum; branching descent | Darwin's principle of divergence of character (P02); divergence with gene flow (P01); cell differentiation in development; bifurcation in physical systems | P01, P02; development and physics unsourced |
| Formal sciences | exponential separation of nearby trajectories (positive global Lyapunov exponent) | divergent series (no finite limit); the divergence operator of vector calculus (net outflow); statistical divergences (e.g. Kullback-Leibler, asymmetric "distances"); topological definitions of chaos (P09) | P09 for trajectories and chaos definitions; series, operator and statistical senses unsourced |
| Social sciences | fragmentation of a population into separated opinion clusters; polarisation | homophily-driven clustering; differentiative (repulsive) influence; event-driven polarisation (P03); economic divergence (income convergence/divergence) | P03; economic sense unsourced |
| Applied sciences | branching clonal evolution producing intratumour heterogeneity | linear vs branched vs punctuated ("Big Bang") models (P04, P05); design-process divergence (generating options); numerical divergence of iterative solvers | P04, P05; engineering senses unsourced |
| Humanities | lexical/genealogical divergence of languages from a common ancestor | qualitative vs cognacy-based classification (P06); images of descent: tree vs coral vs seaweed (P02); textual divergence of manuscripts (stemmatics) | P02, P06; stemmatics unsourced |
| Philosophy / spirituality | differentiation of the many from a common source | Bergson's principle of divergence and differentiation (P08); Plotinian procession/"so-called emanation" from the One (P07); religious schism and denominational branching | P07, P08; schism unsourced |

## Cross-field observations (Baseline)
- The word covers at least three structurally different things: **branching** (one lineage becomes several: species, clones, languages, groups), **separation** (distance between states grows: trajectories, allele frequencies, opinions) and **differentiation** (parts of a whole become unlike each other: tendencies, cell types). Branching and separation are often combined (branching followed by growing distance).
- Whether "Divergence" names one phenomenon across fields is **not established**; the cross-field mapping is an interpretive (PS) or hypothetical (H) claim until a shared formal criterion is defined and tested.

## Updates in x3 (DVA)
| field | newly sourced or newly checked senses | sources / runs | still unsourced |
|---|---|---|---|
| Natural sciences | cell-fate divergence pictured as Waddington's epigenetic landscape (metaphor); selection-driven divergence against gene flow (toy) | P10; SIM-DV-NAT-A iter-1..3 | genomic islands with linkage; physical bifurcation (simulated only) |
| Formal sciences | statistical divergence (KL, asymmetric), divergent series, divergence operator | SIM-DV-FOR-A iter-1..3 (code/analytic checks only) | all three senses (no source read) |
| Social sciences | value divergence across countries with regional convergence; event-sustained polarisation | P11, P03 (re-read in full); SIM-DV-SOC-A iter-1..3 | economic (income) divergence |
| Applied sciences | numerical divergence of an iterative solver; replication of clonal branching | SIM-DV-APP-A iter-1..3 | design-process divergence; numerical analysis sources |
| Humanities | lexicostatistics vs glottochronology; list-size and recurrence principles; manuscript divergence (stemmatics) and contamination | P12, P13; SIM-DV-HUM-A iter-1..3 | artistic divergence |
| Philosophy / spirituality | religious divergence across countries (religion most divergent trait); schisms as trees and the limits of tree thinking | P14, P15; SIM-DV-PHI-A iter-1..3 | non-Western cosmogonies; theological accounts of schism |

## Cross-field observations (x3)
- A fourth structure appears alongside branching, separation and differentiation: **spread of a population of units on a measured scale** (between-group variance share: Fst in genetics, CFst for culture and religion, P15; SD of country means, P11). PL-06 records that CFst is adapted from genetic Fst.
- Several fields measure divergence with tree methods borrowed from biology (texts, P13; languages, P12/P06; religions, P14), and all report the same caveat: horizontal transfer (contamination, borrowing, diffusion) makes histories non-tree-like.
- Divergence and convergence co-occur at different scales (P11: global divergence with regional convergence). This bears on README §12 Q4 (fixed sequence vs recurring states) but does not settle it.

## Updates in x6 (DVB)
| field | newly sourced or newly checked senses | sources / runs | still unsourced |
|---|---|---|---|
| Natural sciences | genome-wide divergence between incipient species despite gene flow; divergence decaying within 1-2 cM of selected loci; linkage 'island' toy | P01 (re-read in full), P02 (re-read); SIM-DV-NAT-B iter-1..6 | genomic islands beyond P01; physical bifurcation |
| Formal sciences | statistical divergence (KL) now sourced, incl. its likelihood reading; divergence without chaos (x -> 1.1x); stretching with folding; operator vs trajectory divergence (Lorenz) | P16 (arXiv, read in full), P09 (re-read); SIM-DV-FOR-B iter-1..6 | divergent series; divergence operator (no source) |
| Social sciences | dispersion vs slope measures of divergence/convergence (statistical caution); noise-maintained dispersion | SIM-DV-SOC-B iter-1..6 (no new source) | economic convergence clubs |
| Applied sciences | numerical divergence (solver instability, O(h) error) now sourced; divergent vs convergent vs parallel tumour evolution | P17 (LibreTexts, read in full), P04/P05 (re-read); SIM-DV-APP-B iter-1..6 | design-process divergence |
| Humanities | scoped Andic result (4 of 6 classifications); measurement precision vs geographic fit; small-family test power | P06 (re-read); SIM-DV-HUM-B iter-1..6 | artistic divergence |
| Philosophy / spirituality | procession paired with reversion (Plotinus); two-way unity/multiplicity movement (Bergson); Daoist differentiation from unity to multiplicity with reversal (first non-Western source) | P07, P08 (re-read), P18 (SEP Laozi, cited passages); SIM-DV-PHI-B iter-1..6 | full read of P18; other non-Western traditions |

## Cross-field observations (x6)
- **Divergence is often paired with a counter-movement**: stretching with folding (P09), procession with reversion (P07), unity-to-multiplicity with contraction (P08), differentiation with reversal (P18), island divergence with recombination (P01 / linkage toy), branching with merging (split-merge toy). In the formal and natural cases this pairing is measured; in the philosophical cases it is a framework reading (DVB-PHI-19; link PL-12 is Hypothetical).
- **Positive divergence rate is not enough to characterise a system**: x -> 1.1x diverges without chaos (P09), forward Euler diverges by method choice (P17), and phase volumes can contract while trajectories diverge (Lorenz). Field definitions should state what is diverging (states, trajectories, distributions, populations, lineages).
- **Measurement caution generalises**: slopes vs dispersion (SOC toy), classification precision vs geographic fit (P06), small-sample power (HUM toy), sampling resolution (P05).
