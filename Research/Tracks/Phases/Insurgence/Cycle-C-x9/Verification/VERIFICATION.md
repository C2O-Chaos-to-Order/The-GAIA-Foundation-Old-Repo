# Verification — Insurgence Cycle-C-x9 (INC)

Checked 2026-10-24T17:59:01+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. INC --snapshots` | 75 claims, 0 with a Fail; {"K-resolve": {"Pass": 75}, "K-access": {"Pass": 10, "n/a": 65}, "K-sim": {"n/a": 25, "Pass": 50}, "K-phrase": {"Pass": 31, "n/a": 44}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. INC` | 54 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 58} |
| Simulation validation checks | EXECUTION_RECORD.json | 54/54 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 65/73 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Insurgence Cycle-C-x9 — 75 claims, 18 sources in the register, 54 simulation runs, 9 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Four new sources read in full: P38 (CC BY; equations read from images), P39 (CC BY-NC), P41 (CC BY), P43 (CC BY; main text, references not read). P40 and P42 were fetched but are long and were not read; they are not cited. FOR received no new source.
- Empty passes: 38 of 54 (mostly replications and variants folded into earlier claims). Diminishing returns are clear: every source-bearing pass is pass 1; passes 8-9 added nothing in any field, and FOR added one simulation claim in nine passes.
- Source issues recorded: P41 Eq. 2 prints the noise ramp as 2.4e-4 t + 0.05, which contradicts its own plateaus (the offset form 2.4e-4 (t - 500) + 0.05 was used); P39's per-year risks (10%/1%) were not reproduced from its stated parameters under either reading (may reflect the empirical distribution or SI details not read).
- New kinds smoke-tested once (seed 99); foreknowledge disclosed in SPECs: static delta 0.877, runaway at A0 = 2.0 vs 1.8, escalation tail 1.73, per-year risks 13%/2.3% and 6.5%/0.2%, N-tipping median 1792 (5 runs), AR1 trend 0.37, fold tipping -0.387 and AR1 trend 0.84, Kramers slope 0.51, gradual vs sudden 0.01 vs 1.06. PHI ramp parameters were retuned in deterministic trial runs (a = 1.5 never took off), so iter-1 to 3 outcomes were seen in advance.
- Not supported: SOC iter-3, iter-4, iter-6 H1 and H2, SOC iter-9 H2 (third seed), APP iter-1 H1, APP iter-2 H2, APP iter-8 H1 (K = 1,000 artefact again).
- Kramers' law, the steady Frank-Kamenetskii solution and the fold value 2/(3 sqrt 3) are standard results used from the agent's knowledge (labelled in SPECs); P38 states 0.88 and P41 names Kramers' rate.
- Pushed to research/phase-insurgence-x9 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. CI (GitHub Actions) is paused for cost; all checks run locally. Gate INDETERMINATE.
