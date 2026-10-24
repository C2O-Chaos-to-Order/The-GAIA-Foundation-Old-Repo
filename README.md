# The GAIA Foundation

**The Foundation In Which GAIA Has Been Built Upon.**

This repository holds the foundational research corpus for GAIA and the governance standard it is held to. Research lives under [`Research/`](Research/). Governance lives under [`GOVERNANCE/`](GOVERNANCE/).

**Research first. Integrity before intelligence. Responsibility at every scale.**

## Current status (2026-10-24)

- **Every research gate is INDETERMINATE.** All internal checks pass or are reported, but no independent human review and no ethics review has been done. INDETERMINATE is never PASS.
- **Merged into `main` means accepted by the owner, not verified.** See [`GOVERNANCE/GATE_AUTHORITY.md`](GOVERNANCE/GATE_AUTHORITY.md). The repository owner (@KyleAlexanderSteen) is the final authority for every gate.
- **Implementation is not authorized.** Research, successful tests and technical capability do not grant permission to deploy (Universal Regulation, Law 7).
- **Universal Regulation standard:** Proposed, not adopted, not implemented. Audit v2 gate: INDETERMINATE (see [`GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v2.md`](GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v2.md)).

## What is on `main` (as of commit `517f901`, PR #7)

| Area | Path | Contents | Gate |
|---|---|---|---|
| Research index and rules | [`Research/README.md`](Research/README.md), [`Research/RESEARCH_PLAN_EXTENSION.md`](Research/RESEARCH_PLAN_EXTENSION.md) | Claim classes, responsibility ladder, integration mandate, lifecycle, report requirements, gates | — |
| Seven-Report cycles | [`Research/Cycles/`](Research/Cycles/) | Cycle 0 (Baseline v2), Cycle 1 (x3), Cycle 2 (x6), Cycle 3 (x9), Cycle 4 (x12). Reports 1 Body, 2 Mind, 3 Soul, 4 Spirit, 5 Consciousness, 6 Earth, 7 Unified, each with claims, sources, simulations and execution records | INDETERMINATE |
| Master Report | [`Research/Master-Report-Unconditional-and-Conditional-Love/`](Research/Master-Report-Unconditional-and-Conditional-Love/) | Unconditional and Conditional Love, v1 (36 claims; SIM-MR-1) | INDETERMINATE |
| Soul / Spirit / Subconscious / Consciousness track | [`Research/Tracks/Soul-Spirit-Subconscious-Consciousness/`](Research/Tracks/Soul-Spirit-Subconscious-Consciousness/) | Track Cycles A (x3), B (x6), C (x9), D (x12) | INDETERMINATE |
| Maps and Matrix | [`Research/Maps-and-Matrix/`](Research/Maps-and-Matrix/) | Versions v1-v8: claim maps, 625-cell matrix, link graphs, simulation index | derived; no gate of their own |
| Research tooling | [`Research/tools/`](Research/tools/) | `gaia_tools` 0.5.1: validators, reruns, claim-source checks, maps (research tooling only; no service, no deployment) | — |

Claims carry one of four labels: **Established, Plausible, Philosophical/Spiritual, Hypothetical**. How these map onto Law 2's six distinctions is in [`GOVERNANCE/LAW2_CROSSWALK.md`](GOVERNANCE/LAW2_CROSSWALK.md).

## Pending branches (not on `main`; the owner reviews and merges)

| Branch | What it adds | State |
|---|---|---|
| `research/governance-universal-regulation` | [`GOVERNANCE/UNIVERSAL_REGULATION.md`](GOVERNANCE/UNIVERSAL_REGULATION.md) (standard 0.1.0, Proposed) and audit v1 (20 PASS / 13 FAIL / 12 INDETERMINATE) | No PR yet; base of PR #8 |
| `research/governance-audit-fixes` | Fixes for the audit v1 failures: this README, [`SECURITY.md`](SECURITY.md), CI workflow, CODEOWNERS, risk levels, owner register, Law 2 crosswalk, gate authority, Master Report manifest, change log, audit v2 | Stacked on the branch above; no PR yet |
| `research/phase-divergence-c0` | Phases track: Divergence Baseline | PR #8 open (base: governance-universal-regulation) |
| `research/phase-divergence-x3` | Divergence x3 | PR #9 open (base: phase-divergence-c0) |
| `research/phase-divergence-x6` | Divergence x6 | Pushed; no PR yet |
| `research/phase-divergence-x9` | Divergence x9 | Being pushed or just pushed; no PR yet |

Branches already merged and kept for history: `research/cycle-0-baseline`, `cycle-1-x3`, `maps-c0-c1`, `cycle-2-x6`, `cycle-3-x9`, `cycle-4-x12`, `master-report`, `track-ssc-a-x3` … `track-ssc-d-x12`.

## Governance and safety

- [`GOVERNANCE/README.md`](GOVERNANCE/README.md): index of the standard, audits, risk levels, gate authority and change log.
- [`SECURITY.md`](SECURITY.md): how to report a vulnerability or an integrity problem privately (coordinated disclosure).
- [`.github/CODEOWNERS`](.github/CODEOWNERS): the owner is the required reviewer for every path. This is enforced only once branch protection is on.
- [`.github/workflows/verify.yml`](.github/workflows/verify.yml): manifest checks, `gaia_tools` tests and both validators on pull requests.
- Agent commits are authored as **Grok Bot** with a `Co-authored-by` line for the owner, so they can be told apart from the owner's own commits (from 2026-10-24; earlier agent commits appear under the owner's name; see [`GOVERNANCE/AGENT_PUSH_LOG.md`](GOVERNANCE/AGENT_PUSH_LOG.md)).

## Owner to-do (settings and decisions only the owner can make)

- **TODO: licence.** No licence has been chosen, so reuse terms are not stated (audit item UR-L6-03). Options: MIT or Apache-2.0 (open reuse), or an "All rights reserved" notice. An agent will not choose this.
- **TODO: branch protection for `main`.** Require a pull request and the owner's review, block force-pushes and deletion (audit item UR-L7-03). This is a repository setting.
- **TODO: name independent reviewers,** including an ethics reviewer, so gates can move beyond INDETERMINATE (UR-L3-04, UR-L4-02).

## Key principles observed in this corpus

- Preserve prior versions; do not silently overwrite. (The previous version of this README is kept at [`docs/history/README-2026-10-23.md`](docs/history/README-2026-10-23.md).)
- Never invent sources, data, results or validations. Unreachable evidence is INDETERMINATE.
- A citation supports only the claims it directly addresses.
- Write the specification before running a simulation, and keep an execution record for every run.
- Keep negative results and failed checks.
- PASS / FAIL / INDETERMINATE gates. INDETERMINATE is never PASS.

---
*This README was revised on 2026-10-24 by Grok Bot (an AI agent) for the repository owner, from the repository's actual contents. It does not claim that any gate has passed.*
