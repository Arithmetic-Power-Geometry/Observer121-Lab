from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
import random

N = 11
Cell = Tuple[int,int]
Matrix = List[List[int]]

@dataclass
class World:
    family: str
    seed: int
    matrix: Matrix
    metadata: Dict

@dataclass
class RunResult:
    family: str
    seed: int
    solver: str
    correct: bool
    total_cost: float
    offdiag_observations: int
    certification_queries: int
    model_checks: int
    inferred_family: str
    stopped_early: bool
    saving_vs_110: float

def diag_cells():
    return [(i,i) for i in range(N)]

def offdiag_cells():
    return [(i,j) for i in range(N) for j in range(N) if i!=j]

def make_world(family:str, seed:int)->World:
    rng=random.Random(seed)
    if family=="additive":
        a=[rng.randint(-20,20) for _ in range(N)]
        b=[rng.randint(-20,20) for _ in range(N)]
        M=[[a[i]+b[j] for j in range(N)] for i in range(N)]
        return World(family,seed,M,{"a":a,"b":b})
    if family=="symmetric":
        M=[[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(i,N):
                v=rng.randint(-50,50)
                M[i][j]=M[j][i]=v
        return World(family,seed,M,{})
    if family=="rank1":
        u=[rng.choice([x for x in range(-7,8) if x]) for _ in range(N)]
        v=[rng.choice([x for x in range(-7,8) if x]) for _ in range(N)]
        M=[[u[i]*v[j] for j in range(N)] for i in range(N)]
        return World(family,seed,M,{"u":u,"v":v})
    if family=="periodic":
        p=rng.choice([3,4,5])
        a=rng.randint(1,6); b=rng.randint(1,6); c=rng.randint(-5,5)
        M=[[a*(i%p)+b*(j%p)+c for j in range(N)] for i in range(N)]
        return World(family,seed,M,{"period":p})
    if family=="block":
        rg=[rng.randrange(3) for _ in range(N)]
        cg=[rng.randrange(3) for _ in range(N)]
        table=[[rng.randint(-25,25) for _ in range(3)] for _ in range(3)]
        M=[[table[rg[i]][cg[j]] for j in range(N)] for i in range(N)]
        return World(family,seed,M,{"rg":rg,"cg":cg})
    if family=="near_additive":
        a=[rng.randint(-20,20) for _ in range(N)]
        b=[rng.randint(-20,20) for _ in range(N)]
        M=[[a[i]+b[j] for j in range(N)] for i in range(N)]
        defect=rng.choice(offdiag_cells())
        M[defect[0]][defect[1]] += rng.choice([7,11,13,17])
        return World(family,seed,M,{"defect":defect})
    if family=="near_rank1":
        u=[rng.choice([x for x in range(-7,8) if x]) for _ in range(N)]
        v=[rng.choice([x for x in range(-7,8) if x]) for _ in range(N)]
        M=[[u[i]*v[j] for j in range(N)] for i in range(N)]
        defect=rng.choice(offdiag_cells())
        M[defect[0]][defect[1]] += rng.choice([5,9,17])
        return World(family,seed,M,{"defect":defect})
    if family=="unstructured":
        M=[[rng.randint(-100,100) for _ in range(N)] for _ in range(N)]
        return World(family,seed,M,{})
    raise ValueError(family)

class Oracle:
    def __init__(self, world:World):
        self.world=world
        self.obs={}
        for c in diag_cells():
            self.obs[c]=world.matrix[c[0]][c[1]]
        self.obs_queries=0
        self.cert_queries=0
    def get(self,c:Cell,cert=False):
        if c not in self.obs:
            self.obs[c]=self.world.matrix[c[0]][c[1]]
            if cert: self.cert_queries += 1
            else: self.obs_queries += 1
        return self.obs[c]

def predict_additive(o:Oracle)->Matrix:
    for j in range(1,N): o.get((0,j),cert=True)
    for i in range(1,N): o.get((i,0),cert=True)
    return [[o.obs[(i,0)] + o.obs[(0,j)] - o.obs[(0,0)] for j in range(N)] for i in range(N)]

def predict_rank1(o:Oracle)->Optional[Matrix]:
    for j in range(1,N): o.get((0,j),cert=True)
    for i in range(1,N): o.get((i,0),cert=True)
    m00=o.obs[(0,0)]
    if m00==0: return None
    pred=[]
    for i in range(N):
        row=[]
        for j in range(N):
            num=o.obs[(i,0)]*o.obs[(0,j)]
            if num % m00 != 0: return None
            row.append(num//m00)
        pred.append(row)
    return pred

def predict_symmetric(o:Oracle)->Matrix:
    pred=[[0]*N for _ in range(N)]
    for i in range(N): pred[i][i]=o.obs[(i,i)]
    for i in range(N):
        for j in range(i+1,N):
            v=o.get((i,j),cert=True)
            pred[i][j]=pred[j][i]=v
    return pred

def exact_solver(world:World, model_check_cost=0.25, query_cost=1.0)->RunResult:
    o=Oracle(world)
    model_checks=0
    stopped=False
    inferred="fallback"
    pred=None
    for h in ["additive","rank1","symmetric"]:
        model_checks += 1
        if h=="additive":
            p=predict_additive(o)
            ok=True
            for c in offdiag_cells():
                if o.get(c,cert=True)!=p[c[0]][c[1]]:
                    ok=False; break
            if ok:
                pred=p; inferred=h; stopped=True; break
        elif h=="rank1":
            p=predict_rank1(o)
            if p is None: continue
            ok=True
            for c in offdiag_cells():
                if o.get(c,cert=True)!=p[c[0]][c[1]]:
                    ok=False; break
            if ok:
                pred=p; inferred=h; stopped=True; break
        elif h=="symmetric":
            ok=True
            for i in range(N):
                for j in range(i+1,N):
                    a=o.get((i,j),cert=True); b=o.get((j,i),cert=True)
                    if a!=b:
                        ok=False; break
                if not ok: break
            if ok:
                pred=[[0]*N for _ in range(N)]
                for i in range(N):
                    pred[i][i]=o.obs[(i,i)]
                for i in range(N):
                    for j in range(i+1,N):
                        pred[i][j]=pred[j][i]=o.obs[(i,j)]
                inferred=h; stopped=True; break
    if pred is None:
        for c in offdiag_cells():
            o.get(c,cert=False)
        pred=[[o.obs[(i,j)] for j in range(N)] for i in range(N)]
    correct=(pred==world.matrix)
    total=(o.obs_queries+o.cert_queries)*query_cost + model_checks*model_check_cost
    return RunResult(world.family,world.seed,"exact_certificate_solver",correct,total,
                     o.obs_queries,o.cert_queries,model_checks,inferred,stopped,
                     110-total)

def oracle_solver(world:World)->RunResult:
    o=Oracle(world)
    pred=None
    fam=world.family
    if fam=="additive":
        pred=predict_additive(o)
    elif fam=="rank1":
        pred=predict_rank1(o)
    elif fam=="symmetric":
        pred=predict_symmetric(o)
    else:
        for c in offdiag_cells(): o.get(c)
        pred=[[o.obs[(i,j)] for j in range(N)] for i in range(N)]
    total=o.obs_queries+o.cert_queries
    return RunResult(fam,world.seed,"oracle_family",pred==world.matrix,total,
                     o.obs_queries,o.cert_queries,0,fam,True,110-total)

def exhaustive_solver(world:World)->RunResult:
    o=Oracle(world)
    for c in offdiag_cells(): o.get(c)
    pred=[[o.obs[(i,j)] for j in range(N)] for i in range(N)]
    total=o.obs_queries
    return RunResult(world.family,world.seed,"exhaustive",pred==world.matrix,total,
                     o.obs_queries,0,0,"none",False,110-total)
