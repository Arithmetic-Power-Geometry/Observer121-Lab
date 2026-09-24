from pathlib import Path
import csv, json

def additive_minimum(m,n):
    # y_ij = mu + alpha_i + beta_j with reference constraints.
    # Parameter dimension = 1+(m-1)+(n-1)=m+n-1.
    # Observed cells are edges of K_{m,n}; connectedness gives estimability.
    return m+n-1

def unrestricted_minimum(m,n):
    # One free mean per cell: saturated interaction model.
    return m*n

def rectangle_interaction_minimum():
    # y11-y12-y21+y22 requires its four coefficients for unrestricted cell means.
    return 4

def main():
    out=Path("artifacts/attribution-minimum"); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for m,n in [(2,2),(3,3),(5,5),(11,11),(11,7)]:
        rows.append({
            "systems":m,"observers":n,"worlds":m*n,
            "additive_min_cells":additive_minimum(m,n),
            "unrestricted_min_cells":unrestricted_minimum(m,n),
            "additive_fraction":additive_minimum(m,n)/(m*n),
            "unrestricted_fraction":1.0
        })
    with (out/"minimum_cells.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    (out/"minimum_cells.json").write_text(json.dumps(rows,indent=2))
    r=[x for x in rows if x["systems"]==11 and x["observers"]==11][0]
    report=f"""# Observer121 minimum-attribution-set kill test

For an m x n observation grid:

1. Additive model y_ij = mu + alpha_i + beta_j:
   parameter dimension is m+n-1. Observed cells form edges of a bipartite graph.
   A connected spanning observation graph is sufficient, and any connected graph
   needs at least m+n-1 edges. Therefore the exact minimum is m+n-1.

2. Saturated/unrestricted cell model:
   each cell has an independent mean, so exact reconstruction/estimation of all
   cell effects requires mn observations.

3. A single unrestricted 2x2 interaction contrast
   y11-y12-y21+y22 requires the four cells entering that contrast.

For Observer121 (11 x 11):
- total worlds: {r['worlds']}
- additive minimum: {r['additive_min_cells']}
- unrestricted minimum: {r['unrestricted_min_cells']}

AESHO decision:
These minima are useful calibration boundaries, but they reduce to classical
linear-model rank/connected-design logic. They are not presented as a new
foundational theorem.
"""
    (out/"REPORT.md").write_text(report); print(report)
if __name__=="__main__": main()
