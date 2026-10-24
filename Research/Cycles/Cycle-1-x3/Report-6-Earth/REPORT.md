# Report 6 — Earth: life systems (Part A) and core, heat and magnetic field (Part B)

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-1-X3-R6 |
| Version | Cycle 1 (x3) |
| Status | Researched (3 passes), simulated (3 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-0-Baseline/Report-6-Earth/REPORT.md` (Baseline v2) |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Cycle-1 access rule | Established literature claims need at least one full-text (or textbook) source; abstract-only claims are capped at Plausible |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Part A: species richness and the planetary-boundaries claims are now full text (six of nine boundaries transgressed; climate and biosphere integrity as core boundaries), microbes are shown (full text) to underpin virtually all ecosystems and biogeochemical cycles, and two abstract-only claims (life ≥ 3.4 Ga; microbial nanomachines co-evolving with cycles) are downgraded to Plausible. The Gaia hypothesis is challenged by four recent critiques (Darwinization problem; 'too many parents'; objections from evolutionary biology), and our Daisyworld tests agree that regulation is fragile: it holds in only 63% of parameter settings and collapses when daisies adapt without bound. Part B: the heat-engine claim is full text; the core-conductivity dispute is now two-sided (2–3x higher by calculation vs 18–44 W/m/K by measurement); inner-core age is contested; the innermost inner core appears distinctly anisotropic. The IGRF spectrum is near-flat at the core–mantle boundary, and free-decay times stay below 10^5 yr across the whole disputed conductivity range, so the field must be regenerated.

## What changed in Cycle 1
Pass 1: C0v2-R6-02 → V02, -05 → V03, -13 → V09 (full text); -01 and -04 downgraded. Pass 2: V22, V26, V27, V28, V29, V32, V38. Pass 3: V30 vs V09 (conductivity), V23–V25 and V39 (Gaia critiques).

Ledger: 28 claims (15 E, 10 P, 3 PS, 0 H); 9 new, 7 revised; the rest carried forward unchanged from Cycle 0 (each row's `c1_change` says which).

## Methods
Three successive research passes (consolidate → widen → challenge; notes in `research/pass-1..3/NOTES.md`) and three chained simulation iterations (`simulation/iter-1..3`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iterations 2 and 3 read the previous iteration's results). Sources were fetched directly, snapshotted, hashed (`../Provenance/SOURCE_REGISTER.csv`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass), *hypothesis* (substantive; Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded).

## Evidence and findings
**Part A.** Biodiversity estimates (C0v2-R6-02/03), planetary boundaries (C0v2-R6-05), microbial underpinning of cycles (C1-R6-06), habitable-zone limits 0.99–1.70 AU (C1-R6-02) — Established. Early life ≥ 3.4 Ga and co-evolution of microbial engines with cycles — Plausible (abstract-only). Tipping elements (C1-R6-01) — Plausible. Gaia's regulatory claim — Plausible/Contested (C0v2-R6-08, C1-R6-05), with toy results against robustness (C1-R6-07/08).

**Part B.** Core structure and the heat engine (C0v2-R6-11..13) — Established. Conductivity (C0v2-R6-14), inner-core age (C1-R6-04), innermost-inner-core anisotropy (C1-R6-03), early dynamo (C0v2-R6-18) — Plausible/Contested. Spectrum and free-decay computations (C1-R6-09) — Established as computations.

**Symbol.** 'Life as Earth's soul' and 'the core as its heart' remain metaphors (C0v2-R6-10/19, Philosophical/Spiritual).

## Competing views and counter-evidence
Strong Gaia (homeostatic regulation) vs coevolution without regulation vs 'sequential selection'. High vs low core conductivity, with consequences for inner-core age and the energy available to the early dynamo.

## Simulation (3 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Is Daisyworld regulation robust to death rate, heat-transfer parameter q and albedo contrast? | D0: Pass, D1: Not supported, D2: Reported | 1/1 | 0/1 |
| 2 | Toy test related to the Darwinization critique (V23-V25, V39): if daisies adapt their optimum temperature to local conditions, does planetary regulation survive? Unbounded and bounded adaptation. | A0: Pass, A1: Not supported, A_bounded_5: Supported, A_bounded_10: Supported, A2: Reported | 1/1 | 2/3 |
| 3 | Geomagnetic spectrum (Lowes-Mauersberger) at Earth's surface and downward-continued to the core-mantle boundary for four epochs; free-decay time across the disputed conductivity range (V09 high vs V30 low, converted with Wiedemann-Franz). | G0: Pass, G1: Supported, G2: Supported | 1/1 | 2/2 |

Iteration 1 (sensitivity) and iteration 2 (adaptation, our own toy design) each produced a 'not supported' hypothesis; iteration 3 (geomagnetism) supported both. Bounded adaptation (±5 °C) preserved regulation, so the toy locates the question: what limits adaptation at planetary scale?

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-1 change |
|---|---|---|---|---|---|
| C0v2-R6-01 | P | Indeterminate | Part A: the rock record indicates a microbial biosphere by at least 3.4 billion years ago; earlier claims are disputed because abiotic processes and contamination can mimic biosignatures. | S23;V08 | Downgraded Established -> Plausible (abstract-only); V08 added. |
| C0v2-R6-02 | E | Supported | Part A: an estimate from higher-taxonomy patterns predicts ~8.7 million (± 1.3 million SE) eukaryotic species, about 86% still undescribed. | V02;U30 | Upgraded to full text V02. |
| C0v2-R6-03 | E | Supported | Part A: IPBES estimates around 1 million animal and plant species are threatened with extinction, many within decades, absent action. | S24 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-04 | P | Indeterminate | Part A (interdependence): nearly all non-equilibrium electron transfers on Earth are driven by microbial nanomachines whose conserved core genes co-evolved with biogeochemical cycles and spread mainly by horizontal gene transfer. | T13 | Downgraded Established -> Plausible (abstract-only). |
| C0v2-R6-05 | E | Supported | Part A (humans within Earth systems): the planetary-boundaries framework identifies climate change and biosphere integrity as 'core boundaries'; its 2023 update finds six of the nine boundaries transgressed. | V03;U31 | Upgraded to full text V03 (Richardson 2023); wording updated. |
| C0v2-R6-06 | E | Supported | Part A: Daisyworld shows that a coupled biota–temperature model with a peaked growth curve stabilises temperature; it was offered as a parable, not a model of Earth. | S21b | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-07 | E | Supported | In SIM-R6-C0, re-implemented Daisyworld kept temperature within 22.5 ± 10 °C over luminosity 0.72–1.54 (width 0.82) vs 0.83–1.07 (0.24) without life, with hysteresis between up and down sweeps. | C0:SIM-R6-C0#E1;C0:SIM-R6-C0#E2;S21b | Carried forward (Cycle-0 run). Robustness re-tested in C1-R6-07/08: regulation is parameter-dependent. |
| C0v2-R6-08 | P | Contested | Part A: Kirchner argues the best available data suggest biologically mediated feedbacks will on net amplify, not reduce, Earth's sensitivity to anthropogenic climate change, contrary to strong homeostatic Gaia. | S22 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-09 | PS | Interpretive | Part A (philosophy): Leopold's land ethic ('land is a community'; right is what preserves the integrity, stability and beauty of the biotic community) and deep ecology extend moral concern to the living whole. | U32 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-10 | PS | Interpretive | Part A: calling life the 'soul of the Earth' is a metaphor; no evidence in this pass shows Earth to be conscious or ensouled. | S22;G03 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-11 | E | Supported | Part B: the core is a solid inner core within a fluid, convecting outer core; the inner core grows ~1 mm/yr as outer-core material freezes onto it, helping drive outer-core convection. | S25 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-12 | E | Supported | Part B: the outer-core radius is ~3480 km and inner-core radius ~1220 km; Lehmann inferred the inner core in 1936 from earthquake waves. | S25;S26 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-13 | E | Supported | Part B (heat transfer): Earth acts as a heat engine driven by radiogenic decay and slow cooling; the geodynamo runs on heat from cooling and inner-core freezing and on chemical convection, with core–mantle-boundary heat flux measuring its power supply. | V09;S29 | Upgraded to full preprint text V09. |
| C0v2-R6-14 | P | Contested | Part B: first-principles calculations gave core thermal and electrical conductivities 2–3 times higher than earlier estimates (V09), but a direct laser-heated diamond-anvil measurement placed core thermal conductivity near the low end of previous estimates, at 18–44 W/m/K (V30); the dispute is unresolved in the sources read. | V09;V30;S29 | Counter-evidence V30 added (challenge pass). |
| C0v2-R6-15 | E | Supported | Part B (planetary dynamics): most plate movement occurs along narrow plate-boundary zones; four boundary types are recognised. | U34 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-16 | P | Mixed | Part B: mantle convection is the commonly assumed driver of plate motion, but the driving mechanism remains among the 'unanswered questions'. | U35 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R6-17 | E | Supported | Part B (magnetic field): IGRF-14 dipole moment fell from 8.32×10²² (1900) to 7.69×10²² A·m² (2025), −7.6%; free ohmic decay time is ~2.4–7.3×10⁴ yr for σ = 0.5–1.5×10⁶ S/m (assumed), far shorter than the paleomagnetic record — consistent with continual regeneration. | C0:SIM-R6-C0#E3;C0:SIM-R6-C0#E4;S27;S25 | Carried forward (Cycle-0 run). Conductivity range widened in C1-R6-09. |
| C0v2-R6-18 | P | Contested | Part B: zircon paleointensities have been read as a geodynamo by 4.2 Ga, but a later combined study found most Jack Hills zircons poor recorders, so a geodynamo before 3.5 Ga 'remains unknown'. | S28;T12;V38;V29 | Sources widened. |
| C0v2-R6-19 | PS | Interpretive | Part B (symbol): traditions locate vitality or mind at the heart (Stoic hêgemonikon at the heart; Chinese xin 'heart-mind'); the core is physically central to heat flow and the geodynamo, but calling it Earth's 'heart' is metaphor — no evidence of consciousness or a literal soul. | S07;T17;S29;G03 | Carried forward unchanged from Cycle 0 (v2). |
| C1-R6-01 | P | Mixed | Lenton et al. introduce 'tipping elements': large-scale components of the Earth system that may pass a tipping point, at which a small perturbation can qualitatively alter the system's state. | V22 | New in Cycle 1. |
| C1-R6-02 | E | Supported | Model estimates place the Solar System's habitable zone between 0.99 AU (inner, water-loss limit) and 1.70 AU (outer, maximum-greenhouse limit), so Earth lies near the inner edge. | V26 | New in Cycle 1. |
| C1-R6-03 | P | Mixed | A seismic study of multiply reverberating waves reports a distinctly anisotropic innermost inner core with a transition to a weakly anisotropic outer shell, possibly a fossilized record of a past global event. | V27 | New in Cycle 1. |
| C1-R6-04 | P | Contested | Inner-core age is contested: a palaeointensity increase between 1 and 1.5 billion years ago has been read as inner-core nucleation (abstract), Late Cambrian geomagnetic instability has been placed after the onset of nucleation, and molecular-dynamics work finds an Fe1-xCx (x = 0.1-0.15) composition compatible with the supercooling required for nucleation. | V38;V29;V28 | New in Cycle 1. |
| C1-R6-05 | P | Contested | Gaia critiques (challenge pass): Boyle argues a testable Gaia hypothesis must invoke an entity that is planetary in scale, habitability-promoting and life-specific, requiring a resolution of the 'Darwinization problem'; Hermida & Okasha conclude Darwinized Gaia still cannot overcome the main objections from evolutionary biology; Doolittle argues Gaia has 'too many parents' to undergo natural selection; Lenton et al. propose 'sequential selection' for global regulation (abstract). | V23;V24;V25;V39 | New in Cycle 1. |
| C1-R6-06 | E | Supported | Virtually all of Earth's ecosystems and biogeochemical cycles are underpinned, and often driven, by the activity or inactivity of microorganisms; microbial dormancy acts as an ecological and biogeochemical regulator. | V32 | New in Cycle 1. |
| C1-R6-07 | E | Supported | In SIM-R6-C1 iteration 1, Daisyworld regulation (habitable band >= 2x the lifeless band) was not supported as robust: it held in 63% of 27 death-rate x heat-transfer x albedo settings and failed in all settings with small albedo contrast (0.45/0.55). | SIM-R6-C1/iter-1#D0;SIM-R6-C1/iter-1#D1;SIM-R6-C1/iter-1#D2 | New in Cycle 1. |
| C1-R6-08 | E | Supported | In SIM-R6-C1 iteration 2 (our own toy), regulation was not supported under unbounded adaptation: when daisies' optimum temperatures tracked local temperature, the regulated band shrank from 0.82 to 0.19-0.35 as optima drifted to 46-93 °C; with adaptation bounded to ±5 °C the band stayed >= 0.93. | SIM-R6-C1/iter-2#A0;SIM-R6-C1/iter-2#A1;SIM-R6-C1/iter-2#A_bounded_5;SIM-R6-C1/iter-2#A2 | New in Cycle 1. |
| C1-R6-09 | E | Supported | In SIM-R6-C1 iteration 3, the IGRF-14 spectrum was steep at Earth's surface (log10 slope -0.51 to -0.57 per degree, n = 2-10) and near-flat when continued to the core-mantle boundary (-0.04 to +0.02) in 1900, 1950, 2000 and 2025; free-decay times were 4.9·10^3-9.8·10^4 yr over 1·10^5-2·10^6 S/m, and 7·10^3-2.2·10^4 yr for V30's 18-44 W/m/K converted by Wiedemann–Franz at assumed 4000-5000 K, all far shorter than a 3.3-Gyr field record. | SIM-R6-C1/iter-3#G0;SIM-R6-C1/iter-3#G1;SIM-R6-C1/iter-3#G2;S27 | New in Cycle 1. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-1 status |
|---|---|---|---|---|
| L01 | R1 Body → R6 Earth | relationship | P | Retained as analogy only. Under pressure: Daisyworld regulation held in only 63% of parameter settings (C1-R6-07), whereas the body-side toy regulation was robust. |
| L02 | R1 Body → R6 Earth | distinction | P | Strengthened by Cycle-1 critiques (V23-V25); no rejection trigger. |
| L03 | R1 Body → R6 Earth | humans within Earth | E | Basis upgraded to full text; Established retained. |
| L13 | R3 Soul → R6 Earth | relationship | E | Widened: 10 of 15 coded conceptions extend soul/life-principle beyond humans. |
| L19 | R6 Earth → R6 Earth | dependency | E | Dependency retained: free decay is far shorter than the field record across the whole disputed conductivity range (G2 supported). |
| L20 | R6 Earth → R6 Earth | feedback loop | P | Downgraded Established -> Plausible: basis C0v2-R6-04 is abstract-only under the Cycle-1 rule. |
| L21 | R6 Earth → R6 Earth | competing interpretation | P | The strong-Gaia side is under pressure in Cycle 1: toy regulation is parameter-dependent and erodes under unbounded adaptation; critiques find no selection mechanism. |
| L22 | R6 Earth → R7 Unified | humans within Earth | E | Basis upgraded; Established retained for the boundary framework statement. |
| L23 | R6 Earth → R3 Soul | competing interpretation | PS | Unchanged (metaphor). |

## Limitations
Daisyworld is a parable; our adaptation rule is not a published model; Wiedemann–Franz conversion assumes core temperatures of 4000–5000 K; free decay ignores inner-core and mode structure; several Part-B sources are abstracts.

## Open questions and falsification
Is there a demonstrated mechanism that limits adaptation in ways that preserve planetary regulation? What is the core's conductivity (independent measurements)? When did the inner core nucleate?

## Conclusion and gate
Earth-system and core science claims are well supported where full text was read; Gaia as regulator remains contested and our toys add evidence of fragility. Gate: **Indeterminate**.

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

## Change history
- Cycle 0 Baseline v2 (2026-10-24): see `../../Cycle-0-Baseline/`.
- Cycle 1 (x3) (2026-10-24): this version; details in `CHANGELOG.md`.
