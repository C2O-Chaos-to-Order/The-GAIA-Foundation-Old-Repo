# Verification — Insurgence Cycle-B-x6 (INB)

Checked 2026-10-24T17:37:37+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. INB --snapshots` | 54 claims, 0 with a Fail; {"K-resolve": {"Pass": 54}, "K-access": {"Pass": 9, "n/a": 45}, "K-sim": {"n/a": 20, "Pass": 34}, "K-phrase": {"Pass": 26, "n/a": 28}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. INB` | 36 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 46} |
| Simulation validation checks | EXECUTION_RECORD.json | 36/36 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 48/57 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Insurgence Cycle-B-x6 — 54 claims, 14 sources in the register, 36 simulation runs, 7 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Six new sources read in full: P29 (arXiv HTML; the INA failure resolved by a different URL), P31, P32, P35 (Europe PMC, CC BY), P36 (lecture slides, no licence), P37 (LibreTexts, CC BY-NC-SA). P33 and P34 were fetched but are long and were not read; they are not cited.
- Empty passes: 16 of 36 (replications and variants folded into earlier claims). Every field gained one new source in pass 1; passes 2-6 added only simulation claims. Diminishing returns are clear in passes 3-6.
- Source issues recorded: P37 derivative sign slip; P29 swapped exo/endo labels in one formula and a caption; P31 describes Percent Committed with its complement's definition; P35 gives an implausible Haiti death toll and contradicts its own caveat on the extinction claim.
- New kinds smoke-tested once (seed 99); the smoke showed in advance the nucleation commitment at n* = 8 (0.33, so the run used n* = 27), the er_critical slope at lambda = 1 (2 points), the Bass G values, the shock reversal and a degenerate pillar-toy regime (parameters retuned once, thresholds unchanged). PHI iter-5 (neutral utility) was foreknown by formula.
- Not supported: SOC iter-2 H1, SOC iter-5 and iter-6 H2, APP iter-2 H1-H3 (H3 placeholder), APP iter-3 and iter-5 H1, PHI iter-5 H1.
- Detailed-balance nucleation kinetics, the birth-death MFPT formula, the NB extinction equation and the R0 (1 - v) rule are standard results used from the agent's knowledge, labelled unsourced in the SPECs.
- Pushed to research/phase-insurgence-x6 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. CI (GitHub Actions) is paused for cost; all checks run locally. Gate INDETERMINATE.
