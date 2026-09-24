from pathlib import Path
import csv, json, math

SIZES=[16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]

def row(n):
    adaptive=math.ceil(math.log2(n))
    nonadaptive=n-1
    info_lb=math.ceil(math.log2(n))
    return {
        "n":n,
        "query_language":"threshold q_t(z)=1[z<=t]",
        "adaptive_queries":adaptive,
        "nonadaptive_queries":nonadaptive,
        "binary_information_lower_bound":info_lb,
        "adaptive_attains_information_lb":adaptive==info_lb,
        "adaptivity_gap_ratio":nonadaptive/adaptive,
        "adaptivity_gap_absolute":nonadaptive-adaptive,
    }

def main():
    out=Path("artifacts/v1-adaptivity"); out.mkdir(parents=True,exist_ok=True)
    rows=[row(n) for n in SIZES]
    with (out/"adaptivity.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    (out/"adaptivity.json").write_text(json.dumps(rows,indent=2))
    last=rows[-1]
    report=f"""# Observer121 V1 matched-language adaptivity audit

Allowable query language for both policies:
q_t(z) = 1[z <= t], for t in {{0,...,n-2}}.

Adaptive policy:
binary search over the same threshold family, requiring ceil(log2 n) queries.

Non-adaptive policy:
all thresholds must be fixed before any answer is seen. m fixed thresholds partition the ordered target set into at most m+1 answer-equivalence intervals. Exact identification of n targets therefore requires m >= n-1, and querying all n-1 thresholds attains the bound.

Largest case n={last['n']:,}:
- adaptive: {last['adaptive_queries']} queries
- non-adaptive: {last['nonadaptive_queries']:,} queries
- exact binary information lower bound: {last['binary_information_lower_bound']}
- gap ratio: {last['adaptivity_gap_ratio']:.2f}x

Conclusion:
The experiment cleanly isolates adaptivity because the allowable query language is identical. The separation is exact for this ordered-threshold family. It is a benchmark control, not a novelty claim: adaptive/non-adaptive query-complexity gaps are established in prior literature.
"""
    (out/"REPORT.md").write_text(report)
    print(report)

if __name__=="__main__":
    main()
