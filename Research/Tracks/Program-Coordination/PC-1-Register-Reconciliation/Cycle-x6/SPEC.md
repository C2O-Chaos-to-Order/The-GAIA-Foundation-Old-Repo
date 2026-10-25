# PC-1 Cycle x6: Specification

Written and pushed **before** any x6 run. Stacked on `research/pc1-x3` (3fd647b4). Pre-registered checks: `config.json` (X6-1 to X6-13).

## Scope (the cross-checks planned for x6)
1. **UR b16 crosswalk** (`../judgments/ur_criteria_x6.csv`). Each of the 26 UR §5 criteria gets one primary TOT domain. The crosswalk tests whether the TOT domains could implement the UR domain standards, which is the b16 question. PC-2 decides the answer; this crosswalk only supplies the evidence.
2. **ToG §19 planned files** (`../judgments/tog19_x6.csv`). Each planned file is assigned to the domains it serves, as one of: `home`, `companion`, `index`, `record`.
3. **Product Register join** (`../judgments/product_rules_x6.csv`). Rules by product kind and overlay map each of the 64 products to its governing domains.
4. **Dependency order.** The tool parses the register's dependency field (named TOT IDs only; "all other totalities" is ignored). It then counts inversions, where a domain is scheduled before a domain it depends on, under two schedules:
   - the roadmap waves, with unnamed domains unscheduled
   - the x3 proposed waves
5. **Remedy rule** (from x3 finding 2). An open audit item whose remedy home is not its primary domain's home counts as explained only when the authority register classifies that file for that domain.
6. **Draft-only domains**. These are domains whose only direct support is the unapproved ToG draft.
7. **PC-4 cross-check**. Domains without a PC-4 primary report are listed alongside draft-only domains. This is informational, with no check.
8. **Corrections carried forward:**
   - the 018 review note
   - 003 now cites Risk Levels RL-3, which holds the ethics-review duty (x3 finding 2)

## Iterations
- **1:** the 038 proposal is Wave 3 (option A)
- **2:** the 038 proposal is Wave 4 (option B)

Both use home rule `as_judged`.

A failed check stays failed. Earlier cycles must verify identically.
