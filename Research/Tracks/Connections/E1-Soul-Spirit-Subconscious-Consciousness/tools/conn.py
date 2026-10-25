#!/usr/bin/env python3
"""The Connection: Soul, Spirit, Subconscious and Consciousness (Work Queue §E): deterministic tooling.

Reads only existing records (SSSC track Cycle-D-x12 ledgers, link and source registers; the six phases'
Cycle-D-x12 ledgers, link and source registers; Research/README.md; Research/WORK_QUEUE.md) and this
report's judgment files. It never edits an input and never creates a source: every basis ID and source
ID must resolve to an existing record.
Commands: run --cycle DIR --iter N | verify --cycle DIR | render --cycle DIR --iter N | maps --cycle DIR --iter N --out DIR --label TEXT
"""
import argparse, csv, hashlib, itertools, json, os, re, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "..", "..", "Program-Coordination", "PC-4-Research-to-Domain-Map", "tools"))
import pc4  # noqa: E402  (boundary scan helper)

LABELS = ["Established", "Plausible", "Philosophical/Spiritual", "Hypothetical"]
RANK = {"Established": 3, "Plausible": 2, "Hypothetical": 1}
TOPICS = ["SOUL", "SPIRIT", "SUBC", "CONS"]
TOPIC_DIR = {"SOUL": "Soul", "SPIRIT": "Spirit", "SUBC": "Subconscious", "CONS": "Consciousness"}
BEING = {"SOUL": "Soul", "SPIRIT": "Spirit", "SUBC": "Mind", "CONS": "Consciousness"}
LINK_TYPES = {"interaction", "dependence", "contrast", "feedback", "conflict", "common cause",
              "absence of a demonstrated connection", "shared method", "shared factor"}
KINDS = {"shared", "difference", "unity", "census", "owner", "framing", "phase"}
PHASES = ["Divergence", "Insurgence", "Allegiance", "Convergence", "Ascendence", "Transcendence"]
PAIRS = list(itertools.combinations(TOPICS, 2))

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def csvrows(p):
    return list(csv.DictReader(open(p, encoding="utf-8")))

def wcsv(p, header, rows):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(header); w.writerows(rows)

def split(s):
    return [t.strip() for t in (s or "").split(";") if t.strip()]

def pair_key(a, b):
    return "-".join(sorted((a, b), key=TOPICS.index))

# ---------------- loading existing records ----------------
def load_records(repo, cfg):
    R = os.path.join(repo, "Research")
    sssc = os.path.join(R, cfg["sssc_cycle"])
    claims = {}
    for t, d in TOPIC_DIR.items():
        for r in csvrows(os.path.join(sssc, d, "claims", "claims.csv")):
            r["_topic"] = t; claims[r["claim_id"]] = r
    links = {r["link_id"]: r for r in csvrows(os.path.join(sssc, "Links", "link_register.csv"))}
    sources = {r["source_id"]: r for r in csvrows(os.path.join(sssc, "Provenance", "SOURCE_REGISTER.csv"))}
    pclaims, plinks, psources = {}, {}, {}
    for ph in PHASES:
        base = os.path.join(R, "Tracks", "Phases", ph, cfg["phase_cycle"])
        for f in sorted(os.listdir(base)):
            cf = os.path.join(base, f, "claims", "claims.csv")
            if os.path.exists(cf):
                for r in csvrows(cf):
                    r["_phase"] = ph; pclaims[r["claim_id"]] = r
        for r in csvrows(os.path.join(base, "Links", "link_register.csv")):
            plinks[r["link_id"]] = r
        for r in csvrows(os.path.join(base, "Provenance", "SOURCE_REGISTER.csv")):
            psources.setdefault(r["source_id"], r)
    return dict(claims=claims, links=links, sources=sources, pclaims=pclaims, plinks=plinks, psources=psources,
                readme=open(os.path.join(R, "README.md"), encoding="utf-8").read(),
                wq=open(os.path.join(R, "WORK_QUEUE.md"), encoding="utf-8").read())

def dup_groups(sources):
    key = {}
    for sid, r in sorted(sources.items()):
        c = r.get("citation", "")
        m = re.search(r"doi:\s*(\S+)", c, re.I) or re.search(r"PMID\s*(\d+)", c)
        if m:
            key.setdefault(m.group(1).lower().rstrip(".,"), []).append(sid)
    return sorted(v for v in key.values() if len(v) > 1)

def canon_map(groups):
    return {s: g[0] for g in groups for s in g}

# ---------------- run ----------------
def load_cfg(cycle_dir):
    return json.load(open(os.path.join(cycle_dir, "config.json")))

def run(cycle_dir, it, outdir=None):
    cfg = load_cfg(cycle_dir)
    icfg = cfg["iterations"][str(it)]
    rule = icfg["rule"]
    repo = os.path.normpath(os.path.join(os.path.abspath(cycle_dir), cfg["repo_root"]))
    P = lambda p: os.path.normpath(os.path.join(os.path.abspath(cycle_dir), p))
    out = outdir or os.path.join(cycle_dir, f"iter-{it}")
    data = os.path.join(out, "data"); os.makedirs(data, exist_ok=True)
    D = load_records(repo, cfg)
    J = {k: csvrows(P(v)) for k, v in sorted(cfg["judgments"].items())}
    fac, cl, lk = J["factors"], J["claims"], J["links"]
    m, problems = {}, []
    # 0 inputs read in full exist
    m["missing_inputs"] = sorted(p for p in cfg["read_in_full"] if not os.path.exists(os.path.join(repo, p)))
    # label lookup across all resolvable IDs
    lab = {}
    for k, r in D["claims"].items(): lab[k] = r["framework_label"]
    for k, r in D["links"].items(): lab[k] = r["framework_label"]
    for k, r in D["pclaims"].items(): lab[k] = r["framework_label"]
    for k, r in D["plinks"].items(): lab[k] = r["framework_label"]
    for r in cl: lab[r["claim_id"]] = r["framework_label"]
    fids = {r["factor_id"] for r in fac}
    allsrc = set(D["sources"]) | set(D["psources"])
    def cited_by(bid):
        if bid in D["claims"]: return set(split(D["claims"][bid]["source_ids"]))
        if bid in D["pclaims"]: return set(split(D["pclaims"][bid]["source_ids"]))
        if bid in D["links"]: return set(split(D["links"][bid]["basis"]))
        if bid in D["plinks"]: return set(split(D["plinks"][bid]["basis"]))
        cr = next((r for r in cl if r["claim_id"] == bid), None)
        if cr: return set(split(cr["source_ids"])) | set().union(*[cited_by(b) for b in split(cr["basis"]) if b != bid] or [set()])
        if bid in allsrc: return {bid}
        return set()
    # 1 factor rows
    fac_rows = []
    for r in fac:
        if r["topic"] not in TOPICS: problems.append(f"factor {r['factor_id']} bad topic {r['topic']}")
        if r["kind"] not in {"method", "substantive", "tradition", "ethics"}: problems.append(f"factor {r['factor_id']} bad kind")
        labs = []
        for b in split(r["basis_claims"]):
            if b not in D["claims"]: problems.append(f"factor {r['factor_id']}/{r['topic']} basis {b} not in SSSC ledger"); continue
            if D["claims"][b]["_topic"] != r["topic"]: problems.append(f"factor {r['factor_id']}/{r['topic']} basis {b} from another topic")
            labs.append(D["claims"][b]["framework_label"])
        ep = any(l in ("Established", "Plausible") for l in labs)
        eo = any(l == "Established" for l in labs)
        counts = {"as_judged": True, "strict": ep, "established_only": eo}[rule]
        fac_rows.append([r["factor_id"], r["factor"], r["kind"], r["topic"], ";".join(labs), ep, counts])
    wcsv(os.path.join(data, "factor_topic.csv"), ["factor_id", "factor", "kind", "topic", "basis_labels", "has_E_or_P_basis", "counted"], fac_rows)
    inc = {}
    for f_, _, kind, t, _, _, c in fac_rows:
        if c: inc.setdefault(f_, set()).add(t)
    fkind = {r["factor_id"]: r["kind"] for r in fac}
    m["factors_total"] = len(fids)
    m["factors_by_ntopics"] = {str(n): sorted(f for f, s in inc.items() if len(s) == n) for n in (1, 2, 3, 4)}
    m["unity_factors"] = sorted(f for f, s in inc.items() if len(s) == 4)
    m["unity_factors_substantive"] = sorted(f for f in m["unity_factors"] if fkind[f] in ("substantive", "tradition"))
    pair_rows, m["pair_shared_factors"] = [], {}
    for a, b in PAIRS:
        A = {f for f, s in inc.items() if a in s}; B = {f for f, s in inc.items() if b in s}
        j = round(len(A & B) / len(A | B), 3) if A | B else 0.0
        m["pair_shared_factors"][pair_key(a, b)] = sorted(A & B)
        pair_rows.append([pair_key(a, b), len(A & B), len(A - B), len(B - A), j, ";".join(sorted(A & B))])
    # 2 objective censuses on existing records
    groups = dup_groups(D["sources"]); canon = canon_map(groups)
    m["register_duplicates"] = groups; m["register_duplicate_groups"] = len(groups)
    tl = [r for r in D["links"].values() if r["from"] in TOPICS and r["to"] in TOPICS]
    m["topic_topic_links"] = sorted(r["link_id"] for r in tl); m["topic_topic_links_in_track"] = len(tl)
    tsrc = {t: set() for t in TOPICS}
    for r in D["claims"].values():
        for s in split(r["source_ids"]):
            if re.match(r"^[KSUGW]\d+$", s): tsrc[r["_topic"]].add(canon.get(s, s) if icfg.get("merge_duplicates") else s)
    xc = {pair_key(a, b): 0 for a, b in PAIRS}; xc_list = []
    rx = re.compile(r"\bT[A-D]-(SOUL|SPIRIT|SUBC|CONS)-\d+\b")
    for r in D["claims"].values():
        for fld in ("deepens", "cross_links", "source_ids", "wording"):
            for mm in rx.finditer(r[fld] or ""):
                if mm.group(1) != r["_topic"]:
                    xc[pair_key(r["_topic"], mm.group(1))] += 1; xc_list.append([r["claim_id"], fld, mm.group(0)])
    wcsv(os.path.join(data, "cross_citations.csv"), ["claim_id", "field", "cites"], sorted(xc_list))
    m["pair_cross_citations"] = xc
    m["pairs_without_cross_citation"] = sorted(k for k, v in xc.items() if v == 0)
    m["pair_shared_sources"] = {pair_key(a, b): sorted(tsrc[a] & tsrc[b]) for a, b in PAIRS}
    m["pairs_without_shared_source"] = sorted(k for k, v in m["pair_shared_sources"].items() if not v)
    fr = set(cfg.get("framing_sources", []))
    m["pairs_without_shared_evidence_source"] = sorted(k for k, v in m["pair_shared_sources"].items() if not set(v) - fr)
    m["topic_sources"] = {t: len(tsrc[t]) for t in TOPICS}
    for row in pair_rows:
        row += [len(m["pair_shared_sources"][row[0]]), xc[row[0]]]
    m["phase_being_claims"] = len([r for r in D["pclaims"].values() if r.get("being")])
    m["phase_being_claim_ids"] = sorted(k for k, r in D["pclaims"].items() if r.get("being"))
    # 3 judged claims and links: resolution, sources, label rule, owner rule, census
    known = set(D["claims"]) | set(D["links"]) | set(D["pclaims"]) | set(D["plinks"]) | {r["claim_id"] for r in cl} | fids | allsrc
    dangling, unres, notin, labv, ownv, cens = [], [], [], [], [], []
    def check_item(iid, label, basis, srcs, kind):
        for b in basis:
            if b not in known: dangling.append(f"{iid}:{b}")
        for s in srcs:
            if s not in allsrc: unres.append(f"{iid}:{s}")
            elif not any(s in cited_by(b) for b in basis): notin.append(f"{iid}:{s}")
        if label not in LABELS: problems.append(f"{iid} bad label {label}")
        if kind in ("census", "owner"): return
        if label in RANK:
            rk = [RANK[lab[b]] for b in basis if b in lab and lab[b] in RANK]
            if not rk and label != "Hypothetical": labv.append(f"{iid}: no ranked basis for {label}")
            elif rk and RANK[label] > min(rk): labv.append(f"{iid}: {label} above weakest basis")
    for r in cl:
        ts = split(r["topics"])
        if r["kind"] not in KINDS: problems.append(f"{r['claim_id']} bad kind")
        if not ts or any(t not in TOPICS for t in ts): problems.append(f"{r['claim_id']} bad topics")
        if not r["wording"].strip() or not r["limits"].strip(): problems.append(f"{r['claim_id']} missing wording or limits")
        check_item(r["claim_id"], r["framework_label"], split(r["basis"]), split(r["source_ids"]), r["kind"])
        if r["kind"] == "owner":
            if r["framework_label"] not in ("Hypothetical", "Philosophical/Spiritual"): ownv.append(f"{r['claim_id']} label")
            if not r["wording"].startswith("Owner's"): ownv.append(f"{r['claim_id']} not marked as the owner's")
            ph = [p for p in r["owner_phrase"].split("|") if p]
            if not ph or any(p not in D["wq"] for p in ph): ownv.append(f"{r['claim_id']} owner phrase not in WORK_QUEUE.md")
        elif r["owner_phrase"]: ownv.append(f"{r['claim_id']} owner phrase on a non-owner claim")
        if r["kind"] == "census":
            if r["framework_label"] != "Established": problems.append(f"{r['claim_id']} census must be Established")
            v = m.get(r["metric"]); v = len(v) if isinstance(v, (list, dict)) else v
            if str(v) != r["value"]: cens.append(f"{r['claim_id']}: {r['metric']}={v} vs stated {r['value']}")
    for r in lk:
        if r["from"] not in TOPICS or r["to"] not in TOPICS or r["from"] == r["to"]: problems.append(f"{r['link_id']} bad endpoints")
        if r["link_type"] not in LINK_TYPES: problems.append(f"{r['link_id']} bad link type")
        check_item(r["link_id"], r["framework_label"], split(r["basis"]), [], "link")
    m["dangling_basis"] = sorted(dangling); m["unresolved_sources"] = sorted(unres)
    m["sources_not_in_basis"] = sorted(notin); m["label_rule_violations"] = sorted(labv)
    m["owner_rule_violations"] = sorted(ownv); m["census_claim_mismatches"] = sorted(cens)
    m["problems"] = sorted(problems)
    lpairs = {pair_key(r["from"], r["to"]) for r in lk}
    m["pairs_without_connection_link"] = sorted(pair_key(a, b) for a, b in PAIRS if pair_key(a, b) not in lpairs)
    m["claims_by_label"] = {l: sum(1 for r in cl if r["framework_label"] == l) for l in LABELS}
    m["claims_by_kind"] = {k: sum(1 for r in cl if r["kind"] == k) for k in sorted(KINDS)}
    m["links_by_label"] = {l: sum(1 for r in lk if r["framework_label"] == l) for l in LABELS}
    m["links_by_pair"] = {pair_key(a, b): sorted(r["link_id"] for r in lk if pair_key(r["from"], r["to"]) == pair_key(a, b)) for a, b in PAIRS}
    for row in pair_rows:
        row.append(len(m["links_by_pair"][row[0]]))
    wcsv(os.path.join(data, "pairs.csv"), ["pair", "shared_factors", "only_first", "only_second", "jaccard", "shared_factor_ids",
                                           "shared_sources", "cross_citations", "connection_links"], pair_rows)
    # 4 boundary scan against the Totality Suite (this report's folder, plus this run's outputs)
    W = cfg["boundary_window"]; here = os.path.abspath(cycle_dir)
    bs = pc4.boundary_scan(cfg["suite_path"], ROOT, W, exclude=(os.path.relpath(here, ROOT) + os.sep,))
    bs += [f"iter-{it}/data/{h}" for h in pc4.boundary_scan(cfg["suite_path"], data, W)]
    m["boundary_suite"] = sorted(bs); m["boundary_overlaps"] = len(bs)
    checks = []
    for c in cfg["checks"]:
        if "iters" in c and it not in c["iters"]: continue
        v = m[c["metric"]]; v = len(v) if isinstance(v, (list, dict)) else v
        res = {"eq": v == c["threshold"], "ge": v >= c["threshold"], "le": v <= c["threshold"]}[c["op"]]
        checks.append({"id": c["id"], "hypothesis": c["hypothesis"], "metric": c["metric"], "value": v,
                       "op": c["op"], "threshold": c["threshold"], "result": "PASS" if res else "FAIL"})
    inputs = {k: sha(P(v)) for k, v in sorted(cfg["judgments"].items())}
    inputs["read_in_full"] = {p: sha(os.path.join(repo, p)) for p in cfg["read_in_full"] if os.path.exists(os.path.join(repo, p))}
    outs = {fn: sha(os.path.join(data, fn)) for fn in sorted(os.listdir(data))}
    rec = {"report": "The Connection: Soul, Spirit, Subconscious and Consciousness", "cycle": cfg["cycle"], "iteration": it,
           "variant": icfg, "inputs": inputs, "outputs": outs, "metrics": m, "checks": checks}
    json.dump(rec, open(os.path.join(out, "EXECUTION_RECORD.json"), "w"), indent=1, ensure_ascii=False, sort_keys=True)
    return rec

def verify(cycle_dir):
    cfg = load_cfg(cycle_dir); res = []
    for it in sorted(cfg["iterations"], key=int):
        tmp = tempfile.mkdtemp()
        try:
            rec = run(cycle_dir, int(it), outdir=tmp)
            orig = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json")))
            res.append((int(it), json.loads(json.dumps(rec, ensure_ascii=False, sort_keys=True)) == orig))
        finally:
            shutil.rmtree(tmp)
    return res

def render(cycle_dir, it):
    rec = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json"))); m = rec["metrics"]
    L = [f"_Generated by `tools/conn.py render` from iter-{it} (rule `{rec['variant']['rule']}`)._\n",
         "### Pre-registered checks\n", "| ID | Hypothesis | Value | Test | Result |", "|---|---|---|---|---|"]
    L += [f"| {c['id']} | {c['hypothesis']} | {c['value']} | {c['op']} {c['threshold']} | **{c['result']}** |" for c in rec["checks"]]
    L.append("\n### Factors by number of topics\n\n| Topics | Factors |\n|---|---|")
    L += [f"| {n} | {', '.join(v) or '(none)'} |" for n, v in m["factors_by_ntopics"].items()]
    L.append(f"\nFactors in all four topics: {', '.join(m['unity_factors']) or 'none'}; of these substantive or tradition factors: {', '.join(m['unity_factors_substantive']) or 'none'}.")
    L.append("\n### Pairs\n\n| Pair | Shared factors | Shared cited sources (existing ledgers) | Cross-citations (existing ledgers) | Connection links (this report) |\n|---|---|---|---|---|")
    L += [f"| {k} | {', '.join(m['pair_shared_factors'][k]) or '(none)'} | {len(m['pair_shared_sources'][k])}{': ' + ', '.join(m['pair_shared_sources'][k]) if m['pair_shared_sources'][k] else ''} | {m['pair_cross_citations'][k]} | {', '.join(m['links_by_pair'][k]) or '(none)'} |" for k in m["pair_shared_factors"]]
    L.append(f"\nDistinct sources cited per topic: " + ", ".join(f"{k} {v}" for k, v in m["topic_sources"].items()) + ".")
    L.append(f"\nTopic-to-topic links already in the SSSC register: {', '.join(m['topic_topic_links']) or 'none'}. Duplicate source registrations: {'; '.join(' = '.join(g) for g in m['register_duplicates']) or 'none'}. Phase claims on the Being axis: {', '.join(m['phase_being_claim_ids'])}.")
    L.append("\n### This report's claims and links\n\n| Label | Claims | Links |\n|---|---|---|")
    L += [f"| {l} | {m['claims_by_label'][l]} | {m['links_by_label'][l]} |" for l in LABELS]
    L.append("\n| Kind | Claims |\n|---|---|"); L += [f"| {k} | {v} |" for k, v in m["claims_by_kind"].items()]
    for key in ("dangling_basis", "unresolved_sources", "sources_not_in_basis", "label_rule_violations", "owner_rule_violations", "census_claim_mismatches", "problems"):
        L.append(f"\n{key}: {', '.join(m[key]) or 'none'}")
    return "\n".join(L) + "\n"

# ---------------- Maps & Matrix overlay ----------------
def maps(cycle_dir, it, outdir, label):
    """Unchanged `gaia_tools.phases maps` base, plus this report's overlay. Never touches earlier versions."""
    outdir = os.path.abspath(outdir)
    cfg = load_cfg(cycle_dir)
    repo = os.path.normpath(os.path.join(os.path.abspath(cycle_dir), cfg["repo_root"]))
    R = os.path.join(repo, "Research"); tools = os.path.join(R, "tools")
    if os.path.exists(outdir): raise SystemExit(f"{outdir} exists; a Maps version is never overwritten")
    subprocess.run([sys.executable, "-m", "gaia_tools.phases", "maps", R, outdir, "--version-label", label],
                   cwd=tools, check=True, stdout=subprocess.DEVNULL)
    sys.path.insert(0, tools)
    from gaia_tools import maps as M  # noqa: E402
    prev = os.path.join(R, "Maps-and-Matrix", cfg["maps"]["base_version"])
    for d in ("data-model", "validation"):
        shutil.copytree(os.path.join(prev, d), os.path.join(outdir, d))
    rec = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json")))
    P = lambda p: os.path.normpath(os.path.join(os.path.abspath(cycle_dir), p))
    cl = csvrows(P(cfg["judgments"]["claims"])); lk = csvrows(P(cfg["judgments"]["links"])); fac = csvrows(P(cfg["judgments"]["factors"]))
    rules = M.lens_rules()
    place = []
    for r in cl:
        ts = split(r["topics"])
        place.append([r["claim_id"], r["kind"], r["framework_label"], ";".join(ts), ";".join(BEING[t] for t in ts),
                      ";".join(M.lenses_for(r["wording"], rules)) or "Unassigned", cfg["cycle"]])
    mx = os.path.join(outdir, "matrix")
    wcsv(os.path.join(mx, "connection_claim_placement.csv"), ["claim_id", "kind", "label", "topics", "beings", "lenses", "connection_cycle"], place)
    wcsv(os.path.join(mx, "connection_factor_x_topic.csv"), ["factor_id", "factor", "kind"] + TOPICS,
         [[f, n, k] + [next((r["basis_claims"] for r in fac if r["factor_id"] == f and r["topic"] == t), "") for t in TOPICS]
          for f, n, k in sorted({(r["factor_id"], r["factor"], r["kind"]) for r in fac})])
    shutil.copy(os.path.join(cycle_dir, f"iter-{it}", "data", "pairs.csv"), os.path.join(mx, "connection_pairs_6.csv"))
    # intersections_625: one added column; every other column unchanged
    ip = os.path.join(mx, "intersections_625.csv"); rows = csvrows(ip); fields = list(rows[0].keys()) + ["connection_claims_in_being_lens_projection"]
    for r in rows:
        r["connection_claims_in_being_lens_projection"] = str(sum(1 for p in place if r["being"] in p[4].split(";") and r["lens"] in p[5].split(";")))
    wcsv(ip, fields, [[r[f] for f in fields] for r in rows])
    # graph: connection edges between the existing topic nodes
    gp = os.path.join(outdir, "graph", "link_graph.json"); g = json.load(open(gp))
    for r in lk:
        g["edges"].append({"id": r["link_id"], "source": r["from"], "target": r["to"], "type": "connection: " + r["link_type"],
                           "framework_label": r["framework_label"], "basis": r["basis"], "statement": r["statement"]})
    g.setdefault("legend", {})
    if isinstance(g["legend"], dict): g["legend"]["connection"] = "CL-* links among the four SSSC topics (Connection report, Work Queue §E)"
    json.dump(g, open(gp, "w"), indent=1, ensure_ascii=False)
    os.makedirs(os.path.join(outdir, "changes"), exist_ok=True)
    wcsv(os.path.join(outdir, "changes", "connection_changes.csv"), ["kind", "id", "connection_cycle", "label", "change_vs_previous"],
         [["claim", r["claim_id"], cfg["cycle"], r["framework_label"], r.get("change_vs_prev", "new")] for r in cl] +
         [["link", r["link_id"], cfg["cycle"], r["framework_label"], r.get("change_vs_prev", "new")] for r in lk])
    json.dump({"cycle": cfg["cycle"], "iteration": it, "checks": rec["checks"], "outputs": rec["outputs"]},
              open(os.path.join(outdir, "validation", f"connection_{cfg['cycle']}.json"), "w"), indent=1, ensure_ascii=False, sort_keys=True)
    m = rec["metrics"]; ver = label
    nproj = sum(int(r["connection_claims_in_being_lens_projection"]) for r in rows)
    readme = f"""# Maps & Matrix — {ver.split('-')[0]} (adds the Connection report, {cfg['cycle']}, to {cfg['maps']['base_version'].split('-')[0]})

**Tooling:** `tools/conn.py maps` in `Research/Tracks/Connections/E1-Soul-Spirit-Subconscious-Consciousness/`. It runs `python -m gaia_tools.phases maps` unchanged, then adds the overlay below. Earlier versions (v1 to {cfg['maps']['base_version'].split('-')[0]}) are kept unchanged.

## What changed
- All base files (`claim_map/`, `matrix/` except one added column, `graph/` except added edges, `changes/changes.csv`, `simulations/`) are regenerated by `phases maps` from the same inputs as {cfg['maps']['base_version'].split('-')[0]}. `data-model/` and `validation/` are copied from it unchanged, plus `validation/connection_{cfg['cycle']}.json`.
- `matrix/connection_claim_placement.csv`: {len(place)} Connection claims placed on the Being axis by the topics they connect (Soul, Spirit, Mind for the Subconscious, Consciousness) and on lenses by the provisional keyword rule.
- `matrix/connection_factor_x_topic.csv`: {m['factors_total']} judged factors × 4 topics, with basis claim IDs. Factors in all four topics: {', '.join(m['unity_factors']) or 'none'}.
- `matrix/connection_pairs_6.csv`: the six topic pairs, with shared factors, shared cited sources, cross-citations in the existing ledgers and Connection links.
- `matrix/intersections_625.csv` gains the column `connection_claims_in_being_lens_projection` ({nproj // 25} claim placements on Being × Lens pairs, each repeated across the 25 Alchemy × Phase cells of that pair, {nproj} in all; a claim connecting several topics counts on each of their Being rows; claims with no keyword lens are not counted). The 625 grid is not re-dimensioned; Alchemy and Phase stay unassigned for these claims.
- `graph/link_graph.json` gains {len(lk)} CL-* edges between the existing topic nodes SOUL, SPIRIT, SUBC and CONS (the base graph had one such edge, TL-08).
- `changes/connection_changes.csv`: claim and link changes for this Connection cycle.

## Honest limits
- Factors, claims and links are one agent's judgments; gate INDETERMINATE (independent review pending).
- Lens placement uses the provisional keyword rule (a navigation aid, not a classification).
- Placing a claim on a Being row says which topics it connects, not that it shows anything about a soul, spirit or mind.

## Reproduce
```
cd Research/Tracks/Connections/E1-Soul-Spirit-Subconscious-Consciousness
python tools/conn.py maps --cycle {os.path.basename(os.path.normpath(cycle_dir))} --iter {it} --out ../../../Maps-and-Matrix/{ver} --label "{label}"
```
"""
    open(os.path.join(outdir, "README.md"), "w", encoding="utf-8").write(readme)
    files = sorted(os.path.relpath(os.path.join(dp, f), outdir) for dp, _, fs in os.walk(outdir) for f in fs if f != "MANIFEST.sha256")
    open(os.path.join(outdir, "MANIFEST.sha256"), "w").write("".join(f"{sha(os.path.join(outdir, f))}  {f}\n" for f in files))
    return {"claims": len(place), "links": len(lk), "projection_total": nproj}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("run"); c.add_argument("--cycle", required=True); c.add_argument("--iter", type=int, required=True)
    c = sp.add_parser("verify"); c.add_argument("--cycle", required=True)
    c = sp.add_parser("render"); c.add_argument("--cycle", required=True); c.add_argument("--iter", type=int, required=True)
    c = sp.add_parser("maps"); c.add_argument("--cycle", required=True); c.add_argument("--iter", type=int, required=True)
    c.add_argument("--out", required=True); c.add_argument("--label", required=True)
    a = ap.parse_args()
    if a.cmd == "run":
        r = run(a.cycle, a.iter); print(" ".join(f"{c['id']}={c['result']}" for c in r["checks"]))
    elif a.cmd == "verify":
        for it, ok in verify(a.cycle): print(f"iter-{it} identical={ok}")
    elif a.cmd == "render":
        sys.stdout.write(render(a.cycle, a.iter))
    else:
        print(json.dumps(maps(a.cycle, a.iter, a.out, a.label)))
