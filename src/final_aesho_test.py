from pathlib import Path
from statistics import mean, median
import csv,json,random
SIZES=[5,11,21,51]
SEEDS=range(200)
def equality_search(n,z,order):
    q=0; trace=[]; remaining=set(range(n))
    for k in order:
        q+=1; ans=(z==k)
        trace.append({"q":q,"type":"primitive_equality","arg":k,"answer":ans,"remaining_before":len(remaining)})
        if ans:return q,trace
        remaining.discard(k)
        if len(remaining)==1:return q,trace
    return q,trace
def generated_balanced(n,z,generation_cost=1.0):
    remaining=list(range(n)); q=0; gen=0.0; trace=[]
    while len(remaining)>1:
        half=len(remaining)//2; A=set(remaining[:half]); gen+=generation_cost; q+=1; ans=z in A
        trace.append({"q":q,"type":"generated_subset","subset_size":len(A),"answer":ans,"remaining_before":len(remaining),"generation_cost":generation_cost})
        remaining=[x for x in remaining if (x in A)==ans]
    return q,gen,trace
def compiled_balanced(n,z):
    remaining=list(range(n)); q=0; trace=[]
    while len(remaining)>1:
        half=len(remaining)//2; A=set(remaining[:half]); q+=1; ans=z in A
        trace.append({"q":q,"type":"precompiled_subset","subset_size":len(A),"answer":ans,"remaining_before":len(remaining)})
        remaining=[x for x in remaining if (x in A)==ans]
    return q,trace
def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True); rows=[]; audit=[]
    for n in SIZES:
        for seed in SEEDS:
            r=random.Random(100000*n+seed); z=r.randrange(n); order=list(range(n)); r.shuffle(order)
            qp,tp=equality_search(n,z,order); qg,cg,tg=generated_balanced(n,z); qc,tc=compiled_balanced(n,z)
            rows += [{"n":n,"seed":seed,"method":"primitive_fixed","queries":qp,"generation_cost":0.0,"total_cost":qp},
                     {"n":n,"seed":seed,"method":"generated_balanced","queries":qg,"generation_cost":cg,"total_cost":qg+cg},
                     {"n":n,"seed":seed,"method":"compiled_balanced","queries":qc,"generation_cost":0.0,"total_cost":qc}]
            if seed<2:audit.append({"n":n,"seed":seed,"target":z,"primitive":tp,"generated":tg,"compiled":tc})
    with(out/"scaling_results.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    summ=[]
    for n in SIZES:
        for m in ["primitive_fixed","generated_balanced","compiled_balanced"]:
            R=[x for x in rows if x["n"]==n and x["method"]==m]
            summ.append({"n":n,"method":m,"trials":len(R),"mean_queries":mean(x["queries"] for x in R),
              "median_queries":median(x["queries"] for x in R),"mean_generation_cost":mean(x["generation_cost"] for x in R),
              "mean_total_cost":mean(x["total_cost"] for x in R)})
    with(out/"scaling_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=summ[0]); w.writeheader(); w.writerows(summ)
    (out/"scaling_summary.json").write_text(json.dumps(summ,indent=2))
    (out/"sequential_audit.json").write_text(json.dumps(audit,indent=2))
    (out/"compilation_audit.json").write_text(json.dumps([{"n":n,"universal_subset_library_size":2**n,"bits_to_index_library":n} for n in SIZES],indent=2))
    lines=["# Observer121 v6 — Final AESHO Compilation Attack","","| n | primitive fixed mean queries | generated queries | generated charged total | compiled balanced queries | universal subset library |","|---:|---:|---:|---:|---:|---:|"]
    for n in SIZES:
        d={x["method"]:x for x in summ if x["n"]==n}
        lines.append(f"| {n} | {d['primitive_fixed']['mean_queries']:.3f} | {d['generated_balanced']['mean_queries']:.3f} | {d['generated_balanced']['mean_total_cost']:.3f} | {d['compiled_balanced']['mean_queries']:.3f} | {2**n} |")
    lines += ["","AESHO verdict: generated intervention beats the restricted primitive library, but not a fixed library containing the same balanced subset tests.","","STOP criterion triggered: no positive foundational separation is established by this branch."]
    (out/"REPORT.md").write_text("\n".join(lines)); print("\n".join(lines))
if __name__=="__main__":main()
