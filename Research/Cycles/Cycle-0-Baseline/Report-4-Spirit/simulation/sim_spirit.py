import os, sys, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); P=json.load(open(f"{H}/params.json")); t0=ER.now(); os.makedirs(f"{H}/outputs",exist_ok=True)
def ev(rr):
    r=1/rr if rr<1 else rr; return r+np.sqrt(r*(r-1))
conv=lambda hr:(1-0.5**np.sqrt(hr))/(1-0.5**np.sqrt(1/hr))   # S14 common-outcome HR->RR approximation
B=lambda a,b:a*b/(a+b-1)                                      # bounding factor (S14)
res=dict(outcome_risk=P["deaths"]/P["n_cohort"],
 rare=dict(RR_point=P["HR"],E_point=ev(P["HR"]),E_CI=ev(P["CI"][1])),
 common=dict(RR_point=conv(P["HR"]),RR_CI=conv(P["CI"][1]),E_point=ev(conv(P["HR"])),E_CI=ev(conv(P["CI"][1]))))
RRstar=1/res["common"]["RR_point"]; E=res["common"]["E_point"]; m=P["mc"]
# Corrected confounding model (harm scale): exposure X = NON-attendance; causal effect of X on death = NONE (null).
# Unmeasured binary U raises death risk by RR_UD and is more prevalent among the exposed by RR_EU = P(U|X=1)/P(U|X=0).
# Worst-case allocation that attains the bound: P(U|X=1)=1, P(U|X=0)=1/RR_EU.  Bias = RR_UD / (1 + (RR_UD-1)/RR_EU) = B(RR_EU,RR_UD).
def mc(rr_eu,rr_ud,seed):
    rng=np.random.default_rng(seed); X=rng.random(m["n"])<m["p_exposed"]
    pU=np.where(X,1.0,1.0/rr_eu); U=rng.random(m["n"])<pU
    pD=np.where(U,m["q_baseline"]*rr_ud,m["q_baseline"]); D=rng.random(m["n"])<pD
    rr_harm=D[X].mean()/D[~X].mean(); return dict(crude_RR_nonattend_vs_attend=float(rr_harm),crude_RR_attend_vs_nonattend=float(1/rr_harm),analytic_bias=float(B(rr_eu,rr_ud)))
res["analytic_B_at_E"]=B(E,E); res["RR_star_harm_scale"]=RRstar
res["mc_at_E"]=mc(E,E,m["seed"]); res["mc_below_E"]=mc(E*m["below_E_factor"],E*m["below_E_factor"],m["seed"]+1); res["mc_weak"]=mc(m["weak"],m["weak"],m["seed"]+2)
json.dump(res,open(f"{H}/outputs/results.json","w"),indent=2)
tol=m["tolerance"]; obs=res["common"]["RR_point"]
chk=[dict(id="E1",expect="E-values > 1 (rare and common-outcome scales)",observed={k:round(v,3) for k,v in {"rare_E":res['rare']['E_point'],"common_E":E,"common_E_CI":res['common']['E_CI']}.items()},result="Pass" if E>1 and res['rare']['E_point']>1 else "Fail"),
 dict(id="E2a",expect=f"analytic bounding factor B(E,E) equals observed harm-scale RR* = {RRstar:.4f} (|diff|<1e-9)",observed=round(res["analytic_B_at_E"],6),result="Pass" if abs(res["analytic_B_at_E"]-RRstar)<1e-9 else "Fail"),
 dict(id="E2",expect=f"null causal effect + confounder at RR_EU=RR_UD=E reproduces observed RR {obs:.3f} within ±{tol}",observed=round(res["mc_at_E"]["crude_RR_attend_vs_nonattend"],4),result="Pass" if abs(res["mc_at_E"]["crude_RR_attend_vs_nonattend"]-obs)<=tol else "Fail"),
 dict(id="E2b",expect=f"confounder at 0.9×E cannot reach observed RR: crude RR > {obs:.3f}+{tol}",observed=round(res["mc_below_E"]["crude_RR_attend_vs_nonattend"],4),result="Pass" if res["mc_below_E"]["crude_RR_attend_vs_nonattend"]>obs+tol else "Fail"),
 dict(id="E3",expect="weak confounding (1.2,1.2) under null gives crude RR > 0.9",observed=round(res["mc_weak"]["crude_RR_attend_vs_nonattend"],4),result="Pass" if res["mc_weak"]["crude_RR_attend_vs_nonattend"]>0.9 else "Fail")]
ER.write(H,"SIM-R4-C0",P,[f"{H}/outputs/results.json"],chk,t0)
