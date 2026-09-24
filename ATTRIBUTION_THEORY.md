# Observer121 attribution formalism

## Experimental configuration

Let an observation procedure be described by a configuration

C = (W, Q, P, R, B),

where:

- W is the world or hypothesis family;
- Q is the admissible observation/query language;
- P is the policy that selects observations;
- R is the representation used to realize the policy;
- B is the resource/accounting rule.

Let J(C) be a measured outcome such as exact-identification query count, predictive accuracy at a fixed label budget, storage, or total cost.

## Matched intervention

For component X in {W,Q,P,R,B}, a matched intervention is a pair (C,C') that differs only in X. The observed X-contrast is

Delta_X(C,C') = J(C') - J(C).

This is an experimental attribution, not a claim that X is a universal causal variable outside the benchmark.

## Attribution identifiability

A source X is identifiable for a contrast if the compared configurations differ only in X under the declared benchmark semantics.

If two or more components change simultaneously and no additional matched contrasts determine their separate contributions, the source is **confounded**.

## Matched-Control Attribution Proposition

For deterministic benchmark semantics, if C and C' agree in every component except X, then the measured contrast Delta = J(C')-J(C) is attributable to the intervention on X within that benchmark.

Conversely, if C and C' differ in X and Y, then Delta alone does not identify separate X and Y contributions: there exist response functions over the four intervention cells that agree on the two observed endpoint values while assigning different X-only and Y-only contrasts.

### Proof sketch

The first statement follows from controlled substitution: X is the only varying benchmark component.

For the converse, observe only J(0,0)=a and J(1,1)=b. The unobserved cells J(1,0) and J(0,1) are unconstrained by the endpoint contrast. Choosing different values for these cells preserves a and b but changes the isolated X and Y contrasts. Therefore endpoint comparison alone cannot identify the separate sources.

## Factorial completion

For two binary components X and Y, observing all four cells

J(0,0), J(1,0), J(0,1), J(1,1)

permits the benchmark to report matched main contrasts and the interaction contrast

I_XY = J(1,1)-J(1,0)-J(0,1)+J(0,0).

This is standard factorial logic. Observer121 uses it as an attribution discipline rather than claiming the factorial identity as new.

## Diagnostic labels

Observer121 reports one of:

- **isolated**: a matched intervention changes only the source under test;
- **confounded**: multiple sources change without sufficient completion;
- **eliminated**: a matched control reproduces the claimed gain without the proposed source;
- **interaction-dependent**: factorial completion shows that the source effect depends on another component;
- **unresolved**: available observations do not support attribution.

## Scientific boundary

The candidate contribution is not the algebra of factorial contrasts, active learning, query complexity, ablation, or knowledge compilation individually. The proposed methodological object is a common observation-process benchmark that forces apparent productivity claims through explicit source-identifiability tests.
