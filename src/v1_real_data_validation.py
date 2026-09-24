from pathlib import Path
import csv, json, statistics
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

SEEDS=range(30)
BUDGETS=[10,20,40,80,120]

def fit_score(X,y,labeled,test):
    sc=StandardScaler().fit(X[labeled])
    model=LogisticRegression(max_iter=2000,solver="liblinear",random_state=0)
    model.fit(sc.transform(X[labeled]),y[labeled])
    return model,sc,accuracy_score(y[test],model.predict(sc.transform(X[test])))

def run(seed,mode,budget):
    rng=np.random.default_rng(seed)
    d=load_breast_cancer(); X=d.data; y=d.target
    idx=rng.permutation(len(y)); test=idx[:114]; pool=idx[114:]
    # matched seed set: ensure both classes
    pos=pool[y[pool]==1][:5]; neg=pool[y[pool]==0][:5]
    labeled=list(np.concatenate([pos,neg])); unl=[i for i in pool if i not in set(labeled)]
    while len(labeled)<budget and unl:
        if mode=="random":
            pick=int(rng.choice(unl))
        elif mode=="uncertainty":
            model,sc,_=fit_score(X,y,np.array(labeled),test)
            p=model.predict_proba(sc.transform(X[unl]))[:,1]
            pick=unl[int(np.argmin(np.abs(p-.5)))]
        else: raise ValueError(mode)
        labeled.append(pick); unl.remove(pick)
    _,_,acc=fit_score(X,y,np.array(labeled),test)
    return acc

def main():
    out=Path("artifacts/v1-real-data"); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for seed in SEEDS:
        for budget in BUDGETS:
            for mode in ("random","uncertainty"):
                rows.append({"seed":seed,"budget":budget,"policy":mode,
                             "accuracy":run(seed,mode,budget)})
    with (out/"trials.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    summary=[]
    for b in BUDGETS:
        for mode in ("random","uncertainty"):
            vals=[r["accuracy"] for r in rows if r["budget"]==b and r["policy"]==mode]
            summary.append({"budget":b,"policy":mode,"mean_accuracy":statistics.mean(vals),
                            "sd_accuracy":statistics.stdev(vals)})
    with (out/"summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=summary[0]); w.writeheader(); w.writerows(summary)
    (out/"summary.json").write_text(json.dumps(summary,indent=2))
    lines=["# Observer121 V1 real-data validation","",
      "Dataset: scikit-learn Wisconsin Diagnostic Breast Cancer.",
      "Model: logistic regression with training-only standardization.",
      "Matched controls: same train/test split, same initial labeled set, same label budget, same model and feature space. Only acquisition policy changes.",
      "",
      "| budget | random accuracy | uncertainty accuracy | delta |",
      "|---:|---:|---:|---:|"]
    for b in BUDGETS:
        a={x["policy"]:x["mean_accuracy"] for x in summary if x["budget"]==b}
        lines.append(f"| {b} | {a['random']:.4f} | {a['uncertainty']:.4f} | {a['uncertainty']-a['random']:+.4f} |")
    lines += ["",
      "Interpretation rule: because query language, model, data, feature representation, and label budget are matched, any reproducible difference here is a selection-policy effect within this experimental design. It is not evidence for a new active-learning theorem.",
      "This stage tests whether Observer121-style attribution remains meaningful on non-constructed data."]
    (out/"REPORT.md").write_text("\n".join(lines)); print("\n".join(lines))
if __name__=="__main__": main()
