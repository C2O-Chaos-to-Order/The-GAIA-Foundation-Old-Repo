#!/usr/bin/env python3
"""PC-4 Research-to-Domain Map: deterministic tooling.

Reads the Work Queue (repo) and the owner-provided GAIA Totality Suite v0.1.0
(EXTERNAL, never filed in this repository; verified by SHA-256), joins the
agent judgment map, runs an independent lexical matcher, and computes coverage.

Commands:
  inventory  --wq WQ --out CSV
  run        --cycle DIR --iter N          (reads DIR/config.json)
  verify     --cycle DIR                   (reruns every iteration in a temp dir)
Standard library only.
"""
import argparse, csv, hashlib, io, json, math, os, re, shutil, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # PC-4 folder
REG_SHA = "057efb5489305f99280f9b350771058686e35fef753682449f2901b152fe8c72"
SUMS_SHA = "2f18e3b36c89bc491d21c89438e4315474e13c22ae03476bafc3581839f6a5d7"  # suite SHA256SUMS.txt
LABELS = ["Established", "Plausible", "Philosophical/Spiritual", "Hypothetical"]

# ---------------------------------------------------------------- inventory
# (heading regex, section code, kind) ; kind decides whether an item is a report
SECTIONS = [
    (r"^## A\. ", "A", "report"), (r"^## B\. ", "B", "report"),
    (r"^## C\. ", "C", "level"), (r"^## D\. ", "D", "report"),
    (r"^## E\. ", "E", "report"), (r"^## F\. ", "F", "report"),
    (r"^## G\. ", "G", "report"), (r"^## H\. ", "H", "report"),
    (r"^## I\. ", "I", "report"), (r"^## J\. ", "J", "report"),
    (r"^## Governance", "GOV", "governance"),
    (r"^### Totality of Governance reports", "TOG", "report"),
    (r"^## Program Coordination", "PCX", "report"),
    (r"^### Coordination reports", "PC", "report"),
    (r"^### Domain reports by wave", "WAVE", "tot-domain-report"),
    (r"^## K\. ", "K", "report"),
    (r"^### Recommended by Grok Bot", "KR", "candidate"),
    (r"^### Added later", "KL", "report"),
    (r"^## L\. ", "L", "update"),
    (r"^## M\. ", "M", "gap"),
    (r"^### \(a\) ", "Ma", "setting"), (r"^### \(b\) ", "Mb", "gap"),
    (r"^### \(c\) ", "Mc", "recommendation"),
    (r"^### \(d\) ", "Md", "out-of-scope"),
    (r"^## N\. ", "N", "report"), (r"^### Cross-repository", "NX", "report"),
    (r"^### Conflicts recorded", "NC", "note"), (r"^### Held", "NH", "note"),
    (r"^## Afterwards", "AFT", "afterwards"), (r"^## Change log", "LOG", "log"),
]
BOX = re.compile(r"^(\s*)- \[( |x)\] (.*)$")

def strip_md(t):
    t = re.sub(r"[`*]", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()

def inventory(wq_text):
    sec, kind, items, count, parent = None, None, [], {}, None
    for ln, line in enumerate(wq_text.splitlines(), 1):
        for rx, code, k in SECTIONS:
            if re.match(rx, line):
                sec, kind = code, k
                break
        m = BOX.match(line)
        if not m or sec in (None, "LOG"):
            continue
        indent, done, text = len(m.group(1)), m.group(2) == "x", m.group(3)
        plain = strip_md(text.replace("✅", "").replace("⬜", ""))
        k = kind
        if sec == "Mc" and re.match(r"s\d+\.", plain):
            k = "candidate"
        if sec == "Mb" and indent > 0:
            k = "cluster"
        if sec == "L" and indent > 0:
            k = "update"
        if sec == "Mb" and indent > 0 and parent:
            iid = f"{parent}.{count.setdefault(parent, 0) + 1}"
            count[parent] += 1
        else:
            count[sec] = count.get(sec, 0) + 1
            iid = f"{sec}-{count[sec]:02d}"
            mm = re.match(r"(b\d+|a\d+|c\d+|s\d+|d\d+)\.", plain)
            if sec in ("Ma", "Mb", "Mc", "Md") and mm:
                iid = "M-" + mm.group(1)
            mm = re.match(r"(PC-\d)", plain)
            if sec == "PC" and mm:
                iid = mm.group(1)
            mm = re.match(r"(N-[AB])\.", plain)
            if sec == "NX" and mm:
                iid = mm.group(1)
            mm = re.match(r"(\d)\. ", plain)
            if sec == "N" and mm:
                iid = f"N-{mm.group(1)}"
            if sec == "TOG":
                mm = re.match(r"ToG (\d+)", plain)
                iid = f"ToG-{int(mm.group(1)):02d}" if mm else f"ToG-SYN"
            if sec == "WAVE":
                mm = re.match(r"Wave (\d)", plain)
                iid = f"WAVE-{mm.group(1)}" if mm else iid
            parent = iid
        items.append(dict(item_id=iid, section=sec, kind=k, line=ln,
                          status="done" if done else "open", text=plain))
    ids = [i["item_id"] for i in items]
    assert len(ids) == len(set(ids)), "duplicate item ids"
    return items

def count_boxes(wq_text):
    n = 0
    in_log = False
    for line in wq_text.splitlines():
        if re.match(r"^## Change log", line):
            in_log = True
        if BOX.match(line) and not in_log:
            n += 1
    return n

# ---------------------------------------------------------------- suite
def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

def load_register(suite):
    path = os.path.join(suite, "TOTALITY_REGISTER.csv")
    got = sha256(path)
    if got != REG_SHA:
        raise SystemExit(f"register sha256 mismatch: {got}")
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 45
    return rows

_VERIFIED = {}
def verify_suite_file(suite, rel):
    """Check a suite file against the suite's SHA256SUMS.txt, itself pinned by SUMS_SHA."""
    if suite not in _VERIFIED:
        sp = os.path.join(suite, "SHA256SUMS.txt")
        if sha256(sp) != SUMS_SHA:
            raise SystemExit("suite SHA256SUMS.txt mismatch")
        sums = {}
        for line in open(sp, encoding="utf-8"):
            if line.strip():
                h, n = line.split(None, 1)
                sums[n.strip().lstrip("*").lstrip("./")] = h
        _VERIFIED[suite] = sums
    want = _VERIFIED[suite].get(rel)
    if want is None or sha256(os.path.join(suite, rel)) != want:
        raise SystemExit(f"suite file not verified: {rel}")

def charter_sections(suite, filename, wanted):
    verify_suite_file(suite, filename)
    with open(os.path.join(suite, filename), encoding="utf-8-sig") as f:
        text = f.read()
    out, cur = [], None
    for line in text.splitlines():
        m = re.match(r"^## (\d+)\.", line)
        if m:
            cur = int(m.group(1))
            continue
        if line.startswith("## "):
            cur = None
            continue
        if cur in wanted:
            out.append(line)
    return strip_md(" ".join(out))

# ---------------------------------------------------------------- matcher
STOP = set("""a an and the of to in on for with by as at or from into is are be
been being it its this that these those which who whom what when where how
not no any all each every per via than then so such can may must should will
shall would could do does done their there they them we our us you your he she
his her i me my one two three more most other some only also own same just
over under about between before after under within without upon across both
gaia report reports owner level levels foundation research""".split())

def stem(w):
    for suf in ("ations", "ation", "ities", "ity", "ings", "ing", "ness", "ments",
                "ment", "ies", "es", "s", "al", "ic", "ed"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w

def tokens(text, do_stem=True):
    ws = re.findall(r"[a-z]+", text.lower())
    ws = [w for w in ws if w not in STOP and len(w) > 2]
    return [stem(w) for w in ws] if do_stem else ws

def domain_docs(suite, reg, variant):
    docs = {}
    for r in reg:
        title = r["title"].split(":", 1)[-1]
        if variant == "title":
            t = title
        elif variant == "title_purpose":
            t = title + " " + r["purpose"]
        elif variant == "charter":
            t = title + " " + r["purpose"] + " " + charter_sections(
                suite, r["filename"], {1, 2, 3, 4, 7})
        else:
            raise ValueError(variant)
        docs[r["stable_id"]] = t
    return docs

def tfidf_rank(items, docs, do_stem=True):
    dtoks = {d: tokens(t, do_stem) for d, t in docs.items()}
    N = len(dtoks)
    df = {}
    for ts in dtoks.values():
        for w in set(ts):
            df[w] = df.get(w, 0) + 1
    idf = {w: math.log((N + 1) / (c + 1)) + 1 for w, c in df.items()}
    def vec(ts):
        v = {}
        for w in ts:
            if w in idf:
                v[w] = v.get(w, 0) + 1
        v = {w: (1 + math.log(c)) * idf[w] for w, c in v.items()}
        n = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {w: x / n for w, x in v.items()}
    dv = {d: vec(ts) for d, ts in dtoks.items()}
    out = {}
    for it in items:
        iv = vec(tokens(it["text"], do_stem))
        sc = sorted(((round(sum(iv.get(w, 0) * x for w, x in v.items()), 6), d)
                     for d, v in dv.items()), key=lambda p: (-p[0], p[1]))
        out[it["item_id"]] = sc
    return out

# ---------------------------------------------------------------- judgments
def load_map(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def split_ids(s):
    return [x for x in re.split(r"[;\s]+", s.strip()) if x]

def tot(n):
    return f"GAIA-TOT-{int(n):03d}"

def named_tots(text):
    """TOT ids a text names explicitly: 'TOT-nnn', lists such as
    'TOT-016, 026, 041' or 'TOT-002/013/035', and ranges 'TOT-003-011'."""
    found = set()
    rx = r"TOT-(\d{3})((?:\s*(?:,|/|–|-|and)\s*\d{3})*)"
    for m in re.finditer(rx, text):
        nums = [m.group(1)] + re.findall(r"\d{3}", m.group(2))
        seps = re.findall(r"(,|/|–|-|and)\s*\d{3}", m.group(2))
        prev = int(nums[0]); found.add(tot(prev))
        for sep, n in zip(seps, nums[1:]):
            n = int(n)
            if sep in ("–", "-") and n > prev:
                for x in range(prev, n + 1):
                    found.add(tot(x))
            else:
                found.add(tot(n))
            prev = n
    return found

# ---------------------------------------------------------------- run
def write_csv(path, rows, fields):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})

def run(cycle_dir, it, outdir=None):
    cfg = json.load(open(os.path.join(cycle_dir, "config.json")))
    suite = os.environ.get("PC4_SUITE", cfg["suite_path"])
    reg = load_register(suite)
    reg_ids = [r["stable_id"] for r in reg]
    wq_path = os.path.normpath(os.path.join(cycle_dir, cfg["work_queue"]))
    wq = open(wq_path, encoding="utf-8").read()
    items = inventory(wq)
    byid = {i["item_id"]: i for i in items}
    jm = load_map(os.path.normpath(os.path.join(cycle_dir, cfg["judgment_map"])))
    icfg = cfg["iterations"][str(it)]
    report_kinds = set(cfg["report_kinds"])
    problems = []
    # judgment integrity
    jmap = {}
    for r in jm:
        iid = r["item_id"]
        if iid not in byid:
            problems.append(f"map row for unknown item {iid}")
            continue
        if iid in jmap:
            problems.append(f"duplicate map row {iid}")
        prim = r["primary"].strip()
        sec = split_ids(r["secondary"])
        for d in ([prim] if prim != "NONE" else []) + sec:
            if d not in reg_ids:
                problems.append(f"{iid}: unknown domain {d}")
        if r["label"] not in LABELS:
            problems.append(f"{iid}: bad label {r['label']}")
        if r["label"] == "Established":
            src = r.get("named_in", "").strip() or iid
            if src not in byid:
                problems.append(f"{iid}: named_in {src} is not an item")
            elif prim not in named_tots(byid[src]["text"]):
                problems.append(f"{iid}: Established but {src} text does not name {prim}")
        if prim == "NONE" and not r["basis"].strip():
            problems.append(f"{iid}: NONE needs a reason")
        jmap[iid] = dict(primary=prim, secondary=sec, label=r["label"], basis=r["basis"])
    unmapped = [i["item_id"] for i in items
                if i["kind"] in cfg["map_kinds"] and i["item_id"] not in jmap]
    for u in unmapped:
        problems.append(f"in-scope item not in map: {u}")
    # matcher
    docs = domain_docs(suite, reg, icfg["variant"])
    mitems = [i for i in items if i["item_id"] in jmap and jmap[i["item_id"]]["primary"] != "NONE"
              and i["kind"] in report_kinds]
    ranks = tfidf_rank(mitems, docs, icfg.get("stem", True))
    k = icfg.get("k", 3)
    hits1 = hitsk = anyk = zero = 0
    rows_m = []
    for i in mitems:
        sc = ranks[i["item_id"]]
        top = [d for s, d in sc[:k] if s > 0]
        j = jmap[i["item_id"]]
        alld = {j["primary"], *j["secondary"]}
        h1 = bool(sc and sc[0][0] > 0 and sc[0][1] == j["primary"])
        hk = j["primary"] in top
        ak = bool(alld & set(top))
        zero += sc[0][0] == 0
        hits1 += h1; hitsk += hk; anyk += ak
        rows_m.append(dict(item_id=i["item_id"], kind=i["kind"], primary=j["primary"],
                           label=j["label"], matcher_top=";".join(top),
                           top_score=sc[0][0], hit1=int(h1), hitk=int(hk), anyk=int(ak)))
    n = len(mitems) or 1
    # per-label agreement
    by_label = {}
    for r in rows_m:
        b = by_label.setdefault(r["label"], [0, 0])
        b[0] += r["hitk"]; b[1] += 1
    # coverage
    def cov(kinds, include_secondary=True):
        hit = {d: [] for d in reg_ids}
        for i in items:
            if i["kind"] not in kinds or i["item_id"] not in jmap:
                continue
            j = jmap[i["item_id"]]
            ds = ([j["primary"]] if j["primary"] != "NONE" else [])
            if include_secondary:
                ds += j["secondary"]
            for d in ds:
                hit[d].append(i["item_id"])
        return hit
    cov_p = cov(report_kinds, include_secondary=False)
    cov_ps = cov(report_kinds)
    cov_cand = cov(report_kinds | set(cfg.get("candidate_kinds", [])))
    reg_by = {r["stable_id"]: r for r in reg}
    cov_rows = [dict(stable_id=d, title=reg_by[d]["title"].split(":", 1)[-1].strip(),
                     priority=reg_by[d]["priority"],
                     n_primary=len(cov_p[d]), n_any=len(cov_ps[d]),
                     n_any_with_candidates=len(cov_cand[d]),
                     primary_items=";".join(cov_p[d]), secondary_items=";".join(
                         x for x in cov_ps[d] if x not in cov_p[d]))
                for d in reg_ids]
    no_report_primary = [d for d in reg_ids if not cov_p[d]]
    no_report_any = [d for d in reg_ids if not cov_ps[d]]
    no_report_cand = [d for d in reg_ids if not cov_cand[d]]
    reports = [i for i in items if i["kind"] in report_kinds]
    no_domain = [i["item_id"] for i in reports if i["item_id"] in jmap
                 and jmap[i["item_id"]]["primary"] == "NONE"]
    # b7 cluster single-home proposals
    clusters_ok, cl_rows = 0, []
    cpath = cfg.get("clusters")
    if cpath:
        for c in load_map(os.path.normpath(os.path.join(cycle_dir, cpath))):
            cid, mem = c["cluster_id"], split_ids(c["members"])
            errs = []
            if cid not in byid:
                errs.append("unknown cluster id")
            for m in mem:
                if m not in byid:
                    errs.append(f"unknown member {m}")
            if c["home_item"] not in mem:
                errs.append("home_item not a member")
            hj = jmap.get(c["home_item"])
            if hj and c["home_domain"] not in [hj["primary"], *hj["secondary"]]:
                errs.append("home_domain not among the home item's judged domains")
            if c["home_domain"] not in reg_ids:
                errs.append("home_domain unknown")
            named = named_tots(byid[cid]["text"]) if cid in byid else set()
            mdom = set(split_ids(c["member_domains"]))
            if not named <= mdom:
                errs.append("cluster names domains missing from member_domains: "
                            + ",".join(sorted(named - mdom)))
            if c["label"] not in LABELS:
                errs.append("bad label")
            clusters_ok += not errs
            for e in errs:
                problems.append(f"{cid}: {e}")
            cl_rows.append(dict(cluster_id=cid, home_item=c["home_item"],
                                home_domain=c["home_domain"], n_members=len(mem),
                                ok=int(not errs)))
    # outputs
    out = outdir or os.path.join(cycle_dir, f"iter-{it}")
    os.makedirs(out, exist_ok=True)
    data = os.path.join(out, "data")
    os.makedirs(data, exist_ok=True)
    write_csv(os.path.join(data, "matcher.csv"), rows_m,
              ["item_id", "kind", "primary", "label", "matcher_top", "top_score",
               "hit1", "hitk", "anyk"])
    write_csv(os.path.join(data, "coverage_domains.csv"), cov_rows,
              ["stable_id", "title", "priority", "n_primary", "n_any",
               "n_any_with_candidates", "primary_items", "secondary_items"])
    joined = []
    for i in items:
        j = jmap.get(i["item_id"])
        joined.append(dict(item_id=i["item_id"], section=i["section"], kind=i["kind"],
                           status=i["status"], line=i["line"],
                           primary=j["primary"] if j else "",
                           secondary=";".join(j["secondary"]) if j else "",
                           label=j["label"] if j else "", basis=j["basis"] if j else "",
                           text=i["text"][:160]))
    write_csv(os.path.join(data, "item_domain_map.csv"), joined,
              ["item_id", "section", "kind", "status", "line", "primary", "secondary",
               "label", "basis", "text"])
    label_counts = {}
    for i in reports:
        if i["item_id"] in jmap:
            l = jmap[i["item_id"]]["label"]
            label_counts[l] = label_counts.get(l, 0) + 1
    metrics = dict(
        n_items=len(items), n_boxes=count_boxes(wq),
        n_reports=len(reports), n_mapped=len(jmap),
        n_matcher_items=len(mitems), k=k, variant=icfg["variant"],
        stem=icfg.get("stem", True),
        top1_rate=round(hits1 / n, 4), topk_primary_rate=round(hitsk / n, 4),
        topk_any_rate=round(anyk / n, 4), zero_score_items=zero,
        topk_by_label={l: [a, b, round(a / b, 4)] for l, (a, b) in sorted(by_label.items())},
        report_label_counts=dict(sorted(label_counts.items())),
        domains_no_report_primary=no_report_primary,
        domains_no_report_any=no_report_any,
        domains_no_report_with_candidates=no_report_cand,
        reports_no_domain=no_domain,
        inventory_gap=count_boxes(wq) - len(items),
        clusters_ok=clusters_ok, clusters=cl_rows,
        problems=problems,
    )
    # pre-registered checks
    checks = []
    for c in cfg["checks"]:
        val = metrics
        for p in c["metric"].split("."):
            val = val[p]
        if isinstance(val, list):
            val = len(val)
        op, thr = c["op"], c["threshold"]
        ok = {"ge": val >= thr, "le": val <= thr, "eq": val == thr}[op]
        checks.append(dict(id=c["id"], hypothesis=c["hypothesis"], metric=c["metric"],
                           op=op, threshold=thr, value=val,
                           result="PASS" if ok else "FAIL",
                           iterations=c.get("iterations")))
    checks = [c for c in checks if not c["iterations"] or it in c["iterations"]]
    for c in checks:
        c.pop("iterations")
    rec = dict(track="PC-4 Research-to-Domain Map", cycle=cfg["cycle"], iteration=it,
               variant=icfg, inputs=dict(
                   work_queue=cfg["work_queue"], work_queue_sha256=sha256(wq_path),
                   judgment_map=cfg["judgment_map"],
                   judgment_map_sha256=sha256(os.path.normpath(os.path.join(cycle_dir, cfg["judgment_map"]))),
                   suite="GAIA Totality Suite v0.1.0 (owner-provided, Proposed, not adopted; external, not filed)",
                   register_sha256=REG_SHA),
               metrics=metrics, checks=checks,
               outputs={f"data/{n}": sha256(os.path.join(data, n)) for n in sorted(os.listdir(data))})
    with open(os.path.join(out, "EXECUTION_RECORD.json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2, ensure_ascii=False, sort_keys=False)
        f.write("\n")
    return rec

def verify(cycle_dir):
    cfg = json.load(open(os.path.join(cycle_dir, "config.json")))
    res = []
    for it in sorted(cfg["iterations"], key=int):
        it = int(it)
        tmp = tempfile.mkdtemp()
        try:
            rec = run(cycle_dir, it, outdir=tmp)
            orig = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json")))
            same = (rec == orig)
            res.append((it, same, rec["outputs"] == orig["outputs"]))
        finally:
            shutil.rmtree(tmp)
    return res

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("inventory"); a.add_argument("--wq", required=True); a.add_argument("--out", required=True)
    b = sp.add_parser("run"); b.add_argument("--cycle", required=True); b.add_argument("--iter", type=int, required=True)
    c = sp.add_parser("verify"); c.add_argument("--cycle", required=True)
    args = ap.parse_args()
    if args.cmd == "inventory":
        txt = open(args.wq, encoding="utf-8").read()
        items = inventory(txt)
        write_csv(args.out, items, ["item_id", "section", "kind", "line", "status", "text"])
        print(len(items), "items;", count_boxes(txt), "checkboxes")
    elif args.cmd == "run":
        rec = run(args.cycle, args.iter)
        print(json.dumps({k: rec["metrics"][k] for k in ("n_items", "n_reports", "n_matcher_items", "top1_rate", "topk_primary_rate", "topk_any_rate")}))
        for c in rec["checks"]:
            print(c["id"], c["result"], c["value"])
        if rec["metrics"]["problems"]:
            print("PROBLEMS:", *rec["metrics"]["problems"], sep="\n  ")
    else:
        ok = True
        for it, same, outs in verify(args.cycle):
            print(f"iter-{it}: record identical={same} outputs identical={outs}")
            ok &= same
        sys.exit(0 if ok else 1)
