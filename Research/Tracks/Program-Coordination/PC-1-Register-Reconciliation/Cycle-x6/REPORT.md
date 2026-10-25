# PC-1 x6: report

Status: **proposal only**. Wave 0 approval is the owner's decision alone. Source: Totality Suite v0.1.0 (owner-provided, Proposed, external, not filed).

## Check results (as they fell; identical in both iterations)

| Check | Result |
|---|---|
| X6-1–X6-5, X6-7–X6-9, X6-11, X6-12 | PASS |
| **X6-6**: each UR criterion's domain matches its TOT domain's UR domains | **FAIL (2)** |
| X6-10: proposals do not add inversions | PASS (−11: 45 → 34) |
| X6-13: at least 10 domains are draft-only | PASS (21) |

The two iterations give the same result. 038's wave has no effect on dependency order, because no domain depends on 038 and 038's own dependencies are all scheduled by Wave 3. Changing 038's wave is therefore free in dependency terms, and the choice rests on priority alone. This is a diminishing-returns result and is reported as one.

## Findings

1. **b16 (UR domain standards vs TOT domains).** All 26 UR §5 criteria have a TOT home, and these land on 17 domains. This is Plausible evidence that the TOT domains *could* carry the UR domain standards. Two criteria cross UR's own domain lines:
   - **SCI-5**: manifests fall under UR-SCI, but under TOT they are records (014, EPI).
   - **ETH-4**: labelling spiritual claims falls under UR-ETH, but under TOT it is interpretive knowledge (023, EPI).

   If PC-2 chooses "TOT replaces UR §5", these two criteria would change UR domain. That needs a recorded decision, because UR Part I governs. The alternative is to keep UR §5 as parent criteria and have TOT standards cite them. That option moves nothing, and the agent prefers it, as a Plausible proposal.
2. **The x3 wave proposals remove 14 dependency inversions and add 3**, a net change from 45 to 34:
   - **Removed:** every inversion involving 028, 024 or 035, and most involving 025.
   - **Added:** 025 depends on 031, 037 and 043, which sit in Waves 3 and 4. Moving 025 to Wave 2 therefore makes it depend on later work.
   - **Remaining:** of the 34 inversions left, many are Wave 1 (P0) domains depending on Wave 2 or 3 domains, for example 012 → 019, 020 and 009 → 016, 018.

   This suggests the dependency graph has mutual or circular dependencies that no wave order removes. x9 will measure this directly.
3. **21 of 45 domains are draft-only.** Their only direct support is the unapproved ToG draft. **Twelve of these also have no PC-4 primary report:** 004, 009, 010, 012, 019, 022, 026, 028, 031, 032, 034, 035. These twelve start from nothing on both the governance and the research side. Five of them are P0 (004, 009, 010, 012, plus 019 at P1) and would need the most new writing in Wave 1–2.
4. **The Product Register concentrates on a few domains.** Through kind and overlay rules:
   - 005, 006, 007 and 023 govern 52–60 products each.
   - 021 and 027 govern 44 products through the W overlay. These are the two domains x3 found to have no direct governing text.

   So the well-being duty applies to 44 products, and no TOT standard yet defines it beyond the ethics-review trigger.
5. **ToG §19 planned files** each have a domain. Six of the ten are registers, records or indexes, which are companions to a domain, not homes for one. Only `TOTALITY_OF_GOVERNANCE.md` (045) and `DOMAIN_STANDARDS/` (the 38 new and shared domains) are homes.
6. **X3-7 explained.** All five remedy-home mismatches now have an authority row for the primary domain citing the remedy file (X6-11 PASS). The cross-reference rule from x3 is consistent with the register.

## Limits and diminishing returns

- X6-8, X6-9 and X6-11 pass by construction once the agent writes the rows.
- The information is in the distributions: products per domain, criteria per domain, inversions.
- The product rules work at the level of product kind, not per product. A finer join would need per-report reading, which is PC-4's territory and is not repeated here.
