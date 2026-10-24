# Gate authority

**Stable ID:** GAIA-GOV-GATE-001 · **Revision:** 0.1.0 · **Status: Proposed** · **Date:** 2026-10-24
**Owner:** KyleAlexanderSteen (repository owner).
**Drafted by:** Grok Bot (AI agent), for audit items UR-L3-05 (gate records name an authority) and UR-L3-06 (merging is not a gate PASS).

## 1. Who decides
1. **The repository owner, KyleAlexanderSteen, is the final authority** for every gate decision in this repository: research cycles, track cycles, phase reports, the Master Report, governance audits and adoption of governance standards. This covers gate records that already exist and those added later. The only exception is a record that names a different authority the owner has approved in writing in the repository.
2. **AI agents (including Grok Bot) are never gate authorities.** An agent may run checks, record evidence and propose a decision. It may not declare a gate PASS, change a recorded decision, or treat its own checks as independent review.
3. **Independent reviewers** (none named yet) record findings under `Research/Reviews/`. Their findings are evidence for the owner's decision; they do not replace it. Where a gate requires independent challenge (UR "Review" standard) or ethics review (ETH-5; overlay W in [`RISK_LEVELS.md`](RISK_LEVELS.md)), the owner cannot record PASS until that review exists.

## 2. Decision rules
- Decisions are **PASS**, **FAIL** or **INDETERMINATE**.
- **INDETERMINATE is never PASS.** It never unlocks the next gate and never counts toward "complete".
- Missing, unreachable or unperformed evidence is INDETERMINATE, not PASS.
- A product's own statement that it is complete is not evidence.
- A gate record missing its authority is INDETERMINATE (Universal Regulation Part II §3). This file supplies the authority for every record listed below.

## 3. Merging is not a gate PASS
Merging a branch into `main` means the owner **accepts the work into the corpus**. It does not mean the work is verified, reviewed or passed. Every gate keeps the decision written in its own record. Today all of them are **INDETERMINATE**. The root `README.md` shows the gate state on `main`.

## 4. Register of existing gate records (authority added by this file)
| Gate record | Scope | Decision on record | Authority |
|---|---|---|---|
| `Research/Cycles/Cycle-0-Baseline/Verification/VERIFICATION.md` | Cycle 0 (Baseline v2), Reports 1-7 | INDETERMINATE | Repository owner |
| `Research/Cycles/Cycle-1-x3/Verification/VERIFICATION.md` | Cycle 1 (x3) | INDETERMINATE | Repository owner |
| `Research/Cycles/Cycle-2-x6/Verification/VERIFICATION.md` | Cycle 2 (x6) | INDETERMINATE | Repository owner |
| `Research/Cycles/Cycle-3-x9/Verification/VERIFICATION.md` | Cycle 3 (x9) | INDETERMINATE | Repository owner |
| `Research/Cycles/Cycle-4-x12/Verification/VERIFICATION.md` | Cycle 4 (x12) | INDETERMINATE | Repository owner |
| `Research/Master-Report-Unconditional-and-Conditional-Love/Verification/VERIFICATION.md` | Master Report v1 | INDETERMINATE | Repository owner |
| `Research/Tracks/Soul-Spirit-Subconscious-Consciousness/Cycle-A-x3/Verification/VERIFICATION.md` | Track Cycle A (x3) | INDETERMINATE | Repository owner |
| `Research/Tracks/Soul-Spirit-Subconscious-Consciousness/Cycle-B-x6/Verification/VERIFICATION.md` | Track Cycle B (x6) | INDETERMINATE | Repository owner |
| `Research/Tracks/Soul-Spirit-Subconscious-Consciousness/Cycle-C-x9/Verification/VERIFICATION.md` | Track Cycle C (x9) | INDETERMINATE | Repository owner |
| `Research/Tracks/Soul-Spirit-Subconscious-Consciousness/Cycle-D-x12/Verification/VERIFICATION.md` | Track Cycle D (x12) | INDETERMINATE | Repository owner |
| `GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v1.md`, `..._v2.md` | Repository against Universal Regulation 0.1.0 | INDETERMINATE | Repository owner |

The decisions above were read from each file on 2026-10-24 (also extracted automatically into `PRODUCT_REGISTER.csv`, column `gate_decision`). The research files themselves are **not modified**: prior versions are preserved, and the authority is recorded here instead.

## 5. Template line for new gate records
New gate records include this line:
`Decision authority: KyleAlexanderSteen (repository owner). Recorded by: <agent or person>. Independent review: <none | record path>. Ethics review: <none | record path>.`

## Change history
- **2026-10-24, 0.1.0 (Proposed):** Owner named as final gate authority; agents excluded; merge ≠ PASS; register of 11 existing gate records.
