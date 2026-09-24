# Observer121-Lab

**121 system–observer worlds. Eleven diagonal observations. One question: when can unknown structure be exploited without mistaking a pattern for a proof?**

This repository is an adversarial computational laboratory for an 11 × 11 system–observer matrix:

- 11 system states
- 11 observer states
- 121 intersections
- 11 diagonal cells initially revealed
- 110 off-diagonal cells hidden

## Core result targeted by the software

The software separates three situations that are often conflated:

1. **Known structure** — classical structured reconstruction can be cheap.
2. **Apparent structure** — a few confirming cells are not an exact certificate.
3. **Certified structure** — a solver may skip observations only after the structural identity has been verified strongly enough for the benchmark's ambient model.

The benchmark includes exact adversarial lookalikes (`near_additive`, `near_rank1`) specifically to kill unsafe early-stopping rules.

## Current experimental finding

The v2 exact-certificate solver is deliberately conservative. It achieves exact reconstruction on the benchmark suite, including adversarial near-structured worlds, but the cost of exact certification can erase the observational savings. This exposes the central research problem rather than hiding it:

> **Can a previously unknown structural law be certified for less than the observations it allows us to skip?**

That *certificate-economy gap* is the quantity the lab is designed to measure.

## Families

- additive
- symmetric
- rank-1
- periodic
- block
- near-additive adversary
- near-rank-1 adversary
- unstructured

## Baselines

- `exhaustive`: observe all 110 hidden cells
- `oracle_family`: reveal the family label; positive control for the value of known structure
- `exact_certificate_solver`: unknown family, explicit structural checks, adversarial fallback

## Reproduce

```bash
python src/run_benchmark.py
```

Artifacts are written to `artifacts/`:

- `results.csv`
- `summary.json`
- `REPORT.md`

## GitHub Actions

The included workflow runs the benchmark on every push and pull request and uploads the generated artifacts.

## Research status

The repository is a falsification laboratory. It does **not** claim that an 11×11 interaction matrix, matrix completion, adaptive experimental design, or model selection is itself novel. Existing work already covers adaptive experimental design, low-rank matrix completion, robust/adversarial matrix recovery, and property testing. The research target is narrower: exact, cost-accounted discovery and certification of previously unknown exploitable structure under adversarial lookalikes.

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
