from pathlib import Path
import csv, json, random

N=11
SEEDS=range(500)

def tree_edges(n=N):
    # star spanning tree: first row + first column, 2n-1 cells
    return {(0,j) for j in range(n)} | {(i,0) for i in range(1,n)}

def additive_matrix(rng,n=N):
    a=[rng.randint(-20,20) for _ in range(n)]
    b=[rng.randint(-20,20) for _ in range(n)]
    return [[a[i]+b[j] for j in range(n)] for i in range(n)]

def reconstruct_from_tree(Y,n=N):
    # exact for additive matrices
    base=Y[0][0]
    return [[Y[i][0]+Y[0][j]-base for j in range(n)] for i in range(n)]

def inject_single_hidden_defect(Y,rng,observed,n=N):
    hidden=[(i,j) for i in range(n) for j in range(n) if (i,j) not in observed]
    i,j=rng.choice(hidden)
    Z=[row[:] for row in Y]
    Z[i][j]+=rng.choice([d for d in range(-9,10) if d])
    return Z,(i,j)

def exact_certificate(Y,observed,n=N):
    pred=reconstruct_from_tree(Y,n)
    checked=set(observed)
    for i in range(n):
        for j in range(n):
            if (i,j) in checked: continue
            checked.add((i,j))
            if Y[i][j]!=pred[i][j]:
                return False,len(checked)
    return True,len(checked)

def main():
    out=Path("artifacts/justified-attribution"); out.mkdir(parents=True,exist_ok=True)
    observed=tree_edges()
    rows=[]
    for seed in SEEDS:
        rng=random.Random(121000+seed)
        A=additive_matrix(rng)
        ok,cost=exact_certificate(A,observed)
        rows.append({"seed":seed,"world":"additive","attribution_cells":len(observed),
                     "certificate_result":ok,"total_cells_examined":cost})
        B,loc=inject_single_hidden_defect(A,rng,observed)
        ok,cost=exact_certificate(B,observed)
        rows.append({"seed":seed,"world":"single_hidden_interaction",
                     "attribution_cells":len(observed),"certificate_result":ok,
                     "total_cells_examined":cost,"defect_i":loc[0],"defect_j":loc[1]})
    with (out/"trials.csv").open("w",newline="") as f:
        fields=sorted({k for r in rows for k in r})
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    summary={
      "n":N,"worlds":N*N,"additive_attribution_cells":len(observed),
      "hidden_cells_after_attribution":N*N-len(observed),
      "exact_unrestricted_certification_worst_case":N*N,
      "saving_if_additivity_is_promised":N*N-len(observed),
      "worst_case_saving_after_exact_certification":0
    }
    (out/"summary.json").write_text(json.dumps(summary,indent=2))
    report=f"""# Observer121 justified-attribution audit

Grid: {N} x {N} = {N*N} worlds.

A connected spanning-tree design uses {len(observed)} cells and exactly reconstructs an additive row+observer model.

However, after those {len(observed)} observations there are {N*N-len(observed)} unobserved cells. Against an unrestricted alternative, any one of them can contain a single interaction defect while agreeing with the additive model on every previously observed cell.

Therefore:
- attribution cost under a trusted additive promise: {len(observed)}
- worst-case exact certification cost against unrestricted alternatives: {N*N}
- worst-case exact saving after certification: 0

This is an exact adversarial statement for the declared unrestricted alternative, not an approximate property-testing claim.
"""
    (out/"REPORT.md").write_text(report); print(report)
if __name__=="__main__": main()
