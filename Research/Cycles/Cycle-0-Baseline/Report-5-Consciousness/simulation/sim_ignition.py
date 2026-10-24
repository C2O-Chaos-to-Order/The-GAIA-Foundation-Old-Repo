import os, sys, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); P=json.load(open(f"{H}/params.json")); t0=ER.now(); os.makedirs(f"{H}/outputs",exist_ok=True)
amps=np.linspace(*P["amps"][:2],int(P["amps"][2])); rng=np.random.default_rng(P["seed"])
f=lambda z:1/(1+np.exp(-z/P["kappa"]))
def late(w):
    n1=int(P["stim_ms"]/P["dt"]); n2=int(P["post_ms"]/P["dt"]); out=np.zeros((len(amps),P["trials"]))
    r=np.zeros((len(amps),P["trials"])); A=amps[:,None]*np.ones_like(r); acc=np.zeros_like(r); cnt=0
    for k in range(n1+n2):
        I=A if k<n1 else 0.0
        r=r+P["dt"]/P["tau"]*(-r+f(w*r+I-P["theta"]))+P["sigma"]*np.sqrt(P["dt"])/P["tau"]*rng.standard_normal(r.shape)
        if k>=n1+int(200/P["dt"]): acc+=r; cnt+=1
    return acc/cnt
Ls,Lw=late(P["w_strong"]),late(P["w_weak"])
fs=(Ls>0.5).mean(1); fw=(Lw>0.5).mean(1)
lo=amps[np.argmax(fs>=0.1)] if (fs>=0.1).any() else None; hi=amps[np.argmax(fs>=0.9)] if (fs>=0.9).any() else None
res=dict(amps=amps.tolist(),frac_ignited_strong=fs.tolist(),frac_ignited_weak=fw.tolist(),transition_band=[lo,hi])
json.dump(res,open(f"{H}/outputs/results.json","w"),indent=2)
np.savetxt(f"{H}/outputs/late_activity_strong.csv",Ls,delimiter=",",fmt="%.5f"); np.savetxt(f"{H}/outputs/late_activity_weak.csv",Lw,delimiter=",",fmt="%.5f")
chk=[dict(id="E1",expect="w=8 transition 10%->90% within <=2 units",observed=[lo,hi],result="Pass" if lo is not None and hi is not None and fs[0]<0.1 and hi-lo<=2 else "Fail"),
 dict(id="E2",expect="w=2 no sustained trials",observed=float(fw.max()),result="Pass" if fw.max()==0 else "Fail"),
 dict(id="E3",expect="w=8, a=0 spontaneous ignition <10%",observed=float(fs[0]),result="Pass" if fs[0]<0.1 else "Fail")]
ER.write(H,"SIM-R5-C0",P,[f"{H}/outputs/{x}" for x in ("results.json","late_activity_strong.csv","late_activity_weak.csv")],chk,t0)
