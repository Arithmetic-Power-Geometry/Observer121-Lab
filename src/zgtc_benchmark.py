from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
from statistics import mean
from typing import List, Tuple
import csv, json, math, random

N=11
Cell=Tuple[int,int]
Matrix=List[List[int]]

@dataclass
class Hypothesis:
    name:str
    matrix:Matrix

@dataclass
class Trial:
    world_seed:int
    solver:str
    queries:int
    identified:bool
    survivors:int
    crash_count:int
    rectangle_queries:int
    mean_elimination_per_query:float

def diag():
    return [(i,i) for i in range(N)]

def offdiag():
    return [(i,j) for i in range(N) for j in range(N) if i!=j]

def rectangles():
    return [(i,j) for i in range(N) for j in range(i+1,N)]

def make_base(seed:int):
    r=random.Random(seed)
    a=[r.randint(-10,10) for _ in range(N)]
    b=[r.randint(-10,10) for _ in range(N)]
    return [[a[i]+b[j] for j in range(N)] for i in range(N)]

def mutate(M, r, mode):
    X=[row[:] for row in M]
    if mode=="single":
        i,j=r.choice(offdiag()); X[i][j]+=r.choice([3,5,7,11])
    elif mode=="rectangle":
        i,j=r.choice(rectangles())
        X[i][j]+=r.choice([4,6,9]); X[j][i]-=r.choice([2,5,8])
    elif mode=="observer_shift":
        j=r.randrange(N); delta=r.choice([2,4,6])
        for i in range(N):
            if i!=j: X[i][j]+=delta*((i+j)%3-1)
    elif mode=="system_shift":
        i=r.randrange(N); delta=r.choice([2,4,6])
        for j in range(N):
            if i!=j: X[i][j]+=delta*((i+j)%3-1)
    elif mode=="multi":
        for _ in range(r.randint(2,5)):
            i,j=r.choice(offdiag()); X[i][j]+=r.choice([-9,-6,-3,3,6,9])
    return X

def make_hypotheses(seed:int, n_h=32):
    r=random.Random(seed)
    base=make_base(seed)
    hyps=[Hypothesis("H00_base",base)]
    modes=["single","rectangle","observer_shift","system_shift","multi"]
    dvals=[base[i][i] for i in range(N)]
    seen={tuple(tuple(row) for row in base)}
    attempts=0
    while len(hyps)<n_h and attempts<10000:
        attempts+=1
        m=mutate(base,r,r.choice(modes))
        for i in range(N): m[i][i]=dvals[i]
        key=tuple(tuple(row) for row in m)
        if key in seen:
            continue
        seen.add(key)
        hyps.append(Hypothesis(f"H{len(hyps):02d}",m))
    if len(hyps)!=n_h:
        raise RuntimeError("Could not generate enough unique hypotheses")
    return hyps

def survivors_after(hyps, obs):
    out=[]
    for h in hyps:
        if all(h.matrix[c[0]][c[1]]==v for c,v in obs.items()):
            out.append(h)
    return out

def elimination_score(c, surv):
    groups={}
    for h in surv:
        v=h.matrix[c[0]][c[1]]
        groups[v]=groups.get(v,0)+1
    total=len(surv)
    return total-sum(n*n for n in groups.values())/total

def gap_score(c, surv):
    vals=[h.matrix[c[0]][c[1]] for h in surv]
    return max(vals)-min(vals) if vals else 0

def zigzag_score(c, queried):
    i,j=c
    d=abs(i-j)
    if not queried: return d
    return d+0.5*min(abs(i-a)+abs(j-b) for a,b in queried)

def rectangle_bonus(c, obs):
    bonus=0.0
    for a,b in rectangles():
        rect={(a,a),(a,b),(b,a),(b,b)}
        if c in rect:
            known=len(rect.intersection(obs.keys()))
            if known>=2: bonus=max(bonus,known/4)
    return bonus

def choose_random(cands,surv,obs,r):
    return r.choice(cands)

def choose_zigzag(cands,surv,obs,r):
    return max(cands,key=lambda c:(zigzag_score(c,list(obs.keys())),r.random()))

def choose_disagreement(cands,surv,obs,r):
    return max(cands,key=lambda c:(elimination_score(c,surv),gap_score(c,surv),r.random()))

def choose_rectangle(cands,surv,obs,r):
    return max(cands,key=lambda c:(rectangle_bonus(c,obs),elimination_score(c,surv),r.random()))

def choose_zgtc(cands,surv,obs,r):
    vals=[]
    for c in cands:
        z=zigzag_score(c,list(obs.keys()))
        g=gap_score(c,surv)
        t=elimination_score(c,surv)
        rb=rectangle_bonus(c,obs)
        score=0.18*z+0.22*math.log1p(g)+0.50*t+0.10*rb*len(surv)
        vals.append((score,t,g,z,rb,r.random(),c))
    return max(vals)[-1]

SOLVERS={
    "random":choose_random,
    "zigzag_only":choose_zigzag,
    "disagreement_greedy":choose_disagreement,
    "rectangle_attack":choose_rectangle,
    "zigzag_gap_target_crash":choose_zgtc,
}

def stable_solver_seed(name:str)->int:
    return sum((i+1)*ord(ch) for i,ch in enumerate(name))

def run_trial(seed,solver_name,n_h=32):
    hyps=make_hypotheses(seed,n_h)
    truth=hyps[random.Random(seed^0xABC121).randrange(len(hyps))]
    obs={(i,i):truth.matrix[i][i] for i in range(N)}
    surv=survivors_after(hyps,obs)
    chooser=SOLVERS[solver_name]
    rng=random.Random(seed ^ stable_solver_seed(solver_name))
    queried=[]; crashes=0; rectq=0; eliminations=[]
    while len(surv)>1 and len(queried)<110:
        cands=[c for c in offdiag() if c not in queried]
        c=chooser(cands,surv,obs,rng)
        before=len(surv)
        if rectangle_bonus(c,obs)>0: rectq+=1
        v=truth.matrix[c[0]][c[1]]
        obs[c]=v; queried.append(c)
        surv=survivors_after(surv,{c:v})
        killed=before-len(surv)
        if killed>0: crashes+=1
        eliminations.append(killed)
    return Trial(seed,solver_name,len(queried),len(surv)==1,len(surv),crashes,rectq,
                 mean(eliminations) if eliminations else 0.0)

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    rows=[]
    for seed in range(500):
        for s in SOLVERS:
            rows.append(asdict(run_trial(seed,s)))
    with (out/"comparison_results.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    summary=[]
    for s in SOLVERS:
        rr=[x for x in rows if x["solver"]==s]
        summary.append({
            "solver":s,
            "trials":len(rr),
            "identification_rate":mean(float(x["identified"]) for x in rr),
            "mean_queries":mean(x["queries"] for x in rr),
            "median_queries":sorted(x["queries"] for x in rr)[len(rr)//2],
            "mean_crash_events":mean(x["crash_count"] for x in rr),
            "mean_rectangle_queries":mean(x["rectangle_queries"] for x in rr),
            "mean_elimination_per_query":mean(x["mean_elimination_per_query"] for x in rr),
        })
    with (out/"comparison_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(summary[0].keys())); w.writeheader(); w.writerows(summary)
    (out/"comparison_summary.json").write_text(json.dumps(summary,indent=2))
    best=min(summary,key=lambda x:x["mean_queries"])
    lines=["# Observer121 ZGTC benchmark report","",
           "500 hypothesis-identification trials; 32 mutually diagonal-equivalent hypotheses per trial.","",
           "| Solver | ID rate | Mean queries | Median | Crash events | Rectangle queries | Elimination/query |",
           "|---|---:|---:|---:|---:|---:|---:|"]
    for s in summary:
        lines.append(f"| {s['solver']} | {s['identification_rate']:.3f} | {s['mean_queries']:.3f} | {s['median_queries']} | {s['mean_crash_events']:.3f} | {s['mean_rectangle_queries']:.3f} | {s['mean_elimination_per_query']:.3f} |")
    lines += ["",f"Lowest mean query count: **{best['solver']}** ({best['mean_queries']:.3f}).",
              "","Controlled synthetic benchmark only; not evidence of universal superiority."]
    (out/"REPORT.md").write_text("\n".join(lines))
    print("\n".join(lines))

if __name__=="__main__":
    main()
