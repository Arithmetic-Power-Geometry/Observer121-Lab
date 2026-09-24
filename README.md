# Observer121-Lab

**A controlled laboratory for locating the source of productivity in adaptive observation.**

## V1 research question

When an observation strategy uses a richer experiment language, does its measured advantage come from additional information, from online generation, or from the representation used to make the experiments available?

The V1 productivity audit keeps these effects separate. It compares a primitive equality-test library, online balanced observation generation, the same balanced policy written in advance as a fixed procedure, and an explicitly materialized balanced decision-tree representation.

Run:

```bash
python src/v1_productivity_audit.py
```

The GitHub Actions workflow `Observer121 V1 productivity audit` stores trial-level results, summaries, and the report as the artifact `observer121-v1-productivity-audit`.

## Current V1 result

Across problem sizes from 16 through 1,048,576, generated balanced observation and the equivalent procedural compiled policy use the same number of observations on every trial. At the largest size both require 20 observations. The primitive equality strategy requires far more observations, while explicit materialization of the balanced policy requires 1,048,575 internal nodes and 20,971,520 split-membership bits.

The experiment therefore does **not** establish a unique information-theoretic advantage for online generation. It does expose a useful representation distinction: a compact procedure can realize the same observation policy without explicitly materializing the full decision tree.

See **V1_TEST.md** for the test definition and kill criterion.

## Earlier falsification controls

Earlier experiments remain in the repository as controls. They tested composite zigzag/disagreement policies, cross-rectangle attacks, decision-relative stopping, and the initial generation-versus-compilation comparison. They are retained because they document which apparent advantages disappear under stronger baselines. They are not presented as separate foundational theories.

See **SEQUENCE.md** for that development record.

## Reproducibility

GitHub Actions executes the V1 audit with Python 3.12 and uploads the complete numerical artifact. The earlier benchmark workflows remain available for independent regression checks.

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
