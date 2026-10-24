import json, os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); P=json.load(open(f"{H}/params.json")); t0=ER.now()
def run(kp,ki,D,sigma,seed):
    rng=np.random.default_rng(seed); n=int(P["T"]/P["dt"]); x=0.0; I=0.0; xs=np.empty(n)
    for k in range(n):
        t=k*P["dt"]; e=x; I+=e*P["dt"]
        u=np.clip(-kp*e-ki*I,-P["u_max"],P["u_max"]); d=D if t>=P["t_d"] else 0.0
        x+=(-P["k_l"]*x+u+d)*P["dt"]+sigma*np.sqrt(P["dt"])*rng.standard_normal(); xs[k]=x
    return xs
s=P["seed"]; dg=P["degrade"]; tail=slice(int(50/P["dt"]),None)
R={"none":run(0,0,P["D"],0,s),"P":run(P["k_p"],0,P["D"],0,s),"PI":run(P["k_p"],P["k_i"],P["D"],P["sigma"],s),
   "PI_degraded":run(P["k_p"]*dg,P["k_i"]*dg,P["D"],P["sigma"],s),"PI_saturated":run(P["k_p"],P["k_i"],P["D_sat"],0,s)}
def rec_time(xs,tol=0.05):
    after=xs[int(P["t_d"]/P["dt"]):]; pk=np.argmax(np.abs(after))
    idx=np.where(np.abs(after[pk:])<tol)[0]; return float((pk+idx[0])*P["dt"]) if len(idx) else None
summ={k:dict(final_mean=float(v[tail].mean()),peak=float(np.max(np.abs(v))),recovery_time=rec_time(v)) for k,v in R.items()}
os.makedirs(f"{H}/outputs",exist_ok=True)
json.dump(summ,open(f"{H}/outputs/summary.json","w"),indent=2)
np.savetxt(f"{H}/outputs/trajectories.csv",np.column_stack([np.arange(len(R['P']))*P['dt']]+list(R.values()))[::10],delimiter=",",header="t,"+",".join(R),comments="",fmt="%.6f")
a1=P["D"]/P["k_l"]; a2=P["D"]/(P["k_l"]+P["k_p"])
# none: not converged by T=60 (tau=10), so compare to analytic transient value
an_none=a1*(1-np.exp(-P["k_l"]*(P["T"]-P["t_d"])))
chk=[dict(id="E1",expect=f"no-control x(T) = analytic {an_none:.3f} (tends to {a1})",observed=round(float(R['none'][-1]),4),result="Pass" if abs(R['none'][-1]-an_none)/an_none<0.01 else "Fail"),
 dict(id="E2",expect=f"P steady error {a2:.4f}",observed=round(summ['P']['final_mean'],4),result="Pass" if abs(summ['P']['final_mean']-a2)/a2<0.01 else "Fail"),
 dict(id="E3",expect="|PI tail mean|<0.02",observed=round(summ['PI']['final_mean'],4),result="Pass" if abs(summ['PI']['final_mean'])<0.02 else "Fail"),
 dict(id="E4",expect="degraded peak > intact peak and slower recovery",observed=[summ['PI_degraded']['peak'],summ['PI']['peak'],summ['PI_degraded']['recovery_time'],summ['PI']['recovery_time']],
      result="Pass" if summ['PI_degraded']['peak']>summ['PI']['peak'] and (summ['PI_degraded']['recovery_time'] is None or summ['PI_degraded']['recovery_time']>summ['PI']['recovery_time']) else "Fail"),
 dict(id="E5",expect="saturated PI final |x| > 0.05",observed=round(summ['PI_saturated']['final_mean'],4),result="Pass" if abs(summ['PI_saturated']['final_mean'])>0.05 else "Fail")]
ER.write(H,"SIM-R1-C0",P,[f"{H}/outputs/summary.json",f"{H}/outputs/trajectories.csv"],chk,t0)
