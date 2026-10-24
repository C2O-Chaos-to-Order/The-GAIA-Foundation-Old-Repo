import os, sys, json, csv, glob, itertools, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); C=os.path.abspath(f"{H}/../.."); P=json.load(open(f"{H}/params.json")); t0=ER.now()
M_=f"{H}/../maps"; os.makedirs(M_,exist_ok=True); os.makedirs(f"{H}/outputs",exist_ok=True)
ax=P["axes"]; names=list(ax)
rows=[]
for i,j,k,l in itertools.product(range(5),repeat=4):
    rows.append(dict(id=f"X-A{i+1}-B{j+1}-P{k+1}-L{l+1}",alchemy=ax["Alchemy"][i],being=ax["Being"][j],phase=ax["Phase"][k],lens=ax["Lens"][l],
      status="Proposed — category only",evidence_class="Undefined",research_question="Undefined (to be specified before use)",ethical_review="Not performed"))
tri=[dict(id=f"T-A{i+1}-B{j+1}-P{k+1}",alchemy=ax["Alchemy"][i],being=ax["Being"][j],phase=ax["Phase"][k],status="Proposed — category only") for i,j,k in itertools.product(range(5),repeat=3)]
ab=[dict(id=f"AB-A{i+1}-B{j+1}",alchemy=ax["Alchemy"][i],being=ax["Being"][j],relationship="Undefined",status="Proposed — no evidence-supported relationship established in Cycle 0",
     note=("Same-name pairing; identity of the two is NOT assumed" if i==j else "")) for i,j in itertools.product(range(5),repeat=2)]
ap=[dict(id=f"AP-A{i+1}-P{k+1}",alchemy=ax["Alchemy"][i],phase=ax["Phase"][k],definition="Phase semantics undefined (fixed sequence vs recurring states unresolved; README §12 Q4)",status="Proposed — category only") for i,k in itertools.product(range(5),repeat=2)]
def wcsv(p,rs):
    with open(p,"w",newline="") as f: w=csv.DictWriter(f,fieldnames=rs[0].keys(),lineterminator="\n"); w.writeheader(); w.writerows(rs)
for fn,rs in (("intersections_625.csv",rows),("triality_125.csv",tri),("alchemy_x_being_25.csv",ab),("alchemy_x_phase_25.csv",ap)): wcsv(f"{M_}/{fn}",rs)
dec_ok=all((r["alchemy"],r["being"],r["phase"],r["lens"])==(ax["Alchemy"][int(r["id"][3])-1],ax["Being"][int(r["id"][6])-1],ax["Phase"][int(r["id"][9])-1],ax["Lens"][int(r["id"][12])-1]) for r in rows)
a=np.array(P["matrix"]["a"]); b=np.array(P["matrix"]["b"]); M=np.outer(a,b)+1; T=np.array(P["matrix"]["readme_table"])
pt=P["pattern"]; prod=(np.array(pt["A"])*np.array(pt["B"])*np.array(pt["C"])*pt["D"]*pt["E"]).tolist()
json.dump(dict(M=M.tolist(),matches_readme_cells=int((M==T).sum()),pattern_product=prod,note="Arithmetic only; semantics undefined"),open(f"{H}/outputs/matrix_checks.json","w"),indent=2)
# consistency
reg={r["source_id"]:r for r in csv.DictReader(open(f"{C}/Provenance/SOURCE_REGISTER.csv"))}
sims={}
for rec in glob.glob(f"{C}/Report-*/simulation/EXECUTION_RECORD.json"):
    j=json.load(open(rec)); sims[j["sim_id"]]={c["id"]:c["result"] for c in j["pre_registered_checks"]}
claims=[]; [claims.extend(list(csv.DictReader(open(p)))) for p in sorted(glob.glob(f"{C}/Report-*/claims/claims.csv"))]
ids={c["claim_id"] for c in claims}
req=["claim_id","report","wording","claim_class","framework_label","conclusion_status","source_ids","confidence"]
bad_fields=[c["claim_id"] for c in claims if any(not c[k].strip() for k in req)]
bad_vocab=[c["claim_id"] for c in claims if c["claim_class"] not in P["classes"] or c["conclusion_status"] not in P["statuses"] or c["framework_label"] not in P["labels"]]
bad_map=[c["claim_id"] for c in claims if c["framework_label"] in P["labels"] and c["conclusion_status"] not in P["label_status_map"][c["framework_label"]]]
dup=len(claims)-len(ids)
def split(s): return [x for x in s.split(";") if x]
unres=[]; e7=[]; self_cites=[]
for c in claims:
    for s in split(c["source_ids"]):
        if s.startswith("SIM-"):
            sid,_,chk=s.partition("#")
            if sid=="SIM-R7-C0": self_cites.append((c["claim_id"],s)); continue
            if sid not in sims or (chk and chk not in sims[sid]): unres.append((c["claim_id"],s)); continue
            if c["framework_label"]=="Established" and (not chk or sims[sid][chk]!="Pass"): e7.append((c["claim_id"],s))
        elif s not in reg: unres.append((c["claim_id"],s))
e10=[c["claim_id"] for c in claims if c["framework_label"]=="Established" and split(c["source_ids"])==["G03"]]
abstract_only=[c["claim_id"] for c in claims if c["framework_label"]=="Established" and (lit:=[s for s in split(c["source_ids"]) if s in reg]) and all(("abstract only" in reg[s]["access_mode"]) or ("excerpt" in reg[s]["access_mode"]) for s in lit)]
links=list(csv.DictReader(open(f"{M_}/link_register.csv")))
lk_bad=[l["link_id"] for l in links if any(not l[k].strip() for k in ("statement","framework_label","basis","test","rejection_criterion","gaia_thread")) or l["framework_label"] not in P["labels"] or l["link_type"] not in P["link_types"] or any(b not in ids for b in split(l["basis"]))]
types_missing=[t for t in P["required_link_types"] if t not in {l["link_type"] for l in links}]
reps=" ".join(l["from"]+" "+l["to"] for l in links); reps_missing=[r for r in ("R1","R2","R3","R4","R5","R6") if r not in reps]
cons=dict(n_claims=len(claims),missing_fields=bad_fields,bad_vocab=bad_vocab,label_status_mismatch=bad_map,duplicate_ids=dup,unresolved_sources=unres,established_on_failed_or_uncited_check=e7,self_citations_SIM_R7_checked_after_run=self_cites,established_backed_only_by_framework=e10,
  warning_established_abstract_only=abstract_only,label_counts={s:sum(c["framework_label"]==s for c in claims) for s in P["labels"]},status_counts={s:sum(c["conclusion_status"]==s for c in claims) for s in P["statuses"]},
  links=dict(n=len(links),bad=lk_bad,types_missing=types_missing,reports_missing=reps_missing,label_counts={s:sum(l["framework_label"]==s for l in links) for s in P["labels"]}))
json.dump(cons,open(f"{H}/outputs/consistency.json","w"),indent=2)
chk=[dict(id="E1",expect="125/625 unique, decodable",observed=[len({r['id'] for r in tri}),len({r['id'] for r in rows}),dec_ok],result="Pass" if len({r['id'] for r in tri})==125 and len({r['id'] for r in rows})==625 and dec_ok else "Fail"),
 dict(id="E2",expect="25+25 map rows",observed=[len(ab),len(ap)],result="Pass" if len(ab)==len(ap)==25 else "Fail"),
 dict(id="E3",expect="20/20 cells match README",observed=int((M==T).sum()),result="Pass" if (M==T).all() else "Fail"),
 dict(id="E4",expect="zero vector",observed=prod,result="Pass" if prod==[0]*5 else "Fail"),
 dict(id="E5",expect="fields/vocab/label-status mapping/unique ok",observed=[bad_fields,bad_vocab,bad_map,dup],result="Pass" if not bad_fields and not bad_vocab and not bad_map and dup==0 else "Fail"),
 dict(id="E6",expect="all sources and SIM#check citations resolve",observed=unres,result="Pass" if not unres else "Fail"),
 dict(id="E7",expect="no Established claim cites a failed or unspecified SIM check",observed=e7,result="Pass" if not e7 else "Fail"),
 dict(id="E8",expect="warning list (Established claims resting only on abstract/excerpt access)",observed=abstract_only,result="Pass"),
 dict(id="E9",expect="link register complete; all 7 link types; R1-R6 all linked",observed=dict(bad=lk_bad,types_missing=types_missing,reports_missing=reps_missing,n=len(links)),result="Pass" if not lk_bad and not types_missing and not reps_missing else "Fail"),
 dict(id="E10",expect="no Established claim backed only by the framework/motherthread document",observed=e10,result="Pass" if not e10 else "Fail")]
ER.write(H,"SIM-R7-C0",P,[f"{H}/outputs/matrix_checks.json",f"{H}/outputs/consistency.json"]+[f"{M_}/{x}" for x in ("intersections_625.csv","triality_125.csv","alchemy_x_being_25.csv","alchemy_x_phase_25.csv","link_register.csv","cross_domain_map.csv")],chk,t0)
