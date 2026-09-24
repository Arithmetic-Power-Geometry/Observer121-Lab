# Observer121-Lab

**A matched-control laboratory for attributing why an observation strategy appears more productive.**

## Research question

A lower observation count does not by itself identify the source of the gain. Observer121 asks whether an apparent improvement is attributable to **selection policy, adaptivity, query-language expressivity, representation, or information efficiency**, and whether that attribution is isolated, confounded, eliminated by a matched control, interaction-dependent, or unresolved.

The scientific framework represents an observation procedure as a configuration

`C = (W, Q, P, R, B)`

with world/hypothesis family, admissible query language, observation-selection policy, representation, and resource/accounting rule.

## Current evidence

The repository contains reproducible positive calibrations, negative controls, and an external real-data validation.

- **Matched-language adaptivity:** adaptive and non-adaptive policies use the same threshold-query language. At `n = 1,048,576`, adaptive binary search uses 20 queries while exact non-adaptive identification requires 1,048,575 thresholds.
- **Query-language calibration:** fixed bit queries reach logarithmic exact identification without requiring online query generation.
- **Generation/compilation control:** generated balanced queries and an equivalent procedural compiled policy match query-for-query; the surviving benefit is representation succinctness rather than a unique information advantage.
- **Promised versus justified attribution:** in the 11 x 11 additive calibration, a connected 21-cell design determines the additive model, while exact certification against an unrestricted single hidden-cell deviation requires all 121 cells.
- **Risk-controlled assurance:** finite-population hypergeometric auditing connects the 21-cell promised design to exhaustive certification under explicit `(K, delta)` assumptions.
- **Real-data validation:** random and uncertainty acquisition are compared on the Wisconsin Diagnostic Breast Cancer dataset with the split, initial labels, learner, features, preprocessing, and label budget held fixed.

## Scientific boundary

Observer121 is **not** presented as a new universal information theory, a new active-learning algorithm, a new factorial-design theorem, a new property-testing bound, or a new succinctness theorem. The candidate contribution is methodological: a common benchmark for testing whether the proposed source of an observation-productivity gain survives matched controls.

See:

- `CLAIM_REGISTER.md` for permitted and excluded claims.
- `CONVERGENCE_AUDIT.md` for the research convergence audit.
- `ATTRIBUTION_THEORY.md` for the formal diagnostic states.
- `ATTRIBUTION_MATRIX.md` for the matched-control map.
- `JUSTIFIED_ATTRIBUTION.md` and `ASSURANCE_FRONTIER.md` for evidence-accounting boundaries.
- `LITERATURE_CONVERGENCE.md` for the prior-art boundary.
- `SEQUENCE.md` for earlier falsification controls and development provenance.

## Reproducibility

GitHub Actions executes the benchmark programs and stores numerical artifacts. Scientific prose uses **Observer121** without a version suffix; version identifiers remain in software/workflow names where needed for provenance.

The principal scripts are in `src/`, including the productivity audit, matched-language adaptivity control, external calibration, real-data validation, attribution-identifiability check, minimum-attribution kill test, justified-attribution audit, and assurance frontier.

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
