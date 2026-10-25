#!/usr/bin/env python3
"""N-A Level-Name Crosswalk (GAIA-Documentation <-> The GAIA Foundation): deterministic tooling.

GAIA-Documentation is READ-ONLY and EXTERNAL. Its files are never filed here; they are read from a
verified local mirror (env GAIA_DOC_SRC, default in config) whose every file is checked against the
git blob SHA recorded in the cycle's ledger. Only derived terms, counts and short locators are written.
Commands: run --cycle DIR --iter N | verify --cycle DIR | render --cycle DIR --iter N
"""
import argparse, csv, hashlib, json, os, re, shutil, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "..", "..", "Program-Coordination", "PC-4-Research-to-Domain-Map", "tools"))
import pc4  # noqa: E402  (boundary scan helper)

LABELS = {"Established", "Plausible", "Philosophical/Spiritual", "Hypothetical"}
RELATIONS = {"same-name-same-sense", "same-name-different-sense", "partial-overlap", "broader", "narrower",
             "different-kind", "no-counterpart", "internal-variant"}
OPTION_TYPES = {"crosswalk-only", "namespace", "align-foundation", "align-gaiadoc", "owner-act", "route", "defer"}
G = "GAIA-Documentation/"

def rd(p):
    return open(p, encoding="utf-8").read()

def blob_sha(path):
    b = open(path, "rb").read()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()

def csvrows(p):
    return list(csv.DictReader(open(p, encoding="utf-8")))

def wcsv(p, header, rows):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n"); w.writerow(header); w.writerows(rows)

def section(text, start, stop):
    a = text.index(start); b = text.index(stop, a + len(start)); return text[a:b]

# ---------------- extractors (each returns an ordered term list) ----------------
def ex_readme_s2(F):
    s = section(F["readme"], "## 2. The responsibility ladder", "## 3.")
    return [m.group(1) for m in re.finditer(r"^\| ((?:\w+ )?Power) \|", s, re.M)]

def ex_wq_c(F):
    s = section(F["wq"], "## C. The upgrade ladder", "## D.")
    return [m.group(1) for m in re.finditer(r"^- \[[ x]\] \S+ (\w+)", s, re.M)]

def ex_wq_b(F):
    s = section(F["wq"], "## B. The six phases", "## C.")
    out = []
    for m in re.finditer(r"^\| (\w+)(?: \([^)]*\))? \| ([^|]+?) \|", s, re.M):
        if m.group(1) not in ("Phase", "Six") and m.group(2).strip() != "—":
            out.append(m.group(1))
    return out

def ex_wq_b_levels(F):
    s = section(F["wq"], "## B. The six phases", "## C.")
    return [f"{m.group(1)}={m.group(2).strip()}" for m in re.finditer(r"^\| (\w+)(?: \([^)]*\))? \| ([^|]+?) \|", s, re.M)
            if m.group(1) not in ("Phase", "Six") and m.group(2).strip() != "—"]

def _axis93(F, n):
    s = section(F["readme"], "### 9.3 Triality", "### 9.4")
    line = [l for l in s.splitlines() if l.startswith(f"{n}. ")][0]
    return [t.strip().rstrip(".") for t in line.split(":**", 1)[1].split(",")]

def ex_readme_93_being(F):
    return _axis93(F, 2)

def ex_readme_93_phase(F):
    return _axis93(F, 3)

def ex_seven(F):
    d = os.path.join(F["repo"], "Research/Cycles/Cycle-4-x12")
    rs = sorted((int(m.group(1)), m.group(2)) for n in os.listdir(d) for m in [re.match(r"Report-(\d+)-(\w+)$", n)] if m)
    return [x for _, x in rs]

def ex_five_level(F):
    return re.findall(r"^### Level \d — (\w+)", F["doc"](G + "GAIA-Five-Level-Knowledge-Skills-and-Intelligence-Taxonomy-Research-Matrix-v1.0-Draft.md"), re.M)

def ex_five_domains(F):
    s = section(F["doc"](G + "GAIA-Five-Level-Knowledge-Skills-and-Intelligence-Taxonomy-Research-Matrix-v1.0-Draft.md"), "### 3.1", "### 3.2")
    return re.findall(r"^\d\. \*\*Human (\w+)\*\*", s, re.M)

def ex_five_phases(F):
    return re.findall(r"^### (Phase [A-Z]) —", F["doc"](G + "GAIA-Five-Level-Knowledge-Skills-and-Intelligence-Taxonomy-Research-Matrix-v1.0-Draft.md"), re.M)

def _reports32(F):
    out = []
    for r in F["ledger"]:
        m = re.match(re.escape(G) + r"(\w+)-(Human|AI)-(\w+) Research Report\.md$", r["path"])
        if m:
            out.append((r["path"],) + m.groups())
    return out

def ex_dims4(F):
    # dimensions present in the 32 filenames, in the order of the Five-Level taxonomy §3.1
    present = {d for _, _, _, d in _reports32(F)}
    return [d for d in ex_five_domains(F) if d in present]

def ex_levels4(F):
    # levels present in the 32 filenames, in the order of the Five-Level taxonomy §2
    present = {l for _, l, _, _ in _reports32(F)}
    return [l for l in ex_five_level(F) if l in present]

def ex_tracks(F):
    return [t for _, t in sorted(phase_census(F)["self"].items())]

def ex_courts(F):
    s = section(F["doc"](G + "GAIA-Integrity-Courts-Audit-Completeness-Genealogy-v1.0-Draft.md"), "## 8. Six-phase", "Treat this")
    return re.findall(r"^\d\. (\S+)$", s, re.M)

def ex_ch28(F):
    t = F["doc"](G + "SYNERGY-RESEARCH-REPORT-v3.0-CHAPTER-28-EDITORIAL-SYNTHESIS.md")
    m = re.search(r"six-rung taxonomy—(.+?)—", t)
    return [x.strip().replace("and ", "") for x in m.group(1).split(",")]

def _matrix_a(F):
    t = F["doc"]("Tablets/MATRIX-5x5.md")
    rows = re.findall(r"^\| \*\*(\w+)\*\* \|(.+)\|$", t, re.M)
    cols = re.findall(r"\*\*(\w+)\*\*", re.search(r"^\|  \|(.+)\|$", t, re.M).group(1))
    return cols, rows

def ex_tab_being(F):
    return [r for r, _ in _matrix_a(F)[1]]

def ex_tab_phase(F):
    return _matrix_a(F)[0]

def _stage_sequences(F):
    """Ordered alchemical stage sequences stated in tablet prose ('sequence ...: A, B, C' or 'A → B → C')."""
    out = {}
    for r in F["ledger"]:
        if not r["path"].endswith("_TABLET.md"):
            continue
        for line in F["doc"](r["path"]).splitlines():
            m = re.search(r"sequence[^:\n]*: (.+)", line)
            if not m:
                continue
            seq = re.findall(r"\b(Nigredo|Albedo|Citrinitas|Rubedo|Celestial|Ariditas|Viriditas|Calcination|Iosis|Caerulitas)\b", m.group(1))
            if len(seq) >= 3:
                out.setdefault(tuple(seq), []).append(os.path.basename(r["path"]).split("_")[0].title())
    return out

def ex_stage4(F):
    return list(min(_stage_sequences(F), key=len))

def ex_stage5(F):
    return list(max(_stage_sequences(F), key=len))

def ex_gem5(F):
    t = F["doc"]("Tablets/TERRA_TABLET.md")
    return re.findall(r"^\| \d \| (\w+) \| \w+ \| \*", t, re.M)

EXTRACTORS = {k[3:]: v for k, v in globals().items() if k.startswith("ex_")}

# ---------------- censuses ----------------
def phase_census(F):
    selfl, nxt, rows = {}, [], []
    for path, lvl, trk, dim in _reports32(F):
        t = F["doc"](path)
        m = re.search(r"Phase (\d+), (Human|AI) (\w+) Track", t)
        n = int(m.group(1)) if m else None
        if m:
            selfl.setdefault(n, f"{m.group(2)} {m.group(3)}")
        named_ok = bool(m) and (m.group(2), m.group(3)) == (trk, lvl)
        rows.append([os.path.basename(path), lvl, trk, dim, n if n else "", "yes" if named_ok else "no"])
        for mm in re.finditer(r"Phase (\d+) \((Human|AI) (\w+) Track\) begins", t):
            nxt.append((os.path.basename(path), int(mm.group(1)), f"{mm.group(2)} {mm.group(3)}"))
    mis = [[f, n, said, selfl.get(n, "")] for f, n, said in nxt if selfl.get(n) != said]
    return {"self": selfl, "rows": rows, "next": nxt, "mislabels": mis}

STATUS_CLASSES = [("draft-sealed-1017", r"^\*\*Status:\*\* Sealed 2026-10-17"),
                  ("discrepancy", r"^\*\*Status:\*\*.*Sealing discrepancy"),
                  ("consistent", r"^\*\*Status:\*\*.*Sealed consistently"),
                  ("sealed-in-source", r"^\*\*Status:\*\*.*Sealed in source"),
                  ("unsealed", r"^\*\*Status:\*\*.*Unsealed")]

def tablet_census(F):
    idx = F["doc"]("Tablets/INDEX.md")
    irows = {m.group(1): m.group(2) for m in re.finditer(r"^\| *\d+ \| (\w+) \| \[[^\]]+\]\([^)]+\) \| (.+) \|$", idx, re.M)}
    comb = {m.group(1): m.group(2).strip() for m in
            re.finditer(r"^\| (\w+) \| \w+ \| \w+ \| [^|]+ \| ([^|]+) \|$", F["doc"]("Tablets/MATRIX-COMBINED.md"), re.M)}
    rows, D = [], {k: [] for k in ("D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9")}
    tabs = sorted(r["path"] for r in F["ledger"] if r["path"].endswith("_TABLET.md"))
    for p in tabs:
        name = os.path.basename(p).split("_")[0].title()
        t = F["doc"](p)
        cls = next((c for c, rx in STATUS_CLASSES if re.search(rx, t, re.M)), "other")
        draft_body = bool(re.search(r"This tablet is a \*draft\*|The tablet is a draft", t))
        not_in_index = "It is not in the INDEX" in t
        seal_dates = sorted(set(re.findall(r"^Sealed: (.+?)(?: —.*)?$", t, re.M)))
        orig_sealed = bool(re.search(r"Original sealed \d{4}-\d\d-\d\d", t))
        ist = irows.get(name, "")
        rows.append([name, cls, "yes" if draft_body else "no", "yes" if not_in_index else "no",
                     ";".join(seal_dates), "yes" if orig_sealed else "no", ist[:40], comb.get(name, "")])
        if ist.startswith("Sealing discrepancy"): D["D1"].append(name)
        if cls == "draft-sealed-1017" and draft_body: D["D2"].append(name)
        if not_in_index and name in irows: D["D3"].append(name)
        if ist.startswith("Unsealed") and (orig_sealed or seal_dates): D["D4"].append(name)
        if cls == "consistent" and re.search(r"This is the only tablet in the transferred set", t): D["D6"].append(name)
    # D5: INDEX count statement vs INDEX rows
    m = re.search(r"(\d+) registry-listed tablets; (\d+) marked sealed and (\d+) marked unsealed", idx)
    sealed_rows = sum(1 for s in irows.values() if s.startswith(("Sealed", "Sealed in source")))
    if int(m.group(1)) != len(irows): D["D5"].append(f"rows={len(irows)} vs stated={m.group(1)}")
    if int(m.group(2)) != sealed_rows: D["D5"].append(f"sealed_rows={sealed_rows} vs stated={m.group(2)}")
    # D7: matrix status lines asserting both 'Not sealed' and 'Sealed 2026-10-17'; footnote 'Not in INDEX' for INDEX rows
    for mf in ("Tablets/MATRIX-5x5.md", "Tablets/MATRIX-5x5-PHASES.md", "Tablets/MATRIX-COMBINED.md"):
        st = re.search(r"^\*\*Status:\*\*(.*)$", F["doc"](mf), re.M).group(1)
        if "Not sealed" in st and "Sealed 2026-10-17" in st: D["D7"].append(os.path.basename(mf))
    # D8: stated vs listed empty cells in MATRIX-5x5 notes
    words = {"Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for mm in re.finditer(r"(Two|Three|Four|Five) cells are empty: ([^.]+)\.", F["doc"]("Tablets/MATRIX-5x5.md")):
        n = len([x for x in mm.group(2).split(",") if x.strip()])
        if n != words[mm.group(1)]: D["D8"].append(f"stated={words[mm.group(1)]} listed={n}")
    # D9: Matrix B table cell vs combined 'Phase Pair'
    tb = F["doc"]("Tablets/MATRIX-5x5-PHASES.md")
    cols = re.findall(r"\*\*(\w+)\*\*", re.search(r"^\|  \|(.+)\|$", tb, re.M).group(1))
    cell = {}
    for rr, body in re.findall(r"^\| \*\*(\w+)\*\* \|(.+)\|$", tb, re.M):
        for c, v in zip(cols, [x.strip() for x in body.split("|")]):
            for nm in re.findall(r"(\w+)\*?", v):
                cell.setdefault(nm, f"{rr} × {c}")
    for mm in re.finditer(r"^\| (\w+) \| \w+ \| \w+ \| (\w+ × \w+) \|", F["doc"]("Tablets/MATRIX-COMBINED.md"), re.M):
        if mm.group(1) in cell and cell[mm.group(1)] != mm.group(2):
            D["D9"].append(f"{mm.group(1)}: table {cell[mm.group(1)]} vs mapping {mm.group(2)}")
    return {"rows": rows, "D": D, "index_rows": len(irows), "set_is_22": "The set is 22" in idx}

NUMW = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8}
COUNT_CLAIMS = [("set_is_N", r"[Tt]he set is (\d+)"), ("N_registry_listed", r"(\d+) registry-listed"),
                ("N_tablet_registry", r"(\d+)-tablet registry"), ("N_Hermetic_Tablets", r"the (\d+) Hermetic Tablets"),
                ("N_Tablets_of_NEXUS", r"[Tt]he (\w+) Tablets of NEXUS"), ("N_gem_tablets", r"[Tt]he (\w+) gem tablets"),
                ("the_N_remain", r"[Tt]he (\d+) remain the \d+")]

def tablet_census_x3(F):
    listing = {r["path"] for r in F["all_listing"]}
    tabs = sorted(r["path"] for r in F["listing_tablets"])
    stages, dangling, phase2, claims = [], [], [], {}
    for p in tabs:
        t = F["doc"](p); name = os.path.basename(p).split("_")[0].title() if p.endswith("_TABLET.md") else os.path.basename(p)
        if p.endswith("_TABLET.md"):
            m = re.search(r"\*\*Governing Stage:?\*\*:? ([^\n]+)|\| Governing Stage \| ([^|]+) \|", t)
            st = (m.group(1) or m.group(2)).strip() if m else ""
            stages.append([name, st.split(" — ")[0].strip()])
            for mm in re.finditer(r"Baseline preserved:\*\* (Tablets/\S+?\.md)", t):
                if mm.group(1) not in listing:
                    dangling.append(f"{name}: {mm.group(1)}")
            if re.search(r"proceed to Phase 2", t):
                phase2.append(name)
        for key, rx in COUNT_CLAIMS:
            for mm in re.finditer(rx, t):
                v = mm.group(1).lower(); v = NUMW.get(v, v)
                claims.setdefault(f"{key}={v}", set()).add(name)
    return {"stages": stages, "dangling": dangling, "phase2": phase2,
            "claims": {k: sorted(v) for k, v in sorted(claims.items())}, "sequences": _stage_sequences(F)}

def vocab_census(F, patterns):
    files = [r["path"] for r in F["all_listing"]]
    out = []
    for key, rx in patterns:
        c = sum(1 for p in files if re.search(rx, F["doc"](p)))
        out.append([key, rx, c, len(files)])
    return out

# ---------------- boundary against GAIA-Documentation ----------------
def gd_boundary(F, root, window, exclude=()):
    """Like pc4.boundary_scan, against the GD mirror. Exact repository paths and basenames from the
    listing are masked on both sides first (a filename is a locator, not copied content); `ledger/`
    (paths, SHAs, sizes only) is excluded by the caller."""
    names = sorted({x for r in F["all_listing"] for x in (r["path"], os.path.basename(r["path"]))}, key=len, reverse=True)
    rx = re.compile("|".join(re.escape(n) for n in names))
    norm = lambda t: pc4._norm(rx.sub("\x00", t))
    grams = set()
    for r in F["all_listing"]:
        t = norm(F["doc"](r["path"]))
        for i in range(0, max(len(t) - window + 1, 0)):
            grams.add(hash(t[i:i + window]))
    hits = []
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if d != "__pycache__")
        for fn in sorted(fns):
            fp = os.path.join(dp, fn); rel = os.path.relpath(fp, root)
            if any(rel.startswith(e) for e in exclude):
                continue
            try:
                t = norm(open(fp, encoding="utf-8").read())
            except UnicodeDecodeError:
                continue
            if any(hash(t[i:i + window]) in grams for i in range(0, max(len(t) - window + 1, 0))):
                hits.append(rel)
    return hits

# ---------------- run ----------------
def load(cycle_dir):
    cfg = json.load(open(os.path.join(cycle_dir, "config.json")))
    P = lambda p: os.path.normpath(os.path.join(cycle_dir, p))
    repo = P(cfg["repo_root"])
    src = os.environ.get("GAIA_DOC_SRC", cfg["gaia_doc_src"])
    ledger = csvrows(P(cfg["ledger"]))
    listing = csvrows(P(cfg["listing"]))
    cache = {}
    def doc(p):
        if p not in cache:
            cache[p] = rd(os.path.join(src, p))
        return cache[p]
    F = {"cfg": cfg, "P": P, "repo": repo, "src": src, "ledger": ledger, "all_listing": listing, "doc": doc,
         "readme": rd(os.path.join(repo, "Research/README.md")), "wq": rd(os.path.join(repo, "Research/WORK_QUEUE.md"))}
    return F

def run(cycle_dir, it, outdir=None):
    F = load(cycle_dir); cfg = F["cfg"]; P = F["P"]
    icfg = cfg["iterations"][str(it)]
    out = outdir or os.path.join(cycle_dir, f"iter-{it}")
    data = os.path.join(out, "data"); os.makedirs(data, exist_ok=True)
    m = {"variant": icfg}
    # 1 ledger: every ledger and listing file present and blob SHA equal
    bad = [r["path"] for r in F["ledger"] + F["all_listing"]
           if not os.path.exists(os.path.join(F["src"], r["path"])) or blob_sha(os.path.join(F["src"], r["path"])) != r["blob_sha"]]
    m["ledger_files"] = len(F["ledger"]); m["listing_files"] = len(F["all_listing"])
    m["ledger_mismatches"] = sorted(set(bad))
    lp = [r["path"] for r in F["ledger"]]
    m["ledger_not_in_listing"] = sorted(set(lp) - {r["path"] for r in F["all_listing"]})
    # 2 schemes: judged terms equal extracted terms
    schemes = csvrows(P(cfg["judgments"]["schemes"]))
    srows, smis, terms = [], [], {}
    for s in schemes:
        judged = s["terms"].split("|")
        got = EXTRACTORS[s["extractor"]](F)
        ok = got == judged
        if not ok: smis.append(f"{s['scheme_id']}: extracted {got}")
        terms[s["scheme_id"]] = judged
        srows.append([s["scheme_id"], s["repo"], len(judged), "|".join(got), "yes" if ok else "no"])
    wcsv(os.path.join(data, "schemes_extracted.csv"), ["scheme_id", "repo", "n_terms", "extracted", "matches_judged"], srows)
    m["scheme_extraction_mismatches"] = smis
    m["scheme_sizes"] = {k: len(v) for k, v in terms.items()}
    m["owner_phase_level_pattern"] = ex_wq_b_levels(F)
    # 3 crosswalk
    xw = csvrows(P(cfg["judgments"]["crosswalk"]))
    problems, covered = [], set()
    for i, r in enumerate(xw, 2):
        if r["from_scheme"] not in terms or r["to_scheme"] not in terms:
            problems.append(f"crosswalk line {i}: unknown scheme"); continue
        if r["from_term"] not in terms[r["from_scheme"]]:
            problems.append(f"crosswalk line {i}: unknown from_term {r['from_term']}")
        if r["to_term"] != "(none)" and r["to_term"] not in terms[r["to_scheme"]]:
            problems.append(f"crosswalk line {i}: unknown to_term {r['to_term']}")
        if r["relation"] not in RELATIONS: problems.append(f"crosswalk line {i}: relation {r['relation']}")
        if (r["to_term"] == "(none)") != (r["relation"] in ("no-counterpart", "different-kind")):
            problems.append(f"crosswalk line {i}: (none) only with no-counterpart/different-kind")
        if r["label"] not in LABELS: problems.append(f"crosswalk line {i}: label {r['label']}")
        if not r["basis"].strip(): problems.append(f"crosswalk line {i}: empty basis")
        covered.add((r["from_scheme"], r["from_term"]))
        if r["to_term"] != "(none)": covered.add((r["to_scheme"], r["to_term"]))
    unm = sorted(f"{s}:{t}" for s, ts in terms.items() for t in ts if (s, t) not in covered)
    m["crosswalk_rows"] = len(xw); m["crosswalk_unmapped_terms"] = unm
    rel = {}
    for r in xw: rel[r["relation"]] = rel.get(r["relation"], 0) + 1
    m["relation_counts"] = dict(sorted(rel.items()))
    # 4 conflicts and options
    cf = csvrows(P(cfg["judgments"]["conflicts"])); op = csvrows(P(cfg["judgments"]["options"]))
    for i, r in enumerate(cf, 2):
        if r["label"] not in LABELS: problems.append(f"conflicts line {i}: label {r['label']}")
        if r["verdict"] not in ("confirmed", "refined", "corrected"): problems.append(f"conflicts line {i}: verdict")
    ov = []
    for c in cf:
        mine = [o for o in op if o["conflict_id"] == c["conflict_id"]]
        if len(mine) < icfg.get("min_options", 2): ov.append(f"{c['conflict_id']}: fewer than {icfg.get('min_options', 2)} options")
        if not any(o["type"] == "defer" for o in mine): ov.append(f"{c['conflict_id']}: no defer option")
    for i, o in enumerate(op, 2):
        if o["decision"] != "open (Kyle)": ov.append(f"options line {i}: decision must be 'open (Kyle)'")
        if o["type"] not in OPTION_TYPES: ov.append(f"options line {i}: type {o['type']}")
        if o["label"] not in LABELS: problems.append(f"options line {i}: label {o['label']}")
        if o["reversible"] not in ("yes", "no", "partly"): ov.append(f"options line {i}: reversible")
        if o["conflict_id"] not in {c["conflict_id"] for c in cf}: ov.append(f"options line {i}: unknown conflict")
    m["conflicts"] = len(cf); m["options"] = len(op); m["options_violations"] = ov
    # the six conflict bullets in the Work Queue
    wqn = section(F["wq"], "### Conflicts recorded for the crosswalk", "### Held:")
    m["wq_conflict_bullets"] = len(re.findall(r"^- \*\*", wqn, re.M))
    # 5 phase census
    pc = phase_census(F)
    wcsv(os.path.join(data, "phase_census.csv"), ["report", "level", "track", "dimension", "self_phase", "self_label_matches_filename"], pc["rows"])
    wcsv(os.path.join(data, "phase_next_mislabels.csv"), ["report", "phase", "stated_track", "self_labelled_track"], pc["mislabels"])
    m["phase_numbers"] = sorted(pc["self"]); m["phase_max"] = max(pc["self"])
    m["phase_tracks"] = {str(k): v for k, v in sorted(pc["self"].items())}
    m["phase_self_label_missing"] = sorted(r[0] for r in pc["rows"] if r[4] == "")
    m["phase_self_label_wrong"] = sorted(r[0] for r in pc["rows"] if r[4] != "" and r[5] == "no")
    m["phase_next_statements"] = len(pc["next"]); m["phase_next_mislabels"] = len(pc["mislabels"])
    # 6 tablets
    tc = tablet_census(F)
    wcsv(os.path.join(data, "tablet_census.csv"), ["tablet", "header_status", "draft_notice_in_body", "says_not_in_INDEX",
         "verse_seal_dates", "original_sealed_note", "INDEX_status", "MATRIX_COMBINED_status"], tc["rows"])
    m["tablet_files"] = len(tc["rows"]); m["index_rows"] = tc["index_rows"]
    m["tablet_header_classes"] = dict(sorted({c: sum(1 for r in tc["rows"] if r[1] == c) for c in {r[1] for r in tc["rows"]}}.items()))
    m["tablet_discrepancies"] = {k: v for k, v in tc["D"].items()}
    m["index_flagged_discrepancies"] = len(tc["D"]["D1"])
    m["tablet_discrepancy_types_found"] = sum(1 for v in tc["D"].values() if v)
    # 6b x3 additions (behind config key, so earlier records are unchanged)
    if cfg.get("x3_census"):
        F["listing_tablets"] = [r for r in F["all_listing"] if r["path"].startswith("Tablets/")]
        t3 = tablet_census_x3(F)
        wcsv(os.path.join(data, "tablet_stages.csv"), ["tablet", "governing_stage"], t3["stages"])
        m["tablet_governing_stages"] = dict(sorted({st: sum(1 for _, x in t3["stages"] if x == st) for _, st in t3["stages"]}.items()))
        m["stage_sequences"] = {" > ".join(k): sorted(v) for k, v in sorted(t3["sequences"].items())}
        m["stage_sequence_variants"] = len(t3["sequences"])
        m["dangling_baseline_refs"] = sorted(t3["dangling"])
        m["tablets_awaiting_phase2"] = len(t3["phase2"])
        m["tablet_count_claims"] = t3["claims"]
        m["tablet_set_size_claims"] = sorted({v for k, v in (x.split("=") for x in t3["claims"]) if k in cfg["x3_census"]["set_size_keys"]}, key=str)
        # sensitivity: same-sense rows that survive a strict rule (label Established only)
        ss = [r for r in xw if r["relation"] == "same-name-same-sense"]
        m["same_sense_rows"] = len(ss)
        m["same_sense_rows_strict"] = sum(1 for r in ss if r["label"] == "Established")
        if icfg.get("rule") == "strict":
            keep = [r for r in xw if r["relation"] != "same-name-same-sense" or r["label"] == "Established"]
            cov = set()
            for r in keep:
                cov.add((r["from_scheme"], r["from_term"]))
                if r["to_term"] != "(none)": cov.add((r["to_scheme"], r["to_term"]))
            m["strict_unmapped_terms"] = sorted(f"{a}:{t}" for a, ts in terms.items() for t in ts if (a, t) not in cov)
    # 7 vocabulary census across the whole listed corpus
    vc = vocab_census(F, cfg["vocab_patterns"])
    wcsv(os.path.join(data, "vocab_census.csv"), ["key", "regex", "files", "of"], vc)
    m["vocab"] = {r[0]: r[2] for r in vc}
    # 8 Foundation ladders
    a, b = ex_readme_s2(F), ex_wq_c(F)
    na_ = [x.replace(" Power", "") for x in a]
    m["foundation_ladder_symdiff"] = sorted(set(na_) ^ set(b))
    m["problems"] = problems
    # 9 boundary: own folder vs suite and vs GAIA-Documentation mirror (current cycle outputs included via data dir)
    W = cfg["boundary_window"]
    here = os.path.abspath(cycle_dir)
    bs = pc4.boundary_scan(cfg["suite_path"], ROOT, W, exclude=(os.path.relpath(here, ROOT) + os.sep,))
    bs += [f"iter-{it}/data/{h}" for h in pc4.boundary_scan(cfg["suite_path"], data, W)]
    bd = gd_boundary(F, ROOT, W, exclude=(os.path.relpath(here, ROOT) + os.sep, "ledger" + os.sep))
    bd += [f"iter-{it}/data/{h}" for h in gd_boundary(F, data, W)]
    m["boundary_suite"] = sorted(bs); m["boundary_gaiadoc"] = sorted(bd)
    m["boundary_overlaps"] = len(bs) + len(bd)
    # checks
    checks = []
    for c in cfg["checks"]:
        if "iters" in c and it not in c["iters"]:
            continue
        v = m[c["metric"]]
        v = len(v) if isinstance(v, (list, dict)) else v
        res = {"eq": v == c["threshold"], "ge": v >= c["threshold"], "le": v <= c["threshold"]}[c["op"]]
        checks.append({"id": c["id"], "hypothesis": c["hypothesis"], "metric": c["metric"], "value": v,
                       "op": c["op"], "threshold": c["threshold"], "result": "PASS" if res else "FAIL"})
    inputs = {k: hashlib.sha256(open(P(v), "rb").read()).hexdigest() for k, v in sorted(cfg["judgments"].items())}
    inputs["ledger"] = hashlib.sha256(open(P(cfg["ledger"]), "rb").read()).hexdigest()
    inputs["listing"] = hashlib.sha256(open(P(cfg["listing"]), "rb").read()).hexdigest()
    inputs["foundation_readme_blob"] = blob_sha(os.path.join(F["repo"], "Research/README.md"))
    inputs["work_queue_blob"] = blob_sha(os.path.join(F["repo"], "Research/WORK_QUEUE.md"))
    datah = {fn: hashlib.sha256(open(os.path.join(data, fn), "rb").read()).hexdigest() for fn in sorted(os.listdir(data))}
    rec = {"report": "N-A Level-Name Crosswalk", "cycle": cfg["cycle"], "iteration": it, "variant": icfg,
           "inputs": inputs, "outputs": datah, "metrics": m, "checks": checks,
           "gaia_documentation": "read-only; verified mirror; nothing written"}
    json.dump(rec, open(os.path.join(out, "EXECUTION_RECORD.json"), "w"), indent=1, ensure_ascii=False, sort_keys=True)
    return rec

def verify(cycle_dir):
    cfg = json.load(open(os.path.join(cycle_dir, "config.json")))
    res = []
    for it in sorted(cfg["iterations"], key=int):
        tmp = tempfile.mkdtemp()
        try:
            rec = run(cycle_dir, int(it), outdir=tmp)
            orig = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json")))
            same = json.loads(json.dumps(rec, ensure_ascii=False, sort_keys=True)) == orig
            res.append((int(it), same))
        finally:
            shutil.rmtree(tmp)
    return res

def render(cycle_dir, it):
    rec = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json")))
    m = rec["metrics"]
    L = [f"_Generated by `tools/na.py render` from iter-{it}._\n", "### Pre-registered checks\n",
         "| ID | Hypothesis | Value | Test | Result |", "|---|---|---|---|---|"]
    for c in rec["checks"]:
        L.append(f"| {c['id']} | {c['hypothesis']} | {c['value']} | {c['op']} {c['threshold']} | **{c['result']}** |")
    L.append("\n### Scheme sizes\n\n| Scheme | Terms |\n|---|---|")
    L += [f"| {k} | {v} |" for k, v in m["scheme_sizes"].items()]
    L.append(f"\n### Crosswalk relations ({m['crosswalk_rows']} rows)\n\n| Relation | Rows |\n|---|---|")
    L += [f"| {k} | {v} |" for k, v in m["relation_counts"].items()]
    L.append("\n### GAIA-Documentation phase numbering (self-labels in the 32 reports)\n\n| Phase | Track |\n|---|---|")
    L += [f"| {k} | {v} |" for k, v in m["phase_tracks"].items()]
    L.append(f"\nNext-phase statements: {m['phase_next_statements']}; mislabelled: {m['phase_next_mislabels']} (see `phase_next_mislabels.csv`).")
    L.append("\n### Tablet discrepancy types\n\n| Type | Count | Items |\n|---|---|---|")
    for k, v in m["tablet_discrepancies"].items():
        L.append(f"| {k} | {len(v)} | {', '.join(v)} |")
    L.append(f"\n### Vocabulary census ({rec['metrics']['listing_files']} listed files)\n\n| Key | Files |\n|---|---|")
    L += [f"| {k} | {v} |" for k, v in m["vocab"].items()]
    L.append(f"\nFoundation ladder difference (README §2 vs Work Queue §C): {', '.join(m['foundation_ladder_symdiff']) or 'none'}.")
    return "\n".join(L) + "\n"

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("run"); c.add_argument("--cycle", required=True); c.add_argument("--iter", type=int, required=True)
    c = sp.add_parser("verify"); c.add_argument("--cycle", required=True)
    c = sp.add_parser("render"); c.add_argument("--cycle", required=True); c.add_argument("--iter", type=int, required=True)
    a = ap.parse_args()
    if a.cmd == "run":
        r = run(a.cycle, a.iter); print(" ".join(f"{c['id']}={c['result']}" for c in r["checks"]))
    elif a.cmd == "verify":
        for it, ok in verify(a.cycle): print(f"iter-{it} identical={ok}")
    else:
        sys.stdout.write(render(a.cycle, a.iter))
