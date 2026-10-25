# ToG 1 Baseline — pre-execution specification

ID: GAIA-RES-TOG1-C0-SIM-001. Version 0.1.0. Written before execution in this response; not externally preregistered or committed to GitHub.

Question: Does an explicitly proposed conjunction of eleven clause-control states prevent a synthetic gate PASS when any required control is FAIL or INDETERMINATE?

Model: Eleven abstract control-evidence states, one per charter clause 4.1–4.11. Values PASS, FAIL, INDETERMINATE. All eleven are assumed applicable in this toy; real applicability, evidence validity, legal duties and human judgment are outside the model. Decision = FAIL if any FAIL; otherwise INDETERMINATE if any INDETERMINATE; otherwise PASS. This is a design proposal, not the adopted GAIA gate or a numerical measure of morality. Missing input becomes INDETERMINATE. Invalid tokens raise ValueError, not PASS. A recorded review result is input data, never an agent's authority to approve.

Inputs: all 3^11 = 177147 vectors; named negative/adversarial fixtures; one mixed FAIL/unknown fixture; missing and malformed vectors; five identity-check fixtures in which reviewer identity equality or blank identity must prevent a review control PASS. No personal data. Identity fixtures use synthetic names.

Algorithm: standard-library Python itertools.product, deterministic aggregation; independently expressed count-based oracle on every vector; compare aggregate outcomes and enumerate mismatches. Mutation controls intentionally use unsafe rules (unknown treated as PASS; majority vote) and must be rejected by fixed fixtures. The oracle and fixtures are written by the same author: not independent review.

Acceptance tests fixed before execution:
V1 exhaustive vector count 177147 and unique input encoding;
V2 zero disagreements with count-based oracle;
V3 exactly one all-PASS vector passes;
V4 no PASS for any FAIL or INDETERMINATE input;
V5 expected counts PASS=1, INDETERMINATE=2047, FAIL=175099;
V6 eleven singleton-unknown and eleven singleton-FAIL vectors block PASS;
V7 missing input returns INDETERMINATE and malformed tokens raise ValueError;
V8 repeated application to a fixed unknown vector never upgrades it;
V9 majority-vote and ignore-unknown mutants each fail at least one negative fixture;
V10 mixed FAIL/INDETERMINATE returns FAIL;
V11 synthetic self-review and blank reviewer are blocked; distinct names only satisfy the identity subcheck, not reviewer competence or independence;
V12 before/after SHA-256 of SPEC.md remains identical.

Execution budget: one baseline execution. No simulation rerun will be called a second baseline. Script is delivered for a later independent rerun; this response will not claim one occurred. Record UTC start/end, Python/platform, input/spec/script/output hashes, every test result and negative findings. Overall research gate remains INDETERMINATE regardless of test outcomes. FAILs remain in records. No test thresholds changed after execution.

Limitations and hypothesis: predicted behavior is foreseeable from the algorithm; this is exhaustive software/model consistency checking over an assumed finite model, not predictive science, empirical rights validation, ethics review, legal compliance certification, security testing or authorization. A high pass rate is not evidence of real-world safety. No weighted aggregate may waive a constitutional control in this proposal. Legal exceptions and policy conflicts require qualified human deliberation, not this toy.
