# Observer121 V1 external calibration

This stage tests the diagnostic benchmark against families with a pre-specified explanation.

## Calibration families

- **Ordered thresholds:** same threshold language for both policies; adaptivity is expected to reduce exact-identification queries.
- **Equality-only:** the same equality language gives no worst-case exact-identification benefit from adaptivity; this is the null adaptivity control.
- **Fixed bit language:** a richer fixed query language reaches logarithmic exact identification without online generation; the expected source is query-language expressivity.
- **Representation-only:** query behavior is held equal while explicit materialization is compared with a compact procedural realization; the expected source is representation.

## Pass criterion

The expected source is specified before observing the benchmark output. A family passes only if the diagnostic recovers that source. The purpose is calibration of attribution, not rediscovery of the underlying known theorem.
