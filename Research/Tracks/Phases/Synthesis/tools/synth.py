"""Six-phase SYNTHESIS aggregation, rendering and citation checks (see ../SPEC.md).
Usage (from Research/Tracks/Phases/Synthesis): python3 tools/synth.py aggregate|render|check [--base <git-ref>]
Deterministic; reads only files already in the repository."""
import csv, glob, hashlib, json, os, re, subprocess, sys, datetime, collections, platform

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../Phases/Synthesis
PH = os.path.dirname(HERE)                                            # .../Tracks/Phases
RES = os.path.dirname(os.path.dirname(PH))                            # .../Research
PHASES = [("DV", "Divergence"), ("IN", "Insurgence"), ("AL", "Allegiance"),
          ("CV", "Convergence"), ("AS", "Ascendence"), ("TR", "Transcendence")]
CYC = [("0", "Cycle-0-Baseline"), ("A", "Cycle-A-x3"), ("B", "Cycle-B-x6"), ("C", "Cycle-C-x9"), ("D", "Cycle-D-x12")]
FIELDS = [("NAT", "Natural-Sciences"), ("FOR", "Formal-Sciences"), ("SOC", "Social-Sciences"),
          ("APP", "Applied-Sciences"), ("HUM", "Humanities"), ("PHI", "Philosophy-Spirituality")]
LAB = {"Established": "E", "Plausible": "P", "Philosophical/Spiritual": "PS", "Hypothetical": "H"}
MAPS = glob.glob(os.path.join(RES, "Maps-and-Matrix", "v38-*"))[0]
D = os.path.join(HERE, "data")

def rcsv(p): return list(csv.DictReader(open(p, encoding="utf-8")))
def wcsv(p, rows, cols):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n"); w.writeheader(); [w.writerow(r) for r in rows]
def cdir(ph, l): return os.path.join(PH, dict(PHASES)[ph], dict(CYC)[l])
def ledger(ph, l):
    out = {}
    for fc, fd in FIELDS:
        for r in rcsv(os.path.join(cdir(ph, l), fd, "claims", "claims.csv")): out[r["claim_id"]] = r
    return out
def all_ledgers():
    return {ph + l: ledger(ph, l) for ph, _ in PHASES for l, _ in CYC}
def links():
    out = {}
    for ph, n in PHASES:
        for l, _ in CYC:
            for r in rcsv(os.path.join(cdir(ph, l), "Links", "link_register.csv")): out.setdefault(r["link_id"], r)
    return out
def sources():
    out = {}
    for ph, n in PHASES:
        for l, _ in CYC:
            for r in rcsv(os.path.join(cdir(ph, l), "Provenance", "SOURCE_REGISTER.csv")): out.setdefault(r["source_id"], r)
    return out
PID = re.compile(r"\bP\d{2,3}\b")

def passes(ph, l, fd):
    t = open(os.path.join(cdir(ph, l), fd, "research", "PASSES.md"), encoding="utf-8").read()
    blocks = re.split(r"\n## Pass \d+\n", t)[1:]
    nothing = sum(1 for b in blocks if "**Added:** Added nothing" in b)
    noread = sum(1 for b in blocks if re.search(r"\*\*Read:\*\* nothing new", b))
    return len(blocks), nothing, noread

def aggregate():
    os.makedirs(D, exist_ok=True)
    L = all_ledgers(); S = sources()
    rows = []; nrec = collections.Counter(); badrec = 0
    for ph, pn in PHASES:
        for l, cn in CYC:
            led = L[ph + l]; lab = collections.Counter(LAB[r["framework_label"]] for r in led.values())
            runs = vp = vt = hs = hn = ho = 0
            for rec in glob.glob(os.path.join(cdir(ph, l), "*", "simulation", "iter-*", "EXECUTION_RECORD.json")):
                d = json.load(open(rec)); runs += 1; nrec[ph] += 1
                if "status" not in d or "pre_registered_checks" not in d: badrec += 1
                for c in d.get("pre_registered_checks", []):
                    if c["kind"] == "validation": vt += 1; vp += c["result"] == "Pass"
                    elif c["kind"] == "hypothesis":
                        hs += c["result"] == "Supported"; hn += c["result"] == "Not supported"
                        ho += c["result"] not in ("Supported", "Not supported")
            np_ = nn = nr = 0
            for fc, fd in FIELDS:
                a, b, c = passes(ph, l, fd); np_ += a; nn += b; nr += c
            new = sorted((s for s, r in S.items() if r["cycle_added"] == ph + l), key=lambda x: int(x[1:]))
            rows.append(dict(phase=pn, cycle=ph + l, claims=len(led), E=lab["E"], P=lab["P"], PS=lab["PS"], H=lab["H"],
                             runs=runs, val_pass=vp, val_total=vt, hyp_supported=hs, hyp_not_supported=hn, hyp_other=ho,
                             passes=np_, passes_added_nothing=nn, passes_read_nothing_new=nr,
                             new_sources=len(new), new_source_ids=";".join(new)))
    wcsv(os.path.join(D, "cycle_totals.csv"), rows, list(rows[0]))
    # field footprint in x12 ledgers
    fr = []; track = collections.defaultdict(lambda: dict(src=set(), claims=0, sim=0))
    for ph, pn in PHASES:
        led = L[ph + "D"]
        for fc, fd in FIELDS:
            cl = [r for r in led.values() if r["field"] == fc]
            lab = collections.Counter(LAB[r["framework_label"]] for r in cl)
            cls = collections.Counter(r["claim_class"] for r in cl)
            src = set(); one = none = 0
            for r in cl:
                s = set(PID.findall(r["source_ids"])); src |= s
                one += len(s) == 1; none += len(s) == 0
            track[fc]["src"] |= src; track[fc]["claims"] += len(cl); track[fc]["sim"] += cls["Simulation"]
            fr.append(dict(phase=pn, field=fc, claims=len(cl), E=lab["E"], P=lab["P"], PS=lab["PS"], H=lab["H"],
                           simulation_class=cls["Simulation"], distinct_sources=len(src),
                           source_ids=";".join(sorted(src, key=lambda x: int(x[1:]))),
                           claims_one_source=one, claims_no_P_source=none))
    wcsv(os.path.join(D, "field_footprint.csv"), fr, list(fr[0]))
    tr = [dict(field=f, claims=v["claims"], simulation_class=v["sim"], sim_share=f"{v['sim']/v['claims']:.2f}",
               distinct_sources=len(v["src"]), source_ids=";".join(sorted(v["src"], key=lambda x: int(x[1:]))))
          for f, v in track.items()]
    wcsv(os.path.join(D, "field_track.csv"), tr, list(tr[0]))
    # phase-relation links
    K = links(); pl = []
    for k, r in sorted(K.items(), key=lambda x: int(x[0][3:])):
        if r["link_type"] != "phase relation" and k != "PL-05": continue
        cited = re.findall(r"\b(?:DV|IN|AL|CV|AS|TR)[0A-D]-[A-Z]{3}-\d{2}\b", r["basis"])
        labs = [f"{c} {L[c[:3]][c]['framework_label']}" for c in cited]
        pl.append(dict(link_id=k, frm=r["from"], to=r["to"], label=r["framework_label"], cited=";".join(labs),
                       statement=r["statement"]))
    wcsv(os.path.join(D, "phase_links.csv"), pl, list(pl[0]))
    # Maps v38
    mx = os.path.join(MAPS, "matrix")
    pf = rcsv(os.path.join(mx, "phase_x_field_30.csv")) + rcsv(os.path.join(mx, "phase_track_transcendence_x_field_6.csv"))
    plz = rcsv(os.path.join(mx, "phase_x_lens_25.csv")) + rcsv(os.path.join(mx, "phase_track_transcendence_x_lens_5.csv"))
    cp = rcsv(os.path.join(mx, "claim_placement.csv")); ix = rcsv(os.path.join(mx, "intersections_625.csv"))
    c125 = rcsv(os.path.join(mx, "phase_track_transcendence_cells_125.csv"))
    phc = [r for r in cp if r["source_set"].startswith("phase cycle")]
    m = dict(maps_version=os.path.basename(MAPS),
             phase_x_field=[{k: r[k] for k in ("phase", "field", "n_claims", "E", "P", "PS", "H", "flag")} for r in pf],
             phase_x_lens=[{k: r[k] for k in ("phase", "lens", "n_claims", "E", "P", "PS", "H")} for r in plz],
             phase_claims_placed=len(phc),
             phase_claims_on_being_axis=sum(1 for r in phc if not r["being"].startswith("outside")),
             phase_claims_being_ids=[r["claim_id"] + " " + r["being"] for r in phc if not r["being"].startswith("outside")],
             phase_claims_alchemy_assigned=sum(1 for r in phc if not r["alchemy"].startswith("Unassigned")),
             intersections_625=len(ix), intersections_flags=dict(collections.Counter(r["flag"].split(" (")[0] for r in ix)),
             intersections_claims_placed_exactly=sum(int(r["claims_placed_exactly"]) for r in ix),
             intersections_phase_claims_nonzero=sum(1 for r in ix if int(r["phase_claims_in_being_phase_lens_projection"] or 0) > 0),
             transcendence_overlay_cells=len(c125), transcendence_overlay_status=sorted({r["status"] for r in c125}),
             transcendence_overlay_nonzero=sum(1 for r in c125 if int(r["phase_claims_in_being_phase_lens_projection"]) > 0))
    json.dump(m, open(os.path.join(D, "matrix_v38.json"), "w"), indent=1)
    # README section 10 arithmetic
    a, b = (0, 1, 3, 5, 0), (3, 6, 9, 12)
    M = [[ai * bj + 1 for bj in b] for ai in a]
    printed = [[1, 1, 1, 1], [4, 7, 10, 13], [10, 19, 28, 37], [16, 31, 46, 61], [1, 1, 1, 1]]
    A, B, C, Dd = (0, 1, 2, 3, 0), (1, 3, 5, 7, 0), (3, 6, 9, 12, 0), 1
    later = [x * y * z * Dd for x, y, z in zip(A, B, C)]
    ar = dict(M=M, printed=printed, M_equals_printed=M == printed, grid_625=5 ** 4, grid_750=5 * 5 * 6 * 5,
              added_cells=5 * 5 * 6 * 5 - 5 ** 4, later_pattern=later, later_all_zero=all(v == 0 for v in later),
              a_length=len(a), phases_now=len(PHASES))
    json.dump(ar, open(os.path.join(D, "arithmetic.json"), "w"), indent=1)
    vt = dict(nrec=dict(nrec), badrec=badrec)
    json.dump(vt, open(os.path.join(D, "_records.json"), "w"), indent=1)
    print("aggregate done", sum(nrec.values()), "records")
    registry_checks()

def registry_checks():
    """Added after SPEC.md (reporting only, disclosed in EXECUTION_RECORD as R2/R3/R4)."""
    L = all_ledgers(); K = links(); S = sources()
    key = collections.defaultdict(list)
    for s, r in S.items():
        mm = re.search(r"doi:(\S+)", r["citation"]); key[mm.group(1).lower() if mm else r["url"].rstrip("/").lower()].append(s)
    dups = [sorted(v, key=lambda x: int(x[1:])) for v in key.values() if len(v) > 1]
    rank = {"Established": 3, "Plausible": 2, "Hypothetical": 1}
    above = []
    for k, r in sorted(K.items(), key=lambda x: int(x[0][3:])):
        cited = re.findall(r"\b(?:DV|IN|AL|CV|AS|TR)[0A-D]-[A-Z]{3}-\d{2}\b", r["basis"])
        labs = [L[c[:3]][c]["framework_label"] for c in cited if c in L.get(c[:3], {})]
        rk = [rank[x] for x in labs if x in rank]
        if r["framework_label"] in rank and rk and rank[r["framework_label"]] > min(rk):
            above.append(dict(link=k, label=r["framework_label"], basis=[f"{c} {L[c[:3]][c]['framework_label']}" for c in cited]))
    led = {}
    for ph, _ in PHASES:
        for r in L[ph + "D"].values():
            for s in set(PID.findall(r["source_ids"])): led.setdefault(s, set()).add(r["field"])
    tert = collections.Counter(); used = collections.Counter()
    for s, fs in led.items():
        st = S[s]["source_type"].lower()
        for f in fs:
            used[f] += 1
            if "encyclopedia" in st or "tertiary" in st: tert[f] += 1
    unused = sorted((s for s in S if s not in led), key=lambda x: int(x[1:]))
    out = dict(duplicate_registrations=dups, distinct_registered=len(S), distinct_works=len(key),
               links_total=len(K), links_labelled_above_weakest_basis_claim=above,
               x12_sources_per_field=dict(used), x12_encyclopedia_or_tertiary_per_field=dict(tert),
               registered_not_cited_in_any_x12_ledger=unused,
               missing_ids_in_P01_P108=[f"P{i:02d}" for i in range(1, 109) if f"P{i:02d}" not in S])
    json.dump(out, open(os.path.join(D, "registry_checks.json"), "w"), indent=1)
    print(json.dumps(out)[:3000])

def md_table(rows, cols, head=None):
    h = head or cols
    return "\n".join(["| " + " | ".join(h) + " |", "|" + "---|" * len(h)] +
                     ["| " + " | ".join(str(r[c]) for c in cols) + " |" for r in rows])

def render():
    t = open(os.path.join(HERE, "tools", "SYNTHESIS.template.md"), encoding="utf-8").read()
    ct = rcsv(os.path.join(D, "cycle_totals.csv"))
    for r in ct:
        r["val"] = f"{r['val_pass']}/{r['val_total']}"
        r["hyp"] = f"{r['hyp_supported']}/{int(r['hyp_supported'])+int(r['hyp_not_supported'])+int(r['hyp_other'])}"
        r["rate"] = f"{int(r['hyp_supported'])/(int(r['hyp_supported'])+int(r['hyp_not_supported'])+int(r['hyp_other'])):.2f}"
        r["labels"] = f"{r['E']}/{r['P']}/{r['PS']}/{r['H']}"
    ff = rcsv(os.path.join(D, "field_footprint.csv")); ftr = rcsv(os.path.join(D, "field_track.csv"))
    for r in ff: r["labels"] = f"{r['E']}/{r['P']}/{r['PS']}/{r['H']}"
    pl = rcsv(os.path.join(D, "phase_links.csv"))
    for r in pl: r["lbl"] = f"{r['link_id']} [{r['label']}]"; r["cit"] = "; ".join(
        f"{x.split(' ',1)[0]} [{x.split(' ',1)[1]}]" for x in r["cited"].split(";") if x) or "—"
    m = json.load(open(os.path.join(D, "matrix_v38.json")))
    pf = m["phase_x_field"]
    piv = []
    for pn in [p for _, p in PHASES]:
        row = {"phase": pn}
        for fc, fd in FIELDS:
            x = [r for r in pf if r["phase"] == pn and r["field"] == fd][0]
            row[fc] = f"{x['n_claims']} ({x['E']}/{x['P']}/{x['PS']}/{x['H']})" + (" †" if x["flag"].startswith("UNDER") else "")
        piv.append(row)
    lz = []
    for pn in [p for _, p in PHASES]:
        row = {"phase": pn}
        for x in [r for r in m["phase_x_lens"] if r["phase"] == pn]: row[x["lens"]] = x["n_claims"]
        lz.append(row)
    T = {
        "cycle_totals": md_table(ct, ["cycle", "claims", "labels", "runs", "val", "hyp", "rate", "passes_read_nothing_new", "passes_added_nothing", "new_sources"],
                                 ["cycle", "claims", "E/P/PS/H", "runs", "validation", "hyp. supported", "rate", "passes 'Read: nothing new'", "passes 'Added nothing'", "new sources"]),
        "field_footprint": md_table(ff, ["phase", "field", "claims", "labels", "simulation_class", "distinct_sources", "source_ids", "claims_one_source"],
                                    ["phase", "field", "claims", "E/P/PS/H", "Simulation-class", "distinct sources", "sources", "claims citing one source"]),
        "field_track": md_table(ftr, ["field", "claims", "simulation_class", "sim_share", "distinct_sources"],
                                ["field", "x12 claims (6 phases)", "Simulation-class", "share", "distinct sources"]),
        "phase_links": md_table(pl, ["lbl", "frm", "to", "cit"], ["link", "from", "to", "claims cited (ledger label)"]),
        "phase_field": md_table(piv, ["phase"] + [f for f, _ in FIELDS]),
        "phase_lens": md_table(lz, ["phase", "Truth", "Integrity", "Love", "Justice", "Wisdom"]),
    }
    out = re.sub(r"\{\{TABLE:(\w+)\}\}", lambda mm: T[mm.group(1)], t)
    open(os.path.join(PH, "SYNTHESIS.md"), "w", encoding="utf-8").write(out)
    print("rendered", len(out), "chars")

DISCLOSED = [
    "V3 failed as pre-registered: SPEC.md read README section 10's later pattern as A*B*C times D; that gives (0, 18, 90, 252, 0), not the all-zero vector README reports, which follows only from multiplying by E = 0. The SPEC's reading was the agent's; README does not say which scalar is meant. Kept as Fail and reported in SYNTHESIS sections 6 and 8; not re-specified.",
    "Added after SPEC.md and before the first check run: registry_checks() (data/registry_checks.json; reporting item R2). It found two duplicate source registrations (P51/P59, P84/P105) not disclosed in their cycles; registers were not edited (C4).",
    "First check run (before any commit): C2 failed on four link mentions written without a label (PL-51, PL-54, PL-61, PL-73) and C4 was Indeterminate because the check ran outside the git worktree. The labels were added to the text (citation typo, allowed by SPEC) and the checks were re-run in the git worktree against base 3ae9bf57.",
    "The first draft said the later pattern gives the zero vector; corrected to the computed result before the first commit. The Divergence x12 attribution statement in this synthesis was checked against git log (commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer).",
    "No new source was read, no claims.csv, link or source register was changed, and no Maps version was made (PLAN sections 6 and 9 assign Maps versions to cycles only).",
]

CID = re.compile(r"\b((?:DV|IN|AL|CV|AS|TR)[0A-D]-[A-Z]{3}-\d{2})\b(\s*\[([^\]]+)\])?")
LID = re.compile(r"\b(PL-\d{2})\b(\s*\[([^\]]+)\])?")

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

def check(base):
    L = all_ledgers(); K = links(); S = sources()
    txt = open(os.path.join(PH, "SYNTHESIS.md"), encoding="utf-8").read()
    checks = []
    # V1
    m = json.load(open(os.path.join(D, "matrix_v38.json"))); eq = 0; bad = []
    for ph, pn in PHASES:
        for fc, fd in FIELDS:
            cl = [r for r in L[ph + "D"].values() if r["field"] == fc]
            lab = collections.Counter(LAB[r["framework_label"]] for r in cl)
            x = [r for r in m["phase_x_field"] if r["phase"] == pn and r["field"] == fd][0]
            ok = int(x["n_claims"]) == len(cl) and all(int(x[k]) == lab[k] for k in ("E", "P", "PS", "H"))
            eq += ok
            if not ok: bad.append(pn + "/" + fc)
    checks.append(dict(id="V1", kind="validation", statement="x12 per-field label counts from ledgers equal Maps v38 phase x field (30 canonical + 6 Transcendence overlay rows)",
                       value=f"{eq}/36", mismatches=bad, result="Pass" if eq == 36 else "Fail"))
    r = json.load(open(os.path.join(D, "_records.json")))
    ok = r["badrec"] == 0 and all(r["nrec"].get(ph) == 186 for ph, _ in PHASES)
    checks.append(dict(id="V2", kind="validation", statement="1,116 EXECUTION_RECORD.json files, 186 per phase, each with status and pre_registered_checks",
                       value=f"{sum(r['nrec'].values())} ({r['nrec']}), malformed {r['badrec']}", result="Pass" if ok else "Fail"))
    a = json.load(open(os.path.join(D, "arithmetic.json")))
    ok = a["M_equals_printed"] and a["grid_625"] == 625 and a["grid_750"] == 750 and a["later_all_zero"]
    checks.append(dict(id="V3", kind="validation", statement="README section 10 arithmetic reproduces; 5^4 = 625; 5x5x6x5 = 750; later pattern is all zero",
                       value=f"M==printed {a['M_equals_printed']}, 625 {a['grid_625']}, 750 {a['grid_750']}, later {a['later_pattern']}", result="Pass" if ok else "Fail"))
    # C1
    c_ok = c_bad = 0; c_err = []; c_ids = set()
    for mm in CID.finditer(txt):
        cid, lab = mm.group(1), mm.group(3); c_ids.add(cid)
        row = L.get(cid[:3], {}).get(cid)
        if row is None: c_bad += 1; c_err.append(cid + " unresolved"); continue
        if lab != row["framework_label"]: c_bad += 1; c_err.append(f"{cid} written [{lab}] ledger {row['framework_label']}"); continue
        c_ok += 1
    checks.append(dict(id="C1", kind="validation", statement="every claim ID in SYNTHESIS.md resolves in its cycle ledger and carries its ledger label",
                       value=f"{c_ok} of {c_ok + c_bad} mentions ({len(c_ids)} distinct IDs)", errors=c_err, result="Pass" if c_bad == 0 and c_ok > 0 else "Fail"))
    l_ok = l_bad = 0; l_err = []; l_ids = set()
    for mm in LID.finditer(txt):
        lid, lab = mm.group(1), mm.group(3); l_ids.add(lid)
        row = K.get(lid)
        if row is None: l_bad += 1; l_err.append(lid + " unresolved"); continue
        if lab != row["framework_label"]: l_bad += 1; l_err.append(f"{lid} written [{lab}] register {row['framework_label']}"); continue
        l_ok += 1
    checks.append(dict(id="C2", kind="validation", statement="every link ID in SYNTHESIS.md resolves and carries its register label",
                       value=f"{l_ok} of {l_ok + l_bad} mentions ({len(l_ids)} distinct IDs)", errors=l_err, result="Pass" if l_bad == 0 and l_ok > 0 else "Fail"))
    s_ids = set(PID.findall(txt)); s_err = sorted(s for s in s_ids if s not in S)
    checks.append(dict(id="C3", kind="validation", statement="every source ID in SYNTHESIS.md resolves in a Phases SOURCE_REGISTER",
                       value=f"{len(s_ids) - len(s_err)} of {len(s_ids)} distinct IDs", errors=s_err, result="Pass" if not s_err else "Fail"))
    ch = subprocess.run(["git", "-C", RES, "diff", "--name-only", base, "--", "Tracks/Phases"], capture_output=True, text=True)
    changed = [p for p in ch.stdout.split() if re.search(r"(claims\.csv|link_register\.csv|SOURCE_REGISTER\.csv)$", p)]
    checks.append(dict(id="C4", kind="validation", statement="no claims.csv, link register or source register changed against the base",
                       value=f"git diff {base}: {len(changed)} such files" if ch.returncode == 0 else "git diff failed",
                       errors=changed, result="Pass" if ch.returncode == 0 and not changed else ("Indeterminate" if ch.returncode else "Fail")))
    rg = json.load(open(os.path.join(D, "registry_checks.json")))
    checks.append(dict(id="R2", kind="reporting", statement="registry checks added after SPEC.md (duplicates, links labelled above their weakest basis claim, unassigned IDs)",
                       value=f"duplicates {rg['duplicate_registrations']}; links above basis {len(rg['links_labelled_above_weakest_basis_claim'])} of {rg['links_total']}; unassigned IDs in P01-P108 {len(rg['missing_ids_in_P01_P108'])}", result="Reported"))
    checks.append(dict(id="R1", kind="reporting", statement="synthesis citation counts",
                       value=f"{len(c_ids)} claim IDs, {len(l_ids)} link IDs, {len(s_ids)} source IDs", result="Reported"))
    files = ["SPEC.md", "tools/synth.py", "tools/SYNTHESIS.template.md"] + sorted("data/" + f for f in os.listdir(D) if not f.startswith("_"))
    rec = dict(sim_id="SIM-PH-SYN", iteration=1, status="completed", layout="Phases synthesis (aggregation, no randomness)",
               finished_utc=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               environment=dict(python=platform.python_version()), command="python3 tools/synth.py aggregate && render && check --base " + base,
               inputs=dict(maps=os.path.basename(MAPS), ledgers=30, execution_records=sum(r["nrec"].values())),
               spec_sha256=sha(os.path.join(HERE, "SPEC.md")), synthesis_sha256=sha(os.path.join(PH, "SYNTHESIS.md")),
               outputs_sha256={f: sha(os.path.join(HERE, f)) for f in files},
               pre_registered_checks=checks, n_checks=len(checks),
               n_validation=sum(c["kind"] == "validation" for c in checks),
               n_validation_pass=sum(c["kind"] == "validation" and c["result"] == "Pass" for c in checks))
    rec["disclosed"] = DISCLOSED
    rec["all_validation_passed"] = rec["n_validation"] == rec["n_validation_pass"]
    json.dump(rec, open(os.path.join(HERE, "EXECUTION_RECORD.json"), "w"), indent=1)
    for c in checks: print(c["id"], c["result"], c["value"], c.get("errors", "") or "")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "aggregate": aggregate()
    elif cmd == "render": render()
    elif cmd == "check": check(sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "HEAD")
