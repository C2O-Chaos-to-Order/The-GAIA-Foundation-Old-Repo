import json, os, sys, numpy as np
from scipy.optimize import curve_fit
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); P=json.load(open(f"{H}/params.json")); t0=ER.now(); os.makedirs(f"{H}/outputs",exist_ok=True)
r=P["rw"]
def rw(pre_cue):
    V={"A":0.0,"B":0.0,"X":0.0}
    for _ in range(r["n_pre"]): V[pre_cue]+=r["alpha"]*r["beta"]*(r["lambda"]-V[pre_cue])
    for _ in range(r["n_comp"]):
        err=r["lambda"]-(V["A"]+V["X"])
        for c in ("A","X"): V[c]+=r["alpha"]*r["beta"]*err
    return V
Vb,Vc=rw("A"),rw("B")
f=P["forgetting"]; t=np.array(f["hours"])
models={"exponential":(lambda t,a,k:a*np.exp(-k*t),[0.5,0.01]),"power":(lambda t,a,c:a*t**(-c),[0.4,0.1]),"log":(lambda t,a,c:a-c*np.log(t),[0.45,0.03])}
fits={}
for ds in ("ebbinghaus","dros"):
    y=np.array(f[ds]); fits[ds]={}
    for m,(fn,p0) in models.items():
        p,_=curve_fit(fn,t,y,p0=p0,maxfev=20000); sse=float(((fn(t,*p)-y)**2).sum()); n=len(y)
        fits[ds][m]=dict(params=[float(v) for v in p],SSE=sse,AIC=float(n*np.log(sse/n)+4))
    fits[ds]["best_by_AIC"]=min(models,key=lambda m:fits[ds][m]["AIC"])
out=dict(rw_blocking=Vb,rw_control=Vc,forgetting_fits=fits)
json.dump(out,open(f"{H}/outputs/results.json","w"),indent=2)
e=fits["ebbinghaus"]
chk=[dict(id="E1",expect="V_X blocking < 0.1*V_X control",observed=[Vb["X"],Vc["X"]],result="Pass" if Vb["X"]<0.1*Vc["X"] else "Fail"),
 dict(id="E2",expect="sum V on AX -> lambda",observed=[Vb["A"]+Vb["X"],Vc["A"]+Vc["X"]],result="Pass" if abs(Vb["A"]+Vb["X"]-1)<0.01 and abs(Vc["A"]+Vc["X"]-1)<0.01 else "Fail"),
 dict(id="E3",expect="Ebbinghaus: power or log AIC < exponential AIC",observed={m:round(e[m]["AIC"],3) for m in models},result="Pass" if min(e["power"]["AIC"],e["log"]["AIC"])<e["exponential"]["AIC"] else "Fail"),
 dict(id="E4",expect="Dros: report only",observed={m:round(fits['dros'][m]["AIC"],3) for m in models},result="Pass")]
ER.write(H,"SIM-R2-C0",P,[f"{H}/outputs/results.json"],chk,t0)
