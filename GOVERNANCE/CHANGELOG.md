# GOVERNANCE — Change log

## 2026-10-24 — Universal Regulation 0.1.0 (Proposed) and audit v1
- **Added** `UNIVERSAL_REGULATION.md` (GAIA-GOV-UR-001, rev 0.1.0, status Proposed): the owner's Universal Regulation Principle, seven universal laws, universality layers, five regulation domains (Epistemic, Scientific, Ethical, Technical, Operational) and absolute boundary, preserved verbatim; decision vocabulary and gate record; universal standards (Evidence, Provenance, Testing, Risk, Review, Authorization); domain-standard stubs UR-EPI/SCI/ETH/TEC/OPS with acceptance criteria; relationship to `Research/README.md` (responsibility ladder, gates) and `Research/RESEARCH_PLAN_EXTENSION.md`; adoption path.
- **Added** `AUDIT_UNIVERSAL_REGULATION_v1.md` and `AUDIT_UNIVERSAL_REGULATION_v1.csv`: 45 items over all main content, Cycles 0-4, Master Report, Tracks A-D, Maps v1-v8 and tools; 20 PASS, 13 FAIL, 12 INDETERMINATE; overall gate INDETERMINATE. Records audit-trail findings: placeholder commit `53b6603` (replaced by `5ee8d0f`/`fd776a5`) and parallel-push slips (C4 b_003/b_004, b_006/b_007; Track A b001/b002).
- **Added** `README.md` and `MANIFEST.sha256` for this folder.
- Branch: `research/governance-universal-regulation`, created from `research/track-ssc-d-x12` @ `9988d35`. No existing file modified. No pull request opened; nothing merged; `main` not written.
- Drafted by Grok Bot for the repository owner. The standard is **not** declared implemented.

## 2026-10-24 — Audit v1 remediation (branch `research/governance-audit-fixes`)
Branch created from `research/governance-universal-regulation` @ `7dded25`. Commits are authored as **Grok Bot** with a `Co-authored-by: Kyle Steen` trailer. **Nothing in history was rewritten. No existing research file was modified.** No pull request was opened; `main` was not written.

### Added
- Root `SECURITY.md`: private reporting route for a private repository, coordinated-disclosure steps, and links to Laws 1, 4, 5, 6 and 7. (UR-L4-04)
- `.github/workflows/verify.yml` and `.github/scripts/check_manifests.sh`: CI running every `MANIFEST.sha256`, the `gaia_tools` pytest suite and both validators on pull requests and `research/*` pushes; `contents: read` only. (UR-L3-08)
- `.github/CODEOWNERS`: `* @KyleAlexanderSteen`. (UR-L5-01)
- `GOVERNANCE/RISK_LEVELS.md` and `PRODUCT_REGISTER.csv`: responsibility-ladder tiers with M/W overlays, applied to 64 products, each with an owner and a decision authority. (UR-L4-01, UR-L5-01)
- `GOVERNANCE/LAW2_CROSSWALK.md` and `LAW2_CROSSWALK_COUNTS.csv`: (label, claim_class) mapped to Law 2's six distinctions over 1,263 claim-map rows; two limits stated. (UR-L2-02)
- `GOVERNANCE/GATE_AUTHORITY.md`: the owner is the final authority for every gate; INDETERMINATE is never PASS; merging is not a gate PASS; register of 11 gate records. (UR-L3-05, UR-L3-06)
- `GOVERNANCE/tools/build_registers.py`: deterministic generator for the two CSV files.
- `Research/Master-Report-Unconditional-and-Conditional-Love/MANIFEST.sha256`: 15 files, computed from the files on `main` (subtree `7050a88`). (UR-L3-09)
- `GOVERNANCE/AGENT_PUSH_LOG.md`: which branches the agent wrote, from its own process log. (UR-L5-03, UR-L5-06)
- `GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v2.md` and `.csv`: re-audit of all 45 items. v1 is kept unchanged.
- `docs/history/README-2026-10-23.md`: verbatim copy of the previous root README.

### Changed
- Root `README.md`: new revision that matches the repository (main @ `517f901`: Cycles 0-4, Master Report, Tracks A-D, Maps v1-v8, tools 0.5.1), lists the pending branches, shows gate state, and adds owner TODOs for the licence and branch protection. Previous text is preserved in `docs/history/` and in git history. (UR-L1-04)
- `GOVERNANCE/README.md` (index) and `GOVERNANCE/MANIFEST.sha256` (re-computed).
- This change log (entries appended; earlier entries unchanged).

### Incidents recorded in the repository (history not rewritten)
1. **Placeholder commit `53b6603`** (`research/track-ssc-d-x12`, 2026-10-24 07:15:10 UTC, "Track Cycle D (x12): batch 000 of 025"). A tool-call error wrote 8 Track D files whose content was the literal text of a `$file:` placeholder path instead of the real file. The next commits, **`5ee8d0f`** ("real contents; replaces placeholder commit 53b6603") and **`fd776a5`**, wrote the real contents. The final Track D tree matches the verified local build (5/5 subtree SHAs). Impact on research content in the final tree: none. The commit stays in history and is now part of `main` through PR #7. (UR-L5-04)
2. **Parallel pushes.** The push procedure requires one write at a time. Pushes were issued concurrently four times: Cycle 4 batches b_003/b_004 and b_006/b_007; Track A batches b001/b002; Divergence x3 pushes 2/27 and 3/27 (commits `fdf53aa`, `4779632`; history checked linear `a0247a6` → `fdf53aa` → `4779632`). Each batch landed as its own commit and the subtree hashes verified, so no content was lost. Before this entry, the Cycle 4 and Divergence x3 slips were recorded only outside the repository. (UR-L5-05)
3. **Attribution.** Agent commits before this branch carry the owner's name (see `AGENT_PUSH_LOG.md`). The newest Divergence x9 commits (2026-10-24 16:41 UTC) are also authored as Kyle Steen. (UR-L5-03, still open)
4. **CI first run.** The first `verify` run on this branch (run 40112949738, commit `07357e2`) ended as *failure* within 4 seconds with no steps executed and no log stored: the job never started on a runner. The cause is not visible to the agent's token. It is consistent with GitHub Actions being unavailable to this private repository (for example an account spending or billing limit). The next two runs (40113207788, 40113366575) ended the same way. The owner can see the reason on the run page.

### Remediation policy (from 2026-10-24)
- Errors are fixed **forward**: a new commit corrects the files and names the bad commit, and the incident is recorded in this change log. History is never rewritten and nothing is force-pushed.
- Agents push one commit or batch at a time, wait for it to finish, verify the remote tree SHA against the local tree, and only then push the next.
- Agent commits are authored as Grok Bot with a `Co-authored-by` trailer for the owner.
- A detected secret is revoked first and then removed in a new commit; the incident is disclosed here.

## 2026-10-24 — CI paused

At Kyle's request, the `verify` workflow now runs only on manual dispatch. GitHub Actions jobs for this private repo were not being started (no runner, no steps; likely billing), and each run sent a failure alert. The same checks run locally before every agent push. UR-L3-08 stays INDETERMINATE.
