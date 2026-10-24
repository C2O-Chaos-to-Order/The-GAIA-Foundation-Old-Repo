# Verification — Allegiance Cycle-B-x6 (ALB)

Checked 2026-10-24T19:21:36+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. ALB --snapshots` | 50 claims, 0 with a Fail; {"K-resolve": {"Pass": 50}, "K-access": {"Pass": 5, "n/a": 45}, "K-sim": {"n/a": 12, "Pass": 38}, "K-phrase": {"Pass": 14, "n/a": 36}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. ALB` | 36 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 39} |
| Simulation validation checks | EXECUTION_RECORD.json | 41/42 Pass; failures: SIM-AL-NAT-B iter-3 V1 |
| Simulation hypotheses | EXECUTION_RECORD.json | 51/73 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Allegiance Cycle-B-x6 — 50 claims, 13 sources in the register, 36 simulation runs, 8 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; validation failures disclosed: SIM-AL-NAT-B iter-3 V1.

## Disclosures
- Five new sources read in full: P55 Benndorf & Schulz 2023 (PMC10602793, CC BY-NC-SA), P56 Leijten et al. 2026 (PMC12699127, CC BY), P57 P52's OSF project huysb (Mplus output; data files summarised by script, no licence stated, raw data not redistributed or committed), P58 Ohtsuki, Bordalo & Nowak 2007 (Harvard DASH manuscript, LAA terms), P59 Kleinig, SEP 'Loyalty' (rev. 2026). P54 (Malkomsen 2025) was fetched but not read or cited in ALB.
- Empty passes: 11 of 36. Diminishing returns are clear: new content came from the five sources; most variant runs reproduce known or analytically expected behaviour.
- New sim kinds adair_identify (NAT), table_audit (SOC) and ci_power (APP) were smoke-tested once (seed 99) before SPECs were written. Foreknowledge: adair_identify H1 not supported, H2 supported; table_audit H1 and H3 not supported, H2 supported; ci_power on developer involvement both supported.
- Further foreknowledge by reasoning or hand arithmetic: corr_regress on raw data (Study 3 fusion -> violent about +0.43; Study 2 flip possible); FOR N = 50 crossing 4.33 (H2 expected not supported); MWC slope peaking at L c^2 = 1; APP P49 run expected not supported from AL0's power.
- Agent errors kept as run: FOR iter-1 SPEC miscomputed the w = 0.9 AD threshold as 1.222 (correct 1.333), so its b/c range missed the threshold; SOC iter-2's H3 wording says 'printed alphas' but alphas computed from the raw items were used; NAT iter-1 purpose text calls the Adair constants 'AL0's cooperative curve' (they are the agent's constants). No thresholds changed after any run.
- NAT iter-3 failed V1 (noise-free refit with 21 concentrations did not recover the true constants); the run is indeterminate and was not rerun with different settings.
- P58's finite-N condition was found after the FOR runs; the SPEC text still calls the formula the agent's (unsourced), which was true when written.
- Source slips recorded: P55 ('CNA 5', 'heteroterameric', 'LGIC 2 s', Fig. 8 legend Eq. 21 for 22, 'at least as good as that for the CHA 3 and CHA 5 model'); P56 ('Observational outcome 11.46 [-16.26, -6.66]', 22 vs 26 databases); P58 ('explicitely', 'Genetaical', 'equilbiria', 'equilibirum', a 2004/2006 reference mix-up); P59 ('the one's who are loyal', 'self-maximation'); P52 Table 3 (Study 3) transposes fusion and identification, and its Study 3 SEM has a Heywood case.
- Owner context unchanged (phase-to-upgrade-level mapping recorded in the phase README as the owner's Hypothetical claim; methods unchanged).
- Pushed to research/phase-allegiance-x6 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. Gate INDETERMINATE (independent review pending).
