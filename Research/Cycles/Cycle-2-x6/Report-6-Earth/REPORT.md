# Report 6 — Earth: the living planet and its core

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-2-X6-R6 |
| Version | Cycle 2 (x6) |
| Status | Researched (6 passes), simulated (6 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-1-x3/Report-6-Earth/REPORT.md` (Cycle 1) and `../../Cycle-0-Baseline/` |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule (Report 7) |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 2 matches the Cycle-1 adaptive-Daisyworld toy to the published literature. Lenton & Lovelock (2001, full text) summarise that adaptation to prevailing conditions undermines regulation (Robertson & Robinson 1998) and that bounds on adaptation with growth limitation near the bounds recover it (Lenton & Lovelock 2000) (W01–W03, E; W02/W03 abstract only). Daisyworld still exists only as a computational construct; a synthetic microbial implementation has been proposed (W14, E). Six iterations reproduce the Cycle-1 result exactly and extend it: unconstrained adaptation shrank the regulated band below 0.8× at every positive rate (0.08–0.35 vs 0.82, **supported**); bounded, costed adaptation largely recovered it (0.62–0.82), but 'every setting ≥ 0.8×' was **not supported** because the growth cost itself narrows the band; across 9 death-rate × heat-transfer settings constrained adaptation kept ≥ 0.8× in 100% and unbounded in 0%. Two expectations failed: slower adaptation was *worse* (rate 0.0003 gave 0.08; Spearman −0.39, **not supported**), and more albedo types with mutation did not extend regulation (0.78 vs 0.82, **not supported**; a non-reproduction of W01's statement citing Stocker 1995, which was not read).

## What changed in Cycle 2
Pass 1 ran logged Europe PMC and OpenAlex searches for Daisyworld adaptation. Pass 2 read W01 in full and W02/W03 as abstracts. Pass 3 widened to Gaia/Earth-system regulation and selected W14. Pass 4 (challenge) searched Gaia critiques (broad and title-restricted); no new source beyond the Cycle-0/1 critiques was selected, and the challenge was carried by the simulations (two not-supported results). Pass 5 executed the carried item. Pass 6 filled seven empty limits fields and re-assessed labels (none changed).

Ledger: 34 claims (20 E, 11 P, 3 PS, 0 H); 6 new; 7 carried claims had their empty limits field filled; 1 carried claims annotated with Cycle-2 evidence; no carried claim changed label or status (each row's `c2_change` says which).

## Methods
Six successive research passes (1 logged systematic search → 2 deepen → 3 widen → 4 challenge → 5 carried agenda item → 6 consolidation; notes in `research/pass-1..6/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and six chained simulation iterations (`simulation/iter-1..6`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded).

## Evidence and findings
- **Literature match (E; C2-R6-01) and design (P; C2-R6-02).**
- **No physical Daisyworld (E; C2-R6-03).**
- **Adaptation vs regulation (E, simulation; C2-R6-04, C2-R6-05, C2-R6-06)** with three not-supported outcomes reported as findings.
- C1-R6-08 is now matched to the literature and replicated.

## Competing views and counter-evidence
Strong Gaia (regulation *for* life) vs weak coupling views; Daisyworld results depend on constraints on adaptation, which supports critics' point that regulation is not automatic. Earth-core claims (Part B) are unchanged.

## Simulation (6 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Replicate the Cycle-1 toy exactly, then test the Robertson & Robinson 1998 (W02) design claim over a finer grid of adaptation rates: unconstrained adaptation of optimum temperature erodes regulation. | R0: Pass, U1: Supported | 1/1 | 1/1 |
| 2 | Test the Lenton & Lovelock 2000 (W03) / 2001 (W01 sec. 6.3) design claim: bounds on adaptation plus growth limitation near the bounds recover regulation. | LL1: Not supported, LL2: Supported | 0/0 | 1/2 |
| 3 | Test the W03 verbal argument that adaptation fast relative to environmental change removes the need for (and the fact of) regulation, by varying forcing speed (steps per luminosity increment) against adaptation rate. | RR1: Not supported | 0/0 | 0/1 |
| 4 | A second, band-independent regulation metric: damping ratio = mean \|dTe/dL\| lifeless / with life inside the habitable band. | DM0: Pass, DM1: Reported | 1/1 | 0/0 |
| 5 | Test W01's statement (citing Stocker 1995, not read) that mutation of the trait extends regulation: k albedo types with neighbour mutation. | M0: Pass, M1: Not supported | 1/1 | 0/1 |
| 6 | Consolidation: do the iteration 1-2 conclusions (unbounded erodes, constrained recovers) hold across death rate gamma and heat-transfer q? | RB1: Supported, RB2: Supported | 0/0 | 2/2 |

Iterations: (1) exact replication plus rate grid; (2) bounds plus growth cost; (3) forcing speed vs adaptation rate; (4) a band-independent damping ratio (none 2.95, unbounded 0.94, constrained 2.67); (5) multiple albedo types with mutation; (6) death-rate × heat-transfer grid.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-2 change |
|---|---|---|---|---|---|
| C0v2-R6-01 | P | Indeterminate | Part A: the rock record indicates a microbial biosphere by at least 3.4 billion years ago; earlier claims are disputed because abiotic processes and contamination can mimic biosignatures. | S23;V08 | Carried unchanged. |
| C0v2-R6-02 | E | Supported | Part A: an estimate from higher-taxonomy patterns predicts ~8.7 million (± 1.3 million SE) eukaryotic species, about 86% still undescribed. | V02;U30 | Carried unchanged. |
| C0v2-R6-03 | E | Supported | Part A: IPBES estimates around 1 million animal and plant species are threatened with extinction, many within decades, absent action. | S24 | Carried unchanged. |
| C0v2-R6-04 | P | Indeterminate | Part A (interdependence): nearly all non-equilibrium electron transfers on Earth are driven by microbial nanomachines whose conserved core genes co-evolved with biogeochemical cycles and spread mainly by horizontal gene transfer. | T13 | Carried unchanged. |
| C0v2-R6-05 | E | Supported | Part A (humans within Earth systems): the planetary-boundaries framework identifies climate change and biosphere integrity as 'core boundaries'; its 2023 update finds six of the nine boundaries transgressed. | V03;U31 | Carried unchanged. |
| C0v2-R6-06 | E | Supported | Part A: Daisyworld shows that a coupled biota–temperature model with a peaked growth curve stabilises temperature; it was offered as a parable, not a model of Earth. | S21b | Counterevidence/limits field filled in Cycle 2 (was empty). Limits field filled; adaptive-Daisyworld literature added (C2-R6-01 to C2-R6-03). |
| C0v2-R6-07 | E | Supported | In SIM-R6-C0, re-implemented Daisyworld kept temperature within 22.5 ± 10 °C over luminosity 0.72–1.54 (width 0.82) vs 0.83–1.07 (0.24) without life, with hysteresis between up and down sweeps. | C0:SIM-R6-C0#E1;C0:SIM-R6-C0#E2;S21b | Carried unchanged. |
| C0v2-R6-08 | P | Contested | Part A: Kirchner argues the best available data suggest biologically mediated feedbacks will on net amplify, not reduce, Earth's sensitivity to anthropogenic climate change, contrary to strong homeostatic Gaia. | S22 | Carried unchanged. |
| C0v2-R6-09 | PS | Interpretive | Part A (philosophy): Leopold's land ethic ('land is a community'; right is what preserves the integrity, stability and beauty of the biotic community) and deep ecology extend moral concern to the living whole. | U32 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R6-10 | PS | Interpretive | Part A: calling life the 'soul of the Earth' is a metaphor; no evidence in this pass shows Earth to be conscious or ensouled. | S22;G03 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R6-11 | E | Supported | Part B: the core is a solid inner core within a fluid, convecting outer core; the inner core grows ~1 mm/yr as outer-core material freezes onto it, helping drive outer-core convection. | S25 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R6-12 | E | Supported | Part B: the outer-core radius is ~3480 km and inner-core radius ~1220 km; Lehmann inferred the inner core in 1936 from earthquake waves. | S25;S26 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R6-13 | E | Supported | Part B (heat transfer): Earth acts as a heat engine driven by radiogenic decay and slow cooling; the geodynamo runs on heat from cooling and inner-core freezing and on chemical convection, with core–mantle-boundary heat flux measuring its power supply. | V09;S29 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C0v2-R6-14 | P | Contested | Part B: first-principles calculations gave core thermal and electrical conductivities 2–3 times higher than earlier estimates (V09), but a direct laser-heated diamond-anvil measurement placed core thermal conductivity near the low end of previous estimates, at 18–44 W/m/K (V30); the dispute is unresolved in the sources read. | V09;V30;S29 | Carried unchanged. |
| C0v2-R6-15 | E | Supported | Part B (planetary dynamics): most plate movement occurs along narrow plate-boundary zones; four boundary types are recognised. | U34 | Carried unchanged. |
| C0v2-R6-16 | P | Mixed | Part B: mantle convection is the commonly assumed driver of plate motion, but the driving mechanism remains among the 'unanswered questions'. | U35 | Carried unchanged. |
| C0v2-R6-17 | E | Supported | Part B (magnetic field): IGRF-14 dipole moment fell from 8.32×10²² (1900) to 7.69×10²² A·m² (2025), −7.6%; free ohmic decay time is ~2.4–7.3×10⁴ yr for σ = 0.5–1.5×10⁶ S/m (assumed), far shorter than the paleomagnetic record — consistent with continual regeneration. | C0:SIM-R6-C0#E3;C0:SIM-R6-C0#E4;S27;S25 | Carried unchanged. |
| C0v2-R6-18 | P | Contested | Part B: zircon paleointensities have been read as a geodynamo by 4.2 Ga, but a later combined study found most Jack Hills zircons poor recorders, so a geodynamo before 3.5 Ga 'remains unknown'. | S28;T12;V38;V29 | Carried unchanged. |
| C0v2-R6-19 | PS | Interpretive | Part B (symbol): traditions locate vitality or mind at the heart (Stoic hêgemonikon at the heart; Chinese xin 'heart-mind'); the core is physically central to heat flow and the geodynamo, but calling it Earth's 'heart' is metaphor — no evidence of consciousness or a literal soul. | S07;T17;S29;G03 | Counterevidence/limits field filled in Cycle 2 (was empty). |
| C1-R6-01 | P | Mixed | Lenton et al. introduce 'tipping elements': large-scale components of the Earth system that may pass a tipping point, at which a small perturbation can qualitatively alter the system's state. | V22 | Carried unchanged. |
| C1-R6-02 | E | Supported | Model estimates place the Solar System's habitable zone between 0.99 AU (inner, water-loss limit) and 1.70 AU (outer, maximum-greenhouse limit), so Earth lies near the inner edge. | V26 | Carried unchanged. |
| C1-R6-03 | P | Mixed | A seismic study of multiply reverberating waves reports a distinctly anisotropic innermost inner core with a transition to a weakly anisotropic outer shell, possibly a fossilized record of a past global event. | V27 | Carried unchanged. |
| C1-R6-04 | P | Contested | Inner-core age is contested: a palaeointensity increase between 1 and 1.5 billion years ago has been read as inner-core nucleation (abstract), Late Cambrian geomagnetic instability has been placed after the onset of nucleation, and molecular-dynamics work finds an Fe1-xCx (x = 0.1-0.15) composition compatible with the supercooling required for nucleation. | V38;V29;V28 | Carried unchanged. |
| C1-R6-05 | P | Contested | Gaia critiques (challenge pass): Boyle argues a testable Gaia hypothesis must invoke an entity that is planetary in scale, habitability-promoting and life-specific, requiring a resolution of the 'Darwinization problem'; Hermida & Okasha conclude Darwinized Gaia still cannot overcome the main objections from evolutionary biology; Doolittle argues Gaia has 'too many parents' to undergo natural selection; Lenton et al. propose 'sequential selection' for global regulation (abstract). | V23;V24;V25;V39 | Carried unchanged. |
| C1-R6-06 | E | Supported | Virtually all of Earth's ecosystems and biogeochemical cycles are underpinned, and often driven, by the activity or inactivity of microorganisms; microbial dormancy acts as an ecological and biogeochemical regulator. | V32 | Carried unchanged. |
| C1-R6-07 | E | Supported | In SIM-R6-C1 iteration 1, Daisyworld regulation (habitable band >= 2x the lifeless band) was not supported as robust: it held in 63% of 27 death-rate x heat-transfer x albedo settings and failed in all settings with small albedo contrast (0.45/0.55). | SIM-R6-C1/iter-1#D0;SIM-R6-C1/iter-1#D1;SIM-R6-C1/iter-1#D2 | Carried unchanged. |
| C1-R6-08 | E | Supported | In SIM-R6-C1 iteration 2 (our own toy), regulation was not supported under unbounded adaptation: when daisies' optimum temperatures tracked local temperature, the regulated band shrank from 0.82 to 0.19-0.35 as optima drifted to 46-93 °C; with adaptation bounded to ±5 °C the band stayed >= 0.93. | SIM-R6-C1/iter-2#A0;SIM-R6-C1/iter-2#A1;SIM-R6-C1/iter-2#A_bounded_5;SIM-R6-C1/iter-2#A2 | Now matched to the published literature (C2-R6-01; W01 full text) and replicated on a finer rate grid (C2-R6-04). |
| C1-R6-09 | E | Supported | In SIM-R6-C1 iteration 3, the IGRF-14 spectrum was steep at Earth's surface (log10 slope -0.51 to -0.57 per degree, n = 2-10) and near-flat when continued to the core-mantle boundary (-0.04 to +0.02) in 1900, 1950, 2000 and 2025; free-decay times were 4.9·10^3-9.8·10^4 yr over 1·10^5-2·10^6 S/m, and 7·10^3-2.2·10^4 yr for V30's 18-44 W/m/K converted by Wiedemann–Franz at assumed 4000-5000 K, all far shorter than a 3.3-Gyr field record. | SIM-R6-C1/iter-3#G0;SIM-R6-C1/iter-3#G1;SIM-R6-C1/iter-3#G2;S27 | Carried unchanged. |
| C2-R6-01 | E | Supported | Lenton & Lovelock (2001) summarise that adaptation to prevailing conditions undermines Daisyworld's environmental regulation (Robertson & Robinson 1998), but that when bounds on the range of adaptation are added and peak growth rate is limited as the bounds are approached, temperature regulation is recovered (Lenton & Lovelock 2000). | W01;W02;W03 | New in Cycle 2. |
| C2-R6-02 | P | Supported | Robertson & Robinson (1998) let daisies shift their optimal growth temperatures toward the prevailing temperature and suggest a trade-off between organisms' ability to collectively regulate the environment and evolving genotypes' ability to adapt to it. | W02 | New in Cycle 2. |
| C2-R6-03 | E | Supported | As of 2024, Daisyworld 'exists only as a mathematical or computational construct'; Maull et al. propose a synthetic microbial implementation (engineered two-strain consortia with pH as the abiotic control parameter) with theoretical case studies. | W14 | New in Cycle 2. |
| C2-R6-04 | E | Supported | SIM-R6-C2 reproduced the Cycle-1 adaptive-Daisyworld result exactly and extended it: unconstrained adaptation shrank the regulated band below 0.8x the non-adapting width at every positive rate tested (0.08-0.35 vs 0.82); bounded, costed adaptation largely recovered it (0.62-0.82, so 'every setting >= 0.8x' was not supported because the growth cost itself narrows the band); across 9 death-rate x heat-transfer settings constrained adaptation kept >= 0.8x in 100% and unbounded in 0%. | SIM-R6-C2/iter-1#R0;SIM-R6-C2/iter-1#U1;SIM-R6-C2/iter-2#LL1;SIM-R6-C2/iter-2#LL2;SIM-R6-C2/iter-6#RB1;SIM-R6-C2/iter-6#RB2 | New in Cycle 2. |
| C2-R6-05 | E | Supported | In SIM-R6-C2, the slowest adaptation rate tested (0.0003) eroded regulation most (band 0.08), so the hypothesis that faster adaptation relative to forcing gives weaker regulation was not supported (Spearman -0.39); a band-independent damping ratio confirmed the pattern (none 2.95, unbounded 0.94, constrained 2.67). | SIM-R6-C2/iter-1#U1;SIM-R6-C2/iter-3#RR1;SIM-R6-C2/iter-4#DM0;SIM-R6-C2/iter-4#DM1 | New in Cycle 2. |
| C2-R6-06 | E | Supported | In SIM-R6-C2 iteration 5, more albedo types with neighbour mutation did not extend the regulated range in our implementation (0.78 vs 0.82 for two types; not supported), so W01's statement citing Stocker 1995 was not reproduced by this toy. | SIM-R6-C2/iter-5#M0;SIM-R6-C2/iter-5#M1 | New in Cycle 2. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-2 status |
|---|---|---|---|---|
| L01 | R1 Body → R6 Earth | relationship | P | Retained as analogy only. The body and Daisyworld toys share the adaptation-vs-regulation pattern (PA1), partly by design; the trade-off is a published Daisyworld result (W01-W03). |
| L02 | R1 Body → R6 Earth | distinction | P | Unchanged in substance; Cycle-2 literature adds that Daisyworld regulation depends on constraints on adaptation. |
| L03 | R1 Body → R6 Earth | humans within Earth | E | Unchanged in Cycle 2. |
| L13 | R3 Soul → R6 Earth | relationship | E | Retained. Note: counts of conceptions come from a coding with re-coding kappa 0.79 and 56% source-silent cells (C2-R3-01, C2-R3-02). |
| L19 | R6 Earth → R6 Earth | dependency | E | Unchanged in Cycle 2. |
| L20 | R6 Earth → R6 Earth | feedback loop | P | Unchanged label; Daisyworld still has no biological implementation (C2-R6-03). |
| L21 | R6 Earth → R6 Earth | competing interpretation | P | Strong-Gaia side under continued pressure: regulation depends on constraints on adaptation (literature and toy); our toy did not reproduce the rate dependence or the mutation benefit. |
| L22 | R6 Earth → R7 Unified | humans within Earth | E | Unchanged in Cycle 2. |
| L23 | R6 Earth → R3 Soul | competing interpretation | PS | Unchanged in Cycle 2. |

## Limitations
Re-implementation from verbal descriptions, not the published equations; iteration 3 confounds forcing speed with equilibration time (noted in SPEC); Stocker 1995 was not read.

## Open questions and falsification
Would the published equations of Lenton & Lovelock 2000 change the cost-narrowing result? Falsification: a constrained-adaptation model that fails to regulate across the 9-setting grid would undercut C2-R6-04.

## Conclusion and gate
Report 6's adaptive-Daisyworld result is now matched to the literature and stress-tested. Gate: **Indeterminate**.

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S07** — Lorenz H. Ancient Theories of Soul. Stanford Encyclopedia of Philosophy (rev. 2024). [full text] <https://plato.stanford.edu/entries/ancient-soul/>
- **S21b** — Watson AJ, Lovelock JE (1983). Biological homeostasis of the global environment: the parable of Daisyworld. Tellus 35B:284-289. [full text (Tellus B PDF)] <https://b.tellusjournals.se/articles/1857/files/submission/proof/1857-1-15588-1-10-20221123.pdf>
- **S22** — Kirchner JW (2003). The Gaia Hypothesis: Conjectures and Refutations. Climatic Change 58:21-45. doi:10.1023/A:1023494111532 [full text (Harvard course PDF)] <https://courses.seas.harvard.edu/climate/eli/Courses/EPS281r/Sources/Gaia/more/Kirchner-2003.pdf>
- **S23** — Javaux EJ (2019). Challenges in evidencing the earliest traces of life. Nature 572:451-460. doi:10.1038/s41586-019-1436-4 [abstract only (NCBI E-utilities PMID 31435057)] <https://pubmed.ncbi.nlm.nih.gov/31435057/>
- **S24** — IPBES (2019). Global Assessment Report on Biodiversity and Ecosystem Services: Summary for Policymakers. [full text PDF] <https://files.ipbes.net/ipbes-web-prod-public-files/ipbes_global_assessment_report_summary_for_policymakers.pdf>
- **S25** — Waszek L, Irving J, Pham T-S, Tkalcic H (2023). Seismic insights into Earth's core. Nat Commun. doi:10.1038/s41467-023-41725-5 [full text] <https://www.nature.com/articles/s41467-023-41725-5>
- **S26** — Boatman L (2023). September 1936: Seismologist Inge Lehmann Concludes That Earth Has an Inner Core. APS News. [full text] <https://www.aps.org/apsnews/2023/08/seismologist-lehmann-earth-inner-core>
- **S27** — IAGA Working Group V-MOD / NOAA NCEI. IGRF-14 coefficient file igrf14coeffs.txt. [full text (official data file)] <https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/igrf14coeffs.txt>
- **S28** — Tarduno JA, Cottrell RD, Davis WJ, Nimmo F, Bono RK (2015). A Hadean to Paleoarchean geodynamo recorded by single zircon crystals. Science 349:521-524. doi:10.1126/science.aaa9114 [abstract only (NCBI E-utilities PMID 26228145)] <https://pubmed.ncbi.nlm.nih.gov/26228145/>
- **S29** — Pozzo M, Davies C, Gubbins D, Alfe D (2012). Thermal and electrical conductivity of iron at Earth's core conditions. Nature 485:355-358 (arXiv:1203.4970). [abstract only (arXiv)] <https://arxiv.org/abs/1203.4970>
- **T12** — Borlina CS, Weiss BP, Lima EA, et al. (2020). Reevaluating the evidence for a Hadean-Eoarchean dynamo. Sci Adv 6(15):eaav9634. doi:10.1126/sciadv.aav9634 [abstract only (NCBI E-utilities PMID 32284988)] <https://pubmed.ncbi.nlm.nih.gov/32284988/>
- **T13** — Falkowski PG, Fenchel T, Delong EF (2008). The microbial engines that drive Earth's biogeochemical cycles. Science 320(5879):1034-1039. doi:10.1126/science.1153213 [abstract only (NCBI E-utilities PMID 18497287)] <https://pubmed.ncbi.nlm.nih.gov/18497287/>
- **T17** — Wong D. Chinese Philosophy of Mind (xin). Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/chinese-mind/>
- **U30** — Mora C, Tittensor DP, Adl S, Simpson AG, Worm B (2011). How many species are there on Earth and in the ocean? PLoS Biol 9(8):e1001127. doi:10.1371/journal.pbio.1001127 [abstract only (NCBI E-utilities PMID 21886479)] <https://pubmed.ncbi.nlm.nih.gov/21886479/>
- **U31** — Steffen W, Richardson K, Rockstrom J, et al. (2015). Planetary boundaries: guiding human development on a changing planet. Science 347(6223):1259855. doi:10.1126/science.1259855 [abstract only (NCBI E-utilities PMID 25592418)] <https://pubmed.ncbi.nlm.nih.gov/25592418/>
- **U32** — Brennan A, Lo NYS. Environmental Ethics. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/ethics-environmental/>
- **U34** — Kious WJ, Tilling RI (1996). This Dynamic Earth: The Story of Plate Tectonics — Understanding plate motions. USGS. [full text] <https://pubs.usgs.gov/gip/dynamic/understanding.html>
- **U35** — Kious WJ, Tilling RI (1996). This Dynamic Earth — Some unanswered questions. USGS. [full text] <https://pubs.usgs.gov/gip/dynamic/unanswered.html>
- **V02** — Mora C, Tittensor DP, Adl S, Simpson AGB, Worm B (2011). How many species are there on Earth and in the ocean? PLoS Biol 9(8):e1001127. doi:10.1371/journal.pbio.1001127 [full text (Europe PMC PMC3160336)] <https://europepmc.org/article/PMC/PMC3160336>
- **V03** — Richardson K, et al. (2023). Earth beyond six of nine planetary boundaries. Sci Adv 9:eadh2458. doi:10.1126/sciadv.adh2458 [full text (Europe PMC PMC10499318)] <https://europepmc.org/article/PMC/PMC10499318>
- **V08** — Schopf JW, Kitajima K, Spicuzza MJ, Kudryavtsev AB, Valley JW (2018). SIMS analyses of the oldest known assemblage of microfossils document their taxon-correlated carbon isotope compositions. PNAS 115(1):53-58. doi:10.1073/pnas.1718063115 [abstract only (NCBI E-utilities; full text not obtained: Europe PMC HTTP 500, publisher PDF HTTP 403)] <https://pubmed.ncbi.nlm.nih.gov/?term=10.1073%2Fpnas.1718063115>
- **V09** — Pozzo M, Davies C, Gubbins D, Alfè D (2012). Thermal and electrical conductivity of iron at Earth's core conditions. Nature 485:355-358. arXiv:1203.4970 (preprint full text) [full text (arXiv preprint PDF)] <https://arxiv.org/abs/1203.4970>
- **V22** — Lenton TM, Held H, Kriegler E, Hall JW, Lucht W, Rahmstorf S, Schellnhuber HJ (2008). Tipping elements in the Earth's climate system. PNAS 105(6):1786-1793. doi:10.1073/pnas.0705414105 [abstract only (NCBI E-utilities; full text not obtained: Europe PMC HTTP 500, publisher PDF HTTP 403)] <https://doi.org/10.1073/pnas.0705414105>
- **V23** — Boyle RA (2025). Overlapping attempts to falsify and Darwinize the Gaia hypothesis. Phil Trans R Soc B. doi:10.1098/rstb.2024.0087 [full text (Europe PMC PMC12329434)] <https://europepmc.org/article/PMC/PMC12329434>
- **V24** — Hermida M, Okasha S (2025). Function, chance and purpose in the biosphere: a critical examination of the Darwinized Gaia hypothesis. Phil Trans R Soc B. doi:10.1098/rstb.2024.0099 [full text (Europe PMC PMC12329436)] <https://europepmc.org/article/PMC/PMC12329436>
- **V25** — Doolittle WF (2025). Darwinizing Gaia: conceptual approaches. Phil Trans R Soc B. doi:10.1098/rstb.2024.0089 [full text (Europe PMC PMC12329432)] <https://europepmc.org/article/PMC/PMC12329432>
- **V26** — Kopparapu RK, et al. (2013). Habitable zones around main-sequence stars: new estimates. Astrophys J 765:131. arXiv:1301.6674 (preprint full text) [full text (arXiv preprint PDF)] <https://arxiv.org/abs/1301.6674>
- **V27** — Phạm T-S, Tkalčić H (2023). Up-to-fivefold reverberating waves through the Earth's center and distinctly anisotropic innermost inner core. Nat Commun 14. doi:10.1038/s41467-023-36074-2 [full text (Europe PMC PMC9944935)] <https://europepmc.org/article/PMC/PMC9944935>
- **V28** — Wilson AJ, Davies CJ, Walker AM, Alfè D (2025). Constraining Earth's core composition from inner core nucleation. Nat Commun. doi:10.1038/s41467-025-62841-4 [full text (Europe PMC PMC12411617)] <https://europepmc.org/article/PMC/PMC12411617>
- **V29** — Li Y-X, Tarduno JA, et al. (2023). Late Cambrian geomagnetic instability after the onset of inner core nucleation. Nat Commun 14. doi:10.1038/s41467-023-40309-7 [full text (Europe PMC PMC10390560)] <https://europepmc.org/article/PMC/PMC10390560>
- **V30** — Konôpková Z, McWilliams RS, Gómez-Pérez N, Goncharov AF (2016). Direct measurement of thermal conductivity in solid iron at planetary core conditions. Nature 534:99-101. doi:10.1038/nature18009 [abstract only (NCBI E-utilities)] <https://doi.org/10.1038/nature18009>
- **V32** — Bradley JA, et al. (2025). Microbial dormancy as an ecological and biogeochemical regulator on Earth. Nat Commun. doi:10.1038/s41467-025-59167-6 [full text (Europe PMC PMC12032139)] <https://europepmc.org/article/PMC/PMC12032139>
- **V38** — Biggin AJ, et al. (2015). Palaeomagnetic field intensity variations suggest Mesoproterozoic inner-core nucleation. Nature 526:245-248. doi:10.1038/nature15523 [abstract only (NCBI E-utilities)] <https://doi.org/10.1038/nature15523>
- **V39** — Lenton TM, Daines SJ, Dyke JG, Nicholson AE, Wilkinson DM, Williams HTP (2018). Selection for Gaia across multiple scales. Trends Ecol Evol 33(8):633-645. doi:10.1016/j.tree.2018.05.006 [abstract only (NCBI E-utilities)] <https://doi.org/10.1016/j.tree.2018.05.006>
- **W01** — Lenton TM, Lovelock JE (2001). Daisyworld revisited: quantifying biological effects on planetary self-regulation. Tellus B 53:288-305. doi:10.3402/tellusb.v53i3.16597 [full text (publisher OA PDF via OpenAlex best_oa_location)] <https://doi.org/10.3402/tellusb.v53i3.16597>
- **W02** — Robertson D, Robinson J (1998). Darwinian Daisyworld. Journal of theoretical biology 195:129-134. doi:10.1006/jtbi.1998.0799 [Europe PMC lists the first author as 'Roberston'; corrected spelling used] [abstract only (Europe PMC; not open access)] <https://doi.org/10.1006/jtbi.1998.0799>
- **W03** — Lenton TM, Lovelock JE (2000). Daisyworld is Darwinian: constraints on adaptation are important for planetary self-regulation. Journal of theoretical biology 206:109-114. doi:10.1006/jtbi.2000.2105 [abstract only (Europe PMC; not open access)] <https://doi.org/10.1006/jtbi.2000.2105>
- **W14** — Maull V, Pla Mauri J, Conde Pueyo N, Solé R (2024). A synthetic microbial Daisyworld: planetary regulation in the test tube. Journal of the Royal Society, Interface 21:20230585. doi:10.1098/rsif.2023.0585 [full text (Europe PMC PMC10847846)] <https://europepmc.org/article/PMC/PMC10847846>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6) (2026-10-24): this version; details in `CHANGELOG.md`.
