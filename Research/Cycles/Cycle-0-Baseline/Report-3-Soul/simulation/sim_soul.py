import os, sys, json, numpy as np, pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist, squareform
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); P=json.load(open(f"{H}/params.json")); t0=ER.now(); os.makedirs(f"{H}/outputs",exist_ok=True)
df=pd.read_csv(f"{H}/{P['coding_file']}",keep_default_na=False); cols=[c for c in df.columns if c[0]=="A" and c[1].isdigit()]
X=df[cols].values.astype(bool); ids=list(df.id); n=len(ids)
def labels(M): return fcluster(linkage(pdist(M,P["metric"]),P["linkage"]),P["k"],"maxclust")
def part(lab): return tuple(sorted(tuple(sorted(i for i,l in zip(ids,lab) if l==k)) for k in set(lab)))
bl=labels(X); base=part(bl)
unc=[(r,cols.index([c for c in cols if c.split("_")[0]==a][0])) for r,s in enumerate(df.uncertain_cells) for a in (s.split(";") if s else [])]
rng=np.random.default_rng(P["seed"]); co=np.zeros((n,n)); same=0
for _ in range(P["mc_draws"]):
    M=X.copy()
    for (r,c) in unc:
        if rng.random()<P["flip_prob"]: M[r,c]=~M[r,c]
    lab=labels(M); same+=(part(lab)==base); co+=(lab[:,None]==lab[None,:])
co/=P["mc_draws"]; frac=same/P["mc_draws"]
J=1-squareform(pdist(X,P["metric"])); np.fill_diagonal(J,1)
pd.DataFrame(J,index=ids,columns=ids).round(3).to_csv(f"{H}/outputs/jaccard_similarity.csv")
pd.DataFrame(co,index=ids,columns=ids).round(3).to_csv(f"{H}/outputs/coclustering_frequency.csv")
stable=[(ids[i],ids[j],round(float(co[i,j]),3)) for i in range(n) for j in range(i+1,n) if co[i,j]>=P["pair_threshold"]]
attr_freq={c:int(X[:,k].sum()) for k,c in enumerate(cols)}
cls="Philosophical/Spiritual — partition robust to flagged uncertainty" if frac>=P["robust_threshold"] else "Philosophical/Spiritual — partition coding-sensitive (Indeterminate)"
res=dict(n_conceptions=n,n_attributes=len(cols),uncertain_cells=len(unc),draws=P["mc_draws"],base_partition=base,base_reproduced_fraction=frac,stable_pairs_ge_threshold=stable,attribute_frequency=attr_freq,classification=cls)
json.dump(res,open(f"{H}/outputs/results.json","w"),indent=2)
ok1=bool((df.source.str.len()>0).all()) and X.shape==(14,12)
chk=[dict(id="E1",expect="14x12 matrix complete; every row has a source",observed=dict(shape=list(X.shape),all_sourced=bool((df.source.str.len()>0).all())),result="Pass" if ok1 else "Fail"),
     dict(id="E2",expect="robustness fraction and stable pairs reported (reporting check)",observed=dict(fraction=round(frac,4),n_stable_pairs=len(stable)),result="Pass"),
     dict(id="E3",expect="no attribute shared by all 14 conceptions (no universal 'soul' definition in this coding)",observed=max(attr_freq.values()),result="Pass" if max(attr_freq.values())<n else "Fail")]
ER.write(H,"SIM-R3-C0",P,[f"{H}/outputs/{f}" for f in ("results.json","jaccard_similarity.csv","coclustering_frequency.csv")],chk,t0)
