# Verification — Insurgence Cycle-A-x3 (INA)

Checked 2026-10-24T17:14:55+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. INA --snapshots` | 32 claims, 0 with a Fail; {"K-resolve": {"Pass": 32}, "K-access": {"Pass": 6, "n/a": 26}, "K-sim": {"n/a": 12, "Pass": 20}, "K-phrase": {"Pass": 17, "n/a": 15}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. INA` | 18 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 28} |
| Simulation validation checks | EXECUTION_RECORD.json | 18/18 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 26/31 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Insurgence Cycle-A-x3 — 32 claims, 8 sources in the register, 18 simulation runs, 5 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Two new sources read in full (P28 PMC, CC BY; P30 arXiv HTML main text, arXiv licence; P30 supplementary pages not rendered and not read). P29 (Ghanbarnejad et al.) fetch failed with HTTP 500 and is neither read nor cited. NAT, FOR, SOC and APP added no new source in this cycle (sources reused from IN0/DVC, re-checked at cited passages).
- Empty passes: 2 of 18 (NAT pass 3, SOC pass 3). Diminishing returns: 4 of 6 fields added only simulation claims; the cycle's new literature is confined to HUM and PHI.
- New sim kinds (saddle_bottleneck, transcritical_noise, er_critical, gw_survival, threshold_cascade, feltgen_semantic, abrams_groups) and branching_outbreak options k and v were smoke-tested once (seed 99, reduced size) before SPECs were written. The smoke runs showed in advance the strong-noise NAT advance, the HUM delta^(-1/2) slope, the PHI clique delays and an er_critical slope of 0.88 at small n; thresholds were not changed. SOC iter-3's outcome was foreknown by reasoning.
- Not-supported results reported: NAT iter-3 H1, SOC iter-3 H2, APP iter-1 H1 and iter-2 H1 (rare chains reach 1,000 cases below R = 1), HUM iter-3 H1 (all runs escape below threshold). APP iter-1 V1 passed at R0 = 0.95 only through the 0.002 allowance.
- The n^(2/3) law (FOR), negative-binomial extinction equation and R0 (1 - v) (APP), and the saddle-node passage integral (NAT) are standard results used from the agent's knowledge, not from sources read.
- The x9 VERIFICATION.md disclosure-text correction was pushed fix-forward as commit 3914c38 on research/phase-insurgence-c0 (changelog item). The x9 commits (head 6adc772) remain authored as Kyle Steen and were not rewritten.
- Pushed to research/phase-insurgence-x3 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. Gate INDETERMINATE (independent review pending).
