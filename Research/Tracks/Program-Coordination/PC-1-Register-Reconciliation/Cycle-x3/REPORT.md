# PC-1 x3: report

Status: **proposal only**. Wave 0 approval is the owner's decision alone. The source suite is v0.1.0: owner-provided, Proposed, external, not filed.

## Check results (as they fell)

| Check | iter-1 | iter-2 | iter-3 |
|---|---|---|---|
| X3-1–X3-5, X3-8–X3-11 | PASS | PASS | PASS |
| **X3-6**: every domain has a `direct` anchor | **FAIL (2: 021, 027)** | FAIL | FAIL |
| **X3-7**: remedy home = primary domain's home | **FAIL (5)** | FAIL | FAIL |
| X3-12: always_new → 7 | – | PASS | – |
| X3-13: no_planned → 1 | – | – | PASS |
| X3-14: shared ≤ 2 | PASS | – | – |

Both failures stay failed. Each one is a finding.

## Findings

1. **021 (human factors and well-being) and 027 (health and clinical safety) have no governing text in the repository** (Established, from re-reading the anchors). The nearest text only partly covers them:
   - Risk Levels' W overlay, a keyword trigger
   - RL-3's health example
   - UR ETH-5's ethics-review duty

   None of these sets a human-factors or clinical-safety rule. Both domains therefore need new standards, written from nothing. They are the two Wave 2 or 3 domains with the least to build on.
2. **For five open audit items, the fix sits outside the proposed domain home** (Plausible). Each is an authority ambiguity the owner should settle:
   - **UR-L3-04** (independent review) is primary domain 007, but the reviewer rule lives in Gate Authority §1. Proposal: 007's standard defines what review means, and Gate Authority names who reviews.
   - **UR-L4-02** (ethics review) is primary domain 003, but the duty sits in RISK_LEVELS RL-3 and UR ETH-5. Proposal: keep the duty in Risk Levels, and let 003 define the ethics review method.
   - **UR-L6-03** (reuse terms) is primary domain 020, but the terms belong in LICENSE. Proposal: 020's standard governs; LICENSE is the instrument.
   - **UR-BND-01** (absolute boundary) is primary domain 001, but the boundary is owner text in UR Part I and cannot move. Proposal: 001 cross-refers to it and never restates it.
   - **UR-GOV-01** (UR adoption) is primary domain 045, but UR Part IV holds the adoption path. Proposal: UR adoption stays a UR record, and 045 governs review of the whole system.

   Rule: where an existing owner-text or gate file already holds the duty, the domain standard cross-refers and does not move the duty. This gives **"no competing source"** a concrete meaning.
3. **The Baseline had one wrong anchor.** 033 cited the numerical-matrix section, which says nothing about interoperability. It was replaced with ToG §6 item 13. Of the 108 anchors now cited, 69 are direct and 39 partial. One review note (018) wrongly says an anchor was replaced; see PASSES.md.
4. **Most citations of authority point to a draft.** 34 of the 68 `parent` relations point to the ToG draft, which binds only once the owner approves it. UR comes next with 20. So until Stage 1 approval, most domains have no binding parent text beyond UR's stub criteria.
5. **Wave proposals** (for the owner):
   - 024: move to Wave 2.
   - 025: name in Wave 2.
   - 028: name in Wave 2 beside 016. 016 depends on 028, so leaving 028 unscheduled inverts a dependency.
   - 035: name in Wave 3.
   - 038: owner choice between Wave 3 and changing the priority to P3.
6. **Audit load is concentrated.** The primary audit items fall mostly on 005 (6), 014 (5), 007 (4) and 013 (4). Twenty-four domains are primary for no audit item.

## Diminishing returns

- X3-8 (authority classified) and X3-9 (proposals present) passed largely by construction, because the agent wrote both registers from the same rows.
- X3-12 and X3-13 are definitional checks of the home-rule logic.
- The checks that carry information are X3-6 and X3-7, and both failed.
- The anchor review is still one agent's reading. An independent reviewer is needed, and none is named (GAP-003).

## Boundary

- No new file overlaps the suite in an 80-character window. This includes this run's own data outputs, which X3-11 now scans.
- The Baseline's two known files stay as recorded.
- Output titles now use the register's short slugs.
