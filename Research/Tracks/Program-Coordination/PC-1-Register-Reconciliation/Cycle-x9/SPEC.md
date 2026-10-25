# PC-1 Cycle x9: Specification

Written and pushed **before** any x9 run. Stacked on `research/pc1-x6` (d09546f3). Pre-registered checks: `config.json` (X9-1 to X9-10).

x9 **tests** the x6 domain rows and does not edit them. Any repair belongs to x12.

## Scope
1. **Reviewer requirements from the risk tiers** (`../judgments/domain_tiers_x9.csv`). Each domain gets a *scope tier*: the highest Risk Levels tier its subject reaches (RL-1 to RL-5), with a basis. Every domain standard is itself an RL-2 Meta Power product, since a standard governs other products. The tool derives the roles required:
   - RL-2 needs `auditor` ("covered by the next audit")
   - RL-3 or higher needs `ethics-rights` (ethics review before PASS) and `community-rep` (affected parties)
   - RL-5 needs `independent` (independent scrutiny)
   - a domain governing any W-overlay product needs `ethics-rights` (ETH-5)

   These are then compared with the proposed reviewer roles.
2. **Change-control rules** (`../judgments/change_control_x9.csv`). There is one rule per home type, drawn from ToG §13 and the repository's CHANGELOG practice.
3. **Owner decision packet** (`../judgments/decisions_x9.csv`). The tool lists every open issue found so far:
   - wave mismatches
   - UR-domain inconsistencies
   - remedy-home ambiguities
   - domains with no direct text
   - b9 domains
   - b16
   - reviewers (GAP-003)
   - dependency cycles
   - Wave 0 approval itself

   Each issue must be covered by a decision row with options and an agent preference. Every decision is INDETERMINATE, and the only authority is the owner.
4. **Dependency structure.** The tool computes strongly connected components of the register's named dependencies. A component of more than one domain means that no wave order can avoid every inversion.

## Iterations
- **1:** with the W keyword overlay rule
- **2:** without it, as a sensitivity test of the keyword scan, which Risk Levels itself says can over-flag

X9-10 expects iteration 2 to show no more missing roles than iteration 1. It is checked in iteration 2 only, as `le 0` on the missing count. That is a strong hypothesis: that the tier rules alone are already satisfied.

A failed check stays failed. Earlier cycles must verify identically.
