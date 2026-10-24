# Report 1 — The Body: the physical foundation of life

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R1 |
| Version | Baseline v2 (Cycle 0, framework-aligned) |
| Status | Researched (1 bounded pass, framework-aligned); simulated (executed, see §Simulation); internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; organizing principle: GAIA Is the Motherthread) |
| Integrity rules | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |
| Conclusion labels | Established / Plausible / Philosophical/Spiritual / Hypothetical (mapping to repository statuses: `../FRAMEWORK.md` appendix) |

## Abstract
What is established about how the body sustains life, and where biological explanation currently ends. The body is organized from cells to eleven organ systems; the nervous system (central and peripheral; somatic, autonomic, enteric) senses, integrates and responds; sensory receptors transduce stimuli from the world and from inside the body; homeostatic regulation — multiple feedback loops plus feedforward — keeps internal variables within viable ranges while the body exchanges heat and matter with its environment. A toy control model (executed, all 7 checks passed) shows how feedback restores a set point, how degraded or saturated effectors fail, and that anticipation (feedforward) and feedback are complementary. Biological explanation currently ends at subjective experience (Report 5) and at the origin of life (Report 6), both recorded as unresolved.

## Contents
Purpose & exclusions · Research questions & definitions · Framework scope coverage · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Scope (framework, Report 1): biological structure, organs, nervous systems, physiology, sensory perception, homeostasis, and the body–environment interaction; domains anatomy, physiology, biology and embodied experience. Excluded: clinical guidance, disease-specific physiology, and any claim about soul or spirit (Reports 3–4).

## Research questions and definitions
1. How is the body organized (levels, organs, organ systems)? 2. How is the nervous system organized and what does it do? 3. How does sensory perception begin in the body? 4. How does the body regulate itself (homeostasis, feedforward/allostasis)? 5. How does the body interact with its environment? 6. Where does biological explanation currently end? *Definitions:* homeostasis = self-regulation that maintains internal variables within ranges while adjusting to external change (S01); interoception = sensing of internal bodily signals (T02); transduction = conversion of a stimulus into a neural signal (U05).

## Framework scope coverage
Every scope item the framework lists for this report, with the claims that address it.

| Framework scope item | Claims | Labels |
|---|---|---|
| Biological structure & organs | C0v2-R1-01 | Established |
| Nervous systems | C0v2-R1-02; C0v2-R1-03 | Established |
| Sensory perception | C0v2-R1-04; C0v2-R1-05; C0v2-R1-10 | Established |
| Physiology & homeostasis | C0v2-R1-06; C0v2-R1-07; C0v2-R1-08; C0v2-R1-11; C0v2-R1-12; C0v2-R1-13; C0v2-R1-15 | Established, Plausible |
| Body–environment interaction | C0v2-R1-09; C0v2-R1-13 | Established |
| Embodied experience | C0v2-R1-14; C0v2-R1-10 | Established, Philosophical/Spiritual |
| Where biological explanation ends | C0v2-R1-16 | Established |

## Methods
One bounded, framework-aligned research pass (2026-10-23/24) that reuses valid v1 sources and adds new ones. Sources were primary texts, primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), open textbooks and official assessments, found by targeted search and fetched directly. Each fetched page was snapshotted and its SHA-256 recorded; third-party text is not redistributed. Each claim is tied to the passage that supports it (locator) and labelled with a framework label plus a repository class/status. Where only an abstract or excerpt was accessible, the access mode says so. Every Established literature claim carries a verification phrase that was re-checked against a fresh fetch of its source (see `../Verification/VERIFICATION.md`). Simulations were specified in `simulation/SPEC.md` before execution and re-run fresh for v2.

## Evidence and findings
Label counts in this report's ledger: Established: 13, Plausible: 2, Philosophical/Spiritual: 1, Hypothetical: 0.

**Structure.** Textbook anatomy describes the body in levels of increasing complexity up to eleven organ systems (C0v2-R1-01, Established).

**Nervous systems.** The CNS is the brain and spinal cord; the PNS is everything else; basic functions are sensation, integration and response; somatic, autonomic and enteric divisions handle voluntary, involuntary and gastrointestinal control (C0v2-R1-02/03, Established).

**Sensory perception.** Receptors transduce light, chemical and mechanical energy into electrochemical signals, serve exteroception, interoception and proprioception, adapt to constant stimuli, and keep modality via labelled lines (C0v2-R1-04/05, Established). Interoception links the internal milieu to the nervous system (C0v2-R1-10, Established for the definition).

**Homeostasis.** Homeostasis is a central organizing concept of physiology, realized by multiple feedback loops plus feedforward (C0v2-R1-06/07/08, Established). Sterling's allostasis argues the goal is anticipatory adjustment rather than constancy (C0v2-R1-11, Plausible / contested).

**Environment.** Thermoregulation is the clearest case of body–environment coupling: hypothalamic integration of skin and core thermoreceptors keeps core temperature near 37 °C (C0v2-R1-09, Established; excerpt-level access).

**Simulation.** SIM-R1-C0 reproduces the textbook behaviours of a feedback loop and shows anticipation reduces peak error but cannot correct its own estimation error without feedback (C0v2-R1-12/13, Established for the toy only).

**Where explanation ends.** How neural and bodily processes give rise to phenomenal experience is unresolved (the 'hard problem', S16), and the origin of life is unresolved (earliest traces disputed, S23) (C0v2-R1-16).

## Competing theories and alternatives
Homeostasis-centred physiology (S01, S02: constancy within ranges, feedback plus feedforward) vs allostasis (T01: prediction and anticipatory adjustment as primary; feedback 'inherently inefficient'). The dispute is partly terminological — S01 already folds feedforward into homeostasis. Embodied cognition (S03) contests whether the body merely causes or partly constitutes cognition. Neither dispute is settled here.

## Simulation
**SIM-R1-C0** — status: executed; run finished 2026-10-24T00:24:40Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **True**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | no-control x(T) = analytic 9.933 (tends to 10.0) | `9.9328` | **Pass** |
| E2 | P steady error 0.4762 | `0.4762` | **Pass** |
| E3 | \|PI tail mean\|<0.02 | `0.001` | **Pass** |
| E4 | degraded peak > intact peak and slower recovery | `[1.790515460146184, 0.3600061867586858, 10.99, 4.49]` | **Pass** |
| E6 | PI+feedforward (anticipation, ff gain) peak < 0.5 x PI peak | `[0.08640535319355025, 0.3600061867586858]` | **Pass** |
| E7 | feedforward-only (no feedback) x(T) = analytic 1.987: anticipation with estimation error cannot restore the set point alone | `1.9866` | **Pass** |
| E5 | saturated PI final \|x\| > 0.05 | `9.9014` | **Pass** |

Specification (written before execution, incl. v2 changes and recorded deviations): `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in `simulation/EXECUTION_RECORD.json`). Simulation results are labelled Established only for the model itself, never for the real-world system.

## Claim-to-source ledger
Machine-readable: `claims/claims.csv` (includes verification phrases); sources: `sources/sources.csv`.

| ID | Claim | Framework label | Repo class / status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0v2-R1-01 | Human body structure is described in textbook anatomy as levels of organization of increasing complexity (chemical → cells → tissues → organs → organ systems → organism), with eleven organ systems. | **Established** | Empirical / Supported | U04 | OpenStax A&P 2e §1.2 learning objectives and Fig. 1.3 text | High | Textbook convention; the level scheme is descriptive, not a mechanism. |
| C0v2-R1-02 | The nervous system is divided anatomically into the central nervous system (brain and spinal cord) and the peripheral nervous system (everything else); its basic functions are sensation, integration and response. | **Established** | Empirical / Supported | U01 | OpenStax A&P 2e §12.1 'The Central and Peripheral Nervous Systems'; 'Basic Functions' | High |  |
| C0v2-R1-03 | Functionally, the somatic nervous system governs conscious perception and voluntary motor responses, the autonomic nervous system governs involuntary responses (smooth/cardiac muscle, glands), and the enteric nervous system handles a set of gastrointestinal functions. | **Established** | Empirical / Supported | U01 | §12.1 'Controlling the Body' | High | 'Voluntary' is used loosely (some somatic responses are reflexes, per source). |
| C0v2-R1-04 | Sensory receptors convert (transduce) stimuli of different kinds into the electrochemical signals of the nervous system; sensory systems include exteroceptors, interoceptors and proprioception. | **Established** | Empirical / Supported | U05;U02 | U05 §14.1 intro; U02 Introduction | High |  |
| C0v2-R1-05 | Sensory receptors show adaptation (declining firing to a constant stimulus) and modality specificity via labeled lines; what is perceived depends on where the nerve fibre terminates in the CNS. | **Established** | Empirical / Supported | U02 | 'Adaptation'; 'Labeled line principle'; 'Issues of Concern' | High (textbook) | StatPearls review; perception itself is not reducible to receptor coding (see R2, R5). |
| C0v2-R1-06 | Homeostasis is treated as a central unifying concept of physiology: a self-regulating process that maintains internal stability while adjusting to changing external conditions. | **Established** | Empirical / Supported | S01 | Abstract | High | Essay-format review by one author; 'central' is a disciplinary judgement. |
| C0v2-R1-07 | Homeostatic regulation involves multiple interacting feedback systems and feedforward control, not a single negative-feedback cycle. | **Established** | Empirical / Supported | S01 | Abstract; feedforward section | High |  |
| C0v2-R1-08 | A generic negative-feedback mechanism comprises sensor, error detector comparing the signal with a set point, controller and effector; 'set point' does not imply a fixed value. | **Established** | Empirical / Supported | S02 | Text on the generic model and set point | High | Pedagogical model; some systems may lack an explicit set-point representation. |
| C0v2-R1-09 | The body interacts with its thermal environment through thermoregulation: the preoptic hypothalamus integrates peripheral (skin) and central thermoreceptor input to keep core temperature near 37 ± 0.5 °C by balancing heat production and loss. | **Established** | Empirical / Supported | U03 | StatPearls 'Physiology, Temperature Regulation' (PubMed excerpt) | High | Excerpt-level access (full Bookshelf page blocked by a bot check). |
| C0v2-R1-10 | Interoception is the nervous system's sensing, interpretation and integration of signals from within the body, contributing to homeostatic functioning; interoceptive dysfunction is increasingly recognized in several mental-health conditions. | **Established** | Empirical / Supported | T02 | Abstract | High (definition) / Medium (clinical link) | Clinical link is associational and heterogeneous (per source: conceptual and methodological challenges). |
| C0v2-R1-11 | Allostasis (Sterling) argues that the primary goal of regulation is anticipatory adjustment, not constancy, and that feedback error-correction is inherently inefficient; this competes with homeostasis-centred accounts (S01) that include feedforward within homeostasis. | **Plausible** | Interpretive/philosophical / Contested | T01;S01 | T01 abstract; S01 abstract | Medium | Disagreement is partly terminological; neither source tests the other. |
| C0v2-R1-12 | In SIM-R1-C0 (toy loop), PI control restored the set point after a step load (tail mean 0.001), P-only left the analytic residual 0.476, degraded gains raised peak deviation (1.79 vs 0.36) and slowed recovery (10.99 vs 4.49), and a load beyond effector capacity was not corrected. | **Established** | Mathematical/computational / Supported | SIM-R1-C0#E2;SIM-R1-C0#E3;SIM-R1-C0#E4;SIM-R1-C0#E5 | Report-1-Body/simulation/outputs/summary.json | High (for the toy only) | Toy model; no physiological parameters. |
| C0v2-R1-13 | In SIM-R1-C0, adding anticipatory (feedforward) control cut the peak deviation from 0.360 to 0.086, while feedforward alone with a 20% estimation error left a residual of 1.987 — in this linear toy, anticipation and feedback are complementary. | **Established** | Mathematical/computational / Supported | SIM-R1-C0#E6;SIM-R1-C0#E7 | outputs/summary.json (PI_feedforward, feedforward_only) | High (toy only) | Does not decide the homeostasis–allostasis dispute (C0v2-R1-11). |
| C0v2-R1-14 | Embodied cognition holds that the body and body–environment interaction contribute to or constitute cognition; whether the role is constitutive or merely causal is disputed. | **Philosophical/Spiritual** | Interpretive/philosophical / Contested | S03 | §§2.1, 5 (coupling–constitution) | High (as description) | Replicability concerns for some embodied-cognition findings (S03). |
| C0v2-R1-15 | The principle that disruption of homeostatic mechanisms is what leads to disease is asserted by S01; its generality was not tested in this pass. | **Plausible** | Interpretive/philosophical / Indeterminate | S01 | Abstract | Medium | Some conditions (e.g. traumatic) are not naturally framed as homeostatic failure. |
| C0v2-R1-16 | Where biological explanation currently ends: how physical/neural processes give rise to phenomenal ('what it is like') experience — the 'hard problem' — remains without an accepted explanation; the origin of life is also unresolved (earliest traces disputed). | **Established** | Interpretive/philosophical / Supported | S16;S23 | S16 §on the hard problem; S23 abstract | Medium-High | A statement about the state of the literature, not a claim that explanation is impossible. |

## Relationships to other reports
R2 Mind: nervous system and interoception as the bodily basis of cognition and emotion (link register L04–L06). R5 Consciousness: level of consciousness tracks brain-state complexity (L17); subjective experience is where biological explanation ends. R6 Earth: homeostasis ↔ Daisyworld is an analogy only (L01, L02); thermoregulation couples the body to Earth's energy flows (L03). GAIA motherthread: the body is the nearest-scale instance of a living system inside Earth's living whole — a Philosophical/Spiritual framing, not a finding.

## Ethical implications
Framing disease as 'homeostatic failure' (C0v2-R1-15) can over-reach; this pass did not test its generality and it should not guide clinical judgement. The toy model is not physiology.

## Limitations and counterevidence
Textbook and review sources (OpenStax, StatPearls) are reliable for consensus anatomy but not for frontier questions. StatPearls thermoregulation was read as a PubMed excerpt only (Bookshelf page blocked by a bot check). Organ-system detail (e.g. cardiovascular, immune, endocrine mechanisms) is covered at survey level only. Single-pass, single-agent research; not independently reviewed.

## Open questions and falsification criteria
- Is anticipatory (allostatic) regulation the primary regulatory strategy? *Test:* compare error magnitude/frequency in systems with and without predictive cues. *Reject* allostasis-as-primary if feedback-only control matches anticipatory control in matched conditions.
- How general is 'homeostatic failure' as an account of disease? *Test:* classify disease categories by whether a regulated variable leaves its range first.
- Where explanation ends: subjective experience (R5) and origin of life (R6) — open.

## Conclusion with evidence classification
Established: body organization, nervous-system divisions and functions, sensory transduction/adaptation, homeostasis as feedback-plus-feedforward regulation, thermoregulatory coupling to the environment, and the toy-model behaviours. Plausible: allostasis as the primary regulatory principle; homeostatic failure as a general account of disease. Philosophical/Spiritual: whether the body constitutes cognition. Unresolved: how bodily processes yield experience; life's origin.

## References
- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md> (accessed 2026-10-23; full text (GitHub connector))
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md> (accessed 2026-10-24; full text (owner-supplied file); snapshot SHA-256 `2bad2984fe2109de…`)
- **S01** — Billman GE (2020). Homeostasis: The Underappreciated and Far Too Often Ignored Central Organizing Principle of Physiology. Front Physiol 11:200. doi:10.3389/fphys.2020.00200 <https://pmc.ncbi.nlm.nih.gov/articles/PMC7076167/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `01b91f81929856e9…`)
- **S02** — Modell H, Cliff W, Michael J, et al. (2015). A physiologist's view of homeostasis. Adv Physiol Educ 39(4):259-266. doi:10.1152/advan.00107.2015 <https://pmc.ncbi.nlm.nih.gov/articles/PMC4669363/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `60a3d718d7c987f5…`)
- **S03** — Shapiro L, Spaulding S (2021). Embodied Cognition. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/embodied-cognition/> (accessed 2026-10-23; full text; snapshot SHA-256 `406f421bebc61f3e…`)
- **S16** — Van Gulick R. Consciousness. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/consciousness/> (accessed 2026-10-23; full text; snapshot SHA-256 `9e814583974e4f21…`)
- **S23** — Javaux EJ (2019). Challenges in evidencing the earliest traces of life. Nature 572:451-460. doi:10.1038/s41586-019-1436-4 <https://pubmed.ncbi.nlm.nih.gov/31435057/> (accessed 2026-10-23; abstract only (NCBI E-utilities PMID 31435057); snapshot SHA-256 `a9af9f5102d2134f…`)
- **T01** — Sterling P (2012). Allostasis: a model of predictive regulation. Physiol Behav 106(1):5-15. doi:10.1016/j.physbeh.2011.06.004 <https://pubmed.ncbi.nlm.nih.gov/21684297/> (accessed 2026-10-24; abstract only (NCBI E-utilities PMID 21684297); snapshot SHA-256 `1bb1ebcdf6858caa…`)
- **T02** — Khalsa SS, Adolphs R, Cameron OG, et al. (2018). Interoception and Mental Health: A Roadmap. Biol Psychiatry Cogn Neurosci Neuroimaging 3(6):501-513. doi:10.1016/j.bpsc.2017.12.004 <https://pmc.ncbi.nlm.nih.gov/articles/PMC6054486/> (accessed 2026-10-23; full text (PMC6054486); snapshot SHA-256 `59856fef067f6301…`)
- **U01** — OpenStax (2022). Anatomy and Physiology 2e, §12.1 Basic Structure and Function of the Nervous System. Rice University. <https://openstax.org/books/anatomy-and-physiology-2e/pages/12-1-basic-structure-and-function-of-the-nervous-system> (accessed 2026-10-24; full text; snapshot SHA-256 `ee048efef6d07a5b…`)
- **U02** — Marzvanyan A, Alhawaj AF (2019). Physiology, Sensory Receptors. StatPearls (UCL Discovery copy). <https://www.ncbi.nlm.nih.gov/books/NBK539861/> (accessed 2026-10-24; full text (PDF); snapshot SHA-256 `9677de11f37f599f…`)
- **U03** — Osilla EV, Marsidi JL, Shumway KR, Sharma S (2023). Physiology, Temperature Regulation. StatPearls (PMID 29939615). <https://www.ncbi.nlm.nih.gov/books/NBK507838/> (accessed 2026-10-24; excerpt (NCBI E-utilities; Bookshelf page blocked by bot check); snapshot SHA-256 `d137a2c30e1c3430…`)
- **U04** — OpenStax (2022). Anatomy and Physiology 2e, §1.2 Structural Organization of the Human Body. <https://openstax.org/books/anatomy-and-physiology-2e/pages/1-2-structural-organization-of-the-human-body> (accessed 2026-10-24; full text; snapshot SHA-256 `33d4fa272c476ceb…`)
- **U05** — OpenStax (2022). Anatomy and Physiology 2e, §14.1 Sensory Perception. <https://openstax.org/books/anatomy-and-physiology-2e/pages/14-1-sensory-perception> (accessed 2026-10-24; full text; snapshot SHA-256 `df37712508c432b6…`)

## Change history
- **2026-10-24 — Baseline v2 (Cycle 0, framework-aligned).** Rewritten against FRAMEWORK.md. Added nervous system (C0v2-R1-02/03), structure (01), sensory perception (04/05), environment/thermoregulation (09), interoception (10), allostasis (11), feedforward simulation checks E6–E7 (13), and 'where explanation ends' (16). v1 claims C0-R1-01…06 map to C0v2-R1-06, 07, 08, 14, 12, 15. Sources added: U01–U05, T01, T02.
- 2026-10-23 — Baseline (Cycle 0) v1: first version, built mainly on Research/README.md and RESEARCH_PLAN_EXTENSION.md (v1 files are superseded in place; the full v1 text remains in this branch's git history, commits before the v2 push). The earlier GAIA-PRELIM v0.1.0 package was deleted from `main` by the owner (commits 802e17a, df9a561) and never contained committed per-report files; nothing from it is reused.
