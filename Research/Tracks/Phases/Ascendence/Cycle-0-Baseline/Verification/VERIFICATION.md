# Verification — Ascendence Cycle-0-Baseline (AS0)

Checked 2026-10-24T23:04:44+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. AS0 --snapshots` | 12 claims, 0 with a Fail; {"K-resolve": {"Pass": 12}, "K-access": {"n/a": 11, "Pass": 1}, "K-sim": {"n/a": 6, "Pass": 6}, "K-phrase": {"Pass": 6, "n/a": 6}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. AS0` | 6 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 17} |
| Simulation validation checks | EXECUTION_RECORD.json | 6/6 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 24/27 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Ascendence Cycle-0-Baseline — 12 claims, 6 sources in the register, 6 simulation runs, 4 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Six new sources (P85-P90) read in full; none reused from earlier phases. Empty passes: 0 of 6.
- Per-field readings of 'Ascendence' (adaptive walks up fitness landscapes, steepest ascent/contraction, upward social mobility, physical ascent and ascent rate, rising intonation, Diotima's ascent of love) are this track's choices; no repository document defines Ascendence. Competing readings are recorded in DEFINITIONS.md.
- New sim kinds (adaptive_walk, contraction_check, arith_audit in sim_soc/sim_app/sim_hum, ascent_ladder) were smoke-tested once at seed 99 with exactly the AS0 configuration before the SPECs were written, so all outcomes were seen in advance; hypotheses and thresholds were written before the smoke test and not changed. The NAT K comparison (H3) was Not supported in the smoke test and Supported at seed 34101: fragile (AS0-NAT-02). Foreknowledge from reading: SOC 77.8% vs 78.8%; APP risk ratio about 2.09 and odds ratio about 9.6.
- Not supported (kept as findings): SOC H2 (Table 5's 78.8%) and H4 (Table 3/4 sample sizes); APP H5 ('odds' wording of 2.069).
- PHI-02 is a Hypothetical toy. Ascent-rate odds/risk computation uses point estimates and natural logs (agent's assumptions).
- P90 (SEP) was fetched directly after one PMC search with one irrelevant hit; it is quoted in short phrases only (SEP copyright).
- Source slips recorded: P87 Table 5 78.8% (77.8% from its deviances; text 79%); P88 Fig. 2 'odds' for a risk ratio; P89 'rise' labelled L* H-H% in the results summary and Fig. 3 caption; P85 reports an incorrect 1/28 calculation in the study it re-examines (Papkou et al.).
- Owner context (does not change methods): 'Ascendence corresponds to Ultra/Ultraphysical' is recorded in the phase README as the owner's Hypothetical claim; no claim depends on it.
- Pushed to research/phase-ascendence-c0 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. Gate INDETERMINATE (independent review pending).
