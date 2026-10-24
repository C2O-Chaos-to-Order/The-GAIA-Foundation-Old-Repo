#!/usr/bin/env python3
"""Build GOVERNANCE/PRODUCT_REGISTER.csv and GOVERNANCE/LAW2_CROSSWALK_COUNTS.csv.

Research tooling only: reads the repository, writes two CSV files under GOVERNANCE/,
never modifies research records. Deterministic (sorted output, no timestamps).

Usage (from the repository root):  python3 GOVERNANCE/tools/build_registers.py

Rules applied (documented in GOVERNANCE/RISK_LEVELS.md and GOVERNANCE/LAW2_CROSSWALK.md):
- Overlay M (Magic Power discipline) applies when the product carries at least one
  claim labelled Philosophical/Spiritual or Hypothetical in the v8 claim map.
- Overlay W (human well-being topic) applies when the product's report text matches the
  well-being keyword pattern below at least once (a bounded scan, not a reading).
- Ladder levels are assigned per product kind (see KIND_LEVEL).
"""
import csv, glob, os, re, sys
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
R = os.path.join(ROOT, "Research")
CLAIM_MAP = "Research/Maps-and-Matrix/v8-cycles-0-4-mr-track-abcd/claim_map/claim_map.csv"
WB = re.compile(r"\b(health\w*|mortality|clinical\w*|patient\w*|psilocybin|psychedelic\w*|"
                r"well-?being|depress\w*|anxiety|suicid\w*|disease\w*|therap\w*)\b", re.I)
OWNER = "KyleAlexanderSteen (repository owner)"
AUTH = "KyleAlexanderSteen (repository owner); final authority for every gate (GOVERNANCE/GATE_AUTHORITY.md)"

# Law 2 crosswalk: (framework_label, claim_class) -> Law 2 category, rule note
def law2(label, cls):
    c = cls.lower()
    math = c in ("mathematical/computational", "computational", "simulation", "theoretical")
    if label == "Established":
        if math: return "Mathematical result", "Established + formal/computational class"
        if c in ("interpretive/philosophical", "interpretive", "philosophical"):
            return "Established finding (description of an interpretation)", "describes what a source argues; content not endorsed (FRAMEWORK appendix)"
        if c in ("spiritual/theological",):
            return "Established finding (description of a spiritual belief)", "describes what a tradition holds; content not endorsed"
        return "Established finding", "Established + empirical/historical/descriptive class"
    if label == "Plausible":
        if math: return "Mathematical result (provisional)", "formal result with stated limits or illustrative parameters"
        if c in ("interpretive/philosophical", "interpretive", "philosophical", "synthesis"):
            return "Interpretation", "evidence-informed interpretation, not established"
        return "Hypothesis (partly supported)", "evidence-based but incomplete or contested; Law 2 has no separate 'partly supported' class"
    if label == "Philosophical/Spiritual":
        if math: return "Mathematical result (about an interpretive coding)", "simulation over coded interpretive material; label kept for its subject"
        if c in ("spiritual/theological",): return "Spiritual belief", "spiritual/theological class"
        return "Interpretation or spiritual belief (not split in historical rows)", "class does not separate interpretation from spiritual belief; row-level review needed"
    if label == "Hypothetical":
        if c == "empirical": return "Hypothesis", "has an empirical test in principle"
        return "Speculation (proxy)", "non-empirical class used as proxy for 'no stated empirical test'; row-level review needed"
    return "UNMAPPED", "label not in the four-label scheme"

def gate_of(path):
    if not path or not os.path.exists(os.path.join(ROOT, path)): return ""
    txt = open(os.path.join(ROOT, path), encoding="utf-8").read()
    m = re.search(r"(?i)gate[^\n:]{0,40}:\s*\**\s*(PASS|FAIL|INDETERMINATE)\b", txt) or \
        re.search(r"(?im)^#+\s*Gate\s*\n+\s*\**(PASS|FAIL|INDETERMINATE)\b", txt)
    return m.group(1).upper() if m else "NOT FOUND"

def main():
    rows = list(csv.DictReader(open(os.path.join(ROOT, CLAIM_MAP), newline="", encoding="utf-8")))
    labels = Counter()
    for r in rows:
        key = r["cycle"], (r["report"].split()[-1] if r["cycle"].startswith("T") else r["report"].split()[0])
        if r["label"] in ("Philosophical/Spiritual", "Hypothetical"): labels[key] += 1
    def m_count(cycle, rep): return labels[(cycle, rep)]

    prods = []
    cyc_dirs = sorted(glob.glob(os.path.join(R, "Cycles", "Cycle-*")))
    for cd in cyc_dirs:
        cn = os.path.basename(cd); ck = "C" + cn.split("-")[1]
        gate = os.path.relpath(os.path.join(cd, "Verification", "VERIFICATION.md"), ROOT)
        for rd in sorted(glob.glob(os.path.join(cd, "Report-*"))):
            rn = os.path.basename(rd); rk = "R" + rn.split("-")[1]
            rep = os.path.join(rd, "REPORT.md")
            txt = open(rep, encoding="utf-8").read() if os.path.exists(rep) else ""
            prods.append(dict(product_id=f"GAIA-PRD-{ck}-{rk}", path=os.path.relpath(rd, ROOT), kind="report+simulations",
                              m=m_count(ck, rk), w=len(WB.findall(txt)), gate_record=gate))
    mr = os.path.join(R, "Master-Report-Unconditional-and-Conditional-Love")
    mtxt = open(os.path.join(mr, "MASTER_REPORT.md"), encoding="utf-8").read()
    prods.append(dict(product_id="GAIA-PRD-MR", path=os.path.relpath(mr, ROOT), kind="report+simulations",
                      m=sum(1 for r in rows if r["cycle"] == "MR" and r["label"] in ("Philosophical/Spiritual", "Hypothetical")),
                      w=len(WB.findall(mtxt)), gate_record=os.path.relpath(os.path.join(mr, "Verification", "VERIFICATION.md"), ROOT)))
    tr = os.path.join(R, "Tracks", "Soul-Spirit-Subconscious-Consciousness")
    topic_key = {"Consciousness": "CONS", "Soul": "SOUL", "Spirit": "SPIRIT", "Subconscious": "SUBC"}
    for cd in sorted(glob.glob(os.path.join(tr, "Cycle-*"))):
        tk = "T" + os.path.basename(cd).split("-")[1]
        gate = os.path.relpath(os.path.join(cd, "Verification", "VERIFICATION.md"), ROOT)
        for topic, key in topic_key.items():
            td = os.path.join(cd, topic)
            if not os.path.isdir(td): continue
            txt = open(os.path.join(td, "REPORT.md"), encoding="utf-8").read()
            prods.append(dict(product_id=f"GAIA-PRD-{tk}-{key}", path=os.path.relpath(td, ROOT), kind="report+simulations",
                              m=labels[(tk, key)], w=len(WB.findall(txt)), gate_record=gate))
    for md in sorted(glob.glob(os.path.join(R, "Maps-and-Matrix", "v*"))):
        prods.append(dict(product_id="GAIA-PRD-MAPS-" + os.path.basename(md).split("-")[0], path=os.path.relpath(md, ROOT),
                          kind="derived map", m=0, w=0, gate_record=""))
    prods.append(dict(product_id="GAIA-PRD-TOOLS", path="Research/tools", kind="research tooling", m=0, w=0, gate_record=""))
    prods.append(dict(product_id="GAIA-PRD-CI", path=".github/workflows/verify.yml", kind="verification automation", m=0, w=0, gate_record=""))
    prods.append(dict(product_id="GAIA-GOV-UR-001", path="GOVERNANCE/UNIVERSAL_REGULATION.md", kind="governance standard", m=0, w=0, gate_record=""))
    prods.append(dict(product_id="GAIA-GOV-UR-AUDIT", path="GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v*.md", kind="governance audit", m=0, w=0, gate_record=""))

    KIND_LEVEL = {"report+simulations": "Power", "derived map": "Power", "research tooling": "Meta Power",
                  "verification automation": "Meta Power", "governance standard": "Meta Power", "governance audit": "Meta Power"}
    EFFECTS = {
        "report+simulations": "Readers may treat labelled claims as guidance or mistake Plausible, Philosophical/Spiritual or Hypothetical claims for established findings; offline synthetic simulations only (no personal data, no network, no deployment).",
        "derived map": "Aggregates claims and links; a reader may read map density or link pressure as evidence strength.",
        "research tooling": "Decides which internal checks pass; a defect could let a faulty record pass or block a valid one. Reads the corpus; reruns in temporary copies; no service, no deployment.",
        "verification automation": "Runs the tooling and manifest checks on every pull request; a false green could be read as verification. contents:read only; no deployment, no secrets.",
        "governance standard": "Sets the rules other products are judged by; errors propagate to every audit and gate.",
        "governance audit": "Self-audit by the producing agent; a reader may take it as independent assurance.",
    }
    out = os.path.join(ROOT, "GOVERNANCE", "PRODUCT_REGISTER.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["product_id", "path", "kind", "owner", "decision_authority", "ladder_level", "overlays",
                    "ps_or_hyp_claims_v8", "wellbeing_keyword_hits", "foreseeable_effects", "required_safeguards",
                    "safeguard_status", "gate_record", "gate_decision"])
        for p in prods:
            lvl = KIND_LEVEL[p["kind"]]
            ov = [x for x, ok in (("M", p["m"] > 0), ("W", p["w"] > 0)) if ok]
            req = ["purpose, foreseeable effects and accountability recorded (Power)"]
            if lvl == "Meta Power": req.append("effects on governed products assessed; owner approval by merge; audited")
            if "M" in ov: req.append("Magic Power discipline: assumptions labelled, never used to bypass evidence or ethics")
            if "W" in ov: req.append("ethics review recorded before any gate PASS (ETH-5)")
            status = "met for current state: recorded here; no gate PASS claimed" if p["gate_record"] else "met for current state: recorded here"
            if "W" in ov: status += "; ethics review NOT done, so gate must stay INDETERMINATE"
            w.writerow([p["product_id"], p["path"], p["kind"], OWNER, AUTH, lvl, "+".join(ov) or "none",
                        p["m"] if p["kind"] == "report+simulations" else "", p["w"] if p["kind"] == "report+simulations" else "",
                        EFFECTS[p["kind"]], "; ".join(req), status, p["gate_record"], gate_of(p["gate_record"])])
    # crosswalk counts
    cnt = Counter((r["label"], r["claim_class"]) for r in rows)
    out2 = os.path.join(ROOT, "GOVERNANCE", "LAW2_CROSSWALK_COUNTS.csv")
    with open(out2, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["framework_label", "claim_class", "law2_category", "rule", "rows_in_v8_claim_map"])
        for (lab, cls), n in sorted(cnt.items()):
            cat, rule = law2(lab, cls)
            w.writerow([lab, cls, cat, rule, n])
    print(f"products: {len(prods)}; crosswalk pairs: {len(cnt)}; claim-map rows: {len(rows)}; unique claim IDs: {len({r['claim_id'] for r in rows})}")

if __name__ == "__main__":
    sys.exit(main())
