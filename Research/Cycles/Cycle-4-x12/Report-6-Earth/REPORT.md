# Report 6 — Earth: the living planet and its core

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-4-X12-R6 |
| Version | Cycle 4 (x12) |
| Status | Researched (12 passes), simulated (12 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-3-x9/Report-6-Earth/REPORT.md` (Cycle 3), Cycles 0-2 |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Rules in force | Cycle-1 access rule (Established literature claims need full text); Cycle-2 strict Established-link rule; Cycle-3 essential-claim definition tested, strict reading kept (Report 7); Cycle-4: Report 7's own new claims excluded from its simulation inputs |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
W03 (Lenton & Lovelock 2000), which holds the constrained-adaptation equations, is still closed. SIM-R6-C4 (12 iterations) found that Cycle 3's constrained run had stopped at the edge of its forcing range (L = 1.7) and extended it to 2.6: our cost form reaches L_max 1.768, still short of W01's published 2.32 (and total life 0.85 vs 1.223), no calibration setting matches both ends, and results depend on our assumed cost shape (linear cost 1.58) and cost width (1.57–1.86). The mismatch was therefore only partly a range artefact. Original Daisyworld shows hysteresis (life reappears at L 1.16 on the reverse sweep). Daisyworld remains a parable: nothing here says Earth is regulated, and the core-as-heart and life-as-soul framings stay Philosophical/Spiritual, separate from geophysics.

## What changed in Cycle 4
Pass 1 logged a Daisyworld/Gaia adaptation query (top hits irrelevant); pass 2 a title search 'Daisyworld' (only closed papers); pass 3 an OpenAlex DOI lookup for W03 (still closed). Passes 4, 6, 9 added nothing (Earth is outside the Being×Lens matrix). Passes 5, 7, 8 ran iterations 1–4, 5–8, 9–12. Pass 10: 2 new claims; C3-R6-05 annotated. Pass 11: L01, L21 updated. Pass 12: no carried label or status changed.

Ledger: 41 claims (24 E, 14 P, 3 PS, 0 H); 2 new; 1 carried claims annotated with Cycle-4 evidence; no carried claim changed label or status (each row's `c4_change` says which).

## Methods
Twelve successive research passes (1 logged search → 2 deepen → 3 DOI/open-access lookups → 4 challenge → 5 carried agenda item (iterations 1–4) → 6 targeted Being×Lens gaps → 7 robustness (iterations 5–8) → 8 extension and challenge (iterations 9–12) → 9 retry of blocked items → 10 consolidation → 11 links → 12 diminishing-returns audit; notes in `research/pass-1..12/NOTES.md`; every query in `../Provenance/SEARCH_LOG.jsonl`) and twelve chained simulation iterations (`simulation/iter-1..12`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iteration k reads iteration k-1 where `prev` is set). Sources were fetched, snapshotted and hashed (`../Provenance/`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass — a failure is reported, not re-specified), *hypothesis* (Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded). Passes that added nothing are recorded as such, not padded.

## Competing views and counter-evidence
Strong Gaia (regulation as a planetary property) vs weak/coevolutionary readings; adaptation can undermine regulation (W01) unless constrained (W03, unread).

## Simulation (12 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Code checks: vectorised copy reproduces Cycle 3; extending the range leaves the original model unchanged. | V1: Pass, V2: Pass, C0: Reported | 2/2 | 0/0 |
| 2 | Does the constrained variant reach the published L_max once the range is not truncated? | H2: Not supported, H2r: Reported | 0/0 | 0/1 |
| 3 | Unbounded adaptation over the extended range. | H3: Supported | 0/0 | 1/1 |
| 4 | Cost width R. | H4: Supported | 0/0 | 1/1 |
| 5 | Adaptation bounds. | H5: Supported | 0/0 | 1/1 |
| 6 | Regulation over the extended range. | H6: Not supported | 0/0 | 0/1 |
| 7 | Cost shape. | H7: Not supported | 0/0 | 0/1 |
| 8 | Hysteresis of the original model (reverse sweep). | H8: Supported | 0/0 | 1/1 |
| 9 | Numerical robustness of the extended constrained run. | H9: Supported | 0/0 | 1/1 |
| 10 | Calibration against the published row (disclosed as calibration). | H10: Not supported | 0/0 | 0/1 |
| 11 | One-at-a-time sensitivity of the constrained L_max. | H11: Supported | 0/0 | 1/1 |
| 12 | Consolidation: was the Cycle-3 mismatch a range artefact? | H12: Supported | 0/0 | 1/1 |

Agreement with the published constrained row would have been calibration, not reproduction.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-4 change |
|---|---|---|---|---|---|
| C0v2-R6-01 | P | Indeterminate | Part A: the rock record indicates a microbial biosphere by at least 3.4 billion years ago; earlier claims are disputed because abiotic processes and contamination can mimic biosignatures. | S23;V08 | Carried unchanged. |
| C0v2-R6-02 | E | Supported | Part A: an estimate from higher-taxonomy patterns predicts ~8.7 million (± 1.3 million SE) eukaryotic species, about 86% still undescribed. | V02;U30 | Carried unchanged. |
| C0v2-R6-03 | E | Supported | Part A: IPBES estimates around 1 million animal and plant species are threatened with extinction, many within decades, absent action. | S24 | Carried unchanged. |
| C0v2-R6-04 | P | Indeterminate | Part A (interdependence): nearly all non-equilibrium electron transfers on Earth are driven by microbial nanomachines whose conserved core genes co-evolved with biogeochemical cycles and spread mainly by horizontal gene transfer. | T13 | Carried unchanged. |
| C0v2-R6-05 | E | Supported | Part A (humans within Earth systems): the planetary-boundaries framework identifies climate change and biosphere integrity as 'core boundaries'; its 2023 update finds six of the nine boundaries transgressed. | V03;U31 | Carried unchanged. |
| C0v2-R6-06 | E | Supported | Part A: Daisyworld shows that a coupled biota–temperature model with a peaked growth curve stabilises temperature; it was offered as a parable, not a model of Earth. | S21b | Carried unchanged. |
| C0v2-R6-07 | E | Supported | In SIM-R6-C0, re-implemented Daisyworld kept temperature within 22.5 ± 10 °C over luminosity 0.72–1.54 (width 0.82) vs 0.83–1.07 (0.24) without life, with hysteresis between up and down sweeps. | C0:SIM-R6-C0#E1;C0:SIM-R6-C0#E2;S21b | Carried unchanged. |
| C0v2-R6-08 | P | Contested | Part A: Kirchner argues the best available data suggest biologically mediated feedbacks will on net amplify, not reduce, Earth's sensitivity to anthropogenic climate change, contrary to strong homeostatic Gaia. | S22 | Carried unchanged. |
| C0v2-R6-09 | PS | Interpretive | Part A (philosophy): Leopold's land ethic ('land is a community'; right is what preserves the integrity, stability and beauty of the biotic community) and deep ecology extend moral concern to the living whole. | U32 | Carried unchanged. |
| C0v2-R6-10 | PS | Interpretive | Part A: calling life the 'soul of the Earth' is a metaphor; no evidence in this pass shows Earth to be conscious or ensouled. | S22;G03 | Carried unchanged. |
| C0v2-R6-11 | E | Supported | Part B: the core is a solid inner core within a fluid, convecting outer core; the inner core grows ~1 mm/yr as outer-core material freezes onto it, helping drive outer-core convection. | S25 | Carried unchanged. |
| C0v2-R6-12 | E | Supported | Part B: the outer-core radius is ~3480 km and inner-core radius ~1220 km; Lehmann inferred the inner core in 1936 from earthquake waves. | S25;S26 | Carried unchanged. |
| C0v2-R6-13 | E | Supported | Part B (heat transfer): Earth acts as a heat engine driven by radiogenic decay and slow cooling; the geodynamo runs on heat from cooling and inner-core freezing and on chemical convection, with core–mantle-boundary heat flux measuring its power supply. | V09;S29 | Carried unchanged. |
| C0v2-R6-14 | P | Contested | Part B: first-principles calculations gave core thermal and electrical conductivities 2–3 times higher than earlier estimates (V09), but a direct laser-heated diamond-anvil measurement placed core thermal conductivity near the low end of previous estimates, at 18–44 W/m/K (V30); the dispute is unresolved in the sources read. | V09;V30;S29 | Carried unchanged. |
| C0v2-R6-15 | E | Supported | Part B (planetary dynamics): most plate movement occurs along narrow plate-boundary zones; four boundary types are recognised. | U34 | Carried unchanged. |
| C0v2-R6-16 | P | Mixed | Part B: mantle convection is the commonly assumed driver of plate motion, but the driving mechanism remains among the 'unanswered questions'. | U35 | Carried unchanged. |
| C0v2-R6-17 | E | Supported | Part B (magnetic field): IGRF-14 dipole moment fell from 8.32×10²² (1900) to 7.69×10²² A·m² (2025), −7.6%; free ohmic decay time is ~2.4–7.3×10⁴ yr for σ = 0.5–1.5×10⁶ S/m (assumed), far shorter than the paleomagnetic record — consistent with continual regeneration. | C0:SIM-R6-C0#E3;C0:SIM-R6-C0#E4;S27;S25 | Carried unchanged. |
| C0v2-R6-18 | P | Contested | Part B: zircon paleointensities have been read as a geodynamo by 4.2 Ga, but a later combined study found most Jack Hills zircons poor recorders, so a geodynamo before 3.5 Ga 'remains unknown'. | S28;T12;V38;V29 | Carried unchanged. |
| C0v2-R6-19 | PS | Interpretive | Part B (symbol): traditions locate vitality or mind at the heart (Stoic hêgemonikon at the heart; Chinese xin 'heart-mind'); the core is physically central to heat flow and the geodynamo, but calling it Earth's 'heart' is metaphor — no evidence of consciousness or a literal soul. | S07;T17;S29;G03 | Carried unchanged. |
| C1-R6-01 | P | Mixed | Lenton et al. introduce 'tipping elements': large-scale components of the Earth system that may pass a tipping point, at which a small perturbation can qualitatively alter the system's state. | V22 | Carried unchanged. |
| C1-R6-02 | E | Supported | Model estimates place the Solar System's habitable zone between 0.99 AU (inner, water-loss limit) and 1.70 AU (outer, maximum-greenhouse limit), so Earth lies near the inner edge. | V26 | Carried unchanged. |
| C1-R6-03 | P | Mixed | A seismic study of multiply reverberating waves reports a distinctly anisotropic innermost inner core with a transition to a weakly anisotropic outer shell, possibly a fossilized record of a past global event. | V27 | Carried unchanged. |
| C1-R6-04 | P | Contested | Inner-core age is contested: a palaeointensity increase between 1 and 1.5 billion years ago has been read as inner-core nucleation (abstract), Late Cambrian geomagnetic instability has been placed after the onset of nucleation, and molecular-dynamics work finds an Fe1-xCx (x = 0.1-0.15) composition compatible with the supercooling required for nucleation. | V38;V29;V28 | Carried unchanged. |
| C1-R6-05 | P | Contested | Gaia critiques (challenge pass): Boyle argues a testable Gaia hypothesis must invoke an entity that is planetary in scale, habitability-promoting and life-specific, requiring a resolution of the 'Darwinization problem'; Hermida & Okasha conclude Darwinized Gaia still cannot overcome the main objections from evolutionary biology; Doolittle argues Gaia has 'too many parents' to undergo natural selection; Lenton et al. propose 'sequential selection' for global regulation (abstract). | V23;V24;V25;V39 | Carried unchanged. |
| C1-R6-06 | E | Supported | Virtually all of Earth's ecosystems and biogeochemical cycles are underpinned, and often driven, by the activity or inactivity of microorganisms; microbial dormancy acts as an ecological and biogeochemical regulator. | V32 | Carried unchanged. |
| C1-R6-07 | E | Supported | In SIM-R6-C1 iteration 1, Daisyworld regulation (habitable band >= 2x the lifeless band) was not supported as robust: it held in 63% of 27 death-rate x heat-transfer x albedo settings and failed in all settings with small albedo contrast (0.45/0.55). | SIM-R6-C1/iter-1#D0;SIM-R6-C1/iter-1#D1;SIM-R6-C1/iter-1#D2 | Carried unchanged. |
| C1-R6-08 | E | Supported | In SIM-R6-C1 iteration 2 (our own toy), regulation was not supported under unbounded adaptation: when daisies' optimum temperatures tracked local temperature, the regulated band shrank from 0.82 to 0.19-0.35 as optima drifted to 46-93 °C; with adaptation bounded to ±5 °C the band stayed >= 0.93. | SIM-R6-C1/iter-2#A0;SIM-R6-C1/iter-2#A1;SIM-R6-C1/iter-2#A_bounded_5;SIM-R6-C1/iter-2#A2 | Carried unchanged. |
| C1-R6-09 | E | Supported | In SIM-R6-C1 iteration 3, the IGRF-14 spectrum was steep at Earth's surface (log10 slope -0.51 to -0.57 per degree, n = 2-10) and near-flat when continued to the core-mantle boundary (-0.04 to +0.02) in 1900, 1950, 2000 and 2025; free-decay times were 4.9·10^3-9.8·10^4 yr over 1·10^5-2·10^6 S/m, and 7·10^3-2.2·10^4 yr for V30's 18-44 W/m/K converted by Wiedemann–Franz at assumed 4000-5000 K, all far shorter than a 3.3-Gyr field record. | SIM-R6-C1/iter-3#G0;SIM-R6-C1/iter-3#G1;SIM-R6-C1/iter-3#G2;S27 | Carried unchanged. |
| C2-R6-01 | E | Supported | Lenton & Lovelock (2001) summarise that adaptation to prevailing conditions undermines Daisyworld's environmental regulation (Robertson & Robinson 1998), but that when bounds on the range of adaptation are added and peak growth rate is limited as the bounds are approached, temperature regulation is recovered (Lenton & Lovelock 2000). | W01;W02;W03 | Carried unchanged. |
| C2-R6-02 | P | Supported | Robertson & Robinson (1998) let daisies shift their optimal growth temperatures toward the prevailing temperature and suggest a trade-off between organisms' ability to collectively regulate the environment and evolving genotypes' ability to adapt to it. | W02 | Carried unchanged. |
| C2-R6-03 | E | Supported | As of 2024, Daisyworld 'exists only as a mathematical or computational construct'; Maull et al. propose a synthetic microbial implementation (engineered two-strain consortia with pH as the abiotic control parameter) with theoretical case studies. | W14 | Carried unchanged. |
| C2-R6-04 | E | Supported | SIM-R6-C2 reproduced the Cycle-1 adaptive-Daisyworld result exactly and extended it: unconstrained adaptation shrank the regulated band below 0.8x the non-adapting width at every positive rate tested (0.08-0.35 vs 0.82); bounded, costed adaptation largely recovered it (0.62-0.82, so 'every setting >= 0.8x' was not supported because the growth cost itself narrows the band); across 9 death-rate x heat-transfer settings constrained adaptation kept >= 0.8x in 100% and unbounded in 0%. | SIM-R6-C2/iter-1#R0;SIM-R6-C2/iter-1#U1;SIM-R6-C2/iter-2#LL1;SIM-R6-C2/iter-2#LL2;SIM-R6-C2/iter-6#RB1;SIM-R6-C2/iter-6#RB2 | Carried unchanged. |
| C2-R6-05 | E | Supported | In SIM-R6-C2, the slowest adaptation rate tested (0.0003) eroded regulation most (band 0.08), so the hypothesis that faster adaptation relative to forcing gives weaker regulation was not supported (Spearman -0.39); a band-independent damping ratio confirmed the pattern (none 2.95, unbounded 0.94, constrained 2.67). | SIM-R6-C2/iter-1#U1;SIM-R6-C2/iter-3#RR1;SIM-R6-C2/iter-4#DM0;SIM-R6-C2/iter-4#DM1 | Carried unchanged. |
| C2-R6-06 | E | Supported | In SIM-R6-C2 iteration 5, more albedo types with neighbour mutation did not extend the regulated range in our implementation (0.78 vs 0.82 for two types; not supported), so W01's statement citing Stocker 1995 was not reproduced by this toy. | SIM-R6-C2/iter-5#M0;SIM-R6-C2/iter-5#M1 | Carried unchanged. |
| C3-R6-01 | P | Supported | Lenton (2025) argues that Earth's biosphere ('Gaia') increased its own persistence through element cycling and net stabilisation of atmosphere and climate, that physical ('most probable trajectory') and biological (selection among ecosystems and nutrient cycles) explanations are converging, and that the resulting theory makes testable predictions. | X15 | Carried unchanged. |
| C3-R6-02 | P | Supported | Molecular-dynamics simulations suggest the inner core may have nucleated in two steps (metastable bcc iron first), which reduces the undercooling required and offers a route out of the inner-core nucleation paradox. | X16 | Carried unchanged. |
| C3-R6-03 | P | Contested | Direct measurements on Fe-Si alloys (up to 144 GPa, 3300 K) found that 15 at% silicon roughly halves iron's thermal conductivity, implying a lower minimum core-mantle heat flow (~3 TW) and an inner core that could be older than two billion years; this conflicts with high-conductivity estimates (S29) that implied a young inner core. | X17;S29;V30 | Carried unchanged. |
| C3-R6-04 | E | Supported | SIM-R6-C3 implemented Daisyworld from the published equations of Lenton & Lovelock 2001 (W01) and reproduced its Table 1: original model life range L 0.684-1.496 (published 0.68-1.50), neutral-daisy control 0.744-1.100 (0.74-1.11), and 'total life' 0.551 and 0.203 (0.556 and 0.204); results were robust to the unstated seed floor and to halving the time step. | SIM-R6-C3/iter-1#V1;SIM-R6-C3/iter-1#V2;SIM-R6-C3/iter-2#H2;SIM-R6-C3/iter-3#H3;SIM-R6-C3/iter-3#H3b;SIM-R6-C3/iter-4#H4;SIM-R6-C3/iter-9#H9 | Carried unchanged. |
| C3-R6-05 | E | Supported | In SIM-R6-C3, unbounded adaptation of growth optima within the published equations removed regulation at every rate (temperature-luminosity slope ratio rose from -0.03 to 1.02-1.08, i.e. like a dead planet) while extending the life range; our bounded, costed variant only partly recovered regulation (0.19; recovery within 0.2 in 4 of 12 settings) and did not match W01's published constrained-adaptation row (0.51-2.32), partly because W01's forcing protocol stops at L = 1.7 and the W03 equations were not available (H6, H7, H8 not supported). | SIM-R6-C3/iter-5#H5;SIM-R6-C3/iter-6#H6;SIM-R6-C3/iter-7#H7;SIM-R6-C3/iter-8#H8 | Extended in Cycle 4 over a wider forcing range: our constrained variant reaches L_max 1.77, still short of the published 2.32 (C4-R6-01); W03 still closed. |
| C4-R6-01 | E | Supported | In SIM-R6-C4, Cycle 3's constrained-adaptation Daisyworld run had stopped at the edge of its forcing range (L = 1.7); over an extended range (to 2.6) our cost form reached L_max 1.768 (establishment 0.524, total life 0.854), still short of W01 Table 1's published row (0.51-2.32, total life 1.223; not supported), and no setting of a calibration grid matched both ends within 0.05 (best error 0.49; not supported). The Cycle-3 mismatch was therefore only partly a range artefact; the W03 equations are still needed. | SIM-R6-C4/iter-1#V1;SIM-R6-C4/iter-1#V2;SIM-R6-C4/iter-1#C0;SIM-R6-C4/iter-2#H2;SIM-R6-C4/iter-2#H2r;SIM-R6-C4/iter-10#H10;SIM-R6-C4/iter-12#H12 | New in Cycle 4. |
| C4-R6-02 | E | Supported | In SIM-R6-C4, the constrained result depended on assumptions we had to supply: L_max rose with cost width (1.57-1.86), changed little with bounds (1.71-1.79) or +-10% in death rate and growth width (1.72-1.82), but a linear instead of quadratic cost gave 1.58 (not supported), regulation over the extended range was weaker than the original (slope ratio 0.23 vs -0.03; not supported), and unbounded adaptation survived to the edge of the range (2.6) without regulating; the original model shows hysteresis (life reappears at L 1.16 on the reverse sweep after dying at 1.50). | SIM-R6-C4/iter-3#H3;SIM-R6-C4/iter-4#H4;SIM-R6-C4/iter-5#H5;SIM-R6-C4/iter-6#H6;SIM-R6-C4/iter-7#H7;SIM-R6-C4/iter-8#H8;SIM-R6-C4/iter-9#H9;SIM-R6-C4/iter-11#H11 | New in Cycle 4. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-4 status |
|---|---|---|---|---|
| L01 | R1 Body → R6 Earth | relationship | P | Retained as analogy only. Body side: the two-state memory stays fragile with a continuous metric; Earth side: constrained adaptation regulates less well than the original over a wider range and depends on our cost form. |
| L02 | R1 Body → R6 Earth | distinction | P | No Cycle-4 evidence targeted this link. |
| L03 | R1 Body → R6 Earth | humans within Earth | E | No Cycle-4 evidence targeted this link. |
| L13 | R3 Soul → R6 Earth | relationship | E | No Cycle-4 evidence targeted this link. |
| L19 | R6 Earth → R6 Earth | dependency | E | No Cycle-4 evidence targeted this link. |
| L20 | R6 Earth → R6 Earth | feedback loop | P | No Cycle-4 evidence targeted this link. |
| L21 | R6 Earth → R6 Earth | competing interpretation | P | Unchanged in substance; constrained-adaptation regulation depends on an assumed cost form. |
| L22 | R6 Earth → R7 Unified | humans within Earth | E | No Cycle-4 evidence targeted this link. |
| L23 | R6 Earth → R3 Soul | competing interpretation | PS | No Cycle-4 evidence targeted this link. |

## Limitations
Cost form ours; W03 unavailable; no new Earth-science source this cycle.

## Open questions and falsification
With W03's equations, does the constrained model reach L 0.51–2.32? Rejection of our cost form as a stand-in: a different L_max under W03's equations.

## Conclusion and gate
The published-equation Daisyworld is reproduced (Cycle 3); the constrained variant still is not. **Gate: Indeterminate** (internal checks pass; no independent review; Indeterminate is never Pass).

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
- **X15** — Lenton TM (2025). The evolution of Gaia(s). Philosophical transactions of the Royal Society of London. Series B, Biological sciences 380:rstb20240095. doi:10.1098/rstb.2024.0095 [full text (Europe PMC PMC12329439)] <https://europepmc.org/article/PMC/PMC12329439>
- **X16** — Sun Y, Zhang F, Mendelev MI, Wentzcovitch RM, Ho KM (2022). Two-step nucleation of the Earth's inner core. Proceedings of the National Academy of Sciences of the United States of America 119:e2113059119. doi:10.1073/pnas.2113059119 [full text (Europe PMC PMC8764699)] <https://europepmc.org/article/PMC/PMC8764699>
- **X17** — Hsieh WP, Goncharov AF, Labrosse S, Holtgrewe N, Lobanov SS, Chuvashova I, Deschamps F, Lin JF (2020). Low thermal conductivity of iron-silicon alloys at Earth's core conditions with implications for the geodynamo. Nature communications 11:3332. doi:10.1038/s41467-020-17106-7 [full text (Europe PMC PMC7335046)] <https://europepmc.org/article/PMC/PMC7335046>

## Change history
- Cycle 0 Baseline v2: `../../Cycle-0-Baseline/`.
- Cycle 1 (x3): `../../Cycle-1-x3/`.
- Cycle 2 (x6): `../../Cycle-2-x6/`.
- Cycle 3 (x9): `../../Cycle-3-x9/`.
- Cycle 4 (x12) (2026-10-24): this version; details in `CHANGELOG.md`.
