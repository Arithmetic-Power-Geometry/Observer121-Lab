from pathlib import Path
import csv, json, math

NS=[16,32,64,128,256,512,1024,2048,4096]

def threshold(n):
    # Same threshold language q_t(z)=1[z<=t].
    return dict(family="ordered_threshold", n=n,
      primitive=n-1, nonadaptive=n-1, adaptive=math.ceil(math.log2(n)),
      rich_fixed=n-1, compiled=math.ceil(math.log2(n)),
      info_lb=math.ceil(math.log2(n)),
      expected_driver="adaptivity")

def equality(n):
    # Equality-only language q_k(z)=1[z=k]. Adaptivity cannot improve worst-case exact ID.
    return dict(family="equality_only", n=n,
      primitive=n-1, nonadaptive=n-1, adaptive=n-1,
      rich_fixed=n-1, compiled=n-1,
      info_lb=math.ceil(math.log2(n)),
      expected_driver="null_adaptivity")

def subset(n):
    # Compare equality primitives to a fixed bit-test language. No online generation needed.
    k=math.ceil(math.log2(n))
    return dict(family="fixed_bit_language", n=n,
      primitive=n-1, nonadaptive=k, adaptive=k,
      rich_fixed=k, compiled=k,
      info_lb=k,
      expected_driver="query_language")

def representation(n):
    # Query behavior identical; representation differs.
    k=math.ceil(math.log2(n))
    return dict(family="representation_only", n=n,
      primitive=k, nonadaptive=k, adaptive=k,
      rich_fixed=k, compiled=k,
      info_lb=k,
      expected_driver="representation")

def diagnose(r):
    if r["family"]=="ordered_threshold":
        return "adaptivity" if r["adaptive"]<r["nonadaptive"] else "none"
    if r["family"]=="equality_only":
        return "null_adaptivity" if r["adaptive"]==r["nonadaptive"] else "adaptivity"
    if r["family"]=="fixed_bit_language":
        return "query_language" if r["rich_fixed"]<r["primitive"] and r["adaptive"]==r["nonadaptive"] else "other"
    if r["family"]=="representation_only":
        return "representation" if r["compiled"]==r["adaptive"] else "other"

def main():
    out=Path("artifacts/v1-external-calibration"); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for n in NS:
        for fn in (threshold,equality,subset,representation):
            r=fn(n); r["diagnosed_driver"]=diagnose(r)
            r["calibration_pass"]=r["diagnosed_driver"]==r["expected_driver"]
            if r["family"]=="representation_only":
                r["explicit_representation_units"]=n-1
                r["compact_parameter_bits"]=max(1,math.ceil(math.log2(math.ceil(math.log2(n))+1)))
            else:
                r["explicit_representation_units"]=""
                r["compact_parameter_bits"]=""
            rows.append(r)
    with (out/"calibration.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    summary=[]
    for fam in sorted(set(r["family"] for r in rows)):
        rr=[r for r in rows if r["family"]==fam]
        summary.append({"family":fam,"cases":len(rr),"passed":sum(r["calibration_pass"] for r in rr),
                        "expected":rr[0]["expected_driver"],"diagnosed":rr[0]["diagnosed_driver"]})
    (out/"summary.json").write_text(json.dumps(summary,indent=2))
    lines=["# Observer121 V1 external calibration","",
      "| family | expected source | diagnosed source | cases passed |",
      "|---|---|---|---:|"]
    for s in summary:
        lines.append(f"| {s['family']} | {s['expected']} | {s['diagnosed']} | {s['passed']}/{s['cases']} |")
    lines += ["","These are theory-calibration families, not evidence that their underlying separations are novel.",
      "The benchmark passes only if it recovers the pre-specified causal source of the apparent productivity change."]
    (out/"REPORT.md").write_text("\n".join(lines)); print("\n".join(lines))
if __name__=="__main__": main()
