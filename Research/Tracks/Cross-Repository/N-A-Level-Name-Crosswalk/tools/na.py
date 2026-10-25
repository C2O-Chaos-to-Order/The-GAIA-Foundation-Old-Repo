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

STAGE_WORDS_V2 = r"\b(Nigredo|Albedo|Citrinitas|Rubedo|Celestial|Ember|Cauda Pavonis)\b"
SEQ_MARK_V2 = re.compile(r"(sequence[^:\n]*:|Derivation:|^\s*Nigredo(?: \([A-Za-z]+\))?(?:,| to | →))")

def _seqs_v2(text):
    """v2 (x6): candidate segments are (a) arrow chains bounded by ':' or '.', (b) the first sentence
    after a sequence marker; stage words kept in order; a segment needs >= 3 stage words."""
    out = []
    for line in text.replace("**", "").splitlines():
        segs = re.findall(r"[^.:\u2192]*(?:\u2192[^.\u2192]*)+", line)
        m = SEQ_MARK_V2.search(line)
        if m:
            segs.append(re.split(r"(?<=[a-z\)])\. ", line[m.start():], maxsplit=1)[0])
        for seg in segs:
            seq = re.findall(STAGE_WORDS_V2, seg)
            if len(seq) >= 3 and seq not in out:
                out.append(seq)
    return out

def _stage_sequences_v2(F):
    out = {}
    for r in F["ledger"]:
        if r["path"].endswith("_TABLET.md"):
            for seq in _seqs_v2(F["doc"](r["path"])):
                out.setdefault(tuple(seq), []).append(os.path.basename(r["path"]).split("_")[0].title())
    return out

def ex_stage_albedo(F):
    return _seqs_v2(F["doc"]("Tablets/ALBEDO_TABLET.md"))[0]

def ex_stage_citrine(F):
    return _seqs_v2(F["doc"]("Tablets/CITRINE_TABLET.md"))[0]

def ex_stage_ruby_arc(F):
    return [s for s in _seqs_v2(F["doc"]("Tablets/RUBY_TABLET.md")) if "Ember" in s][0]

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

def stage_census_v2(F):
    rows = []
    for r in sorted(F["listing_tablets"], key=lambda r: r["path"]):
        if not r["path"].endswith("_TABLET.md"):
            continue
        t = F["doc"](r["path"]).replace("**", "")
        m = re.search(r"^Governing Stage:? ([^\n]+)|^\| (?:Governing )?Stage \| ([^|]+) \|", t, re.M)
        st = (m.group(1) or m.group(2)).strip() if m else ""
        rows.append([os.path.basename(r["path"]).split("_")[0].title(), st])
    return rows

ORD = {"First": 1, "Second": 2, "Third": 3, "Fourth": 4, "Fifth": 5, "Sixth": 6, "Seventh": 7}

def position_claims(F):
    zero, laws = set(), []
    for r in sorted(F["listing_tablets"], key=lambda r: r["path"]):
        if not r["path"].endswith("_TABLET.md"):
            continue
        name = os.path.basename(r["path"]).split("_")[0].title(); t = F["doc"](r["path"])
        if re.search(r"Tablet 0\b|Zeroth Tablet", t):
            zero.add(name)
        for mm in re.finditer(r"\b(\w+),? (?:is )?position 0\b", t):
            if mm.group(1).istitle() and mm.group(1) not in ("Position",):
                zero.add(mm.group(1))
        mm = re.search(r"^## The (\w+) Hermetic Law of GAIA|^\*The (\w+) Hermetic Law of GAIA\*", t, re.M)
        if mm:
            laws.append([name, ORD.get(mm.group(1) or mm.group(2), mm.group(1) or mm.group(2))])
    return sorted(zero), laws

def phase_senses(F, rows):
    t = F["doc"]("Tablets/MATRIX-COMBINED.md")
    line = [l for l in t.splitlines() if l.startswith("- **Phase**")][0]
    gl = {m.group(1): m.group(2) for m in re.finditer(r"(\w+) is ([a-z ]+)\.", line)}
    bad = []
    for r in rows:
        want = None if r["tablets_gloss"] == "(none)" else r["tablets_gloss"]
        if gl.get(r["phase"]) != want:
            bad.append(f"{r['phase']}: tablets gloss {gl.get(r['phase'])!r}")
        fp = os.path.join(F["repo"], r["foundation_file"])
        if not os.path.exists(fp) or r["foundation_anchor"] not in rd(fp):
            bad.append(f"{r['phase']}: foundation anchor not found")
        if r["relation"] not in RELATIONS or r["label"] not in LABELS:
            bad.append(f"{r['phase']}: relation/label")
    return gl, bad

def meta_census(F, cfgm):
    rx_r, rx_m = re.compile(cfgm["reflexive"], re.I), re.compile(cfgm["metaphysical"], re.I)
    tot = {"reflexive_files": 0, "metaphysical_files": 0}
    rep = {"reflexive": 0, "metaphysical": 0}; by = {}
    for r in F["all_listing"]:
        t = F["doc"](r["path"])
        a, b = len(rx_r.findall(t)), len(rx_m.findall(t))
        tot["reflexive_files"] += a > 0; tot["metaphysical_files"] += b > 0
        mm = re.match(re.escape(G) + r"(\w+)-(Human|AI)-\w+ Research Report\.md$", r["path"])
        if mm:
            by.setdefault(mm.group(1), [0, 0]); by[mm.group(1)][0] += a; by[mm.group(1)][1] += b
            if mm.group(1) == "Meta":
                rep["reflexive"] += a; rep["metaphysical"] += b
    return tot, rep, dict(sorted(by.items()))

VERDICTS = {"survives", "survives-qualified", "weakened", "superseded"}

def _foundation_files(F, exts):
    here = os.path.relpath(ROOT, F["repo"]) + os.sep
    out = []
    for d, dirs, fs in os.walk(F["repo"]):
        dirs[:] = sorted(x for x in dirs if x != ".git" and x != "__pycache__")
        for f in sorted(fs):
            rp = os.path.relpath(os.path.join(d, f), F["repo"])
            if rp.startswith(here) or not any(rp.endswith(e) for e in exts):
                continue
            out.append(rp)
    return out

def repro_dependents(F, target):
    """config.json / *.py files under Research/ that name the target (they read or hash it)."""
    needle = target if os.path.basename(target) == "README.md" else os.path.basename(target)
    deps = []
    for d, dirs, fs in os.walk(os.path.join(F["repo"], "Research")):
        dirs[:] = sorted(x for x in dirs if x not in (".git", "__pycache__"))
        for f in sorted(fs):
            if f == "config.json" or f.endswith(".py"):
                fp = os.path.join(d, f)
                if needle in rd(fp):
                    deps.append(os.path.relpath(fp, F["repo"]))
    return deps

def option_review(F, rev, op, rule):
    md = _foundation_files(F, (".md",))
    texts = {}
    def T(p):
        if p not in texts: texts[p] = rd(os.path.join(F["repo"], p))
        return texts[p]
    rows, probs, deps_cache = [], [], {}
    ids_o = {o["option_id"] for o in op}; ids_r = [r["option_id"] for r in rev]
    mism = sorted((ids_o ^ set(ids_r)) | {i for i in ids_r if ids_r.count(i) > 1})
    for r in rev:
        if r["verdict"] not in VERDICTS: probs.append(f"{r['option_id']}: verdict")
        if r["objection_label"] not in LABELS: probs.append(f"{r['option_id']}: label")
        if not r["objection"].strip(): probs.append(f"{r['option_id']}: empty objection")
        if (r["verdict"] == "superseded") != bool(r["superseded_by"].strip()): probs.append(f"{r['option_id']}: superseded_by")
        if r["superseded_by"].strip() and r["superseded_by"] not in ids_o: probs.append(f"{r['option_id']}: unknown superseded_by")
        tg = [t for t in r["ripple_targets"].split(";") if t and t != "(none)"]
        for t in tg:
            if not os.path.exists(os.path.join(F["repo"], t)): probs.append(f"{r['option_id']}: target {t} missing")
            if t not in deps_cache: deps_cache[t] = repro_dependents(F, t)
        dep = sorted({x for t in tg for x in deps_cache[t]})
        rx = re.compile(r["ripple_regex"]) if r["ripple_regex"] else None
        hits = [p for p in md if rx.search(T(p))] if rx else []
        rows.append([r["option_id"], r["verdict"], ";".join(tg) or "(none)", len(dep), len(hits)])
    typ = {o["option_id"]: (o["conflict_id"], o["type"]) for o in op}
    ok = {"survives"} | ({"survives-qualified"} if rule != "adversarial" else set())
    conf = sorted({c for c, _ in typ.values()})
    surv = {c: [r["option_id"] for r in rev if r["option_id"] in typ and typ[r["option_id"]][0] == c
                and typ[r["option_id"]][1] != "defer" and r["verdict"] in ok] for c in conf}
    af = sorted(r[0] for r in rows if typ.get(r[0], ("", ""))[1] == "align-foundation" and r[3] > 0)
    return rows, probs, mism, surv, af, deps_cache

def evidence_check(F, cf, xw, m, jdir):
    ids = {r["row_id"] for r in xw}; bad = []
    for c in cf:
        for part in [x.strip() for x in c["evidence"].split(";")]:
            part = re.sub(r"^(x\d+ )?metrics? ", "", part)
            for tok in [t.strip() for t in part.split(",")]:
                for x in re.findall(r"\bX\d+\b", tok):
                    if x not in ids: bad.append(f"{c['conflict_id']}: {x}")
                if re.fullmatch(r"[a-z][a-z0-9_]*(\.[a-z0-9_]+)?", tok):
                    k, _, sub = tok.partition(".")
                    if k not in m or (sub and (not isinstance(m[k], dict) or sub not in m[k])):
                        bad.append(f"{c['conflict_id']}: metric {tok}")
                if tok.endswith(".csv") and not os.path.exists(os.path.join(jdir, tok)):
                    bad.append(f"{c['conflict_id']}: file {tok}")
    return bad

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
    # 6c x6 additions (behind config key)
    if cfg.get("x6"):
        x6 = cfg["x6"]
        F.setdefault("listing_tablets", [r for r in F["all_listing"] if r["path"].startswith("Tablets/")])
        seqs = _stage_sequences_v2(F)
        m["stage_sequences_v2"] = {" > ".join(k): sorted(v) for k, v in sorted(seqs.items())}
        m["stage_sequence_variants_v2"] = len(seqs)
        sc = stage_census_v2(F)
        wcsv(os.path.join(data, "tablet_stages_v2.csv"), ["tablet", "governing_stage"], sc)
        m["stage_none_stated_v2"] = sorted(n for n, st in sc if not st)
        z, laws = position_claims(F)
        m["position0_claimants"] = z; m["hermetic_law_numbers"] = laws
        nums = [n for _, n in laws if isinstance(n, int)]
        m["hermetic_law_gaps"] = [k for k in range(1, max(nums) + 1) if k not in nums] if nums else []
        ps = csvrows(P(x6["phase_senses"]))
        gl, bad = phase_senses(F, ps)
        m["tablets_phase_glosses"] = dict(sorted(gl.items()))
        m["phase_sense_mismatches"] = bad
        m["phase_sense_relations"] = {r["phase"]: r["relation"] for r in ps}
        tot, rep, by = meta_census(F, x6["meta_patterns"])
        m["meta_sense_files"] = tot; m["meta_reports_counts"] = rep; m["meta_counts_by_report_level"] = by
        m["meta_reports_reflexive_minus_metaphysical"] = rep["reflexive"] - rep["metaphysical"]
    # 6d x9 additions (behind config key)
    if cfg.get("x9"):
        x9 = cfg["x9"]
        rev = csvrows(P(x9["option_review"]))
        rows, probs, mism, surv, af, deps = option_review(F, rev, op, icfg.get("rule"))
        wcsv(os.path.join(data, "option_ripple.csv"), ["option_id", "verdict", "targets", "repro_dependents", "foundation_md_files_matching"], rows)
        m["review_mismatches"] = mism; m["review_problems"] = probs
        m["review_verdicts"] = dict(sorted({v: sum(1 for r in rev if r["verdict"] == v) for v in {r["verdict"] for r in rev}}.items()))
        m["surviving_options_by_conflict"] = surv
        m["conflicts_without_surviving_option"] = sorted(c for c, v in surv.items() if not v)
        m["align_foundation_with_repro_dependents"] = af
        m["repro_dependents"] = {t: v for t, v in sorted(deps.items())}
        mm = re.search(r"The (\d+) tablet files", F["wq"])
        n_tab = sum(1 for r in F["all_listing"] if r["path"].endswith("_TABLET.md"))
        m["wq_tablet_files_claim"] = int(mm.group(1)) if mm else None
        m["listing_tablet_files"] = n_tab
        m["wq_tablet_files_claim_diff"] = abs((m["wq_tablet_files_claim"] or 0) - n_tab)
    # 7 vocabulary census across the whole listed corpus
    vc = vocab_census(F, cfg["vocab_patterns"])
    wcsv(os.path.join(data, "vocab_census.csv"), ["key", "regex", "files", "of"], vc)
    m["vocab"] = {r[0]: r[2] for r in vc}
    # 8 Foundation ladders
    a, b = ex_readme_s2(F), ex_wq_c(F)
    na_ = [x.replace(" Power", "") for x in a]
    m["foundation_ladder_symdiff"] = sorted(set(na_) ^ set(b))
    m["problems"] = problems
    if cfg.get("x9"):
        m["evidence_dangling"] = evidence_check(F, cf, xw, m, os.path.dirname(P(cfg["judgments"]["conflicts"])))
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
    if cfg.get("x9"):
        inputs["option_review"] = hashlib.sha256(open(P(cfg["x9"]["option_review"]), "rb").read()).hexdigest()
    if cfg.get("x6"):
        inputs["phase_senses"] = hashlib.sha256(open(P(cfg["x6"]["phase_senses"]), "rb").read()).hexdigest()
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
    if "tablet_governing_stages" in m:
        L.append("\n### x3 tablet census\n\n| Governing stage (header) | Tablets |\n|---|---|")
        L += [f"| {k or '(none stated)'} | {v} |" for k, v in m["tablet_governing_stages"].items()]
        L.append("\n| Stated stage sequence (as extracted) | Tablets |\n|---|---|")
        L += [f"| {k} | {', '.join(v)} |" for k, v in m["stage_sequences"].items()]
        L.append("\n| Count claim | Files |\n|---|---|")
        L += [f"| {k} | {', '.join(v)} |" for k, v in m["tablet_count_claims"].items()]
        L.append(f"\nUnresolved 'Baseline preserved' references: {len(m['dangling_baseline_refs'])}. Tablets ending 'proceed to Phase 2': {m['tablets_awaiting_phase2']}. Same-sense rows: {m['same_sense_rows']}, of which Established: {m['same_sense_rows_strict']}.")
        if "strict_unmapped_terms" in m:
            L.append(f"\nStrict rule: {len(m['strict_unmapped_terms'])} terms lose their only row: " + ", ".join(m["strict_unmapped_terms"]) + ".")
    if "stage_sequences_v2" in m:
        L.append("\n### x6 tablet census\n\n| Stated stage sequence (v2 extractor) | Tablets |\n|---|---|")
        L += [f"| {k} | {', '.join(v)} |" for k, v in m["stage_sequences_v2"].items()]
        L.append(f"\nTablets with no governing stage found by the v2 census: {', '.join(m['stage_none_stated_v2']) or 'none'} (per-tablet values in `tablet_stages_v2.csv`).")
        L.append(f"\nPosition-0 claimants: {', '.join(m['position0_claimants'])}. Hermetic Law numbers: " + ", ".join(f"{a} {b}" for a, b in m["hermetic_law_numbers"]) + f"; gaps: {m['hermetic_law_gaps'] or 'none'}.")
        L.append("\n| Phase | Tablets gloss | Relation to Foundation sense |\n|---|---|---|")
        L += [f"| {k} | {m['tablets_phase_glosses'].get(k, '(none)')} | {v} |" for k, v in m["phase_sense_relations"].items()]
        L.append(f"\nPhase-sense mismatches: {len(m['phase_sense_mismatches'])}.")
        L.append("\n| Report level | Reflexive meta- markers | Metaphysic- terms |\n|---|---|---|")
        L += [f"| {k} | {a} | {b} |" for k, (a, b) in m["meta_counts_by_report_level"].items()]
        L.append(f"\nFiles with any reflexive marker: {m['meta_sense_files']['reflexive_files']}; with any metaphysic- term: {m['meta_sense_files']['metaphysical_files']}.")
    if "review_verdicts" in m:
        L.append("\n### x9 option review\n\n| Verdict | Options |\n|---|---|")
        L += [f"| {k} | {v} |" for k, v in m["review_verdicts"].items()]
        L.append("\n| Conflict | Surviving non-defer options (this rule) |\n|---|---|")
        L += [f"| {k} | {', '.join(v) or '(none)'} |" for k, v in m["surviving_options_by_conflict"].items()]
        L.append("\n| Foundation file an option would edit | Config or tool files that name it |\n|---|---|")
        L += [f"| {k} | {len(v)}: {', '.join(v)} |" for k, v in m["repro_dependents"].items()]
        L.append(f"\nalign-foundation options whose targets are named by other records' configs or tools: {', '.join(m['align_foundation_with_repro_dependents']) or 'none'}. Per-option ripple in `option_ripple.csv`.")
        L.append(f"\nWork Queue tablet-file claim: {m['wq_tablet_files_claim']}; tablet files in the listing: {m['listing_tablet_files']}. Dangling conflict evidence citations: {', '.join(m['evidence_dangling']) or 'none'}.")
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
