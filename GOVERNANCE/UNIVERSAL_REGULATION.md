# GAIA Universal Regulation Standard

**Stable ID:** GAIA-GOV-UR-001 · **Revision:** 0.1.0 · **Status: Proposed** · **Date:** 2026-10-24
**Owner:** repository owner, GitHub `KyleAlexanderSteen` (author of the principle and the seven laws)
**Drafted by:** Grok Bot, from the owner's text of 2026-10-24 (preserved verbatim in Part I)
**Decision authority for adoption:** the repository owner, by reviewing and merging this branch. Until then this standard is **Proposed**, not adopted and not implemented.
**Audit against this standard:** [`AUDIT_UNIVERSAL_REGULATION_v1.md`](AUDIT_UNIVERSAL_REGULATION_v1.md) (gate: INDETERMINATE).

> This document does not declare the standard implemented, does not pass any gate, and does not authorize implementation or deployment of anything.

---

## Part I — The owner's text (verbatim)

### The Universal Regulation Principle
Every GAIA research product, knowledge structure, model, simulation, system, and implementation must operate under a common framework of integrity, evidence, safety, accountability, verification, and authorization.

I recommend seven universal laws:

1. **Integrity Before Intelligence** — honesty, truthfulness, and traceable evidence take precedence over capability or persuasive conclusions.
2. **Evidence Before Assertion** — distinguish established findings, mathematical results, interpretations, spiritual beliefs, hypotheses, and speculation.
3. **Verification Before Advancement** — define acceptance criteria, test, challenge, reproduce, and document results before passing a gate.
4. **Safety Before Capability** — safeguards must scale with potential harm, autonomy, reach, and impact.
5. **Accountability Before Authority** — every consequential action has a defined owner, permission boundary, and audit trail.
6. **Consent Before Access** — protect privacy, rights, autonomy, and legitimate ownership.
7. **Authorization Before Implementation** — research, successful testing, and technical capability never independently grant permission to deploy.

### How universality should work

| Layer | Content |
|---|---|
| **Universal principles** | Mandatory across all GAIA domains and repositories |
| **Universal standards and procedures** | Evidence · Provenance · Testing · Risk · Review · Authorization |
| **Research** | Sources, claims, uncertainty, falsification |
| **Simulations** | Specifications, executions, reproducibility |
| **Knowledge systems** | Identity, provenance, versioning, consistency |
| **Implementation** | Security, testing, approval, monitoring |
| **Auditable decisions** | PASS · FAIL · INDETERMINATE |

No mandatory gate is bypassed because a project claims completion.

### The critical distinction
Universal regulation must govern both what GAIA is allowed to **claim** and what GAIA is allowed to **do**.

- **Epistemic regulation** governs knowledge and evidence.
- **Scientific regulation** governs methods, tests, and reproducibility.
- **Ethical regulation** governs harm, rights, and responsibility.
- **Technical regulation** governs security, reliability, and system behavior.
- **Operational regulation** governs permissions, deployment, and oversight.

These are connected under one standard, but their individual acceptance criteria remain appropriate to their domains.

**Recommendation (owner):** establish Universal Regulation as a foundational GAIA governance standard, then derive domain-specific standards from it. Audit the current repository against that standard before declaring it implemented.

### Absolute boundary
**No claim of intelligence, consciousness, spiritual significance, or exceptional capability exempts any system from evidence, safety, accountability, or authorization.**

---

## Part II — Normative structure (drafted from Part I; Proposed)

Everything below derives from Part I. Where wording here and Part I differ, **Part I governs**.

### 1. Scope
Applies to every GAIA research product, knowledge structure, model, simulation, system and implementation, in this repository and in any other GAIA repository, including work produced by AI agents acting for the owner. An agent's output is regulated exactly like a human's; the absolute boundary applies to AI systems as much as to any claim about people, traditions or Earth.

### 2. Decision vocabulary
Every regulated decision is recorded as **PASS**, **FAIL** or **INDETERMINATE**.

- **PASS** — every acceptance criterion is met, with evidence a reviewer can inspect.
- **FAIL** — at least one criterion is demonstrably not met.
- **INDETERMINATE** — evidence is missing, inconsistent, or depends on a check not yet performed (for example independent human review). **INDETERMINATE is never PASS** and never unlocks the next gate.
- A product's own statement that it is complete is not evidence (Part I: no gate is bypassed because a project claims completion).

### 3. Gate record (applies in all five domains)
A gate decision is valid only if it records: **scope · acceptance criteria · evidence (paths/hashes) · decision · decision authority (a named person or role) · timestamp · remaining blockers**. This is the existing Research/README.md §7 rule, made universal. A gate record missing its authority is itself INDETERMINATE.

### 4. Universal standards and procedures
| Standard | Minimum procedure |
|---|---|
| **Evidence** | Every claim cites the source passage or execution record that supports it; general topical relevance is not support. |
| **Provenance** | Every source records title, issuer, locator, access date, access mode and a digest of the version read; every file set carries a manifest of digests. |
| **Testing** | Acceptance criteria are written before the test runs; failures and negative results are kept and reported. |
| **Risk** | Every product records its responsibility-ladder level (Research/README.md §2) and the safeguards that level requires. |
| **Review** | Gates that require independent challenge stay INDETERMINATE until a reviewer who did not produce the work records findings. |
| **Authorization** | Integration into `main`, deployment, external release or irreversible change requires the owner's explicit, recorded approval. |

### 5. Derived domain standards (stubs, Proposed)
Each stub lists the acceptance criteria the audit checks. The stubs are drafts for the owner to refine; each will become its own file (`GOVERNANCE/UR-<DOMAIN>.md`) only when the owner approves.

#### 5.1 UR-EPI — Epistemic (knowledge and evidence) · Laws 1, 2
- EPI-1 Every claim carries exactly one evidence class and a stable ID.
- EPI-2 The evidence classes distinguish, at minimum, established findings, mathematical results, interpretations, spiritual beliefs, hypotheses and speculation (Law 2), or a documented crosswalk maps the classes in use onto these six.
- EPI-3 Every Established claim resolves to a source actually read (full text or stated access mode) or to a passing, reproduced execution record.
- EPI-4 No source, datum, validation or review is invented; unreachable evidence is INDETERMINATE.
- EPI-5 Repository-level status statements (READMEs, summaries) are accurate for the branch they sit on, and every link in them resolves.
- EPI-6 Negative findings, failed checks and contrary evidence are retained, not deleted.

#### 5.2 UR-SCI — Scientific (methods, tests, reproducibility) · Law 3
- SCI-1 Each simulation has a specification (question, model, inputs, algorithm, expected outputs, failure criteria, environment) written before execution, and the time ordering can be checked.
- SCI-2 Every execution has a record (parameters, seeds, environment, output hashes); a rerun reproduces it, or the difference is reported.
- SCI-3 Each claim states uncertainty and limits, and non-established claims state what would falsify or revise them.
- SCI-4 Internal consistency, independent challenge and reproducibility are reported separately (Research/README.md §4); repetition is never presented as independence.
- SCI-5 Manifests and digests agree with the delivered files.

#### 5.3 UR-ETH — Ethical (harm, rights, responsibility) · Laws 4, 6 and the absolute boundary
- ETH-1 Each product records its responsibility-ladder level and foreseeable effects; safeguards meet that level's minimum.
- ETH-2 No personal, sensitive or human-subject data without consent, authority and protection.
- ETH-3 Third-party material is used within its licence (quotation, access terms); reuse terms for GAIA's own work are stated.
- ETH-4 Spiritual, philosophical and extraordinary claims are labelled as such and never used to bypass evidence or ethics (Magic Power rung; absolute boundary).
- ETH-5 Where human well-being, health or safety is discussed, an ethics review is recorded before any gate PASS.

#### 5.4 UR-TEC — Technical (security, reliability, system behaviour) · Laws 4, 7
- TEC-1 Code states what it does and does not do (e.g. "research tooling only; no service; no deployment").
- TEC-2 Automated tests exist and run on every change (continuous integration), with results recorded.
- TEC-3 Dependencies are declared; security-relevant dependencies are pinned or reviewed.
- TEC-4 A security policy and a vulnerability-disclosure route exist (to be informed by the planned coordinated-disclosure report).
- TEC-5 Tools never modify the records they check; reruns happen in isolated copies.

#### 5.5 UR-OPS — Operational (permissions, deployment, oversight) · Laws 5, 7
- OPS-1 Every product and gate names an owner and a decision authority.
- OPS-2 Writes to `main` happen only through owner-approved pull requests; this is technically enforced (branch protection), not only by convention.
- OPS-3 Every consequential action, including those taken by AI agents, is attributable to the actor that took it (human or agent) and is recorded in the repository's audit trail.
- OPS-4 Process deviations and errors (bad commits, procedure slips) are disclosed inside the repository, not only in off-repository notes.
- OPS-5 Implementation, deployment and external release require a recorded authorization by the owner; research, tests and capability do not grant it (Law 7).

### 6. Law-to-domain matrix
| Law | Epistemic | Scientific | Ethical | Technical | Operational |
|---|:-:|:-:|:-:|:-:|:-:|
| 1 Integrity Before Intelligence | ● | ○ | ○ | | ○ |
| 2 Evidence Before Assertion | ● | ○ | | | |
| 3 Verification Before Advancement | ○ | ● | | ○ | ○ |
| 4 Safety Before Capability | | | ● | ● | ○ |
| 5 Accountability Before Authority | | | ○ | | ● |
| 6 Consent Before Access | | | ● | ○ | ○ |
| 7 Authorization Before Implementation | | | | ○ | ● |

● primary domain · ○ contributes. Each domain keeps its own acceptance criteria (Part I).

---

## Part III — Relationship to existing governing documents

This standard **adds to** and **does not replace** `Research/README.md` or `Research/RESEARCH_PLAN_EXTENSION.md`. Neither file is modified on this branch. Where they are stricter, they apply.

| Existing rule | Where | Relationship to this standard |
|---|---|---|
| Motto "Integrity before intelligence" | README header | Becomes Law 1, extended from research to every system. |
| Responsibility ladder (Power → Magic Power) | README §2 | Is the scale Law 4 uses: the ladder level sets the minimum safeguards. Ultra Power's "explicit authorization" is Law 7; Magic Power's "never use extraordinary language to bypass evidence or ethics" is the absolute boundary. "No capability level waives responsibility" = Law 5 + absolute boundary. |
| Six claim classes | README §1 | Law 2 / EPI-2. The cycles use four labels (Established, Plausible, Philosophical/Spiritual, Hypothetical) with a mapping appendix (`Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md`); EPI-2 asks for an explicit crosswalk to Law 2's six distinctions. |
| Integration mandate (identity, links, provenance, change control, gates, integrity checks, privacy) | README §3 | Becomes the Knowledge-systems standard (identity, provenance, versioning, consistency) and EPI/SCI/ETH criteria. |
| Research lifecycle and three checks | README §4 | Law 3 / SCI-4. |
| Report requirements (owner, status, etc.) | README §5 | OPS-1 (owner) and EPI/SCI criteria. |
| Gates Pass / Fail / Indeterminate; gate record contents | README §3.8, §7 | Universal decision vocabulary and gate record (Part II §2–3). |
| "Do not authorize implementation … merely because research has advanced" | README §7 | Law 7 verbatim in spirit. |
| "Implementation is not authorized" | root README.md | Current OPS-5 state; unchanged. |
| Methodology, simulation requirement, QC checklist | RESEARCH_PLAN_EXTENSION.md §5, §6, §9 | SCI-1…SCI-5 and EPI criteria; "a successful software test demonstrates only what the test was designed to check" is Law 7's "successful testing never independently grants permission". |
| "No result or Greater-Good claim overrides dignity, rights, safety, or consent" | RESEARCH_PLAN_EXTENSION.md §4 | Laws 4 and 6; absolute boundary. |
| Five phases (Divergence … Ascendence), 625-cell matrix, numerical matrix hypothesis | README §9–§10; Extension §3 | Regulated content, not exempt: Law 2 keeps them Proposed/Hypothetical until defined and tested. |

### Precedence
1. Part I of this standard (owner's text) and the absolute boundary.
2. The stricter of this standard's Part II and the existing README / plan extension, for the matter at hand.
3. Cycle- and track-level FRAMEWORK files, within the limits above.

## Part IV — Adoption path (nothing here has happened yet)
1. Owner reviews this standard and the v1 audit (status Proposed).
2. Owner decides adoption (merge) and names reviewers.
3. Domain standards UR-EPI/SCI/ETH/TEC/OPS are written from the stubs.
4. Remediation items in the audit are completed and re-audited (audit v2).
5. Only after a re-audit with no FAIL in a domain, and independent review, may that domain be described as implemented.

## Change history
- **2026-10-24 — 0.1.0 (Proposed):** Owner's Universal Regulation Principle, seven laws, universality layers, five regulation domains and absolute boundary recorded verbatim; normative structure, domain-standard stubs and relationship to Research/README.md and RESEARCH_PLAN_EXTENSION.md drafted. First audit (v1) attached. Not adopted; not implemented.
