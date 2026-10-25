# PC-1 Program Charter and Master Register Reconciliation: Plan

Status: **Proposed research output, not adopted.** This is Work Queue item PC-1 (Program Coordination, Wave 0). Everything here is a proposal. **Wave 0 approval is the owner's decision alone** (Work Queue: "an owner decision, not a report"). Author: Grok Bot, with the Kyle Steen trailer on every commit. Kyle approved the start on 2026-10-25 (relayed in the agent task).

## 1. Question
For each of the 45 Totality domains (GAIA-TOT-001 to 045), how does the domain reconcile with the governance that already exists? Six sources are checked:

- the Universal Regulation (GAIA-GOV-UR-001)
- Gate Authority (GAIA-GOV-GATE-001)
- Risk Levels (GAIA-GOV-RISK-001)
- the Product Register
- audits v1 and v2
- the Totality of Governance draft (GAIA-GOV-TOG-001)

For each domain, this work proposes a canonical home, a stable ID and an owner. Two further inputs are required:

- **Gap b9:** the domains that the suite's crosswalk (04) omits from every specific row.
- **The wave/priority mismatches** for TOT-024, 025, 035 and 038, which the Work Queue records next to the wave list.

## 2. Inputs and the adoption boundary
| Input | Where | Pinned by |
|---|---|---|
| Work Queue, governance files | this branch (stacked on `research/pc4-x12` @ 1dd84f62) | SHA-256 in every EXECUTION_RECORD |
| PC-4 result | `../PC-4-Research-to-Domain-Map/` (MAP.md, x12 data, ToG §6 map) | SHA-256 in every EXECUTION_RECORD |
| GAIA Totality Suite v0.1.0 | **owner-provided, external, not filed**; read at `/workspace/coord/zip/gaia_totality_suite_v0_1/` (override `PC4_SUITE`) | register and SHA256SUMS hashes as in PC-4 |

From the suite, this track stores only derived facts:

- stable IDs, short titles and priorities;
- which domains the crosswalk rows name (computed by the tool);
- the owner's reading of the roadmap's wave lists (agent judgment, with a basis).

The suite is quoted only in short cited phrases. A pre-registered boundary scan (`pc1.py boundary`) uses an **80-character** window, stricter than PC-4's 120, to avoid the PC-4 X12-7 issue.

## 3. What each domain row proposes
- **Stable ID.** Keep `GAIA-TOT-nnn` as the domain's identity: it is already used in the Work Queue and PC-4, and it does not collide with anything. Propose `GAIA-GOV-TOT-nnn` for the eventual approved domain standard document. This follows the repository's `GAIA-GOV-<NAME>-001` convention. The tool checks both for collisions against every ID found in the repository and the suite.
- **Canonical home.** Either *extend* an existing governance document (when one already governs most of the domain; ToG §19: "extend it through a reviewed schema change rather than creating a competing source of truth"), or a *new* file under `GOVERNANCE/DOMAIN_STANDARDS/` (the ToG §19 planned location, created only after ToG Stage 1 approval, gap b15). A home may be *shared* when the Encyclopedia holds part of it (ToG §19). Homes must be unique: no two domains share one canonical file.
- **Owner.** The decision authority recorded in Gate Authority §1 and in every register row: KyleAlexanderSteen (repository owner). Required reviewer roles come from ToG §7.1. A `specialist:<field>` role marks a domain that needs a qualification ToG §7.1 does not name. **No reviewer is named anywhere yet** (GAP-003), so every gate stays INDETERMINATE.
- **Reconciliation.** The Universal Regulation domain(s) (EPI, SCI, ETH, TEC, OPS; laws derived mechanically from UR §5 headings); anchors in existing documents (`file#text`, checked to exist); audit v2 items mapped to the domain; the ToG §6 governance domain (from PC-4 x6–x12); and PC-4's primary reports.

Labels per row (the claim "this is the right home / reconciliation"): Established when an existing document already assigns it, Plausible for agent judgment with a basis, Hypothetical for weak fits. Gates are PASS, FAIL or INDETERMINATE; INDETERMINATE is never PASS.

## 4. Cycles
Baseline → x3 → x6 → x9 → x12 on `research/pc1-<cycle>`, each stacked on the last. Each cycle has its SPEC and config pushed before the run, then the EXECUTION_RECORDs, REPORT, VERIFICATION (fresh-clone rerun) and MANIFEST. Failed pre-registered checks stay failed. Diminishing returns are reported per pass.
