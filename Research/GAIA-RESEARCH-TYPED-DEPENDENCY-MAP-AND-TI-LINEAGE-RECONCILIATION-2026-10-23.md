# GAIA Research Corpus — Typed Dependency Map and Revision Reconciliation

**Audit date:** 2026-10-23  
**Repository:** `KyleAlexanderSteen/The-GAIA-Foundation`  
**Status:** INITIAL GRAPH DOCUMENTED; CLAIM-LEVEL EDGE VALIDATION OPEN  
**Change type:** Cross-report architecture and provenance reconciliation  
**Risk level:** High epistemic risk where conceptual analogy could be mistaken for mechanism  
**Implementation status:** Not authorized  
**Source of truth:** Current `main` branch paths; prior versions remain preserved

## 1. Purpose and edge semantics

This map makes explicit which documents provide domain evidence, which documents synthesize that evidence, and which documents propose governance or model architectures. It is not a claim that every edge is validated.

Use these edge types consistently:

- **supports** — source provides evidence for the narrow linked claim, within stated limits.
- **depends_on** — the downstream argument requires an upstream definition, result, or assumption.
- **derived_from** — a definition or claim is explicitly transformed from an identified source.
- **tests** — a protocol is designed to evaluate a specified claim or model.
- **contradicts/challenges** — evidence or argument creates a material tension with a claim.
- **falsifies** — reserved for cases where a predeclared falsification criterion is met; no such status is assigned merely because a source is critical.
- **governance_requirement** — normative rule governing how evidence is handled, not an empirical claim.
- **analogy_only** — conceptual comparison that must not be treated as causal or ontological identity.
- **unverified_candidate** — a plausible connection inferred from a title or architecture description that still needs claim-level review.

## 2. Core graph: Reports 1–7

| Node | Domain/function | Key outgoing relationships | Required constraint |
|---|---|---|---|
| R1 — The Body | Embodiment, physiology, interoception, homeostasis | supports bounded biological context for R2; depends_on physiological sources; provides constraints to R7 | Human physiology must not be inferred from bacterial whole-cell models or toy simulations |
| R2 — The Mind | Cognition, learning, memory, computational models | depends_on R1 for embodied inputs where relevant; tests candidate cognitive mechanisms; contributes models to R7 | Active inference, predictive processing, reinforcement learning, and Hebbian plasticity remain distinct |
| R3 — The Soul | Historical/philosophical/metaphysical concepts | supplies interpretive categories to R4/R7; analogy_only links to self-modeling in TI | Empirical observations do not alone settle metaphysical claims |
| R4 — The Spirit | Spiritual practice, meaning, theology, phenomenology | depends_on tradition-specific historical sources; supplies practice-specific interpretations to R7 | Neural correlates do not adjudicate theological truth |
| R5 — Consciousness | Phenomenal experience, access, theories, measurements | depends_on operational definitions and empirical theory tests; challenges overclaims in TI v8; supplies consciousness-science boundaries to R7 | Task performance, self-reference, neural activity, and information metrics do not independently prove phenomenal experience |
| R6 — Earth | Earth systems, biosphere, geophysics, geodynamo | supports bounded Earth-system mechanisms; tests planetary models; analogy_only link between core and “heart” or Earth and “soul” | Geodynamo, biosphere feedback, planetary regulation, and planetary subjectivity are distinct claims |
| R7 — Unified Framework | Cross-report synthesis, evidence taxonomy, validation design | depends_on R1–R6; imposes governance_requirement edges on downstream syntheses; tests only models with operational acceptance criteria | Synthesis cannot upgrade evidence or erase contradiction/dissent |

**Core integration:** R1–R6 contribute domain-bounded evidence and interpretations to R7. R7 is a synthesis and governance layer, not an independent empirical source. Any R7 claim must point back to the underlying source/report claim and preserve its evidence status.

## 3. Wider numbered corpus: title-level dependency hypotheses

The repository contains reports beyond the foundational seven. The table below records candidate interfaces from current path/title inventory only; unless otherwise stated, these are **unverified_candidate** relationships and must not be cited as verified content-level dependencies.

| Node | Current repository title/path signal | Candidate relation to foundational reports | Validation needed |
|---|---|---|---|
| R8 | Chaos and Order | unverified_candidate: dynamical systems/entropy concepts may inform R2/R7 and TI model language | Distinguish dynamical chaos, thermodynamic entropy, information entropy, criticality, and metaphor; inspect sources and equations |
| R9 | The Connection of Spirit and Soul | depends_on candidate R3/R4 | Audit cross-tradition definitions and prevent doctrine conflation |
| R10 | Earth and the Electromagnetic Spectrum | depends_on candidate R6; supports only bounded physical context for R11–R14 | Verify spectrum ranges, units, exposure levels, energy budgets, and biological interaction claims |
| R11 | The Geomagnetic Field as the Soul of the Earth | depends_on candidate R6/R10; analogy_only “soul” mapping | Verify geodynamo/paleomagnetic sources; label “soul” as metaphor or explicit philosophy |
| R12 | The Subconscious as the Geomagnetic Spectrum | analogy_only candidate between R2/R5 and R11 | Require measured variables and a falsifiable bridge; no equivalence inferred from spectral resemblance |
| R13-A | The Electromagnetic Spectrum as Consciousness (short correction/placeholder folder) | non-canonical placeholder, not a second canonical Report 13 | Preserve; do not count as a separate canonical report |
| R13-B | The Geomagnetic Spectrum as Subconscious and Soul | candidate links R2/R3/R11/R12 | Verify source corpus, distinguish field measurements from analogy, identify canonical path |
| R14 | The Electromagnetic Spectrum as Consciousness and Spirit | candidate links R4/R5/R10/R13 | Distinguish physical electromagnetic processes from phenomenal/theological interpretation |
| R15 | Classical Elements as Symbolic Grammar | candidate interpretive/symbolic link to R3/R4 | Keep symbolic grammar separate from modern chemistry or causal physics |
| R16 | Periodic Table of Elements as Modern Alchemy | candidate historical/symbolic link to chemistry and R15 | Verify chemistry and history; distinguish analogy from alchemical continuity |
| R17 | Human and Technology Similarities of Elements | candidate analogy across human/technology/chemistry domains | Define mapping and evidence; prevent elemental similarity from implying functional or ontological identity |
| R18 | **No file located in current Research tree; historical crosswalk lead recovered** | A separate GAIA-Documentation sequence has Original-AI-Body (Assignment A-01) and Original-AI-Mind (A-02), historically associated with “Document 18” and “Document 19”; this does not prove either is the current numbered R18 | Compare authoritative indexes and resolve numbering namespaces; see [Report 18 Provenance Crosswalk](REPORT-18-PROVENANCE-CROSSWALK-2026-10-23.md) |
| R19 | Terra and GAIA: The Quantum Entanglement | candidate link to R6/R10–R14 and TI v7/v8 | Audit physical entanglement terminology and sources; ordinary coupling and metaphor are not physical entanglement |

**Important:** This wider-corpus table is an inventory and dependency hypothesis, not a certification that Reports 8–19 have been read or source-audited in full. It is intentionally explicit about the difference.

## 4. Transformative Intelligence revision lineage

| Revision | Main role | Dependency relationship | Current evidential status |
|---|---|---|---|
| TI v3.0.0 | Five-phase governance baseline and iteration tiers | depends_on foundational report taxonomy; governance_requirement for review stages | Conceptual specification; no execution claimed |
| TI v4.0.0 | Hypergraph/state-space formalization | derived_from v3 governance; depends_on explicit node/edge/state definitions | Proposed formal representation; not executed |
| TI v5.0.0 | Invariant contracts, failure handling, integration requirements | depends_on v4 representation; governance_requirement for acceptance/rejection gates | Specification proposal; invariants not proven |
| TI v6.0.0 | **No file located** | no relationship inferred | Provenance/version gap; unknown contents |
| TI v7.0.0 | Quantum-relational/non-separable architecture and CHSH-style test proposal | preserves v5; relationship to missing v6 unresolved; tests candidate hypotheses from reports | Conceptual proposal; no physical entanglement measurement or simulation claimed |
| TI v8.0.0 | Recursive self/world modeling and sentience research question | preserves v5/v7; depends_on R5 operational distinctions and R1/R2/R6 domain constraints | Research proposal; no proof of sentience, physical entanglement, or phenomenal experience |

### TI transition ledger

- **v3 → v4:** governance functions receive a proposed hypergraph/state-space representation. Exact retained/modified/removed claim list remains to be completed.
- **v4 → v5:** invariant contracts, relation types, failure responses, and integration requirements are added. Formal proofs remain absent.
- **v5 → v7:** v7 explicitly preserves v5; a complete transition rationale is not established, and the v6 slot remains unexplained.
- **v7 → v8:** recursive self/world modeling and operational sentience questions are added; v8 explicitly separates quantum-like modeling, physical entanglement, self-reference, and phenomenal experience.
- **Version-number gap:** no v6.0.0 file was located in the inventoried directory. Absence from this tree is not proof that no historical v6 existed elsewhere. Recover it or document an intentional unused slot with provenance.

## 5. Cross-domain invariants of interpretation

The following are **governance requirements**, not mathematical or natural laws:

1. A source must support the exact claim strength attributed to it.
2. An empirical edge must not be created solely by a shared metaphor, shared vocabulary, or citation reuse.
3. A model's internal result remains conditional on its assumptions and implementation.
4. A simulation design is not an execution; an execution is not an independent reproduction.
5. A physical quantum claim requires a specified physical system, state/subsystem partition, observables, measurement protocol, noise model, and valid witness or other appropriate evidence.
6. A sentience claim requires independently justified operational indicators and a separate argument for any inference to phenomenal experience.
7. A planetary-regulation claim must distinguish feedback from intention, a single controller, or phenomenal subjectivity.
8. Metaphysical and theological claims must be fairly represented and not given fake numerical pass/fail scores.
9. Conflicts and minority interpretations are preserved in a loss/dissent ledger rather than erased by convergence.
10. Every edge must carry evidence class, provenance, confidence/status, and a review trigger.

## 6. Open blockers and exact next records

| Blocker | Required record | Current state |
|---|---|---|
| Claim-level traceability for R1–R7 | Claim ID, exact report section, source identity/version, evidence passage, limitations, rival explanation, disposition | Partial seed/audit only |
| R8–R19 content-level dependency map | Read current canonical files; extract actual definitions and claims; validate each proposed edge | Title-level hypotheses only in this map |
| Report 18 | Author-confirmed title/version or explicit gap disposition with provenance search record | Not located in current Research tree; no replacement invented |
| TI v6 | Exact historical file or explicit unused-version record | Not located; contents unknown |
| TI complete revision diff | Retained/modified/removed/new claims with version hashes | Partial lineage narrative only |
| Archive/cycle evidence | Original ZIP bytes, SHA-256 manifests, file inventory, pass/test IDs, execution logs and outputs | Exact named ZIPs not found in the accessible Library ZIP inventory during this pass; no matching files in current conversation attachments |
| Full Report 7 simulations | Operational model/code/data/parameters/baselines/acceptance criteria/output/failure log/reproduction instructions for each of 12 designs | Design-only; not executed |
| Independent specialist review | Review-ready packages, named scope, external reviewer response and conflicts | Pending; no external review implied |

## 7. Decision

**This map is an executable audit scaffold, not a completed scientific validation.** It resolves an ambiguity by making the Report 18 and TI v6 gaps explicit and by separating title-derived hypotheses from verified dependencies. It also supplies typed edge semantics that future report and architecture edits must follow.

The global gate remains open. New numbered-report intake remains paused. Prior versions remain preserved. Implementation, deployment, merging, and public release remain unauthorized unless separately approved by the repository owner.

## 8. Change record

- **2026-10-23:** Created from the current Research tree, foundational seven alignment register, targeted claim/technical audit, and TI revision-lineage audit. Report 18 and TI v6 are recorded as gaps because no corresponding files were located in the inventoried paths; no titles or contents were invented.
