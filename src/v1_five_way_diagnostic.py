from pathlib import Path
import csv, json, math, random, statistics

SIZES=[32,128,512,2048]
SEEDS=range(200)

def entropy(counts):
    n=sum(counts)
    return 0.0 if n==0 else -sum((c/n)*math.log2(c/n) for c in counts if c)

def primitive_order(n,z,order):
    q=0
    for k in order[:-1]:
        q+=1
        if z==k: return q
    return q

def adaptive_balanced(n,z):
    lo,hi,q=0,n,0
    while hi-lo>1:
        mid=(lo+hi)//2; q+=1
        if z<mid: hi=mid
        else: lo=mid
    return q

def fixed_bits(n,z):
    return math.ceil(math.log2(n))

def trial(n,seed):
    r=random.Random(121000+n*1000+seed); z=r.randrange(n)
    natural=list(range(n))
    shuffled=natural[:]; r.shuffle(shuffled)
    q_nat=primitive_order(n,z,natural)
    q_sel=primitive_order(n,z,shuffled)
    q_adapt=adaptive_balanced(n,z)
    q_rich=fixed_bits(n,z)
    # generated and compiled balanced are intentionally identical controls
    q_gen=q_adapt; q_comp=q_adapt
    explicit_nodes=n-1
    return dict(n=n,seed=seed,target=z,
        primitive_natural=q_nat,selection_only=q_sel,
        adaptive_generated=q_adapt,rich_fixed=q_rich,
        generated=q_gen,procedural_compiled=q_comp,
        information_lower_bound=math.ceil(math.log2(n)),
        explicit_tree_nodes=explicit_nodes)

def main():
    out=Path("artifacts/v1-diagnostic"); out.mkdir(parents=True,exist_ok=True)
    rows=[trial(n,s) for n in SIZES for s in SEEDS]
    with (out/"trials.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    summary=[]
    for n in SIZES:
        rr=[x for x in rows if x["n"]==n]
        m=lambda k: statistics.mean(x[k] for x in rr)
        primitive=m("primitive_natural"); selection=m("selection_only")
        adaptive=m("adaptive_generated"); rich=m("rich_fixed")
        compiled=m("procedural_compiled"); lb=m("information_lower_bound")
        summary.append(dict(n=n,
          primitive_mean=primitive,selection_mean=selection,
          adaptive_mean=adaptive,rich_fixed_mean=rich,
          generated_mean=adaptive,compiled_mean=compiled,information_lb=lb,
          selection_delta=primitive-selection,
          query_language_delta=selection-rich,
          online_generation_delta=adaptive-compiled,
          information_slack=adaptive-lb,
          explicit_tree_nodes=n-1))
    with (out/"summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=summary[0]); w.writeheader(); w.writerows(summary)
    (out/"summary.json").write_text(json.dumps(summary,indent=2))
    lines=["# Observer121 V1 five-way diagnostic","",
      "This artifact attributes apparent productivity under matched identification tasks.",
      "",
      "| n | primitive | selection-only | rich fixed | generated | compiled | info LB |",
      "|---:|---:|---:|---:|---:|---:|---:|"]
    for s in summary:
        lines.append(f"| {s['n']} | {s['primitive_mean']:.3f} | {s['selection_mean']:.3f} | {s['rich_fixed_mean']:.3f} | {s['generated_mean']:.3f} | {s['compiled_mean']:.3f} | {s['information_lb']:.0f} |")
    lines += ["","## Attribution",
      "- Selection effect: compare primitive natural order with shuffled fixed-library order.",
      "- Adaptivity/query-language control: compare primitive equality observations with balanced binary observations.",
      "- Online-generation effect: generated minus equivalent procedural compiled policy.",
      "- Representation effect: explicit tree nodes versus compact procedural realization.",
      "- Information effect: query count minus the exact binary lower bound.",
      "",
      "A zero generated-minus-compiled delta kills a unique online-generation claim. A zero information slack shows the rich/generated policies already attain the binary information bound."
    ]
    (out/"REPORT.md").write_text("\n".join(lines)); print("\n".join(lines))
if __name__=="__main__": main()
