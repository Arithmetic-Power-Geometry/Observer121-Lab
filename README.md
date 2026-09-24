# Observer121

**A matched-control framework for attributing productivity in adaptive observation**

Observer121 is a diagnostic framework for determining why one observation strategy appears more efficient than another. It separates gains associated with **selection policy, adaptivity, query-language expressivity, representation, and information efficiency** through matched experimental controls.

## Framework

An observation experiment is represented by

`C = (W, Q, P, R, B)`

where `W` is the world or hypothesis family, `Q` the admissible query language, `P` the observation-selection policy, `R` the representation used to realize the policy, and `B` the resource-accounting rule.

For a declared source of improvement, Observer121 compares configurations under matched interventions and records whether the observed gain is isolated, confounded, reproduced by an equivalent control, interaction-dependent, or unresolved.

## Main experiments

### Matched-language adaptivity

For an ordered target with threshold queries, adaptive binary search requires `ceil(log2 n)` queries, whereas exact non-adaptive identification requires `n - 1` thresholds. At `n = 1,048,576`, the corresponding counts are 20 and 1,048,575.

### Query generation and procedural compilation

Balanced generated queries and an equivalent procedural realization produce the same query sequence and attain the same binary information bound. Their query efficiency is therefore identical, while their representation requirements can differ substantially from explicit tree materialization.

### Observer121 system-observer laboratory

The core laboratory contains 11 systems and 11 observers, giving 121 system-observer cells. Under an additive model, a connected spanning design determines the model from 21 observations. When the additive assumption itself must be certified against an unrestricted hidden single-cell deviation, exact certification requires all 121 cells in the worst case.

### Risk-controlled assurance

Between a trusted structural promise and exhaustive certification, the repository implements a finite-population audit. If the 100 unchecked cells contain at least `K` violations and `s` cells are sampled without replacement, the miss probability is

`P_miss = C(100-K, s) / C(100, s)`.

The audit computes the smallest sample size meeting a declared miss-risk tolerance.

### Real-data validation

The real-data experiment uses the Wisconsin Diagnostic Breast Cancer dataset distributed with scikit-learn. Across 30 seeds, random acquisition and uncertainty acquisition use the same train/test split, initial labels, feature representation, logistic-regression learner, preprocessing, and label budget; only the acquisition rule changes. The reported mean test accuracies reproduce the matched-selection results in the paper.

## Reproducibility

The `src/` directory contains the programs used for the computational experiments. GitHub Actions workflows in `.github/workflows/` rerun the corresponding analyses and preserve their generated artifacts.

Principal reproducibility programs include:

- `v1_adaptivity_matched_language.py`
- `v1_external_calibration.py`
- `v1_productivity_audit.py`
- `v1_succinctness_attack.py`
- `justified_attribution_audit.py`
- `assurance_frontier.py`
- `v1_real_data_validation.py`
- `attribution_identifiability.py`
- `zgtc_benchmark.py`

Version identifiers in program and workflow filenames are retained for computational provenance.

## Citation

If you use Observer121, please cite:

> Akhtar, M. A. K. (2026). *Observer121: A Matched-Control Framework for Attributing Productivity in Adaptive Observation* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22943547

BibTeX:

```bibtex
@software{akhtar2026observer121,
  author    = {Akhtar, Mohammad Amir Khusru},
  title     = {Observer121: A Matched-Control Framework for Attributing Productivity in Adaptive Observation},
  year      = {2026},
  version   = {V1},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22943547},
  url       = {https://doi.org/10.5281/zenodo.22943547}
}
```

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
