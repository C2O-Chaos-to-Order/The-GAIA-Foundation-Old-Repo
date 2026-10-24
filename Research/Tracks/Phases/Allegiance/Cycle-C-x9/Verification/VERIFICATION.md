# Verification — Allegiance Cycle-C-x9 (ALC)

Checked 2026-10-24T19:39:51+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. ALC --snapshots` | 71 claims, 0 with a Fail; {"K-resolve": {"Pass": 71}, "K-access": {"Pass": 6, "n/a": 65}, "K-sim": {"n/a": 17, "Pass": 54}, "K-phrase": {"Pass": 19, "n/a": 52}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. ALC` | 54 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 49} |
| Simulation validation checks | EXECUTION_RECORD.json | 55/57 Pass; failures: SIM-AL-APP-C iter-7 V1, SIM-AL-NAT-C iter-9 V1 |
| Simulation hypotheses | EXECUTION_RECORD.json | 79/105 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Allegiance Cycle-C-x9 — 71 claims, 18 sources in the register, 54 simulation runs, 13 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; validation failures disclosed: SIM-AL-APP-C iter-7 V1, SIM-AL-NAT-C iter-9 V1.

## Disclosures
- Five new sources read in full: P54 Malkomsen et al. 2025 (PMC11817821, CC BY; fetched in ALB, first read and cited in ALC), P60 Song 2025 (PMC12968234, CC BY), P61 Shen et al. 2026 (PMC13603169, CC BY), P62 Shibayama 2025 (PMC12168133, CC BY-NC), P63 Parker & Pratt, SEP 'Josiah Royce' (rev. 15 Jan 2026; SEP copyright, free to read). Reference lists not read.
- Empty passes: 24 of 54. Diminishing returns are strong: new content came from the five sources and the new kinds' first runs; variants mostly reproduce known or analytically expected behaviour.
- New sim kinds mixture_hill (NAT), moran_game (FOR), summary_audit (SOC), t_power (APP), three_language (HUM) and betrayal_echo (PHI) were smoke-tested once (seed 99) before SPECs were written, each with the exact configuration of its iter-1 (and SOC iter-2): the outcomes of NAT-1 H1/H2, FOR-1, SOC-2, APP-1, HUM-1 and PHI-1 H1/H2 were seen in advance.
- Further foreknowledge by hand arithmetic or reasoning while reading: P61 Tukey HSD about 2.69 > 2.54 (SOC-2 H2 expected not supported); implied MSW 5.25 and eta squared 0.47 (SOC-4); mediation parts 0.20 vs 0.21 (SOC-6); Eq. 4 x* 0.267 at N 4 (FOR-3); HDRS power about 0.57 (APP-5); CTFT 2-round repair and 2.98 payoff (PHI-1 H3, PHI-5); flat MWC slope near the optimum L (NAT-7); FOR-9 crossing 4.08.
- Two runs failed validation and are indeterminate (not rerun with changed settings): NAT iter-9 (noise-free Adair refit with 14 concentrations, error 164.7) and APP iter-7 (log odds-ratio estimate 0.011 off the CI midpoint, above the 0.01 tolerance).
- Agent text error corrected before any push: the first local run of NAT iter-1 to iter-6 carried an invented title for P62 in the SPEC source text; the six local records were set aside, the text corrected to P62's actual title, and the runs re-executed with the same seeds and parameters. All 54 results hashes are identical to the first run. No thresholds changed.
- FOR iter-7 re-specifies ALB's w = 0.9 run with the correct AD threshold (1.333); the ALB record is unchanged.
- P61's post-test fusion comparison names no post hoc method; SOC-2 tests it with Tukey (the method P61 names for the prosocial outcome). An LSD test would reach significance.
- Source slips recorded: P54 (Table 4 '0.14 (1.00)', 'Cohens d', '23 participants' vs '23%', 'neither ... or'); P60 ('chronically organized', 'the entity of CHLs research', a Germany study among Inner Circle countries, funding statement inconsistent, 'co-occured'); P61 (direct-effect CI labelled 'partial mediation'; mediation parts 0.20 of 0.21); P62 ('Biochemisty' in the reference list, seen by search); P63 ('scrutinze', 'versons', 'were the truth of the conditional', a missing parenthesis, 'Russell's 1903 The Principles of Logic').
- Missing sources sought: fitted Hb MWC parameters (not found; P62 instead); identity-fusion meta-analysis (not found; P61 instead); spiritual-tradition text (P63 is a secondary philosophical survey of a Christian philosopher, partial).
- Owner context unchanged (phase-to-upgrade-level mapping recorded in the phase README as the owner's Hypothetical claim; methods unchanged).
- Pushed to research/phase-allegiance-x9 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. Gate INDETERMINATE (independent review pending).
