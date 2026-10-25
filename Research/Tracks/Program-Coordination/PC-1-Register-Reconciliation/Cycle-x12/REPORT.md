# PC-1 x12: report

Status: **proposal only**. Wave 0 approval is the owner's decision alone. Source: Totality Suite v0.1.0 (owner-provided, Proposed, external, not filed).

## Check results (as they fell; identical in both iterations)

All 15 checks **PASS**: X12-1 to X12-15.
- X12-7: the issue list now holds all 29 issues; x9 held 18.
- X12-15: the final wave proposals give 33 inversions, against 45 for the roadmap (delta −12). x6 gave delta −11. The x9 revision of 025 removed one more.

## Diminishing returns, stated plainly

x12 found nothing new. The passes are mostly the result of construction:
- **X12-5** (required roles) passes because pass 1 adds exactly the roles the x9 rule asks for.
- **X12-6 and X12-7** pass because the enumeration bug was fixed and D-10 already listed the b9 domains.
- **X12-14** shows the repair touched nothing else.

The substantive results of PC-1 were already in place by x9. x12 consolidates them into `../REGISTER.md` and closes the two defects found along the way: x9's issue enumeration, and the reviewer shortfall. Another cycle of the same method would most likely only re-confirm these results. Better next steps:
- **owner decisions D-01 to D-12**
- **a named independent reviewer** (GAP-003)

## Failed checks across PC-1 (kept as they fell)

| Cycle | Check | Result | Status now |
|---|---|---|---|
| Baseline | C0-9 boundary | PASS as computed, but blind to its own cycle. The full scan flags 2 Baseline files, because of two register titles. | Fixed from x3 on (short slugs; own outputs scanned). The Baseline files are frozen. |
| x3 | X3-6: every domain has a direct anchor | FAIL (021, 027) | Open finding (D-09) |
| x3 | X3-7: remedy home = primary domain's home | FAIL (5) | Explained by the authority register (X6-11) and proposed rule D-08 |
| x6 | X6-6: UR domain consistency | FAIL (SCI-5, ETH-4) | Open finding (D-07) |
| x9 | X9-4, X9-10: reviewer roles | FAIL (84 and 81) | Repaired in x12 (X12-5) |
| x9 | X9-6: issue coverage | PASS, but incomplete (b9 not enumerated) | Fixed in x12 (X12-6, X12-7) |
