# V1 productivity test

## Question

Does online generation retain an observation advantage after comparison with an equivalently expressive pre-written procedural policy and an explicitly materialized policy representation?

## Controls

The test reports query count separately from representation size. It compares:

1. a primitive equality-test library;
2. online balanced observation generation;
3. the same balanced policy written in advance as a fixed procedure; and
4. the storage required by an explicitly materialized balanced decision tree.

No weighted aggregate cost is used.

## Kill criterion

A unique online-generation claim is rejected if the procedural compiled policy matches the generated policy query-for-query.

## Interpretation

A storage advantage over explicit materialization is useful, but it is not treated as a new information-theoretic principle. The purpose of this test is to identify the source of measured productivity rather than force a positive novelty claim.
