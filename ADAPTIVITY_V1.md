# Matched-language adaptivity control

## Goal

Isolate adaptivity without changing the allowable observation language.

## Common query language

For an ordered hidden target z in {0,...,n-1}, both methods may use only threshold observations

q_t(z) = 1[z <= t],  t in {0,...,n-2}.

## Adaptive policy

Choose thresholds according to previous answers. Binary search identifies z in ceil(log2 n) observations.

## Non-adaptive policy

Choose every threshold before seeing any answer. With m fixed thresholds, the ordered domain is split into at most m+1 answer-equivalence intervals. Exact identification of all n targets therefore requires m >= n-1. Asking all n-1 thresholds is sufficient.

Hence, for this family,

Q_adaptive = ceil(log2 n),
Q_nonadaptive = n-1.

The experiment language, target family, response alphabet, and exact-identification objective are held fixed. Only access to previous outcomes when selecting the next threshold changes.

## AESHO interpretation

This control establishes that Observer121 can represent and measure an isolated adaptivity effect. It does not establish a new adaptivity theorem: adaptive versus non-adaptive query gaps are known. Its role is diagnostic validation.
