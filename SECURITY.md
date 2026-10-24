# Security policy

**Owner:** KyleAlexanderSteen (repository owner) · **Status:** Proposed (adopted when the owner merges it) · **Date:** 2026-10-24
Part of the GAIA Universal Regulation standard: Law 4 (Safety Before Capability), Law 5 (Accountability Before Authority) and Law 6 (Consent Before Access). See [`GOVERNANCE/UNIVERSAL_REGULATION.md`](GOVERNANCE/UNIVERSAL_REGULATION.md), domain standard UR-TEC, criterion TEC-4.

## What this repository contains
Research documents, offline synthetic simulations, and research tooling (`Research/tools`, a Python package that reads and checks the corpus). There is **no deployed service, no user data and no production system**. Nothing here is authorized for deployment (Law 7).

## What to report
- **Security problems:** a credential, token or private data committed by mistake; a script that reaches the network, runs untrusted input or writes outside its folder; a dependency with a known vulnerability; a CI workflow with more permissions than it needs.
- **Integrity problems:** a manifest that does not match its files; a claim whose cited passage does not exist; a simulation result that does not reproduce; a record changed without a change-log entry. These count as security problems here, because the corpus's value depends on its integrity (Law 1).
- **Safety or rights problems:** personal or sensitive data, misuse potential, or content that could cause harm if acted on (Laws 4 and 6).

## How to report privately
This repository is **private**, and GitHub's private vulnerability reporting and repository security advisories are available only for public repositories ([GitHub Docs](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository)). Until that changes:

1. **Do not put the details in a public place**, an issue, a pull request, a commit or a chat that others can read.
2. **People with access:** open an issue titled `Security contact request` with **no details**. The owner will reply and agree a private channel. If you already have a private channel with the owner, use it directly.
3. **If the repository becomes public:** the owner enables *Private vulnerability reporting* (Settings → Advanced Security). Then use **Security → Advisories → Report a vulnerability**, which replaces step 2.
4. **AI agents** acting for the owner report to the owner in their private conversation, never in a public place, and never test a problem against a live system they are not authorized to touch.

Please include what you found, where (path and commit), how to reproduce it, and what you think the impact is.

## What happens next (coordinated disclosure)
| Step | Target |
|---|---|
| Owner acknowledges the report | within 7 days |
| Assessment: valid or not, severity, which files and branches | within 14 days |
| Fix on a `research/*` branch, merged by the owner; records corrected in new versions (history is not rewritten) | as soon as practical; severity first |
| Disclosure in `GOVERNANCE/CHANGELOG.md` (what happened, impact, fix) after the fix lands, crediting the reporter if they wish | after the fix |

These targets are the owner's goals, not guarantees. If a committed secret is involved, the **first** step is to revoke or rotate it, because removing it from the files does not remove it from git history.

## Out of scope
Disagreements about research conclusions are not security reports. Raise them as normal review findings (see `GOVERNANCE/GATE_AUTHORITY.md` and `Research/README.md` §4 "Independent challenge").

## Related
- [`GOVERNANCE/RISK_LEVELS.md`](GOVERNANCE/RISK_LEVELS.md): risk tiers for every product.
- [`GOVERNANCE/CHANGELOG.md`](GOVERNANCE/CHANGELOG.md): past incidents (for example the placeholder commit `53b6603`) and the remediation policy.
- A research report on coordinated vulnerability disclosure is planned. This policy will be revised after it.
