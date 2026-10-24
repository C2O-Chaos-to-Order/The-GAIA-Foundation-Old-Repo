"""Maps & Matrix over ALL work (gaia_tools 0.5.0): main cycles + Master Report + track cycles.

Usage:  python -m gaia_tools.maps_all <Research dir> <out dir> --version-label "covers C0-C4, MR, Track A"
First runs gaia_tools.maps.build (main cycles, unchanged behaviour), then extends every artefact:
  claim_map      + Master Report rows (cycle 'MR') + every track cycle's rows (cycle 'TA', 'TB', ...)
  matrix         placement = latest main cycle + Master Report + latest track cycle; Being of a track topic:
                 SOUL->Soul, SPIRIT->Spirit, CONS->Consciousness, SUBC->Mind (pre-declared); MR claims by report_feed
  graph          + nodes MR and the four topics; + motherthread edges GAIA->topic and GAIA->MR (PS);
                 + typed, labelled track links (TL-*) with label history across track cycles;
                 'structure_edges' (topic deepens report, report feeds MR) are organisational and carry no E/P/PS/H label
  changes        + track claim and link changes between consecutive track cycles
  simulations    + track runs"""
import argparse, csv, itertools, json, os, sys
from . import data as D, maps as M, tracks as T

TOPIC_BEING = {"SOUL": "Soul", "SPIRIT": "Spirit", "CONS": "Consciousness", "SUBC": "Mind"}
MR_DIR = "Master-Report-Unconditional-and-Conditional-Love"


def _read(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build(research_dir, out_dir, label):
    base = M.build(research_dir, out_dir, label); rules = M.lens_rules()
    mr_path = os.path.join(research_dir, MR_DIR, "claims", "claims.csv"); mr = _read(mr_path) if os.path.exists(mr_path) else []
    tcs = T.track_cycles(research_dir); tcl = {tid: {r["claim_id"]: r for r in T.claims(cp)} for tid, cp, _ in tcs}
    tll = {tid: {l["link_id"]: l for l in T.links(cp)} for tid, cp, _ in tcs}
    # 1 claim map
    cm_p = os.path.join(out_dir, "claim_map", "claim_map.csv"); cm = _read(cm_p); f = list(cm[0].keys())
    for r in mr:
        cm.append(dict(cycle="MR", claim_id=r["claim_id"], report=f"MR (feeds {r['report_feed']})", label=r["framework_label"], label_code=D.LABELS[r["framework_label"]],
                       conclusion_status=r["conclusion_status"], claim_class=r["claim_class"], source_ids=r["source_ids"], change_vs_prev_cycle="Master Report v1",
                       change_note=r.get("origin", ""), wording=r["wording"]))
    prev = None
    for tid, cp, _ in tcs:
        for k, r in tcl[tid].items():
            pr = tcl[prev].get(k) if prev else None
            ch = "new (first track cycle)" if prev is None else ("new" if pr is None else M.classify_claim_change(pr, r, r["change_vs_prev_track_cycle"]))
            cm.append(dict(cycle=tid, claim_id=k, report=f"Track {r['topic']}", label=r["framework_label"], label_code=D.LABELS[r["framework_label"]],
                           conclusion_status=r["conclusion_status"], claim_class=r["claim_class"], source_ids=r["source_ids"],
                           simulation_checks=";".join(s for s in D.split_ids(r["source_ids"]) if T.TRACK_SIM_REF.match(s)),
                           literature_sources=";".join(s for s in D.split_ids(r["source_ids"]) if not T.TRACK_SIM_REF.match(s)),
                           prev_label=pr["framework_label"] if pr else "", prev_status=pr["conclusion_status"] if pr else "",
                           change_vs_prev_cycle=ch, change_note=r["change_vs_prev_track_cycle"], wording=r["wording"]))
        if prev:
            for k, pr in tcl[prev].items():
                if k not in tcl[tid]:
                    cm.append(dict(cycle=tid, claim_id=k, report=f"Track {pr['topic']}", label="(dropped)", prev_label=pr["framework_label"], change_vs_prev_cycle="dropped", wording=pr["wording"]))
        prev = tid
    M._csv(cm_p, cm, f)
    # 2 matrix: latest main cycle + MR + latest track cycle
    pl_p = os.path.join(out_dir, "matrix", "claim_placement.csv"); place = _read(pl_p)
    for r in place: r["source_set"] = "main cycle (latest)"
    for r in mr:
        ls = M.lenses_for(r["wording"], rules); b = M.BEING_OF_REPORT.get(r["report_feed"], "")
        place.append(dict(claim_id=r["claim_id"], report="MR", label=r["framework_label"], being=b or f"outside Being axis (MR feeds {r['report_feed']})",
                          lenses=";".join(ls) or "Unassigned", alchemy=place[0]["alchemy"], phase=place[0]["phase"], source_set="Master Report"))
    if tcs:
        lt = tcs[-1][0]
        for k, r in tcl[lt].items():
            ls = M.lenses_for(r["wording"], rules)
            place.append(dict(claim_id=k, report=f"Track {r['topic']}", label=r["framework_label"], being=TOPIC_BEING[r["topic"]], lenses=";".join(ls) or "Unassigned",
                              alchemy=place[0]["alchemy"], phase=place[0]["phase"], source_set=f"track cycle {lt}"))
    M._csv(pl_p, place, ["claim_id", "report", "label", "being", "lenses", "alchemy", "phase", "source_set"])
    bl = []
    for b, l in itertools.product(M.AXES["Being"], M.AXES["Lens"]):
        cs = [p for p in place if p["being"] == b and l in p["lenses"].split(";")]
        cnt = {c: sum(p["label"] == lab for p in cs) for lab, c in D.LABELS.items()}
        flag = "EMPTY" if not cs else ("UNDER-RESEARCHED (<%d claims)" % M.UNDER_RESEARCHED_MIN if len(cs) < M.UNDER_RESEARCHED_MIN
                                       else ("UNDER-RESEARCHED (no E/P claim)" if cnt["E"] + cnt["P"] == 0 else "populated"))
        bl.append(dict(being=b, lens=l, n_claims=len(cs), E=cnt["E"], P=cnt["P"], PS=cnt["PS"], H=cnt["H"],
                       n_main=sum(p["source_set"].startswith("main") for p in cs), n_mr=sum(p["source_set"] == "Master Report" for p in cs),
                       n_track=sum(p["source_set"].startswith("track") for p in cs), flag=flag, claim_ids=";".join(p["claim_id"] for p in cs)))
    M._csv(os.path.join(out_dir, "matrix", "being_x_lens_25.csv"), bl, ["being", "lens", "n_claims", "E", "P", "PS", "H", "n_main", "n_mr", "n_track", "flag", "claim_ids"])
    blx = {(r["being"], r["lens"]): r for r in bl}; cells = _read(os.path.join(out_dir, "matrix", "intersections_625.csv"))
    for c in cells:
        pr = blx[(c["being"], c["lens"])]; c["claims_in_being_lens_projection"] = pr["n_claims"]
        c["track_claims_in_projection"] = pr["n_track"]; c["mr_claims_in_projection"] = pr["n_mr"]
        c["flag"] = ("EMPTY (Being x Lens projection has no claim)" if pr["n_claims"] == 0 else
                     ("UNDER-RESEARCHED (Being x Lens projection: " + pr["flag"].split(" ", 1)[1].strip("()") + ")" if pr["flag"].startswith("UNDER")
                      else "UNPLACED (projection populated; Alchemy/Phase undefined)"))
        c["topics_on_being"] = ";".join(t for t, b in TOPIC_BEING.items() if b == c["being"])
    M._csv(os.path.join(out_dir, "matrix", "intersections_625.csv"), cells, list(cells[0].keys()))
    rp = _read(os.path.join(out_dir, "matrix", "report_placement.csv"))
    for name in ["MR"] + [f"Track {t}" for t in T.TOPICS]:
        cs = [p for p in place if p["report"] == name]
        rp.append(dict(report=name, name=(T.TOPICS.get(name.split()[-1], "Master Report")), being=TOPIC_BEING.get(name.split()[-1], "by report_feed"), n_claims=len(cs),
                       **{l: sum(l in p["lenses"].split(";") for p in cs) for l in M.AXES["Lens"]}, Unassigned_lens=sum(p["lenses"] == "Unassigned" for p in cs),
                       cells_in_625=125 if name.split()[-1] in TOPIC_BEING else "by report_feed"))
    M._csv(os.path.join(out_dir, "matrix", "report_placement.csv"), rp, list(rp[0].keys()))
    # 3 graph
    gp = os.path.join(out_dir, "graph", "link_graph.json"); g = json.load(open(gp)); g["version_label"] = label
    g["nodes"].append(dict(id="MR", label="Master Report: Unconditional and Conditional Love", kind="master report"))
    g["nodes"] += [dict(id=t, label=f"Track topic: {n}", kind="track topic", being=TOPIC_BEING[t]) for t, n in T.TOPICS.items()]
    g["edges"] += [dict(id=f"M-{t}", source="GAIA", target=t, type="motherthread", label_code="PS", framework_label="Philosophical/Spiritual", basis="G03; track FRAMEWORK.md",
                        statement="GAIA as motherthread organizes this topic (framework, not a finding)") for t in list(T.TOPICS) + ["MR"]]
    if tcs:
        lt = tcs[-1][0]
        for lid, l in sorted(tll[lt].items()):
            hist = {tid: D.LABELS[tll[tid][lid]["framework_label"]] for tid, _, _ in tcs if lid in tll[tid]}
            g["edges"].append(dict(id=lid, source=l["from"], target=l["to"], type=l["link_type"], label_code=D.LABELS[l["framework_label"]], framework_label=l["framework_label"],
                                   label_history=hist, basis=l["basis"], statement=l["statement"], status=l["status"], origin=f"track cycle {lt}"))
    feeds = sorted({r["report_feed"] for r in mr if r["report_feed"] in D.REPORTS})
    g["structure_edges"] = ([dict(source=t, target=r, type="deepens") for t, r in (("SOUL", "R3"), ("SPIRIT", "R4"), ("SUBC", "R2"), ("SUBC", "R5"), ("CONS", "R5"))] +
                            [dict(source=r, target="MR", type="feeds") for r in feeds])
    g["structure_edges_note"] = "Organisational relations (which report a topic deepens; which reports feed the Master Report). Not evidential claims, so no E/P/PS/H label."
    M._json(gp, g)
    mm = ["flowchart LR", '  GAIA(("GAIA<br/>motherthread [PS]"))'] + [f'  {r}["{r} {n}"]' for r, n in D.REPORTS.items()] + ['  ALL[["All reports"]]', '  MR{{"Master Report<br/>Love"}}'] + \
         [f'  {t}(["{n} (track)"])' for t, n in T.TOPICS.items()]
    style = {"E": "stroke:#1b7f3b,stroke-width:3px", "P": "stroke:#1f5fbf,stroke-width:2px", "PS": "stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4", "H": "stroke:#c0392b,stroke-width:2px,stroke-dasharray:2 4"}
    ls = []
    for i, e in enumerate(g["edges"]):
        arrow = "-.->" if e["type"] == "motherthread" else "-->"
        txt = "motherthread [PS]" if e["type"] == "motherthread" else f"{e['id']} {e['type']} [{e['label_code']}]"
        mm.append(f'  {e["source"]} {arrow}|"{txt}"| {e["target"]}'); ls.append(f"  linkStyle {i} {style[e['label_code']]}")
    n = len(g["edges"])
    for j, e in enumerate(g["structure_edges"]):
        mm.append(f'  {e["source"]} ---|"{e["type"]}"| {e["target"]}'); ls.append(f"  linkStyle {n + j} stroke:#999,stroke-width:1px")
    open(os.path.join(out_dir, "graph", "link_graph.mmd"), "w", newline="\n").write("\n".join(mm + ls) + "\n")
    # 4 changes
    chp = os.path.join(out_dir, "changes", "changes.csv"); ch = _read(chp)
    ch += [dict(kind="claim", id=r["claim_id"], cycle=r["cycle"], report=r["report"], prev_label=r.get("prev_label", ""), label=r["label"], change=r["change_vs_prev_cycle"], note=r.get("change_note", ""))
           for r in cm if r["cycle"].startswith("T")]
    for i, (tid, cp, _) in enumerate(tcs):
        pv = tll[tcs[i - 1][0]] if i else {}
        for lid in sorted(set(pv) | set(tll[tid])):
            a, b = pv.get(lid), tll[tid].get(lid)
            c = "new" if a is None else ("dropped" if b is None else ("weakened (label downgraded)" if M.LABEL_RANK[b["framework_label"]] < M.LABEL_RANK[a["framework_label"]] else
                 ("strengthened (label upgraded)" if M.LABEL_RANK[b["framework_label"]] > M.LABEL_RANK[a["framework_label"]] else
                  ("updated (label unchanged)" if (a["statement"], a["basis"]) != (b["statement"], b["basis"]) else "re-assessed (label unchanged)"))))
            ch.append(dict(kind="link", id=lid, cycle=tid, report="Track", prev_label=a["framework_label"] if a else "", label=b["framework_label"] if b else "(dropped)", change=c, note=(b or {}).get("status", "")))
    M._csv(chp, ch, ["kind", "id", "cycle", "report", "prev_label", "label", "change", "pressure", "note"])
    # 5 simulations
    sp = os.path.join(out_dir, "simulations", "simulations_index.json"); idx = json.load(open(sp))
    for tid, cp, track in tcs:
        for s in T.runs(cp, tid):
            s["track"] = track; idx.append(s)
    M._json(sp, idx)
    return dict(claim_rows=len(cm), placements=len(place), being_lens=bl, edges=len(g["edges"]), track_cycles=[t for t, _, _ in tcs], sims=len(idx), changes=ch)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0]); ap.add_argument("research_dir"); ap.add_argument("out_dir"); ap.add_argument("--version-label", required=True)
    a = ap.parse_args(argv); r = build(a.research_dir, a.out_dir, a.version_label)
    print(json.dumps({k: v for k, v in r.items() if isinstance(v, (int, list)) and k not in ("being_lens", "changes")})); return 0


if __name__ == "__main__":
    sys.exit(main())
