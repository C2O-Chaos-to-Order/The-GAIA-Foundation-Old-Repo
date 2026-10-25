# PC-1 x9: report

Status: **proposal only**. Wave 0 approval is the owner's decision alone. Source: Totality Suite v0.1.0 (owner-provided, Proposed, external, not filed).

## Check results (as they fell)

| Check | iter-1 | iter-2 |
|---|---|---|
| X9-1–X9-3, X9-5, X9-7–X9-9 | PASS | PASS |
| **X9-4**: required reviewer roles present | **FAIL (84)** | **FAIL (81)** |
| X9-6: every open issue has a decision | PASS (18/18), **incomplete: see below** | PASS |
| **X9-10**: tier rules alone are satisfied | – | **FAIL (81)** |

**X9-6 is weaker than specified.** The SPEC lists the b9 domains among the open issues. The tool, however, read b9 from the wrong metrics object, so it enumerated 18 issues instead of 29 and left out the 11 b9 issues. The check passed on those 18 only.

A manual reading shows that decision D-10 lists all 11 b9 domains, so in substance nothing is uncovered. The check as run did not test this, though. The x9 records stay as they fell. x12 fixes the enumeration behind a new config key, so that x9 still reproduces.

**X9-10's config hypothesis text is imprecise.** It says "fewer ... than with it". The test itself is `le 0` on iteration 2's missing count, as the SPEC states. The test is what was scored.

## Findings

1. **The proposed reviewer roles fall well short of what Risk Levels requires** (Plausible, given the tier judgments). 84 required roles are missing:
   - `auditor` on 36 domains. Every domain standard is RL-2, and RL-2 work must be covered by the next audit.
   - `community-rep` on 24 domains and `ethics-rights` on 22. These follow from RL-3 or higher, or from the W overlay.
   - `independent` on 2 domains: the RL-5 domains 017 and 037 (016 already has it).

   Turning the W keyword overlay off removes only 3 missing roles (84 → 81). Nearly all of the shortfall comes from the tiers themselves, not from the keyword scan.

   The Baseline assigned roles by subject only. x12 will propose roles derived from the tiers.
2. **The register's dependencies are almost entirely circular** (Established, computed from the register's named dependencies).
   - One strongly connected component contains **38 of the 45 domains**.
   - 240 of the 286 named dependency edges lie inside it.
   - Only 001, 002, 026, 038, 040, 042 and 045 are outside every cycle. (045's "all other totalities" is not parsed.)

   So no wave order can satisfy the dependency field. This explains why x6 could cut inversions only from 45 to 34. It also means the waves have to be read as priority groups, not as dependency order. Decision D-12 proposes drafting the cyclic group together, against the two acyclic starting points 001 and 002.
3. **The change-control rules exist for all four home types** (X9-5). For extend homes, the existing file's ID is kept and a TOT domain line is added. This respects the preservation rule (UR-KS-02).
4. **Decision packet:** 12 decisions for the owner. The packet has no "approve" default. Every decision is INDETERMINATE until the owner records it.

## Diminishing returns

- X9-2, X9-3, X9-5 and X9-6 pass by construction once the agent writes the rows. X9-6 was also weaker than specified, as explained above.
- The information in this cycle is in X9-4 (reviewer shortfall) and X9-7/X9-8 (circular dependencies).
- The tier judgments are the agent's own. A different reading of "when it applies" would move domains between RL-2 and RL-3, and this would change the role counts.
