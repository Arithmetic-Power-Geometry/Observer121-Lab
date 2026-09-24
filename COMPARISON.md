# Comparison with related approaches

This table separates conceptual overlap from the numerical benchmark in this repository. The numerical rows in `artifacts/comparison_summary.csv` are implementations inside Observer121-Lab; they are not reruns of third-party packages.

| Approach | Main objective | Zigzag exploration | Rival-disagreement target | Multi-hypothesis elimination | 2x2 system-observer rectangle attack | Falsification-first | Relation |
|---|---|---|---|---|---|---|---|
| Crow Search Algorithm | population metaheuristic optimization | heuristic movement | no | no | no | no | inspiration only |
| Active Model Discrimination | design separating inputs for rival dynamic models | no | yes | yes | no | separation-focused | close prior art |
| Adaptive sample selection for hypothesis falsification | select samples likely to falsify a hypothesis | no | yes | limited | no | yes | close prior art |
| Factorial interaction contrast | estimate main and interaction effects | no | no | no | yes | no | supplies rectangle mathematics |
| Random baseline | uniform hidden-cell sampling | no | no | no | no | no | internal baseline |
| Zigzag-only baseline | geometric off-diagonal coverage | yes | no | no | incidental | no | ablation |
| Disagreement-greedy baseline | maximize expected eliminated hypotheses | no | yes | yes | no | yes | strongest classical-style baseline here |
| Rectangle-attack baseline | preferentially complete cross-swap rectangles | no | partial | partial | yes | yes | interaction ablation |
| ZGTC | zigzag + gap + multi-target + crash score | yes | yes | yes | yes | yes | proposed composite policy |

The research claim is intentionally narrow: the composite policy is an experimental algorithmic combination whose value must be judged by benchmark evidence and deeper prior-art audit. No individual ingredient is claimed as new.
