import os, sys, json, itertools, numpy as np, pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); t0=ER.now(); os.makedirs(f"{H}/outputs",exist_ok=True)
df=pd.read_csv(f"{H}/coding.csv",keep_default_na=False); cols=[c for c in df.columns if c.startswith("A")]
X=df[cols].values.astype(bool); ids=list(df.id)
def part(M):
    lab=fcluster(linkage(pdist(M,"jaccard"),"average"),3,"maxclust")
    return tuple(sorted(tuple(sorted(i for i,l in zip(ids,lab) if l==k)) for k in set(lab)))
base=part(X)
unc=[(r,cols.index([c for c in cols if c.startswith(a+"_")][0])) for r,s in enumerate(df.uncertain_cells) for a in (s.split(";") if s else [])]
co=np.zeros((len(ids),len(ids))); same=0; N=0
for flips in itertools.product([0,1],repeat=len(unc)):
    M=X.copy()
    for f,(r,c) in zip(flips,unc):
        if f: M[r,c]=~M[r,c]
    p=part(M); N+=1; same+=(p==base)
    for g in p:
        for a in g:
            for b in g: co[ids.index(a),ids.index(b)]+=1
co/=N
J=1-np.array([[0 if i==j else pdist(X[[i,j]],"jaccard")[0] for j in range(len(ids))] for i in range(len(ids))])
np.fill_diagonal(J,1)
pd.DataFrame(J,index=ids,columns=ids).round(3).to_csv(f"{H}/outputs/jaccard_similarity.csv")
pd.DataFrame(co,index=ids,columns=ids).round(3).to_csv(f"{H}/outputs/coclustering_frequency.csv")
frac=same/N; cls="Interpretive (robust to flagged uncertainty only)" if frac>=0.5 else "Indeterminate (coding-sensitive)"
json.dump(dict(base_partition=base,uncertain_cells=len(unc),combinations=N,base_reproduced_fraction=frac,classification=cls),open(f"{H}/outputs/results.json","w"),indent=2)
chk=[dict(id="E1",expect="complete matrix + sources",observed=bool(df.source.all() and X.shape==(9,10)),result="Pass" if df.source.all() and X.shape==(9,10) else "Fail"),
     dict(id="E2",expect="robustness reported",observed=dict(fraction=round(frac,4),classification=cls,base=base),result="Pass")]
ER.write(H,"SIM-R3-C0",{"coding_file":"coding.csv","linkage":"average","k":3,"metric":"jaccard"},[f"{H}/outputs/{f}" for f in ("results.json","jaccard_similarity.csv","coclustering_frequency.csv")],chk,t0)
