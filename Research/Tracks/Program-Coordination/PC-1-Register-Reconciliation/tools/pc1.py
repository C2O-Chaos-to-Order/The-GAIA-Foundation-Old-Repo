#!/usr/bin/env python3
"""PC-1 Program Charter and Master Register Reconciliation: deterministic tooling.

Reuses the PC-4 helpers (register and suite hash checks, TOT-id parsing, boundary scan).
The owner-provided GAIA Totality Suite v0.1.0 is EXTERNAL and never filed here.
Commands: run --cycle DIR --iter N | verify --cycle DIR | boundary | render --cycle DIR --iter N --out F
"""
import argparse, csv, json, os, re, shutil, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "..", "PC-4-Research-to-Domain-Map", "tools"))
import pc4  # noqa: E402

ROLES = {"independent", "ethics-rights", "security-privacy", "data-steward", "auditor", "community-rep"}
UR_DOMAINS = {"EPI", "SCI", "ETH", "TEC", "OPS", "ALL"}
HOME_TYPES = {"extend", "extend-planned", "new", "shared"}
NEW_PREFIX = "GOVERNANCE/DOMAIN_STANDARDS/"

def rd(path):
    return open(path, encoding="utf-8").read()

def ur_laws(repo):
    laws = {}
    for line in rd(os.path.join(repo, "GOVERNANCE/UNIVERSAL_REGULATION.md")).splitlines():
        m = re.match(r"#### 5\.\d UR-([A-Z]+) .*· Laws? ([0-9, and]+)", line)
        if m:
            laws[m.group(1)] = sorted({int(x) for x in re.findall(r"\d", m.group(2))})
    return laws

def tog19_planned(repo):
    t = rd(os.path.join(repo, "GOVERNANCE/TOTALITY_OF_GOVERNANCE_DRAFT_v0.1.0.md"))
    sec = t.split("## 19.")[1].split("## 20.")[0]
    return set(re.findall(r"`(GOVERNANCE/[^`]+)`", sec))

def suite_crosswalk(suite):
    rel = "04_EXISTING_REPOSITORY_COVERAGE_CROSSWALK.md"
    pc4.verify_suite_file(suite, rel)
    rows = []
    for line in open(os.path.join(suite, rel), encoding="utf-8-sig"):
        cells = [c.strip() for c in line.strip().split("|")]
        if len(cells) >= 6 and "TOT-" in cells[3]:
            rows.append((cells[1][:60], sorted(pc4.named_tots(cells[3]))))
    return rows

def collect_ids(paths, exclude=None):
    ids = set()
    for base in paths:
        for dp, dns, fns in os.walk(base):
            dns[:] = sorted(d for d in dns if d not in (".git", "__pycache__")
                            and os.path.abspath(os.path.join(dp, d)) != exclude)
            for fn in fns:
                if fn.endswith((".md", ".csv", ".json", ".txt")):
                    try:
                        ids |= set(re.findall(r"GAIA-[A-Z0-9]+(?:-[A-Z0-9]+)*", rd(os.path.join(dp, fn))))
                    except UnicodeDecodeError:
                        pass
    return ids

def run(cycle_dir, it, outdir=None):
    P = lambda p: os.path.normpath(os.path.join(cycle_dir, p))
    cfg = json.load(open(os.path.join(cycle_dir, "config.json")))
    icfg = cfg["iterations"][str(it)]
    suite = os.environ.get("PC4_SUITE", cfg["suite_path"])
    repo = P(cfg["repo_root"])
    reg = pc4.load_register(suite)
    reg_by = {r["stable_id"]: r for r in reg}
    ids = [r["stable_id"] for r in reg]
    wq = rd(P(cfg["work_queue"]))
    items = {i["item_id"]: i for i in pc4.inventory(wq)}
    problems = []
    laws = ur_laws(repo)
    planned = tog19_planned(repo)
    # domain rows
    drows = pc4.load_map(P(cfg["domains"]))
    seen, rows_ok, anchors_bad, homes = {}, 0, [], {}
    for r in drows:
        d = r["stable_id"]
        if d not in reg_by:
            problems.append(f"unknown domain {d}"); continue
        if d in seen:
            problems.append(f"duplicate row {d}")
        seen[d] = r
        if r["owner"] != reg_by[d]["decision_authority"]:
            problems.append(f"{d}: owner differs from the register's decision authority")
        if r["label"] not in pc4.LABELS:
            problems.append(f"{d}: bad label")
        for role in pc4.split_ids(r["reviewer_roles"]):
            if role not in ROLES and not role.startswith("specialist:"):
                problems.append(f"{d}: unknown role {role}")
        for u in pc4.split_ids(r["ur_domains"]):
            if u not in UR_DOMAINS:
                problems.append(f"{d}: unknown UR domain {u}")
        ht, home = r["home_type"], r["canonical_home"]
        if ht not in HOME_TYPES:
            problems.append(f"{d}: bad home type {ht}")
        if ht == "extend" and not os.path.exists(os.path.join(repo, home)):
            problems.append(f"{d}: extend target missing {home}")
        if ht == "extend-planned" and home not in planned:
            problems.append(f"{d}: {home} is not a ToG section 19 planned file")
        if ht in ("new", "shared") and not home.startswith(NEW_PREFIX):
            problems.append(f"{d}: new home must be under {NEW_PREFIX}")
        if r["domain_id"] != d:
            problems.append(f"{d}: domain_id must keep the register stable ID")
        if r["doc_id"] != "GAIA-GOV-TOT-" + d[-3:]:
            problems.append(f"{d}: doc_id must be GAIA-GOV-TOT-{d[-3:]}")
        homes.setdefault(home, []).append(d)
        for a in [x.strip() for x in r["anchors"].split(";") if x.strip()]:
            f, _, txt = a.partition("#")
            fp = os.path.join(repo, f)
            if not os.path.exists(fp) or (txt and txt not in rd(fp)):
                anchors_bad.append(f"{d}: {a}")
    rows_ok = sum(1 for d in ids if d in seen)
    dup_homes = {h: ds for h, ds in homes.items() if len(ds) > 1}
    # home-rule variants
    rule = icfg.get("home_rule", "as_judged")
    def eff(r):
        if rule == "always_new":
            return "new"
        if rule == "no_planned" and r["home_type"] == "extend-planned":
            return "new"
        return r["home_type"]
    eff_types = {d: eff(seen[d]) for d in ids if d in seen}
    competing = [d for d in ids if d in seen and seen[d]["home_type"].startswith("extend") and eff_types[d] == "new"]
    # IDs
    others = collect_ids([repo, suite], exclude=os.path.abspath(ROOT))
    collisions = sorted(r["doc_id"] for r in seen.values() if r["doc_id"] in others)
    # b9
    xw = suite_crosswalk(suite)
    covered = set().union(*[set(t) for _, t in xw]) if xw else set()
    b9_calc = sorted(d for d in ids if d not in covered)
    b9_wq = sorted(pc4.named_tots(items["M-b9"]["text"]))
    b9_sd = sorted(set(b9_calc) ^ set(b9_wq))
    # waves
    rm = {r["stable_id"]: r for r in pc4.load_map(P(cfg["roadmap"]))}
    pw = {"P0": "1", "P1": "2", "P2": "3", "P3": "4"}
    waves, mism = [], []
    for d in ids:
        rw_ = rm.get(d, {}).get("roadmap_wave", "")
        if not rw_:
            problems.append(f"{d}: no roadmap row")
        imp = pw[reg_by[d]["priority"]]
        mm = rw_ != imp
        waves.append(dict(stable_id=d, priority=reg_by[d]["priority"], implied_wave=imp,
                          roadmap_wave=rw_, mismatch=int(mm), basis=rm.get(d, {}).get("basis", "")))
        if mm:
            mism.append(d)
    exp_missing = [d for d in cfg["expected_mismatches"] if d not in mism]
    # audits
    aud = list(csv.DictReader(open(os.path.join(repo, "GOVERNANCE/AUDIT_UNIVERSAL_REGULATION_v2.csv"), encoding="utf-8")))
    amap = {r["audit_id"]: pc4.split_ids(r["domains"]) for r in pc4.load_map(P(cfg["audit_map"]))}
    unm = [a["id"] for a in aud if not amap.get(a["id"])]
    for a, ds in amap.items():
        for d in ds:
            if d not in reg_by:
                problems.append(f"audit {a}: unknown domain {d}")
    open_by = {d: [] for d in ids}
    all_by = {d: [] for d in ids}
    for a in aud:
        for d in amap.get(a["id"], []):
            if d in all_by:
                all_by[d].append(a["id"])
                if a["decision"] != "PASS":
                    open_by[d].append(f"{a['id']}:{a['decision']}")
    # PC-4 joins
    cov = {r["stable_id"]: r for r in csv.DictReader(open(P(cfg["pc4_coverage"]), encoding="utf-8"))}
    t24 = {d: [] for d in ids}
    for r in csv.DictReader(open(P(cfg["pc4_tog24"]), encoding="utf-8")):
        for d in [r["primary"]] + pc4.split_ids(r["secondary"]):
            t24[d].append(r["tog_id"])
    # joined table
    def title_of(d):
        if cfg.get("title_style") == "short":
            return re.sub(r"^GAIA-TOT-\d+-", "", os.path.basename(reg_by[d]["filename"])).replace(".md", "")
        return reg_by[d]["title"].split(":", 1)[-1].strip()
    joined = []
    for d in ids:
        r = seen.get(d, {})
        urs = pc4.split_ids(r.get("ur_domains", ""))
        lw = sorted({l for u in urs for l in (range(1, 8) if u == "ALL" else laws.get(u, []))})
        joined.append(dict(stable_id=d, title=title_of(d),
            priority=reg_by[d]["priority"], doc_id=r.get("doc_id", ""), home_type=r.get("home_type", ""),
            effective_home_type=eff_types.get(d, ""), canonical_home=r.get("canonical_home", ""),
            owner=r.get("owner", ""), reviewer_roles=r.get("reviewer_roles", ""),
            ur_domains=" ".join(urs), ur_laws=" ".join(map(str, lw)),
            tog6=" ".join(t24[d]), audit_items=" ".join(all_by[d]), audit_open=" ".join(open_by[d]),
            pc4_primary_reports=cov[d]["primary_items"].replace(";", " "),
            in_crosswalk_04=int(d in covered), roadmap_wave=next(w["roadmap_wave"] for w in waves if w["stable_id"] == d),
            implied_wave=next(w["implied_wave"] for w in waves if w["stable_id"] == d),
            label=r.get("label", ""), basis=r.get("basis", "")))
    specialist = [d for d in ids if d in seen and any(x.startswith("specialist:") for x in pc4.split_ids(seen[d]["reviewer_roles"]))]
    # boundary (current cycle excluded for determinism; full scan in VERIFICATION)
    here = os.path.relpath(os.path.abspath(cycle_dir), ROOT)
    bnd = pc4.boundary_scan(suite, ROOT, cfg["boundary_window"], exclude=(here + os.sep,))
    out = outdir or os.path.join(cycle_dir, f"iter-{it}")
    data = os.path.join(out, "data"); os.makedirs(data, exist_ok=True)
    pc4.write_csv(os.path.join(data, "reconciliation.csv"), joined, list(joined[0].keys()))
    pc4.write_csv(os.path.join(data, "waves.csv"), waves, list(waves[0].keys()))
    pc4.write_csv(os.path.join(data, "crosswalk_04_rows.csv"),
                  [dict(artifact=a, domains=" ".join(t)) for a, t in xw], ["artifact", "domains"])
    ht_counts = {}
    for v in eff_types.values():
        ht_counts[v] = ht_counts.get(v, 0) + 1
    metrics = dict(domain_rows_ok=rows_ok, problems=problems, anchors_unresolved=anchors_bad,
        duplicate_homes=sorted(f"{h}: {' '.join(ds)}" for h, ds in dup_homes.items()),
        id_collisions=collisions, b9_calculated=b9_calc, b9_work_queue=b9_wq,
        b9_symmetric_difference=b9_sd, crosswalk_rows=len(xw),
        wave_mismatches=mism, expected_mismatches_missing=exp_missing,
        audit_items=len(aud), audit_unmapped=unm,
        audit_open_items=sum(1 for a in aud if a["decision"] != "PASS"),
        domains_with_open_audit_items=[d for d in ids if open_by[d]],
        home_rule=rule, home_type_counts=dict(sorted(ht_counts.items())),
        competing_sources_under_rule=competing,
        specialist_role_domains=specialist,
        domains_without_tog6=[d for d in ids if not t24[d]],
        domains_without_audit_item=[d for d in ids if not all_by[d]],
        boundary_overlaps=bnd)
    metrics.update(extra_metrics(cfg, P, repo, seen, ids, aud, mism, problems, suite, data, it, bnd, reg_by, icfg, rm))
    checks = []
    for c in cfg["checks"]:
        if c.get("iterations") and it not in c["iterations"]:
            continue
        v = metrics
        for p in c["metric"].split("."):
            v = v[p]
        if isinstance(v, (list, dict)):
            v = len(v)
        ok = {"eq": v == c["threshold"], "le": v <= c["threshold"], "ge": v >= c["threshold"]}[c["op"]]
        checks.append(dict(id=c["id"], hypothesis=c["hypothesis"], metric=c["metric"], op=c["op"],
                           threshold=c["threshold"], value=v, result="PASS" if ok else "FAIL"))
    ins = {k: cfg[k] for k in ("work_queue", "domains", "audit_map", "roadmap", "pc4_coverage", "pc4_tog24")}
    rec = dict(track="PC-1 Program Charter and Master Register Reconciliation", cycle=cfg["cycle"], iteration=it,
               variant=icfg, inputs={k: dict(path=v, sha256=pc4.sha256(P(v))) for k, v in ins.items()},
               suite="GAIA Totality Suite v0.1.0 (owner-provided, Proposed, not adopted; external, not filed)",
               register_sha256=pc4.REG_SHA, metrics=metrics, checks=checks,
               outputs={f"data/{n}": pc4.sha256(os.path.join(data, n)) for n in sorted(os.listdir(data))})
    with open(os.path.join(out, "EXECUTION_RECORD.json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2, ensure_ascii=False); f.write("\n")
    return rec

def _anchors(r):
    return [x.strip() for x in r["anchors"].split(";") if x.strip()]

def extra_metrics(cfg, P, repo, seen, ids, aud, mism, problems, suite, data, it, bnd, reg_by=None, icfg=None, rm=None):
    """x3+ metrics; added only when the cycle config names their inputs (earlier records unchanged)."""
    m = {}
    if "anchor_review" in cfg:
        rv = {(r["stable_id"], r["anchor"].strip()): r["support"] for r in pc4.load_map(P(cfg["anchor_review"]))}
        for k, v in rv.items():
            if v not in ("direct", "partial", "none"):
                problems.append(f"{k[0]}: bad support value {v}")
        prior = pc4.load_map(P(cfg["prior_domains"]))
        m["prior_anchors_unreviewed"] = [f"{r['stable_id']}: {a}" for r in prior for a in _anchors(r) if (r["stable_id"], a) not in rv]
        m["anchors_unsupported"] = [f"{d}: {a}" for d in ids if d in seen for a in _anchors(seen[d]) if rv.get((d, a), "none") == "none"]
        m["domains_without_direct_anchor"] = [d for d in ids if d in seen and not any(rv.get((d, a)) == "direct" for a in _anchors(seen[d]))]
        m["anchor_support_counts"] = {k: sum(1 for d in ids if d in seen for a in _anchors(seen[d]) if rv.get((d, a)) == k) for k in ("direct", "partial", "none")}
        m["anchors_replaced"] = sorted(f"{r['stable_id']}: {a}" for r in prior for a in _anchors(r) if r["stable_id"] in seen and a not in _anchors(seen[r["stable_id"]]))
    am = pc4.load_map(P(cfg["audit_map"]))
    if am and "primary" in am[0]:
        dec = {a["id"]: a["decision"] for a in aud}
        home = {d: seen[d]["canonical_home"] for d in seen}
        mis, mis_t = [], []
        for r in am:
            pr = pc4.split_ids(r["primary"])
            if len(pr) != 1 or pr[0] not in home:
                problems.append(f"audit {r['audit_id']}: needs exactly one known primary domain")
                continue
            if pr[0] not in pc4.split_ids(r["domains"]):
                problems.append(f"audit {r['audit_id']}: primary not in domains")
            if dec.get(r["audit_id"]) != "PASS":
                if r["remedy_home"] != home[pr[0]]:
                    mis.append(f"{r['audit_id']}: {r['remedy_home'] or '(none)'} vs {home[pr[0]]}")
                    mis_t.append((r["audit_id"], pr[0], r["remedy_home"]))
            elif r["remedy_home"]:
                problems.append(f"audit {r['audit_id']}: PASS item has a remedy home")
        m["open_remedy_mismatch"] = mis
        prim = {}
        for r in am:
            prim.setdefault(r["primary"], []).append(r["audit_id"])
        m["primary_audit_load"] = {d: len(v) for d, v in sorted(prim.items())}
    if "authority" in cfg:
        RELS = {"parent", "companion", "subordinate", "evidence", "superseded-on-approval"}
        au = {}
        for r in pc4.load_map(P(cfg["authority"])):
            if r["relation"] not in RELS:
                problems.append(f"{r['stable_id']}: bad relation {r['relation']}")
            au[(r["stable_id"], r["source"])] = r["relation"]
        unc = []
        for d in ids:
            if d not in seen:
                continue
            for a in _anchors(seen[d]):
                f = a.partition("#")[0]
                if f != seen[d]["canonical_home"] and (d, f) not in au:
                    unc.append(f"{d}: {f}")
        m["authority_unclassified"] = sorted(set(unc))
        cnt = {}
        for v in au.values():
            cnt[v] = cnt.get(v, 0) + 1
        m["authority_relation_counts"] = dict(sorted(cnt.items()))
        par = {}
        for (d, f), v in au.items():
            if v == "parent":
                par.setdefault(f, []).append(d)
        m["parent_sources"] = {f: len(v) for f, v in sorted(par.items())}
        if cfg.get("remedy_rule") == "authority":
            m["open_remedy_unexplained"] = [f"{a}: {d} {f}" for a, d, f in mis_t if (d, f) not in au]
    if "anchor_review" in cfg:
        draft = "GOVERNANCE/TOTALITY_OF_GOVERNANCE_DRAFT_v0.1.0.md"
        if cfg.get("ur_criteria"):
            m["draft_only_domains"] = [d for d in ids if d in seen and all(a.partition("#")[0] == draft for a in _anchors(seen[d]) if rv.get((d, a)) == "direct") and any(rv.get((d, a)) == "direct" for a in _anchors(seen[d]))]
    if cfg.get("ur_criteria"):
        crit = re.findall(r"^- ((EPI|SCI|ETH|TEC|OPS)-\d+) ", rd(os.path.join(repo, "GOVERNANCE/UNIVERSAL_REGULATION.md")), re.M)
        uc = {r["criterion"]: r["primary"] for r in pc4.load_map(P(cfg["ur_criteria"]))}
        m["ur_criteria"] = len(crit)
        m["ur_criteria_unmapped"] = [c for c, _ in crit if c not in uc]
        m["ur_domain_inconsistent"] = []
        for c, u in crit:
            d = uc.get(c)
            if d and d not in seen:
                problems.append(f"UR {c}: unknown domain {d}")
            elif d:
                urs = pc4.split_ids(seen[d]["ur_domains"])
                if u not in urs and "ALL" not in urs:
                    m["ur_domain_inconsistent"].append(f"{c} -> {d} ({' '.join(urs)})")
        m["ur_domains_uncovered"] = [u for u in ("EPI", "SCI", "ETH", "TEC", "OPS") if not any(u in pc4.split_ids(seen[d]["ur_domains"]) for d in seen)]
        load = {}
        for c, d in uc.items():
            load[d] = load.get(d, 0) + 1
        m["ur_criteria_per_domain"] = dict(sorted(load.items()))
    if cfg.get("tog19"):
        planned = tog19_planned(repo)
        tg = pc4.load_map(P(cfg["tog19"]))
        for r in tg:
            if r["planned_file"] not in planned or r["relation"] not in ("home", "companion", "index", "record"):
                problems.append(f"ToG19 row {r['planned_file']}: unknown file or relation")
            if r["domains"] != "NEW" and any(d not in seen for d in pc4.split_ids(r["domains"])):
                problems.append(f"ToG19 row {r['planned_file']}: unknown domain")
        m["tog19_unassigned"] = sorted(planned - {r["planned_file"] for r in tg})
        m["tog19_records_per_domain"] = dict(sorted({d: sum(1 for r in tg if r["domains"] != "NEW" and d in pc4.split_ids(r["domains"])) for r in tg for d in pc4.split_ids(r["domains"]) if r["domains"] != "NEW"}.items()))
    if cfg.get("product_rules"):
        pr_ = pc4.load_map(P(cfg["product_rules"]))
        rule = {(r["field"], r["value"]): pc4.split_ids(r["domains"]) for r in pr_}
        prods = list(csv.DictReader(open(os.path.join(repo, "GOVERNANCE/PRODUCT_REGISTER.csv"), encoding="utf-8")))
        ung, pc = [], {}
        for p_ in prods:
            ds = set(rule.get(("kind", p_["kind"]), []))
            for o in p_["overlays"].split("+"):
                ds |= set(rule.get(("overlay", o.strip()), []))
            if not ds:
                ung.append(p_["product_id"])
            for d in ds:
                pc[d] = pc.get(d, 0) + 1
        m["products"] = len(prods)
        m["products_ungoverned"] = ung
        m["products_per_domain"] = dict(sorted(pc.items()))
    if reg_by is not None and cfg.get("ur_criteria"):
        deps = {}
        for d in ids:
            ds = sorted(x for x in pc4.named_tots(reg_by[d]["dependencies"]) if x != d)
            for x in ds:
                if x not in reg_by:
                    problems.append(f"{d}: unknown dependency {x}")
            deps[d] = ds
        road = {d: rm[d]["roadmap_wave"] for d in ids}
        prop = dict(road)
        for r in pc4.load_map(P(cfg["wave_proposals"])):
            prop[r["stable_id"]] = icfg.get("wave_038", "4") if r["proposed_wave"] == "owner" else r["proposed_wave"]
        def inv(sch):
            out = []
            for d in ids:
                if not sch[d].isdigit():
                    continue
                for x in deps[d]:
                    if not sch[x].isdigit() or int(sch[x]) > int(sch[d]):
                        out.append(f"{d}<-{x}")
            return out
        ir, ip = inv(road), inv(prop)
        m["dependency_edges"] = sum(len(v) for v in deps.values())
        m["inversions_roadmap"] = ir
        m["inversions_proposed"] = ip
        m["inversions_delta"] = len(ip) - len(ir)
        m["unscheduled_under_proposal"] = [d for d in ids if not prop[d].isdigit()]
        cov = {r["stable_id"]: r for r in csv.DictReader(open(P(cfg["pc4_coverage"]), encoding="utf-8"))}
        m["pc4_no_primary_report"] = [d for d in ids if not cov[d]["primary_items"]]
        if cfg.get("decisions"):
            m.update(x9_metrics(cfg, P, seen, ids, problems, deps, mism, m, icfg, rule if cfg.get("product_rules") else {}, prods if cfg.get("product_rules") else []))
    if "wave_proposals" in cfg:
        wp = {r["stable_id"] for r in pc4.load_map(P(cfg["wave_proposals"]))}
        m["mismatches_without_proposal"] = [d for d in mism if d not in wp]
    if "boundary_known" in cfg:
        own = [f"iter-{it}/data/{h}" for h in pc4.boundary_scan(suite, data, cfg["boundary_window"])]
        m["boundary_own_outputs"] = own
        m["boundary_new_overlaps"] = [h for h in list(bnd) + own if h not in cfg["boundary_known"]]
    return m

def scc(nodes, edges):
    """Tarjan, iterative-safe for 45 nodes (recursion fine)."""
    idx, low, st, on, out, c = {}, {}, [], set(), [], [0]
    def go(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in edges.get(v, []):
            if w not in idx:
                go(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = st.pop(); on.discard(w); comp.append(w)
                if w == v:
                    break
            out.append(sorted(comp))
    for v in nodes:
        if v not in idx:
            go(v)
    return sorted(out, key=lambda x: (-len(x), x))

def x9_metrics(cfg, P, seen, ids, problems, deps, mism, m, icfg, rule, prods):
    x = {}
    tiers = {r["stable_id"]: r["scope_tier"] for r in pc4.load_map(P(cfg["tiers"]))}
    for d, t in tiers.items():
        if t not in ("RL-1", "RL-2", "RL-3", "RL-4", "RL-5"):
            problems.append(f"{d}: bad tier {t}")
    x["domains_without_tier"] = [d for d in ids if d not in tiers]
    wdom = set()
    if icfg.get("w_overlay_rule", True):
        for p_ in prods:
            if "W" in [o.strip() for o in p_["overlays"].split("+")]:
                wdom |= set(rule.get(("kind", p_["kind"]), []))
                for o in p_["overlays"].split("+"):
                    wdom |= set(rule.get(("overlay", o.strip()), []))
    need, miss = {}, []
    for d in ids:
        t = int(tiers.get(d, "RL-2")[-1]); r = {"auditor"}
        if t >= 3:
            r |= {"ethics-rights", "community-rep"}
        if t >= 5:
            r.add("independent")
        if d in wdom:
            r.add("ethics-rights")
        need[d] = sorted(r)
        have = set(pc4.split_ids(seen[d]["reviewer_roles"])) if d in seen else set()
        for role in sorted(r - have):
            miss.append(f"{d}: {role}")
    x["required_roles_missing"] = miss
    x["required_roles_missing_by_role"] = {k: sum(1 for z in miss if z.endswith(": " + k)) for k in ("auditor", "ethics-rights", "community-rep", "independent")}
    x["tier_counts"] = {t: sum(1 for v in tiers.values() if v == t) for t in sorted(set(tiers.values()))}
    x["w_governing_domains"] = sorted(wdom)
    cc = {r["home_type"] for r in pc4.load_map(P(cfg["change_control"]))}
    x["home_types_without_rule"] = sorted({seen[d]["home_type"] for d in seen} - cc)
    dec = pc4.load_map(P(cfg["decisions"]))
    covered = set()
    for r in dec:
        if r["gate_state"] != "INDETERMINATE":
            problems.append(f"{r['decision_id']}: gate state must be INDETERMINATE")
        if r["authority"] != "KyleAlexanderSteen (repository owner)":
            problems.append(f"{r['decision_id']}: authority must be the owner")
        covered |= set(r["covers"].split())
    issues = [f"wave:{d}" for d in mism] + [f"ur:{z.split(' ')[0]}" for z in m.get("ur_domain_inconsistent", [])] \
        + [f"remedy:{z.split(':')[0]}" for z in m.get("open_remedy_mismatch", [])] + [f"notext:{d}" for d in m.get("domains_without_direct_anchor", [])] \
        + [f"b9:{d}" for d in m.get("b9_calculated", [])] + ["b16", "reviewers", "cycles", "wave0"]
    x["open_issues"] = len(issues)
    x["open_issues_without_decision"] = [i for i in issues if i not in covered]
    x["decisions"] = len(dec)
    comps = scc(ids, deps)
    cyc = [c for c in comps if len(c) > 1]
    x["cyclic_components"] = [" ".join(c) for c in cyc]
    x["largest_component"] = len(comps[0]) if comps else 0
    x["intra_component_edges"] = sum(1 for d in ids for y in deps[d] if any(d in c and y in c for c in cyc))
    x["acyclic_domains"] = [d for d in ids if not any(d in c for c in cyc)]
    return x

def verify(cycle_dir):
    cfg = json.load(open(os.path.join(cycle_dir, "config.json")))
    res = []
    for it in sorted(cfg["iterations"], key=int):
        tmp = tempfile.mkdtemp()
        try:
            rec = run(cycle_dir, int(it), outdir=tmp)
            orig = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json")))
            res.append((int(it), rec == orig))
        finally:
            shutil.rmtree(tmp)
    return res

def render(cycle_dir, it):
    rec = json.load(open(os.path.join(cycle_dir, f"iter-{it}", "EXECUTION_RECORD.json")))
    m = rec["metrics"]; sh = lambda x: x.replace("GAIA-TOT-", "")
    rows = list(csv.DictReader(open(os.path.join(cycle_dir, f"iter-{it}", "data", "reconciliation.csv"), encoding="utf-8")))
    L = [f"_Generated by `tools/pc1.py render` from iter-{it} (home rule `{m['home_rule']}`)._\n",
         "### Pre-registered checks\n\n| ID | Hypothesis | Value | Test | Result |\n|---|---|---|---|---|"]
    for c in rec["checks"]:
        L.append(f"| {c['id']} | {c['hypothesis']} | {c['value']} | {c['op']} {c['threshold']} | **{c['result']}** |")
    L.append(f"\n### Gap b9\n\nRecomputed from the suite's crosswalk ({m['crosswalk_rows']} rows naming domains): {len(m['b9_calculated'])} domains in no specific row: " + ", ".join(sh(x) for x in m["b9_calculated"]) + f". Work Queue b9 lists {len(m['b9_work_queue'])}; difference: " + (", ".join(sh(x) for x in m["b9_symmetric_difference"]) or "none") + ".")
    L.append("\n### Wave / priority mismatches\n\n| Domain | Priority | Implied wave | Roadmap wave |\n|---|---|---|---|")
    for r in rows:
        if r["roadmap_wave"] != r["implied_wave"]:
            L.append(f"| {sh(r['stable_id'])} {r['title']} | {r['priority']} | {r['implied_wave']} | {r['roadmap_wave']} |")
    L.append(f"\n### Summary\n\n- Home types: {m['home_type_counts']}\n- Audit v2: {m['audit_items']} items, {m['audit_open_items']} not PASS; domains with an open item: {len(m['domains_with_open_audit_items'])}; domains with no audit item: {len(m['domains_without_audit_item'])} ({', '.join(sh(x) for x in m['domains_without_audit_item'])})\n- Domains needing a reviewer qualification ToG §7.1 does not name: {len(m['specialist_role_domains'])} ({', '.join(sh(x) for x in m['specialist_role_domains'])})\n- Domains reached by no ToG §6 domain: {', '.join(sh(x) for x in m['domains_without_tog6']) or 'none'}")
    L.append("\n### Proposed register (proposals; Wave 0 approval is the owner's alone)\n\n| Domain | Pri. | Doc ID | Home | Owner | Reviewer roles | UR (laws) | ToG §6 | Audit (open) | PC-4 primary reports | Label |\n|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        L.append(f"| {sh(r['stable_id'])} {r['title']} | {r['priority']} | {r['doc_id']} | {r['home_type']}: `{r['canonical_home']}` | {r['owner'].split(' (')[0]} | {r['reviewer_roles']} | {r['ur_domains']} ({r['ur_laws']}) | {r['tog6'].replace('ToG6-', '')} | {r['audit_open'] or '—'} | {r['pc4_primary_reports'] or '—'} | {r['label']} |")
    if "anchor_support_counts" in m:
        L.append(f"\n### Anchor review\n\n- Support of cited anchors: {m['anchor_support_counts']}\n- Baseline anchors replaced: " + ("; ".join(m["anchors_replaced"]) or "none") + "\n- Domains with no anchor reviewed `direct`: " + (", ".join(sh(x) for x in m["domains_without_direct_anchor"]) or "none"))
    if "open_remedy_mismatch" in m:
        L.append("\n### Non-PASS audit items whose remedy home is not the primary domain's home\n\n| Item | Remedy home vs primary domain's home |\n|---|---|")
        for x in m["open_remedy_mismatch"]:
            a, _, b = x.partition(": ")
            L.append(f"| {a} | {b} |")
        L.append("\nPrimary audit load per domain: " + ", ".join(f"{sh(k)} {v}" for k, v in m["primary_audit_load"].items()))
    if "authority_relation_counts" in m:
        L.append(f"\n### Authority register\n\n- Relations: {m['authority_relation_counts']}\n- Parent sources (domains citing each): " + ", ".join(f"`{k}` {v}" for k, v in m["parent_sources"].items()))
    if "ur_criteria_unmapped" in m:
        L.append(f"\n### UR §5 criteria → TOT domains (b16)\n\n- {m['ur_criteria']} criteria; unmapped: {len(m['ur_criteria_unmapped'])}; UR-domain inconsistencies: " + ("; ".join(m["ur_domain_inconsistent"]) or "none") + "\n- Criteria per primary domain: " + ", ".join(f"{sh(k)} {v}" for k, v in m["ur_criteria_per_domain"].items()))
    if "products_per_domain" in m:
        L.append(f"\n### Product Register join\n\n- {m['products']} products; ungoverned: {len(m['products_ungoverned'])}\n- Products per domain: " + ", ".join(f"{sh(k)} {v}" for k, v in m["products_per_domain"].items()))
    if "inversions_delta" in m:
        both = sorted(set(m["draft_only_domains"]) & set(m["pc4_no_primary_report"]))
        L.append(f"\n### Dependency order\n\n- Named dependency edges: {m['dependency_edges']}\n- Inversions (a domain scheduled before a dependency, or the dependency unscheduled): roadmap {len(m['inversions_roadmap'])}, proposed {len(m['inversions_proposed'])} (delta {m['inversions_delta']})\n- Removed by the proposals: " + ", ".join(sh(x) for x in sorted(set(m["inversions_roadmap"]) - set(m["inversions_proposed"]))) + "\n- Remaining under the proposals: " + ", ".join(sh(x) for x in m["inversions_proposed"]))
        L.append(f"\n### Draft-only and report-less domains\n\n- Draft-only (every direct anchor is in the ToG draft): {len(m['draft_only_domains'])}: " + ", ".join(sh(x) for x in m["draft_only_domains"]) + f"\n- No PC-4 primary report: {len(m['pc4_no_primary_report'])}\n- Both: {len(both)}: " + ", ".join(sh(x) for x in both))
    if "required_roles_missing" in m:
        L.append(f"\n### Reviewer roles required by Risk Levels\n\n- Scope tiers: {m['tier_counts']}\n- Domains governing W-overlay products: " + (", ".join(sh(x) for x in m["w_governing_domains"]) or "none (rule off)") + f"\n- Missing required roles: {len(m['required_roles_missing'])} {m['required_roles_missing_by_role']}")
        L.append(f"\n### Dependency structure\n\n- Cyclic components: {len(m['cyclic_components'])}; largest: {m['largest_component']} domains; edges inside cyclic components: {m['intra_component_edges']} of {m['dependency_edges']}\n- Domains outside every cycle: " + ", ".join(sh(x) for x in m["acyclic_domains"]))
        L.append(f"\n### Owner decision packet\n\n- {m['decisions']} decisions cover {m['open_issues']} open issues; uncovered: {len(m['open_issues_without_decision'])}")
    return "\n".join(L) + "\n"

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("run"); a.add_argument("--cycle", required=True); a.add_argument("--iter", type=int, required=True)
    b = sp.add_parser("verify"); b.add_argument("--cycle", required=True)
    c = sp.add_parser("boundary"); c.add_argument("--window", type=int, default=80)
    e = sp.add_parser("render"); e.add_argument("--cycle", required=True); e.add_argument("--iter", type=int, required=True); e.add_argument("--out", required=True)
    g = ap.parse_args()
    if g.cmd == "run":
        rec = run(g.cycle, g.iter)
        for c_ in rec["checks"]:
            print(c_["id"], c_["result"], c_["value"])
        for k in ("problems", "anchors_unresolved", "duplicate_homes", "id_collisions", "b9_symmetric_difference", "audit_unmapped", "boundary_overlaps",
                  "prior_anchors_unreviewed", "anchors_unsupported", "domains_without_direct_anchor", "open_remedy_mismatch",
                  "authority_unclassified", "mismatches_without_proposal", "boundary_new_overlaps",
                  "ur_criteria_unmapped", "ur_domain_inconsistent", "tog19_unassigned", "products_ungoverned", "open_remedy_unexplained", "draft_only_domains",
                  "domains_without_tier", "required_roles_missing_by_role", "home_types_without_rule", "open_issues_without_decision", "largest_component", "acyclic_domains"):
            if rec["metrics"].get(k):
                print(k, rec["metrics"][k])
    elif g.cmd == "verify":
        ok = True
        for it, same in verify(g.cycle):
            print(f"iter-{it}: record identical={same}"); ok &= same
        sys.exit(0 if ok else 1)
    elif g.cmd == "boundary":
        hits = pc4.boundary_scan(os.environ.get("PC4_SUITE", "/workspace/coord/zip/gaia_totality_suite_v0_1"), ROOT, g.window)
        print(f"files sharing a {g.window}-character window with the suite: {len(hits)}", *hits, sep="\n  ")
        sys.exit(1 if hits else 0)
    else:
        open(g.out, "w", encoding="utf-8").write(render(g.cycle, g.iter))
