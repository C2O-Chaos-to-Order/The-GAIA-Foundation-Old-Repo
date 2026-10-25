# PC-1 Program Charter and Master Register Reconciliation: proposed register (Wave 0)

**Status: Proposal.** Gate state is **INDETERMINATE**. **Wave 0 approval is the owner's decision alone** (Gate Authority §1). This file adopts nothing, files nothing and authorizes nothing (Law 7). Written by Grok Bot (AI agent), which is never a gate authority.

**Source.** GAIA Totality Suite v0.1.0 is owner-provided, Proposed and not adopted. It is held outside the repository; its register SHA-256 (`057efb54…2c8e72`) is checked on every run. This file contains only stable IDs, short slugs, priorities and short cited phrases. The suite's own text is not reproduced.

**Built on.** PC-4's map (`../PC-4-Research-to-Domain-Map/MAP.md`, branch `research/pc4-x12`), the governance files in this branch, and five cycles:
- Baseline
- x3
- x6
- x9
- x12

Each cycle has a SPEC, EXECUTION_RECORDs, VERIFICATION and MANIFEST.

## 1. What is proposed for each domain

| Field | Proposal | Basis |
|---|---|---|
| Stable domain ID | keep `GAIA-TOT-nnn` | register stable IDs (no renumbering) |
| Document ID | `GAIA-GOV-TOT-nnn` | follows the `GAIA-GOV-…-001` pattern of Gate Authority and Risk Levels; collides with no existing ID (C0-7, X12-11) |
| Owner | **KyleAlexanderSteen (repository owner)** for all 45 | the register's decision authority; Gate Authority §1; Product Register |
| Canonical home | 6 extend an existing file, 1 extends a ToG §19 planned file, 36 new and 2 shared under `GOVERNANCE/DOMAIN_STANDARDS/` | one home per domain, none shared by two domains (X12-10) |
| Reviewer roles | ToG §7.1 roles, plus those Risk Levels requires for the domain's scope tier and overlays, plus 8 `specialist:` roles | x9 tiers; x12 repair. **No reviewer is named yet (GAP-003)**, so every reviewer-dependent gate stays INDETERMINATE |
| Scope tier | RL-2 for 16 domains, RL-3 for 19, RL-4 for 7, RL-5 for 3 | Risk Levels "when it applies" (x9) |
| Change control | one rule per home type | `Cycle-x9`, `../judgments/change_control_x9.csv` |

The homes that extend existing files are:
- 002 → `GOVERNANCE/GATE_AUTHORITY.md`
- 005 → `GOVERNANCE/LAW2_CROSSWALK.md`
- 008 → `GOVERNANCE/RISK_LEVELS.md`
- 039 → `Research/WORK_QUEUE.md`
- 040 → `SECURITY.md`
- 044 → `GOVERNANCE/CHANGELOG.md`
- 045 → the planned `GOVERNANCE/TOTALITY_OF_GOVERNANCE.md`

The two shared homes are 014 and 033, which are shared with the Encyclopedia.

## 2. Requested reconciliations

- **Gap b9 (crosswalk omissions).** The gap was recomputed from the suite's crosswalk, after the crosswalk was verified against its own SHA256SUMS. Eleven domains are named in no specific crosswalk row: 021, 022, 024, 025, 026, 029, 031, 032, 036, 040, 042. This matches the Work Queue exactly. The proposed homes in §5 serve as the missing crosswalk entries (decision D-10).
- **Wave and priority mismatches.** The four mismatches in the Work Queue are confirmed, and a fifth was found:

  | Domain | Priority | Roadmap | Proposed |
  |---|---|---|---|
  | 024 | P1 | Wave 3 | Wave 2 |
  | 025 | P1 | unnamed | Wave 3, with priority P2 |
  | 028 | P1 | **unnamed (new finding)** | Wave 2, beside 016 |
  | 035 | P2 | unnamed | Wave 3 |
  | 038 | P2 | Wave 4 | **owner's choice** |

  For 038, the choice of wave has no effect on dependencies; the table in §5 scores it as Wave 3.
- **Universal Regulation.**
  - All 26 UR §5 criteria have a TOT primary domain.
  - Two cross UR's domain lines: SCI-5 → 014 and ETH-4 → 023 (decision D-07 on b16).
  - All 45 audit v2 items map to domains, each with one primary domain.
  - The 16 items not at PASS are listed per domain.
  - Five of them have their fix in an existing owner-text or gate file, not in the domain home. The proposed rule is that the domain standard cross-refers to that file and does not move the duty (D-08).
- **Gate Authority, Risk Levels, Product Register.**
  - Gate Authority and Risk Levels become homes for 002 and 008, keeping their own IDs.
  - All 64 products are governed by at least one domain.
  - The W overlay ties 44 products to 021 and 027, the two domains with **no governing text** in the repository (D-09).
- **ToG draft.**
  - All ten §19 planned files are assigned to domains. Six are records or indexes, not homes.
  - 21 domains rest only on the unapproved draft. Twelve of those also have no PC-4 primary report.

## 3. Owner decision packet (all INDETERMINATE; the only authority is the owner)

| ID | Question | Agent preference |
|---|---|---|
| D-01 | Approve this register as the Wave 0 baseline? | none: owner decision |
| D-02 | 024 wave | Wave 2 |
| D-03 | 025 wave | Wave 3, with priority P2 |
| D-04 | 028 wave | Wave 2, beside 016 |
| D-05 | 035 wave | Wave 3 |
| D-06 | 038 wave | none |
| D-07 | b16: do the TOT domains replace UR §5? | no: keep UR §5 as parent criteria |
| D-08 | When a duty is already held in owner text or a gate file, cross-refer rather than move it? | cross-refer |
| D-09 | 021 and 027: new standards? | yes |
| D-10 | b9: use the PC-1 homes as the crosswalk entries? | yes, within PC-1 only |
| D-11 | Name reviewers (GAP-003) | only the owner can |
| D-12 | The dependency cycle covering 38 domains: draft those domains together? | yes |

Full options and evidence: `judgments/decisions_x9.csv`.

## 4. Structural findings the owner should know

1. **The dependencies in the register form one cycle covering 38 of the 45 domains**, with 240 of the 286 named edges inside it. No wave order can satisfy them. The proposed waves reduce dependency inversions from 45 to 33. The waves are best read as priority groups.
2. **Most domains have little existing material.** 36 need a new file, 21 rest only on draft text, and 2 (021 and 027) have none at all.
3. **The review load is large.** Every domain needs `auditor`, and the 29 domains at RL-3 or above also need `ethics-rights` and `community-rep`. No reviewer is named.

## 5. Register (generated)

_Generated by `tools/pc1.py register` from `Cycle-x12/iter-1` (register SHA-256 `057efb548930…`). Every row is a proposal; gate state INDETERMINATE; decision authority: the repository owner._

| Domain | Pri. | Doc ID | Home | Owner | Reviewer roles | Tier | UR (laws) | Wave: roadmap → proposed | Open audit items |
|---|---|---|---|---|---|---|---|---|---|
| 001 purpose-identity-scope-boundaries | P0 | GAIA-GOV-TOT-001 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-001-purpose-identity-scope-boundaries.md` | KyleAlexanderSteen | independent auditor | RL-2 | ALL (1 2 3 4 5 6 7) | 1 → 1 | UR-BND-01 (I) |
| 002 governance-authority-decision-rights | P0 | GAIA-GOV-TOT-002 | extend: `GOVERNANCE/GATE_AUTHORITY.md` | KyleAlexanderSteen | independent auditor | RL-2 | OPS (5 7) | 1 → 1 | UR-L7-03 (F) |
| 003 good-greater-good-ethics-values | P0 | GAIA-GOV-TOT-003 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-003-good-greater-good-ethics-values.md` | KyleAlexanderSteen | ethics-rights independent auditor community-rep | RL-3 | ETH (4 6) | 1 → 1 | UR-L4-02 (I) |
| 004 rights-duties-consent-human-agency | P0 | GAIA-GOV-TOT-004 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-004-rights-duties-consent-human-agency.md` | KyleAlexanderSteen | ethics-rights community-rep auditor | RL-3 | ETH (4 6) | 1 → 1 | — |
| 005 evidence-truth-knowledge-epistemics | P0 | GAIA-GOV-TOT-005 | extend: `GOVERNANCE/LAW2_CROSSWALK.md` | KyleAlexanderSteen | independent data-steward auditor ethics-rights | RL-2 | EPI (1 2) | 1 → 1 | UR-L2-02 (I) UR-L3-10 (I) |
| 006 research-methodology-scientific-integrity | P0 | GAIA-GOV-TOT-006 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-006-research-methodology-scientific-integrity.md` | KyleAlexanderSteen | independent auditor ethics-rights | RL-2 | SCI (3) | 1 → 1 | UR-L3-01 (I) UR-L3-10 (I) |
| 007 verification-validation-falsification-reproducibility | P0 | GAIA-GOV-TOT-007 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-007-verification-validation-falsification-reproducibility.md` | KyleAlexanderSteen | independent auditor ethics-rights | RL-2 | SCI (3) | 1 → 1 | UR-L1-05 (I) UR-L3-01 (I) UR-L3-04 (I) UR-L3-08 (I) |
| 008 risk-impact-assurance | P0 | GAIA-GOV-TOT-008 | extend: `GOVERNANCE/RISK_LEVELS.md` | KyleAlexanderSteen | independent auditor | RL-2 | ETH TEC (4 6 7) | 1 → 1 | — |
| 009 safety-security-protection-boundaries | P0 | GAIA-GOV-TOT-009 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-009-safety-security-protection-boundaries.md` | KyleAlexanderSteen | security-privacy auditor ethics-rights community-rep | RL-4 | TEC ETH (4 6 7) | 1 → 1 | — |
| 010 harm-transformation-restoration | P0 | GAIA-GOV-TOT-010 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-010-harm-transformation-restoration.md` | KyleAlexanderSteen | ethics-rights community-rep auditor | RL-3 | ETH (4 6) | 1 → 1 | — |
| 011 accountability-audit-grievance-appeals | P0 | GAIA-GOV-TOT-011 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-011-accountability-audit-grievance-appeals.md` | KyleAlexanderSteen | auditor independent ethics-rights community-rep | RL-3 | OPS (5 7) | 1 → 1 | UR-L3-04 (I) |
| 012 privacy-data-information-governance | P0 | GAIA-GOV-TOT-012 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-012-privacy-data-information-governance.md` | KyleAlexanderSteen | security-privacy data-steward auditor ethics-rights community-rep | RL-3 | ETH TEC (4 6 7) | 1 → 1 | — |
| 013 identity-access-permission-authorization | P0 | GAIA-GOV-TOT-013 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-013-identity-access-permission-authorization.md` | KyleAlexanderSteen | security-privacy auditor ethics-rights community-rep | RL-4 | OPS (5 7) | 1 → 1 | UR-L5-03 (F) UR-L5-06 (I) UR-L7-03 (F) |
| 014 provenance-records-knowledge-architecture | P0 | GAIA-GOV-TOT-014 | shared: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-014-provenance-records-knowledge-architecture.md` | KyleAlexanderSteen | data-steward auditor | RL-2 | EPI (1 2) | 1 → 1 | UR-L1-05 (I) |
| 015 software-systems-architecture-engineering | P1 | GAIA-GOV-TOT-015 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-015-software-systems-architecture-engineering.md` | KyleAlexanderSteen | security-privacy independent auditor ethics-rights community-rep | RL-4 | TEC (4 7) | 2 → 2 | UR-L3-08 (I) UR-L4-05 (I) |
| 016 ai-models-intelligence-autonomy | P1 | GAIA-GOV-TOT-016 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-016-ai-models-intelligence-autonomy.md` | KyleAlexanderSteen | independent ethics-rights security-privacy auditor community-rep | RL-5 | TEC OPS (4 5 7) | 2 → 2 | UR-L5-06 (I) UR-BND-01 (I) |
| 017 operations-deployment-change-release | P1 | GAIA-GOV-TOT-017 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-017-operations-deployment-change-release.md` | KyleAlexanderSteen | security-privacy auditor ethics-rights community-rep independent | RL-5 | OPS (5 7) | 2 → 2 | UR-L7-04 (I) |
| 018 incident-response-continuity-recovery | P1 | GAIA-GOV-TOT-018 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-018-incident-response-continuity-recovery.md` | KyleAlexanderSteen | security-privacy auditor ethics-rights community-rep | RL-4 | OPS (5 7) | 2 → 2 | — |
| 019 law-regulation-contract-jurisdiction | P1 | GAIA-GOV-TOT-019 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-019-law-regulation-contract-jurisdiction.md` | KyleAlexanderSteen | specialist:legal auditor ethics-rights community-rep | RL-3 | ETH (4 6) | 2 → 2 | UR-L6-03 (F) |
| 020 intellectual-property-licensing-third-party-rights | P1 | GAIA-GOV-TOT-020 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-020-intellectual-property-licensing-third-party-rights.md` | KyleAlexanderSteen | specialist:legal auditor ethics-rights community-rep | RL-3 | ETH (4 6) | 2 → 2 | UR-L6-02 (I) UR-L6-03 (F) |
| 021 human-factors-wellbeing-interaction-ethics | P1 | GAIA-GOV-TOT-021 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-021-human-factors-wellbeing-interaction-ethics.md` | KyleAlexanderSteen | ethics-rights auditor community-rep | RL-3 | ETH (4 6) | 2 → 2 | UR-L4-02 (I) |
| 022 equity-accessibility-inclusion-fairness | P1 | GAIA-GOV-TOT-022 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-022-equity-accessibility-inclusion-fairness.md` | KyleAlexanderSteen | community-rep ethics-rights auditor | RL-3 | ETH (4 6) | 2 → 2 | — |
| 023 culture-spiritual-theological-knowledge-integrity | P1 | GAIA-GOV-TOT-023 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-023-culture-spiritual-theological-knowledge-integrity.md` | KyleAlexanderSteen | independent community-rep auditor ethics-rights | RL-3 | EPI (1 2) | 2 → 2 | UR-BND-01 (I) |
| 024 indigenous-knowledge-data-sovereignty | P1 | GAIA-GOV-TOT-024 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-024-indigenous-knowledge-data-sovereignty.md` | KyleAlexanderSteen | community-rep ethics-rights auditor | RL-3 | ETH (4 6) | 3 → 2 | — |
| 025 environment-ecology-planetary-stewardship | P1 | GAIA-GOV-TOT-025 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-025-environment-ecology-planetary-stewardship.md` | KyleAlexanderSteen | specialist:environment auditor ethics-rights community-rep | RL-3 | ETH (4 6) | unnamed → 3 | — |
| 026 animal-welfare | P2 | GAIA-GOV-TOT-026 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-026-animal-welfare.md` | KyleAlexanderSteen | specialist:animal-welfare auditor ethics-rights community-rep | RL-3 | ETH (4 6) | 3 → 3 | — |
| 027 health-biomedical-clinical-safety | P2 | GAIA-GOV-TOT-027 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-027-health-biomedical-clinical-safety.md` | KyleAlexanderSteen | specialist:clinical ethics-rights auditor community-rep | RL-3 | ETH (4 6) | 3 → 3 | UR-L4-02 (I) |
| 028 synthetic-media-image-video-content | P1 | GAIA-GOV-TOT-028 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-028-synthetic-media-image-video-content.md` | KyleAlexanderSteen | ethics-rights security-privacy auditor community-rep | RL-3 | TEC ETH (4 6 7) | unnamed → 2 | — |
| 029 communications-transparency-public-claims | P1 | GAIA-GOV-TOT-029 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-029-communications-transparency-public-claims.md` | KyleAlexanderSteen | independent auditor ethics-rights community-rep | RL-3 | EPI OPS (1 2 5 7) | 2 → 2 | — |
| 030 education-training-competency-responsibility | P2 | GAIA-GOV-TOT-030 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-030-education-training-competency-responsibility.md` | KyleAlexanderSteen | auditor | RL-2 | OPS (5 7) | 3 → 3 | — |
| 031 economics-finance-resources-sustainability | P2 | GAIA-GOV-TOT-031 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-031-economics-finance-resources-sustainability.md` | KyleAlexanderSteen | specialist:finance auditor ethics-rights community-rep | RL-3 | OPS (5 7) | 3 → 3 | — |
| 032 procurement-supply-chain-third-parties | P2 | GAIA-GOV-TOT-032 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-032-procurement-supply-chain-third-parties.md` | KyleAlexanderSteen | security-privacy auditor ethics-rights community-rep | RL-4 | TEC (4 7) | 3 → 3 | UR-L4-05 (I) |
| 033 interoperability-standards-semantics | P2 | GAIA-GOV-TOT-033 | shared: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-033-interoperability-standards-semantics.md` | KyleAlexanderSteen | data-steward auditor | RL-2 | EPI (1 2) | 3 → 3 | — |
| 034 evaluation-metrics-outcomes-impact | P1 | GAIA-GOV-TOT-034 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-034-evaluation-metrics-outcomes-impact.md` | KyleAlexanderSteen | independent auditor | RL-2 | SCI (3) | 2 → 2 | — |
| 035 organization-collaboration-conflicts-succession | P2 | GAIA-GOV-TOT-035 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-035-organization-collaboration-conflicts-succession.md` | KyleAlexanderSteen | auditor | RL-2 | OPS (5 7) | unnamed → 3 | UR-L5-03 (F) |
| 036 lifecycle-maintenance-deprecation-decommission | P2 | GAIA-GOV-TOT-036 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-036-lifecycle-maintenance-deprecation-decommission.md` | KyleAlexanderSteen | data-steward auditor | RL-2 | OPS (5 7) | 3 → 3 | UR-L7-04 (I) |
| 037 physical-infrastructure-global-grid | P3 | GAIA-GOV-TOT-037 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-037-physical-infrastructure-global-grid.md` | KyleAlexanderSteen | specialist:engineering security-privacy auditor ethics-rights community-rep independent | RL-5 | TEC OPS (4 5 7) | 4 → 4 | — |
| 038 mathematics-physics-cosmology-quantum-claims | P2 | GAIA-GOV-TOT-038 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-038-mathematics-physics-cosmology-quantum-claims.md` | KyleAlexanderSteen | specialist:physics independent auditor | RL-2 | EPI SCI (1 2 3) | 4 → 3 | — |
| 039 research-portfolio-work-queue-prioritization | P1 | GAIA-GOV-TOT-039 | extend: `Research/WORK_QUEUE.md` | KyleAlexanderSteen | auditor | RL-2 | OPS (5 7) | 2 → 2 | — |
| 040 security-vulnerability-disclosure | P1 | GAIA-GOV-TOT-040 | extend: `SECURITY.md` | KyleAlexanderSteen | security-privacy auditor ethics-rights community-rep | RL-4 | TEC (4 7) | 2 → 2 | — |
| 041 human-subject-research-ethics | P1 | GAIA-GOV-TOT-041 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-041-human-subject-research-ethics.md` | KyleAlexanderSteen | ethics-rights auditor community-rep | RL-3 | ETH (4 6) | 2 → 2 | UR-L4-02 (I) |
| 042 decision-making-conflicts-tradeoffs | P1 | GAIA-GOV-TOT-042 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-042-decision-making-conflicts-tradeoffs.md` | KyleAlexanderSteen | independent auditor ethics-rights community-rep | RL-3 | OPS ETH (4 5 6 7) | 2 → 2 | — |
| 043 resilience-emergency-environmental-disaster | P2 | GAIA-GOV-TOT-043 | new: `GOVERNANCE/DOMAIN_STANDARDS/GAIA-TOT-043-resilience-emergency-environmental-disaster.md` | KyleAlexanderSteen | security-privacy auditor ethics-rights community-rep | RL-4 | TEC OPS (4 5 7) | 3 → 3 | — |
| 044 archives-preservation-long-term-memory | P2 | GAIA-GOV-TOT-044 | extend: `GOVERNANCE/CHANGELOG.md` | KyleAlexanderSteen | data-steward auditor | RL-2 | OPS (5 7) | 3 → 3 | UR-L5-06 (I) |
| 045 governance-of-governance-meta-review | P0 | GAIA-GOV-TOT-045 | extend-planned: `GOVERNANCE/TOTALITY_OF_GOVERNANCE.md` | KyleAlexanderSteen | auditor independent | RL-2 | ALL (1 2 3 4 5 6 7) | 1 → 1 | UR-GOV-01 (I) |
