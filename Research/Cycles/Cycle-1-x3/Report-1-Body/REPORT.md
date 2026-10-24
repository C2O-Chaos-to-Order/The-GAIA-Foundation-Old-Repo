# Report 1 — The Body: the physical foundation of life

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-1-X3-R1 |
| Version | Cycle 1 (x3) |
| Status | Researched (3 passes), simulated (3 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-0-Baseline/Report-1-Body/REPORT.md` (Baseline v2) |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Cycle-1 access rule | Established literature claims need at least one full-text (or textbook) source; abstract-only claims are capped at Plausible |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 1 keeps the Cycle-0 picture of the body (levels of organization, nervous systems, sensory transduction, homeostasis as multiple feedback loops plus feedforward) and tightens its evidence: thermoregulation now rests on a full-text textbook source (36.5–37.5 °C core, negative feedback with a hypothalamic thermostat), and a new full-text estimate puts the body at about 3.0·10^13 human cells and 3.8·10^13 bacteria (ratio about 1.3, not 10:1), which widens 'the body' toward the microbial life it carries (a link to Report 6). Three chained simulation iterations test the regulation toy harder: gain space (all validation checks pass), delay and parameter uncertainty (feedforward plus feedback is robust: 100% restoration, median peak cut to 0.22), and a core/shell thermal toy in which skin-signal anticipation helps at nominal parameters but is **not supported** as robust (benefit in only 55% of perturbed draws).

## What changed in Cycle 1
Pass 1 (consolidate) upgraded C0v2-R1-09 to the full-text OpenStax section (V06). Pass 2 (widen) added the revised human/bacterial cell count (V36). Pass 3 (challenge) tried to read Sterling's allostasis paper in full (V10 in the fetch log; host unavailable), so the homeostasis–allostasis dispute stays at abstract level, and the simulations were pushed toward failure modes (delay, parameter uncertainty).

Ledger: 20 claims (17 E, 2 P, 1 PS, 0 H); 4 new, 2 revised; the rest carried forward unchanged from Cycle 0 (each row's `c1_change` says which).

## Methods
Three successive research passes (consolidate → widen → challenge; notes in `research/pass-1..3/NOTES.md`) and three chained simulation iterations (`simulation/iter-1..3`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iterations 2 and 3 read the previous iteration's results). Sources were fetched directly, snapshotted, hashed (`../Provenance/SOURCE_REGISTER.csv`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass), *hypothesis* (substantive; Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded).

## Evidence and findings
**Structure, nervous systems, sensation** — carried forward unchanged (Established; C0v2-R1-01..05).

**Regulation.** Homeostasis as multiple interacting feedback loops plus feedforward (C0v2-R1-06..08, Established). Thermoregulation is the textbook example of negative feedback: core temperature is held around 36.5–37.5 °C, the hypothalamus works as a thermostat, and about 60% of the energy of ATP production appears as heat (C0v2-R1-09, Established, now full text).

**The body is not only human cells.** A reference adult carries about 3.8·10^13 bacteria alongside 3.0·10^13 human cells (C1-R1-01, Established), which places microbial life inside the body's own accounting.

**Where explanation ends** — unchanged: subjective experience (Report 5) and the origin of life (Report 6) (C0v2-R1-16).

## Competing views and counter-evidence
Allostasis (anticipatory regulation as primary) vs homeostasis-centred accounts that include feedforward (C0v2-R1-11, Plausible/Contested); Cycle 1 could not read the allostasis source in full. The simulations add a toy-level point: anticipation is valuable only while its internal model is roughly right (C1-R1-04, benefit not robust under ±50% parameter error), which is compatible with both camps' claim that feedback remains necessary.

## Simulation (3 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Map the controller-gain space of the C0 toy loop (step load D=1, plant leak kl=0.1) and record the best-peak gain pair for iteration 2. | G1: Pass, G2: Pass | 2/2 | 0/0 |
| 2 | Add sensor/effector delay (the main way real feedback fails) and parameter uncertainty. The iteration-1 best-peak gains are added to the PI delay scan (adaptive refinement). | D1: Pass, D2: Reported, M1: Supported, M2: Supported | 1/1 | 2/2 |
| 3 | Core/shell thermal toy: a skin (shell) signal used as feedforward for core regulation, the structure OpenStax describes (V06: hypothalamic thermostat, skin and core). Robustness to +/-50% parameter perturbation. | T1: Supported, T2: Pass, T3: Not supported | 1/1 | 1/2 |

Iteration 1 mapped the gain grid; iteration 2 added delay and uncertainty using the iteration-1 best gains; iteration 3 moved to a two-compartment (core/shell) toy. The one 'not supported' outcome (T3) is a substantive finding and is carried to Cycle 2 as a refinement target (bounded perturbation ranges; learning feedforward).

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-1 change |
|---|---|---|---|---|---|
| C0v2-R1-01 | E | Supported | Human body structure is described in textbook anatomy as levels of organization of increasing complexity (chemical → cells → tissues → organs → organ systems → organism), with eleven organ systems. | U04 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-02 | E | Supported | The nervous system is divided anatomically into the central nervous system (brain and spinal cord) and the peripheral nervous system (everything else); its basic functions are sensation, integration and response. | U01 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-03 | E | Supported | Functionally, the somatic nervous system governs conscious perception and voluntary motor responses, the autonomic nervous system governs involuntary responses (smooth/cardiac muscle, glands), and the enteric nervous system handles a set of gastrointestinal functions. | U01 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-04 | E | Supported | Sensory receptors convert (transduce) stimuli of different kinds into the electrochemical signals of the nervous system; sensory systems include exteroceptors, interoceptors and proprioception. | U05;U02 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-05 | E | Supported | Sensory receptors show adaptation (declining firing to a constant stimulus) and modality specificity via labeled lines; what is perceived depends on where the nerve fibre terminates in the CNS. | U02 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-06 | E | Supported | Homeostasis is treated as a central unifying concept of physiology: a self-regulating process that maintains internal stability while adjusting to changing external conditions. | S01 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-07 | E | Supported | Homeostatic regulation involves multiple interacting feedback systems and feedforward control, not a single negative-feedback cycle. | S01 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-08 | E | Supported | A generic negative-feedback mechanism comprises sensor, error detector comparing the signal with a set point, controller and effector; 'set point' does not imply a fixed value. | S02 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-09 | E | Supported | The body keeps core temperature at about 36.5–37.5 °C by thermoregulation, which the textbook gives as an example of negative feedback, with the hypothalamus working as a thermostat; about 60% of the energy produced in ATP production appears as heat used to maintain body temperature. | V06;U03 | Upgraded to full-text source V06 (Cycle-1 access rule); wording aligned to V06. |
| C0v2-R1-10 | E | Supported | Interoception is the nervous system's sensing, interpretation and integration of signals from within the body, contributing to homeostatic functioning; interoceptive dysfunction is increasingly recognized in several mental-health conditions. | T02 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-11 | P | Contested | Allostasis (Sterling) argues that the primary goal of regulation is anticipatory adjustment, not constancy, and that feedback error-correction is inherently inefficient; this competes with homeostasis-centred accounts (S01) that include feedforward within homeostasis. | T01;S01 | Limits updated (full-text attempt failed). |
| C0v2-R1-12 | E | Supported | In SIM-R1-C0 (toy loop), PI control restored the set point after a step load (tail mean 0.001), P-only left the analytic residual 0.476, degraded gains raised peak deviation (1.79 vs 0.36) and slowed recovery (10.99 vs 4.49), and a load beyond effector capacity was not corrected. | C0:SIM-R1-C0#E2;C0:SIM-R1-C0#E3;C0:SIM-R1-C0#E4;C0:SIM-R1-C0#E5 | Carried forward; cites the Cycle-0 run (C0: prefix). Extended by C1-R1-02..04. |
| C0v2-R1-13 | E | Supported | In SIM-R1-C0, adding anticipatory (feedforward) control cut the peak deviation from 0.360 to 0.086, while feedforward alone with a 20% estimation error left a residual of 1.987 — in this linear toy, anticipation and feedback are complementary. | C0:SIM-R1-C0#E6;C0:SIM-R1-C0#E7 | Carried forward; cites the Cycle-0 run (C0: prefix). Robustness re-tested in C1-R1-03/04. |
| C0v2-R1-14 | PS | Contested | Embodied cognition holds that the body and body–environment interaction contribute to or constitute cognition; whether the role is constitutive or merely causal is disputed. | S03 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-15 | P | Indeterminate | The principle that disruption of homeostatic mechanisms is what leads to disease is asserted by S01; its generality was not tested in this pass. | S01 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R1-16 | E | Supported | Where biological explanation currently ends: how physical/neural processes give rise to phenomenal ('what it is like') experience — the 'hard problem' — remains without an accepted explanation; the origin of life is also unresolved (earliest traces disputed). | S16;S23 | Carried forward unchanged from Cycle 0 (v2). |
| C1-R1-01 | E | Supported | Revised estimates for a 70 kg reference man give about 3.0·10^13 human cells and 3.8·10^13 bacteria, a bacteria:human cell ratio of about 1.3 rather than the often-quoted 10:1. | V36 | New in Cycle 1. |
| C1-R1-02 | E | Supported | In SIM-R1-C1 (toy regulation loop), proportional-only control left the analytic residual D/(kl+kp) (max error 0.2%), every stable PI setting returned to set point, the numerical critical feedback delay matched the analytic value within 2.4%, and stronger PI gains tolerated less delay (critical delay 1.13 at gains (1, 0.5) down to 0.19 at (8, 2)). | SIM-R1-C1/iter-1#G1;SIM-R1-C1/iter-1#G2;SIM-R1-C1/iter-2#D1;SIM-R1-C1/iter-2#D2 | New in Cycle 1. |
| C1-R1-03 | E | Supported | In SIM-R1-C1 iteration 2, across 200 draws of uncertain plant leak, gains and delay, adding an imperfect feedforward (20% estimation error) to feedback never prevented restoration of the set point (100% of runs with and without it) and cut the median peak deviation to 0.22 of feedback alone (5-95%: 0.04-0.49). | SIM-R1-C1/iter-2#M1;SIM-R1-C1/iter-2#M2 | New in Cycle 1. |
| C1-R1-04 | E | Supported | In SIM-R1-C1 iteration 3 (core/shell thermal toy), using the shell (skin) signal as feedforward lowered peak core deviation from 0.053 to 0.046 at nominal parameters, but the benefit was not supported as robust: under ±50% parameter perturbation it held in only 55% of draws (worst case 2.7x worse). | SIM-R1-C1/iter-3#T1;SIM-R1-C1/iter-3#T2;SIM-R1-C1/iter-3#T3 | New in Cycle 1. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-1 status |
|---|---|---|---|---|
| L01 | R1 Body → R6 Earth | relationship | P | Retained as analogy only. Under pressure: Daisyworld regulation held in only 63% of parameter settings (C1-R6-07), whereas the body-side toy regulation was robust. |
| L02 | R1 Body → R6 Earth | distinction | P | Strengthened by Cycle-1 critiques (V23-V25); no rejection trigger. |
| L03 | R1 Body → R6 Earth | humans within Earth | E | Basis upgraded to full text; Established retained. |
| L04 | R1 Body → R2 Mind | dependency | E | Unchanged. |
| L05 | R1 Body → R2 Mind | feedback loop | P | Under pressure in the toy: the anticipatory benefit was not robust to parameter perturbation (T3 not supported). |
| L06 | R1 Body → R2 Mind | competing interpretation | PS | Unchanged. |
| L14 | R4 Spirit → R1 Body | relationship | P | Association better supported (full text); the Swedish cohort points to social participation as a pathway or confounder. |
| L15 | R4 Spirit → R1 Body | dependency | H | Still Hypothetical: quasi-causal designs point the same way but can be biased (C1-R4-09); V16 read as abstract only. |
| L17 | R5 Consciousness → R1 Body | dependency | E | Basis upgraded to full text; Established retained. |

## Limitations
All simulations are dimensionless toys. The cell-count estimate is for a 70 kg reference man and varies up to two-fold across groups. The allostasis source remains abstract-only.

## Open questions and falsification
Does anticipatory regulation outperform feedback in real physiology when its model is wrong? (falsifiable with perturbation experiments on thermoregulatory feedforward). How should microbial cells be counted in 'the body'?

## Conclusion and gate
Body-level findings are Established and now meet the Cycle-1 full-text rule; the regulation toy is robust for feedback and fragile for anticipation. Gate for this report: **Indeterminate** (internal checks pass; no independent review).

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S01** — Billman GE (2020). Homeostasis: The Underappreciated and Far Too Often Ignored Central Organizing Principle of Physiology. Front Physiol 11:200. doi:10.3389/fphys.2020.00200 [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC7076167/>
- **S02** — Modell H, Cliff W, Michael J, et al. (2015). A physiologist's view of homeostasis. Adv Physiol Educ 39(4):259-266. doi:10.1152/advan.00107.2015 [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC4669363/>
- **S03** — Shapiro L, Spaulding S (2021). Embodied Cognition. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/embodied-cognition/>
- **S16** — Van Gulick R. Consciousness. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/consciousness/>
- **S23** — Javaux EJ (2019). Challenges in evidencing the earliest traces of life. Nature 572:451-460. doi:10.1038/s41586-019-1436-4 [abstract only (NCBI E-utilities PMID 31435057)] <https://pubmed.ncbi.nlm.nih.gov/31435057/>
- **T01** — Sterling P (2012). Allostasis: a model of predictive regulation. Physiol Behav 106(1):5-15. doi:10.1016/j.physbeh.2011.06.004 [abstract only (NCBI E-utilities PMID 21684297)] <https://pubmed.ncbi.nlm.nih.gov/21684297/>
- **T02** — Khalsa SS, Adolphs R, Cameron OG, et al. (2018). Interoception and Mental Health: A Roadmap. Biol Psychiatry Cogn Neurosci Neuroimaging 3(6):501-513. doi:10.1016/j.bpsc.2017.12.004 [full text (PMC6054486)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC6054486/>
- **U01** — OpenStax (2022). Anatomy and Physiology 2e, §12.1 Basic Structure and Function of the Nervous System. Rice University. [full text] <https://openstax.org/books/anatomy-and-physiology-2e/pages/12-1-basic-structure-and-function-of-the-nervous-system>
- **U02** — Marzvanyan A, Alhawaj AF (2019). Physiology, Sensory Receptors. StatPearls (UCL Discovery copy). [full text (PDF)] <https://www.ncbi.nlm.nih.gov/books/NBK539861/>
- **U03** — Osilla EV, Marsidi JL, Shumway KR, Sharma S (2023). Physiology, Temperature Regulation. StatPearls (PMID 29939615). [excerpt (NCBI E-utilities; Bookshelf page blocked by bot check)] <https://www.ncbi.nlm.nih.gov/books/NBK507838/>
- **U04** — OpenStax (2022). Anatomy and Physiology 2e, §1.2 Structural Organization of the Human Body. [full text] <https://openstax.org/books/anatomy-and-physiology-2e/pages/1-2-structural-organization-of-the-human-body>
- **U05** — OpenStax (2022). Anatomy and Physiology 2e, §14.1 Sensory Perception. [full text] <https://openstax.org/books/anatomy-and-physiology-2e/pages/14-1-sensory-perception>
- **V06** — OpenStax, Anatomy and Physiology 2e, section 24.6 'Energy and Heat Balance' (CC BY) [full text (OpenStax web page)] <https://openstax.org/books/anatomy-and-physiology-2e/pages/24-6-energy-and-heat-balance>
- **V36** — Sender R, Fuchs S, Milo R (2016). Revised estimates for the number of human and bacteria cells in the body. PLoS Biol 14(8):e1002533. doi:10.1371/journal.pbio.1002533 [full text (Europe PMC PMC4991899)] <https://europepmc.org/article/PMC/PMC4991899>

## Change history
- Cycle 0 Baseline v2 (2026-10-24): see `../../Cycle-0-Baseline/`.
- Cycle 1 (x3) (2026-10-24): this version; details in `CHANGELOG.md`.
