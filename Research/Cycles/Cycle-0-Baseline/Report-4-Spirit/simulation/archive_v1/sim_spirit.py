import os, sys, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); P=json.load(open(f"{H}/params.json")); t0=ER.now(); os.makedirs(f"{H}/outputs",exist_ok=True)
def ev(rr):
    r=1/rr if rr<1 else rr; return r+np.sqrt(r*(r-1))
conv=lambda hr:(1-0.5**np.sqrt(hr))/(1-0.5**np.sqrt(1/hr))
res=dict(outcome_risk=P["deaths"]/P["n_cohort"],
 rare=dict(RR_point=P["HR"],E_point=ev(P["HR"]),E_CI=ev(P["CI"][1])),
 common=dict(RR_point=conv(P["HR"]),RR_CI=conv(P["CI"][1]),E_point=ev(conv(P["HR"])),E_CI=ev(conv(P["CI"][1]))))
m=P["mc"]
def mc(s,seed):
    rng=np.random.default_rng(seed); U=rng.random(m["n"])<m["pU"]
    # U=1 is "healthier": more attendance (RR_EU) and lower death (1/RR_UD)
    pa=np.where(U,min(1,m["p_attend_U0"]*s),m["p_attend_U0"]); A=rng.random(m["n"])<pa
    pd_=np.where(U,m["p_death_U0"]/s,m["p_death_U0"]); D=rng.random(m["n"])<pd_
    return float(D[A].mean()/D[~A].mean())
E=res["common"]["E_point"]; res["mc_at_E"]=mc(E,m["seed"]); res["mc_weak"]=mc(m["weak"],m["seed"])
json.dump(res,open(f"{H}/outputs/results.json","w"),indent=2)
chk=[dict(id="E1",expect="E-values > 1",observed={k:round(v,3) for k,v in {"rare_E":res['rare']['E_point'],"common_E":E,"common_E_CI":res['common']['E_CI']}.items()},result="Pass" if E>1 else "Fail"),
 dict(id="E2",expect=f"crude RR at E <= {res['common']['RR_point']:.3f}+0.02",observed=round(res["mc_at_E"],4),result="Pass" if res["mc_at_E"]<=res["common"]["RR_point"]+0.02 else "Fail"),
 dict(id="E3",expect="weak confounding crude RR > 0.9",observed=round(res["mc_weak"],4),result="Pass" if res["mc_weak"]>0.9 else "Fail")]
ER.write(H,"SIM-R4-C0",P,[f"{H}/outputs/results.json"],chk,t0)
