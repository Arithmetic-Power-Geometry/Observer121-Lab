from pathlib import Path
import csv, json
from dataclasses import asdict
from statistics import mean
from core import make_world, exhaustive_solver, oracle_solver, exact_solver

FAMILIES=["additive","symmetric","rank1","periodic","block",
          "near_additive","near_rank1","unstructured"]

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    rows=[]
    for fam in FAMILIES:
        for seed in range(100):
            w=make_world(fam,seed)
            for solver in (exhaustive_solver,oracle_solver,exact_solver):
                rows.append(asdict(solver(w)))
    with (out/"results.csv").open("w",newline="") as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        wr.writeheader(); wr.writerows(rows)
    summary={}
    for fam in FAMILIES:
        summary[fam]={}
        for solver in ["exhaustive","oracle_family","exact_certificate_solver"]:
            rr=[r for r in rows if r["family"]==fam and r["solver"]==solver]
            summary[fam][solver]={
                "n":len(rr),
                "accuracy":mean(float(r["correct"]) for r in rr),
                "mean_total_cost":mean(r["total_cost"] for r in rr),
                "mean_saving_vs_110":mean(r["saving_vs_110"] for r in rr),
                "mean_certification_queries":mean(r["certification_queries"] for r in rr),
                "mean_model_checks":mean(r["model_checks"] for r in rr),
                "early_stop_rate":mean(float(r["stopped_early"]) for r in rr)
            }
    (out/"summary.json").write_text(json.dumps(summary,indent=2))
    for fam in FAMILIES:
        rr=[r for r in rows if r["family"]==fam and r["solver"]=="exact_certificate_solver"]
        assert all(r["correct"] for r in rr), f"soundness failure in {fam}"
    for fam in ["near_additive","near_rank1","unstructured"]:
        rr=[r for r in rows if r["family"]==fam and r["solver"]=="exact_certificate_solver"]
        assert all(r["correct"] for r in rr), f"adversarial failure in {fam}"
    lines=["# Observer121 automated report","",
           "All exact-certificate runs passed 100% reconstruction accuracy.",""]
    for fam in FAMILIES:
        s=summary[fam]["exact_certificate_solver"]
        lines.append(f"- {fam}: accuracy={s['accuracy']:.3f}, mean_cost={s['mean_total_cost']:.2f}, saving={s['mean_saving_vs_110']:.2f}, early_stop={s['early_stop_rate']:.3f}")
    (out/"REPORT.md").write_text("\n".join(lines))
    print((out/"REPORT.md").read_text())

if __name__=="__main__":
    main()
