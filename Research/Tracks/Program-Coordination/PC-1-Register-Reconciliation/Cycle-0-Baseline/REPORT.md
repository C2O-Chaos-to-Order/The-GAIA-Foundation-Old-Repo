# PC-1 Baseline: report

Track: PC-1 Program Charter and Master Register Reconciliation (Wave 0). Status: **proposal only**. Wave 0 approval is the owner's decision alone (Gate Authority §1). Nothing here adopts, files or authorizes anything.

Source: GAIA Totality Suite v0.1.0 (owner-provided, Proposed, not adopted). It is held outside the repository, and its register SHA-256 is checked on every run. This folder holds only IDs, titles, priorities and short cited phrases from it.

## Results (iteration 1, as they fell)

| Check | Result |
|---|---|
| C0-1 to C0-9 | all **PASS** (see TABLES.md) |

**Diminishing returns, stated honestly.** Seven of the nine checks (C0-1–C0-3 and C0-6–C0-9) test the consistency of the agent's own judgments. They passed on the first run, so they show the proposal is well formed. They do not show it is correct. As a sanity test, each check was run once on a deliberately broken copy (a doc ID changed and an anchor misspelled), and C0-2 and C0-3 both failed as they should. That copy was then discarded and is not in this branch.

## Findings

1. **Gap b9 reproduced** (Established, from the suite's crosswalk 04, which is verified against its SHA256SUMS). Eleven domains appear in no specific crosswalk row: 021, 022, 024, 025, 026, 029, 031, 032, 036, 040, 042. This is exactly the Work Queue's M-b9 list.
2. **Wave/priority mismatches: five, not four** (Established). The four the Work Queue records (024, 025, 035, 038) are confirmed. A fifth appears: **028 (synthetic media)** is P1, but no roadmap wave list names it, so its implied Wave 2 is unconfirmed. The Work Queue line does not mention 028. For the owner: either add 028 to Wave 2, or record why it is held back.
3. **Homes** (Plausible, proposals):
   - Seven domains extend files that already exist or are planned:
     - 002 → Gate Authority
     - 005 → Law 2 crosswalk
     - 008 → Risk Levels
     - 039 → Work Queue
     - 040 → SECURITY.md
     - 044 → CHANGELOG
     - 045 → the planned `GOVERNANCE/TOTALITY_OF_GOVERNANCE.md` (ToG §19)
   - Two homes are shared with the Encyclopedia: 014 (records and provenance) and 033 (identifiers and interoperability).
   - The other 36 domains get new files under the planned `GOVERNANCE/DOMAIN_STANDARDS/`.
   - No two domains share a home.
   - Because the planned registers in §19 (risk, decision, incident) are indexes and not standards, they stay companions of 008, 042 and 018, not their homes.
4. **IDs**:
   - Stable IDs stay `GAIA-TOT-nnn`.
   - The proposed document IDs `GAIA-GOV-TOT-nnn` follow the `GAIA-GOV-…-001` pattern of Gate Authority and Risk Levels.
   - None collides with an ID already used in the repository or the suite.
5. **Owner**: all 45 domains are owned by the register's decision authority, the repository owner (Kyle Alexander Steen). This matches Gate Authority §1 and the Product Register.
   - Reviewer roles are proposed from ToG §7.1.
   - Eight domains need a qualification that §7.1 does not name: legal (019, 020), environment (025), animal welfare (026), clinical (027), finance (031), engineering (037), physics (038).
   - No reviewer is named anywhere yet (suite GAP-003). Until one is, any gate that needs a reviewer is **INDETERMINATE**.
6. **Audits**:
   - All 45 audit v2 items map to at least one domain.
   - The 16 items not at PASS (13 INDETERMINATE, 3 FAIL: UR-L5-03, UR-L6-03, UR-L7-03) touch 21 domains.
   - 16 domains have no audit item at all: 003, 004, 010, 018, 022, 024, 025, 026, 028, 030, 031, 033, 034, 037, 042, 043. For these, the UR audit gives no evidence either way.
7. **ToG §6**: three domains have no ToG §6 governance area (021, 027, 037). This repeats PC-4's finding.

## Limits

- The anchors prove that a cited heading or phrase exists. They do not prove that the passage supports the judgment. x3 re-reads the anchors for exactly this reason.
- The audit mapping is one agent's reading of each criterion.
- The roadmap waves were taken from short phrases by hand.
