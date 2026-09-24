from pathlib import Path
from math import comb
import csv, json

N=121
BASE=21
H=N-BASE
DELTAS=[0.10,0.05,0.01,0.001]
KS=[1,2,5,10,20,50,100]

def miss_prob(H,K,s):
    if s>H: return 0.0
    if s>H-K: return 0.0
    return comb(H-K,s)/comb(H,s)

def min_sample(H,K,delta):
    for s in range(H+1):
        if miss_prob(H,K,s)<=delta:
            return s
    return H

def main():
    out=Path("artifacts/assurance-frontier"); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for K in KS:
        for delta in DELTAS:
            s=min_sample(H,K,delta)
            rows.append({
                "total_worlds":N,"base_attribution_cells":BASE,
                "unchecked_cells":H,"minimum_violating_cells":K,
                "minimum_violation_fraction":K/H,
                "delta":delta,"audit_sample":s,
                "total_evidence_cost":BASE+s,
                "saving_vs_full":N-(BASE+s),
                "miss_probability":miss_prob(H,K,s)
            })
    with (out/"frontier.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    (out/"frontier.json").write_text(json.dumps(rows,indent=2))
    lines=["# Observer121 finite-population assurance frontier","",
      f"Base additive attribution design: {BASE} cells; unchecked population H={H}.",
      "Assumption: if additivity is false, at least K of the H unchecked cells violate the additive prediction.",
      "Audit: sample unchecked cells uniformly without replacement.",
      "Exact miss probability: C(H-K,s)/C(H,s).","",
      "| K violations | delta | audit s | total cost | saving vs 121 |",
      "|---:|---:|---:|---:|---:|"]
    for r in rows:
        lines.append(f"| {r['minimum_violating_cells']} | {r['delta']:.3g} | {r['audit_sample']} | {r['total_evidence_cost']} | {r['saving_vs_full']} |")
    lines += ["",
      "Boundary: K=1 is the single-hidden-defect adversary. To make miss probability <= delta, sampling without replacement must inspect at least ceil((1-delta)H) unchecked cells; as delta approaches 0 the cost approaches full inspection.",
      "This frontier is a finite-population sampling calculation, not a new property-testing theorem."]
    (out/"REPORT.md").write_text("\n".join(lines)); print("\n".join(lines))
if __name__=="__main__": main()
