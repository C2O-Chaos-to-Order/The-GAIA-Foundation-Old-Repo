# Verification — Allegiance Cycle-D-x12 (ALD)

Checked 2026-10-24T19:58:25+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. ALD --snapshots` | 88 claims, 0 with a Fail; {"K-resolve": {"Pass": 88}, "K-access": {"Pass": 6, "n/a": 82}, "K-sim": {"n/a": 21, "Pass": 67}, "K-phrase": {"Pass": 23, "n/a": 65}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. ALD` | 72 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 58} |
| Simulation validation checks | EXECUTION_RECORD.json | 78/78 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 101/128 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Allegiance Cycle-D-x12 — 88 claims, 22 sources in the register, 72 simulation runs, 17 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Four new sources read in full: P64 Henry et al. 2021 (PMC8390878, CC BY), P65 Chen et al. 2026 (PMC13655717, CC BY), P66 Varmann et al. 2023 (published-version PDF on the UNED Identity Fusion project site, free to read, licence not stated), P67 Book of Ruth, KJV (Project Gutenberg #8008, public domain in the US). Reference lists not read.
- Empty passes: 42 of 72. Diminishing returns are strong: new content came almost entirely from the four new sources and first runs on them; variants reproduce known or analytically expected behaviour.
- New code: mwc_binding gained an optional 'hyps' list (H4+; absent hyps leaves earlier behaviour unchanged), summary_audit gained optional sums, medians, fisher and sign_ci sections, and a new count_audit kind was added to sim_hum. Each was smoke-tested at seed 99 before SPECs were written. The mwc smoke used NAT iter-1's exact configuration (outcome seen in advance); the summary_audit and count_audit smokes used toy values plus P66's Model 1 CI for the Fisher section.
- Foreknowledge from reading or hand arithmetic: P66 effect-type counts 98 vs 106 (SOC-2 H2), .09 outside [-.20, .01] (SOC-3 H1), P65 245 - 184 = 61 (HUM-1 H1), 2,134 vs 2,104 and median 74 (HUM-2), resistance 11 > ambivalence 10 (HUM-3), N 30 crossing 4.6 (FOR-11).
- Two run starts crashed before producing results and were restarted: NAT iter-4 (dictionary key '4823' vs '4823.0' in the agent's hypothesis expression; expression changed to use the main curve at the same L, disclosed in its SPEC) and HUM iter-1 to iter-3 (summary_audit is a SOC kind; the count_audit kind was added to sim_hum and the HUM audits re-specified to use it). The crashed iteration folders (SPEC only, no results) were set aside. No thresholds changed.
- Two hypotheses were ill-posed by the agent and are reported as not supported without re-running: PHI iter-10 (recovered quality settles at theta, so Q >= 0.45 at theta 0.4 is unreachable) and SOC iter-1 H1 (a 0.01 z-scale threshold is about the size of two-decimal rounding).
- All 72 runs passed validation (no indeterminate runs in ALD).
- Source slips recorded: P64 ('12 mM voxelotor' vs uM, 'Pharmakokinetics', two references with one title); P65 ('most frequently observed' vs counts, 'four' vs 'three' recursive pathways, 61 vs 60, a miscited Greek example); P66 ('.09 [-.20, .01]', 'keffects = 8, keffects = 10', 'Please not that', 'the the Society', 98 of 106 effects).
- Missing sources sought: fitted Hb MWC parameters (found, P64); identity-fusion meta-analysis (found, P66); primary religious text (found, P67 Ruth; non-Abrahamic still missing); P56 and P66 OSF data not fetched.
- Owner context unchanged (phase-to-upgrade-level mapping recorded in the phase README as the owner's Hypothetical claim; methods unchanged).
- Pushed to research/phase-allegiance-x12 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. Gate INDETERMINATE (independent review pending).
