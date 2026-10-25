# The GAIA Foundation

**The Foundation In Which GAIA Has Been Built Upon.**

This repository holds the foundational research corpus for GAIA and the governance standard it is held to. Research lives under [`Research/`](Research/). Governance lives under [`GOVERNANCE/`](GOVERNANCE/).

**Research first. Integrity before intelligence. Responsibility at every scale.**

## Current status (2026-10-25)

- **Every research gate is INDETERMINATE.** All internal checks pass or are reported, but no independent human review and no ethics review has been done. INDETERMINATE is never PASS. **The research and ethics gates stay INDETERMINATE until the required independent reviews (including an ethics review) and their evidence are complete.** Nothing in this README upgrades any gate.
- **Merged into `main` means accepted by the owner, not verified.** See [`GOVERNANCE/GATE_AUTHORITY.md`](GOVERNANCE/GATE_AUTHORITY.md). The repository owner (@KyleAlexanderSteen) is the final authority for every gate.
- **Implementation is not authorized.** Research, successful tests and technical capability do not grant permission to deploy (Universal Regulation, Law 7).
- **Universal Regulation standard:** Proposed, not adopted, not implemented. Audit v2 gate: INDETERMINATE (see [`GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v2.md`](GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v2.md)).

## What is on `main` (as of commit `fdec378a`, PR #39)

| Area | Path | Contents | Gate |
|---|---|---|---|
| Research index and rules | [`Research/README.md`](Research/README.md), [`Research/RESEARCH_PLAN_EXTENSION.md`](Research/RESEARCH_PLAN_EXTENSION.md) | Claim classes, responsibility ladder, integration mandate, lifecycle, report requirements, gates | — |
| Work queue | [`Research/WORK_QUEUE.md`](Research/WORK_QUEUE.md) | Checklist of completed and incoming reports, ticked as each is verified | — |
| Seven-Report cycles | [`Research/Cycles/`](Research/Cycles/) | Cycle 0 (Baseline v2), Cycle 1 (x3), Cycle 2 (x6), Cycle 3 (x9), Cycle 4 (x12). Reports 1 Body, 2 Mind, 3 Soul, 4 Spirit, 5 Consciousness, 6 Earth, 7 Unified, each with claims, sources, simulations and execution records | INDETERMINATE |
| Master Report | [`Research/Master-Report-Unconditional-and-Conditional-Love/`](Research/Master-Report-Unconditional-and-Conditional-Love/) | Unconditional and Conditional Love, v1 (36 claims; SIM-MR-1) | INDETERMINATE |
| Soul / Spirit / Subconscious / Consciousness track | [`Research/Tracks/Soul-Spirit-Subconscious-Consciousness/`](Research/Tracks/Soul-Spirit-Subconscious-Consciousness/) | Track Cycles A (x3), B (x6), C (x9), D (x12) | INDETERMINATE |
| Phases track | [`Research/Tracks/Phases/`](Research/Tracks/Phases/) | Six phases (Divergence, Insurgence, Allegiance, Convergence, Ascendence, Transcendence), each Baseline, x3, x6, x9, x12, and the six-phase synthesis (`SYNTHESIS.md`) | INDETERMINATE |
| Program Coordination track | [`Research/Tracks/Program-Coordination/`](Research/Tracks/Program-Coordination/) | PC-4 Research-to-Domain Map (`PC-4-Research-to-Domain-Map/MAP.md`, PR #30) and PC-1 Program Charter and Master Register Reconciliation (`PC-1-Register-Reconciliation/REGISTER.md`, PR #31), each Baseline, x3, x6, x9, x12; owner decisions open | INDETERMINATE |
| Cross-repository reports | [`Research/Tracks/Cross-Repository/`](Research/Tracks/Cross-Repository/) | N-A Level-Name Crosswalk, GAIA-Documentation ↔ Foundation (`N-A-Level-Name-Crosswalk/CROSSWALK.md`, PR #32), Baseline, x3, x6, x9, x12; options open for the owner. GAIA-Documentation: *Removed 2026-10-25: repository deleted by owner; to be uploaded later.* The report's files are kept as they were. | INDETERMINATE |
| Connections | [`Research/Tracks/Connections/`](Research/Tracks/Connections/) | The Connection: Soul, Spirit, Subconscious and Consciousness (`E1-Soul-Spirit-Subconscious-Consciousness/CONNECTION.md`, PR #33), Baseline, x3, x6, x9, x12, with a self-audit note (`AUDIT_2026-10-25.md`) | INDETERMINATE |
| Totality of Governance track | [`Research/Tracks/Totality-of-Governance/`](Research/Tracks/Totality-of-Governance/) | ToG 1 Constitutional Commitments, Baseline, x3, x6, x9, x12 (owner-supplied; produced outside this repo by Perplexity (AI) per the files; `INTAKE_RECORD.md`). On branch `research/tog1-filed` until the owner merges | INDETERMINATE; x9 validator-reuse FAIL and x12 check A1 FAIL recorded |
| Maps and Matrix | [`Research/Maps-and-Matrix/`](Research/Maps-and-Matrix/) | Versions v1–v44 (v39–v43: the Connection overlay; v44: the ToG 1 overlay, on `research/tog1-filed` until merged): claim maps, 625-cell matrix (Transcendence in phases-track overlay files; 625 -> 750 pending owner approval), link graphs, simulation index | derived; no gate of their own |
| Governance | [`GOVERNANCE/`](GOVERNANCE/) | Universal Regulation standard 0.1.0 (Proposed), Totality of Governance draft v0.1.0 (`TOTALITY_OF_GOVERNANCE_DRAFT_v0.1.0.md`), audits v1 and v2, risk levels, gate authority, Law 2 crosswalk, product register, change log, agent push log | INDETERMINATE |
| Research tooling | [`Research/tools/`](Research/tools/) | `gaia_tools` 0.6.0 (data model 1.5.0): validators, reruns, claim-source checks, maps (research tooling only; no service, no deployment) | — |

Claims carry one of four labels: **Established, Plausible, Philosophical/Spiritual, Hypothetical**. How these map onto Law 2's six distinctions is in [`GOVERNANCE/LAW2_CROSSWALK.md`](GOVERNANCE/LAW2_CROSSWALK.md).

### Reports finished since PR #27

| Report | PR | Merged into `main` |
|---|---|---|
| PC-4: Research-to-Domain Map | #30 | 2026-10-25 |
| PC-1: Program Charter and Master Register Reconciliation | #31 | 2026-10-25 |
| N-A: Level-Name Crosswalk | #32 | 2026-10-25 |
| The Connection: Soul, Spirit, Subconscious and Consciousness | #33 | 2026-10-25 |

Merged means accepted by the owner, not verified: every one of these stays INDETERMINATE.

### Merged after PR #33 (housekeeping, no new research)

| PR | Change |
|---|---|
| #34 | README status reconcile, branch-protection check recorded (not active), self-audit of The Connection |
| #35 | Removed committed `__pycache__` files; added `.gitignore` |
| #36 | `PRINCIPLES.md`: founding principle 1, Truth with Integrity |
| #37 | GAIA repositories section: links to the ten new GAIA repositories (Human and Intelligence Knowledge, Capabilities, Skills and Powers; Ontology; Map and Matrix) |
| #38 | Wording reconcile: the Foundation is the active source of truth, the Encyclopedia backup only; Map v1.2 latest |
| #39 | Maps & Matrix index: all 43 versions (v1–v43) listed from the actual folders |

## Work in progress (not on `main`; the owner reviews and merges)

**Update 2026-10-25:** `research/tog1-filed` (PR PR_PLACEHOLDER) files ToG 1 (Baseline–x12), adds Maps v44, restructures the Work Queue's ToG checklist and removes live references to deleted repositories. The paragraph below is kept as written at PR #38.

As of 2026-10-25 (`main` @ `bd3a085a`, PR #37) there were **no open research pull requests** before this README update (checked with the GitHub pull-request list). PR #28 (`research/work-queue-gaiadoc`) and PR #29 (`research/work-queue-phases-done`), listed here before, are both merged. This wording reconcile is on `research/authority-reconcile` until the owner merges it.

The full list of incoming reports is in [`Research/WORK_QUEUE.md`](Research/WORK_QUEUE.md).

Branches already merged and kept for history: `research/cycle-0-baseline`, `cycle-1-x3`, `maps-c0-c1`, `cycle-2-x6`, `cycle-3-x9`, `cycle-4-x12`, `master-report`, `track-ssc-a-x3` … `track-ssc-d-x12`, `governance-universal-regulation`, `governance-audit-fixes`, `phase-divergence-c0` … `phase-divergence-x12`, `phase-insurgence-c0` … `phase-insurgence-x12`, `phase-allegiance-c0` … `phase-allegiance-x12`, `phase-convergence-c0` … `phase-convergence-x12`, `phase-ascendence-c0` … `phase-ascendence-x12`, `phase-transcendence-c0` … `phase-transcendence-x12`, `phase-synthesis`, `work-queue`, `work-queue-update`, `work-queue-indigenous`, `docs-reconcile-main`, `governance-totality`, `work-queue-program-coordination`, `work-queue-golden-age`, `gapcheck-totality`, `work-queue-gaiadoc` (PR #28), `work-queue-phases-done` (PR #29), `pc4-c0` … `pc4-x12` (PR #30), `pc1-c0` … `pc1-x12` (PR #31), `crosswalk-c0` … `crosswalk-x12` (PR #32), `connection-c0` … `connection-x12` (PR #33).

## GAIA repositories (added 2026-10-25)

The-GAIA-Foundation is the active source of truth. The-Official-GAIA-Encyclopedia is a backup only (*Removed 2026-10-25: repository deleted by owner; to be uploaded later.*). The founding principle for every repository is [Truth with Integrity](https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/main/PRINCIPLES.md): "A Truth That Is Never Twisted."

| Repository | What it holds |
|---|---|
| [The-GAIA-Foundation](https://github.com/KyleAlexanderSteen/The-GAIA-Foundation) | Primary source: the research corpus (reports, tracks, cycles, Maps and Matrix v1–v44), governance and `PRINCIPLES.md`. Every research gate is INDETERMINATE |
| [The-GAIA-Human-Knowledge](https://github.com/KyleAlexanderSteen/The-GAIA-Human-Knowledge) | Human Subjects of Knowledge (H-K) |
| [The-GAIA-Human-Capabilities](https://github.com/KyleAlexanderSteen/The-GAIA-Human-Capabilities) | Human Capabilities (H-C) |
| [The-GAIA-Human-Skills](https://github.com/KyleAlexanderSteen/The-GAIA-Human-Skills) | Human Skills (H-S) |
| [The-GAIA-Human-Powers](https://github.com/KyleAlexanderSteen/The-GAIA-Human-Powers) | Human Powers (H-P) |
| [The-GAIA-Intelligence-Knowledge](https://github.com/KyleAlexanderSteen/The-GAIA-Intelligence-Knowledge) | Intelligence Subjects of Knowledge (I-K) |
| [The-GAIA-Intelligence-Capabilities](https://github.com/KyleAlexanderSteen/The-GAIA-Intelligence-Capabilities) | Intelligence Capabilities (I-C) |
| [The-GAIA-Intelligence-Skills](https://github.com/KyleAlexanderSteen/The-GAIA-Intelligence-Skills) | Intelligence Skills (I-S) |
| [The-GAIA-Intelligence-Powers](https://github.com/KyleAlexanderSteen/The-GAIA-Intelligence-Powers) | Intelligence Powers (I-P) |
| [The-GAIA-Ontology](https://github.com/KyleAlexanderSteen/The-GAIA-Ontology) | Master Ontology: the eight documents above compiled, with a shared source register |
| [The-GAIA-Map-and-Matrix](https://github.com/KyleAlexanderSteen/The-GAIA-Map-and-Matrix) | Human–Intelligence Map and Matrix: v1.2 is the latest version mapping the Foundation's completed work across all ten repositories (v1.1 and v1.0 kept as prior versions) |

How they connect is recorded in Map and Matrix v1.2, the latest version (`v1.2/`, sheet `Foundation x Repositories`): explicit links carry an evidence path; inferred links are on the `Proposed` sheet, labelled Hypothetical, until the owner approves them.

## Governance and safety

- [`GOVERNANCE/README.md`](GOVERNANCE/README.md): index of the standard, audits, risk levels, gate authority and change log.
- [`SECURITY.md`](SECURITY.md): how to report a vulnerability or an integrity problem privately (coordinated disclosure).
- [`.github/CODEOWNERS`](.github/CODEOWNERS): the owner is the required reviewer for every path. This is enforced only once branch protection is on, and it is currently **off** (see the owner to-do below).
- [`.github/workflows/verify.yml`](.github/workflows/verify.yml): manifest checks, `gaia_tools` tests and both validators on pull requests.
- Agent commits are authored as **Grok Bot** with a `Co-authored-by` line for the owner, so they can be told apart from the owner's own commits (from 2026-10-24; earlier agent commits appear under the owner's name; see [`GOVERNANCE/AGENT_PUSH_LOG.md`](GOVERNANCE/AGENT_PUSH_LOG.md)).

## Owner to-do (settings and decisions only the owner can make)

- **Licence:** All rights reserved (see [`LICENSE`](LICENSE)), chosen by Kyle on 2026-10-24. Third-party sources keep their own licences.
- **TODO: branch protection for `main`.** Require a pull request and the owner's review, block force-pushes and deletion (audit item UR-L7-03). This is a repository setting. **Checked 2026-10-25 (read-only, GitHub API `GET /repos/KyleAlexanderSteen/The-GAIA-Foundation/branches/main`): `protected: false`, `protection.enabled: false`; `GET .../rules/branches/main` returned no rulesets. Branch protection is NOT active on `main`.** Nothing was changed; only the owner can turn it on.
- **TODO: name independent reviewers,** including an ethics reviewer, so gates can move beyond INDETERMINATE (UR-L3-04, UR-L4-02).

## Key principles observed in this corpus

- **Founding principle: Truth with Integrity.** "A Truth That Is Never Twisted." See [`PRINCIPLES.md`](PRINCIPLES.md) (owner commitment, 2026-10-25).
- Preserve prior versions; do not silently overwrite. (Previous versions of this README are kept at [`docs/history/README-2026-10-23.md`](docs/history/README-2026-10-23.md), [`docs/history/README-2026-10-24-pre-reconcile.md`](docs/history/README-2026-10-24-pre-reconcile.md) and [`docs/history/README-2026-10-25-pre-status-reconcile.md`](docs/history/README-2026-10-25-pre-status-reconcile.md); before ToG 1: [`docs/history/README-2026-10-25-pre-tog1.md`](docs/history/README-2026-10-25-pre-tog1.md).)
- Never invent sources, data, results or validations. Unreachable evidence is INDETERMINATE.
- A citation supports only the claims it directly addresses.
- Write the specification before running a simulation, and keep an execution record for every run.
- Keep negative results and failed checks.
- PASS / FAIL / INDETERMINATE gates. INDETERMINATE is never PASS.

---
*This README was revised on 2026-10-25 by Grok Bot (an AI agent) for the repository owner, from the repository's actual contents. It does not claim that any gate has passed.*
