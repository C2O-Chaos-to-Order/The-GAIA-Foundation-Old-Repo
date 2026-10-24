"""Generate the Map & Matrix artefacts from the on-disk corpus.

Usage:  python -m gaia_tools.maps <Research dir> <out dir> --version-label "covers Cycles 0-1"
Writes (all deterministic; re-running on the same data gives byte-identical files):
  claim_map/claim_map.csv            every claim x cycle: label, sources, report, status, change vs previous cycle
  matrix/intersections_625.csv       the 625 Alchemy x Being x Phase x Lens cells with placement counts and flags
  matrix/being_x_lens_25.csv         the populated projection (Being x Lens) with label counts and flags
  matrix/claim_placement.csv         per-claim placement (Being from report; Lens from lens_rules.json;
                                     Alchemy and Phase 'Unassigned' because G01 leaves them undefined)
  matrix/report_placement.csv        per-report placement summary
  graph/link_graph.json, graph/link_graph.mmd   GAIA-centred link graph (typed, labelled E/P/PS/H)
  changes/changes.csv                cross-cycle change classification for claims and links
  simulations/simulations_index.json every executed run (schema: simulation.schema.json)
"""
import argparse, csv, glob, io, itertools, json, os, re, sys
from importlib import resources
from . import data as D

AXES = {"Alchemy": ["Body Alchemy", "Mind Alchemy", "Soul Alchemy", "Spirit Alchemy", "Consciousness Alchemy"],
        "Being": ["Body", "Mind", "Soul", "Spirit", "Consciousness"],
        "Phase": ["Divergence", "Insurgence", "Allegiance", "Convergence", "Ascendence"],
        "Lens": ["Truth", "Integrity", "Love", "Justice", "Wisdom"]}
BEING_OF_REPORT = {"R1": "Body", "R2": "Mind", "R3": "Soul", "R4": "Spirit", "R5": "Consciousness"}
UNDER_RESEARCHED_MIN = 3   # pre-declared: a Being x Lens projection with fewer claims than this is 'under-researched'
LABEL_RANK = {"Hypothetical": 0, "Philosophical/Spiritual": 0, "Plausible": 1, "Established": 2}


def lens_rules():
    with resources.files("gaia_tools").joinpath("lens_rules.json").open() as f:
        return json.load(f)


def lenses_for(text, rules):
    t = text.lower(); out = []
    for lens in AXES["Lens"]:
        if any(re.search(r"\b" + k, t) for k in rules["lenses"][lens]):
            out.append(lens)
    return out


def _csv(path, rows, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    buf = io.StringIO(); w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n"); w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, "") for k in fields})
    open(path, "w", encoding="utf-8", newline="").write(buf.getvalue())


def _json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8", newline="\n").write(json.dumps(obj, indent=1, ensure_ascii=False, sort_keys=False) + "\n")


def classify_claim_change(prev, cur, note):
    """Deterministic change classes, applied in this order."""
    if prev is None:
        return "new"
    if cur is None:
        return "dropped"
    pl, cl = prev["framework_label"], cur["framework_label"]
    if pl != cl:
        return "weakened (label downgraded)" if LABEL_RANK[cl] < LABEL_RANK[pl] else (
            "strengthened (label upgraded)" if LABEL_RANK[cl] > LABEL_RANK[pl] else "relabelled")
    n = (note or "").lower()
    if n.startswith("upgraded"):
        return "strengthened (full-text source added)"
    if "counter-evidence" in n:
        return "weakened (counter-evidence added; label unchanged)"
    if prev["conclusion_status"] != cur["conclusion_status"]:
        return f"status changed ({prev['conclusion_status']} -> {cur['conclusion_status']})"
    if prev["wording"] == cur["wording"] and prev["source_ids"] == cur["source_ids"]:
        return "unchanged"
    if n.startswith("carried forward"):
        return "carried forward (citation re-pointed to the earlier run; see note)"
    return "updated (label unchanged)"


def build(research_dir, out_dir, version_label):
    cyc = D.cycles(research_dir); rules = lens_rules()
    per = {cid: {r["claim_id"]: r for r in D.claims(cp)} for cid, cp in cyc}
    regs = {cid: {s["source_id"]: s for s in D.sources(cp)} for cid, cp in cyc}
    lk = {cid: {l["link_id"]: l for l in D.links(cp)} for cid, cp in cyc}
    ids = list(cyc)
    files = []

    # 1 claim map
    rows = []
    for i, (cid, cp) in enumerate(cyc):
        prev = per[ids[i - 1][0]] if i else {}
        for k, r in per[cid].items():
            note_col = f"c{cid[1:]}_change"
            pr = prev.get(k) if i else None
            rows.append(dict(cycle=cid, claim_id=k, report=r["report"], label=r["framework_label"],
                             label_code=D.LABELS[r["framework_label"]], conclusion_status=r["conclusion_status"],
                             claim_class=r["claim_class"], source_ids=r["source_ids"],
                             literature_sources=";".join(s for s in D.split_ids(r["source_ids"]) if not D.SIM_REF.match(s)),
                             simulation_checks=";".join(s for s in D.split_ids(r["source_ids"]) if D.SIM_REF.match(s)),
                             full_text_sources=";".join(s for s in D.split_ids(r["source_ids"]) if s in regs[cid] and regs[cid][s]["access_mode"].startswith("full")),
                             prev_label=pr["framework_label"] if pr else "", prev_status=pr["conclusion_status"] if pr else "",
                             change_vs_prev_cycle=("first cycle" if i == 0 else classify_claim_change(pr, r, r.get(note_col, ""))),
                             change_note=r.get(note_col, ""), wording=r["wording"]))
        if i:
            for k, pr in prev.items():
                if k not in per[cid]:
                    rows.append(dict(cycle=cid, claim_id=k, report=pr["report"], label="(dropped)", label_code="",
                                     prev_label=pr["framework_label"], prev_status=pr["conclusion_status"],
                                     change_vs_prev_cycle="dropped", wording=pr["wording"]))
    f = ["cycle", "claim_id", "report", "label", "label_code", "conclusion_status", "claim_class", "source_ids", "literature_sources",
         "simulation_checks", "full_text_sources", "prev_label", "prev_status", "change_vs_prev_cycle", "change_note", "wording"]
    _csv(os.path.join(out_dir, "claim_map", "claim_map.csv"), rows, f); claim_map = rows

    # 2 matrix (latest cycle)
    last, lcp = cyc[-1]
    place = []
    for k, r in per[last].items():
        being = BEING_OF_REPORT.get(r["report"], "")
        ls = lenses_for(r["wording"], rules)
        place.append(dict(claim_id=k, report=r["report"], label=r["framework_label"],
                          being=being or f"outside Being axis ({D.REPORTS[r['report']]})",
                          lenses=";".join(ls) if ls else "Unassigned",
                          alchemy="Unassigned (undefined: G01 9.3 / 12 Q3)", phase="Unassigned (undefined: G01 9.3 / 12 Q4)"))
    _csv(os.path.join(out_dir, "matrix", "claim_placement.csv"), place,
         ["claim_id", "report", "label", "being", "lenses", "alchemy", "phase"])
    bl = []
    for b, l in itertools.product(AXES["Being"], AXES["Lens"]):
        cs = [p for p in place if p["being"] == b and l in p["lenses"].split(";")]
        cnt = {c: sum(p["label"] == lab for p in cs) for lab, c in D.LABELS.items()}
        flag = "EMPTY" if not cs else ("UNDER-RESEARCHED (<%d claims)" % UNDER_RESEARCHED_MIN if len(cs) < UNDER_RESEARCHED_MIN
                                       else ("UNDER-RESEARCHED (no E/P claim)" if cnt["E"] + cnt["P"] == 0 else "populated"))
        bl.append(dict(being=b, lens=l, n_claims=len(cs), E=cnt["E"], P=cnt["P"], PS=cnt["PS"], H=cnt["H"], flag=flag,
                       claim_ids=";".join(p["claim_id"] for p in cs)))
    _csv(os.path.join(out_dir, "matrix", "being_x_lens_25.csv"), bl, ["being", "lens", "n_claims", "E", "P", "PS", "H", "flag", "claim_ids"])
    blx = {(r["being"], r["lens"]): r for r in bl}
    cells = []
    for (i, a), (j, b), (k, p), (m, l) in itertools.product(*(list(enumerate(AXES[x], 1)) for x in ("Alchemy", "Being", "Phase", "Lens"))):
        pr = blx[(b, l)]
        cells.append(dict(id=f"X-A{i}-B{j}-P{k}-L{m}", alchemy=a, being=b, phase=p, lens=l,
                          reports_on_being=next(r for r, bb in BEING_OF_REPORT.items() if bb == b),
                          claims_placed_exactly=0, claims_in_being_lens_projection=pr["n_claims"],
                          flag=("EMPTY (Being x Lens projection has no claim)" if pr["n_claims"] == 0 else
                                ("UNDER-RESEARCHED (Being x Lens projection: " + pr["flag"].split(" ", 1)[1].strip("()") + ")"
                                 if pr["flag"].startswith("UNDER") else "UNPLACED (projection populated; Alchemy/Phase undefined)")),
                          status="Proposed - category only (G01 9.4)"))
    _csv(os.path.join(out_dir, "matrix", "intersections_625.csv"), cells,
         ["id", "alchemy", "being", "phase", "lens", "reports_on_being", "claims_placed_exactly", "claims_in_being_lens_projection", "flag", "status"])
    rp = []
    for rid, name in D.REPORTS.items():
        cs = [p for p in place if p["report"] == rid]
        rp.append(dict(report=rid, name=name, being=BEING_OF_REPORT.get(rid, "outside Being axis"), n_claims=len(cs),
                       **{l: sum(l in p["lenses"].split(";") for p in cs) for l in AXES["Lens"]},
                       Unassigned_lens=sum(p["lenses"] == "Unassigned" for p in cs),
                       cells_in_625=125 if rid in BEING_OF_REPORT else 0))
    _csv(os.path.join(out_dir, "matrix", "report_placement.csv"), rp,
         ["report", "name", "being", "n_claims"] + AXES["Lens"] + ["Unassigned_lens", "cells_in_625"])

    # rejection screen of the latest cycle (Report-7 results 'rejection' list), if present
    pressure = {}
    for it in sorted(glob.glob(os.path.join(lcp, "Report-7-Unified", "simulation", "iter-*", "outputs", "results.json"))):
        res = json.load(open(it))
        for x in res.get("rejection", []) if isinstance(res, dict) else []:
            pressure[x["link_id"]] = x["screen"]
        for x in res.get("strict_rule", []) if isinstance(res, dict) else []:
            if x.get("old") != x.get("new"):
                pressure[x["link_id"]] = "strict Established-link rule: downgraded (procedural)"

    # 3 link graph
    nodes = [dict(id="GAIA", label="GAIA - the motherthread", kind="motherthread", framework_label="Philosophical/Spiritual",
                  note="Organizing principle (G03 FRAMEWORK.md); Philosophical/Spiritual, kept separate from science")]
    nodes += [dict(id=r, label=f"{r} {n}", kind="report") for r, n in D.REPORTS.items()]
    nodes += [dict(id="ALL", label="All reports (target of L24)", kind="collective")]
    edges = [dict(id=f"M{r[1]}", source="GAIA", target=r, type="motherthread", label_code="PS",
                  framework_label="Philosophical/Spiritual", basis="G03", statement="GAIA as motherthread organizes this report (framework, not a finding)")
             for r in D.REPORTS]
    for lid in sorted(lk[last]):
        l = lk[last][lid]
        hist = {cid: lk[cid][lid]["framework_label"] for cid, _ in cyc if lid in lk[cid]}
        edges.append(dict(id=lid, source=l["from"].split()[0], target=("ALL" if l["to"] == "All" else l["to"].split()[0]),
                          type=l["link_type"], label_code=D.LABELS[l["framework_label"]], framework_label=l["framework_label"],
                          label_history={c: D.LABELS[v] for c, v in hist.items()}, basis=l["basis"], statement=l["statement"],
                          status=l.get(f"c{last[1:]}_status", ""), rejection_screen=pressure.get(lid, "")))
    graph = dict(version_label=version_label, cycle=last, center="GAIA", nodes=nodes, edges=edges,
                 legend={"E": "Established", "P": "Plausible", "PS": "Philosophical/Spiritual", "H": "Hypothetical"})
    _json(os.path.join(out_dir, "graph", "link_graph.json"), graph)
    mm = ["flowchart LR"]
    mm.append('  GAIA(("GAIA<br/>motherthread [PS]"))')
    for r, n in D.REPORTS.items():
        mm.append(f'  {r}["{r} {n}"]')
    mm.append('  ALL[["All reports"]]')
    style = {"E": "stroke:#1b7f3b,stroke-width:3px", "P": "stroke:#1f5fbf,stroke-width:2px",
             "PS": "stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4", "H": "stroke:#c0392b,stroke-width:2px,stroke-dasharray:2 4"}
    ls = []
    for i, e in enumerate(edges):
        arrow = "-.->" if e["type"] == "motherthread" else "-->"
        txt = "motherthread [PS]" if e["type"] == "motherthread" else f"{e['id']} {e['type']} [{e['label_code']}]"
        mm.append(f'  {e["source"]} {arrow}|"{txt}"| {e["target"]}')
        ls.append(f"  linkStyle {i} {style[e['label_code']]}")
    mm += ls
    open(os.path.join(out_dir, "graph", "link_graph.mmd"), "w", newline="\n").write("\n".join(mm) + "\n")

    # 4 changes
    ch = [dict(kind="claim", id=r["claim_id"], cycle=r["cycle"], report=r["report"], prev_label=r["prev_label"],
               label=r["label"], change=r["change_vs_prev_cycle"], note=r.get("change_note", ""))
          for r in claim_map if r["cycle"] != ids[0][0]]
    for i in range(1, len(cyc)):
        a, b = ids[i - 1][0], ids[i][0]
        for lid in sorted(set(lk[a]) | set(lk[b])):
            pa, pb = lk[a].get(lid), lk[b].get(lid)
            if pa is None: c = "new"
            elif pb is None: c = "dropped"
            elif LABEL_RANK[pb["framework_label"]] < LABEL_RANK[pa["framework_label"]]: c = "weakened (label downgraded)"
            elif LABEL_RANK[pb["framework_label"]] > LABEL_RANK[pa["framework_label"]]: c = "strengthened (label upgraded)"
            elif any(pa[k] != pb.get(k) for k in pa if not re.match(r"c\d+_", k)): c = "updated (label unchanged)"
            else: c = "re-assessed (label unchanged)"
            ch.append(dict(kind="link", id=lid, cycle=b, report="R7", prev_label=pa["framework_label"] if pa else "",
                           label=pb["framework_label"] if pb else "(dropped)", change=c,
                           pressure=pressure.get(lid, "") if b == last else "",
                           note=(pb or {}).get(f"c{b[1:]}_status", "")))
    _csv(os.path.join(out_dir, "changes", "changes.csv"), ch, ["kind", "id", "cycle", "report", "prev_label", "label", "change", "pressure", "note"])

    # 5 simulations index
    idx = [s for cid, cp in cyc for s in D.simulations(cp, cid)]
    _json(os.path.join(out_dir, "simulations", "simulations_index.json"), idx)
    return dict(claim_rows=len(claim_map), placements=len(place), cells=len(cells), being_lens=bl, edges=len(edges),
                changes=ch, sims=len(idx), report_placement=rp)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("research_dir"); ap.add_argument("out_dir"); ap.add_argument("--version-label", required=True)
    a = ap.parse_args(argv)
    r = build(a.research_dir, a.out_dir, a.version_label)
    print(json.dumps({k: v for k, v in r.items() if isinstance(v, int)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
