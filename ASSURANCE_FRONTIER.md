# Observer121 assurance-cost frontier

After the 21-cell additive spanning design, H=100 cells remain unchecked.

Suppose a declared assurance model says that, whenever the additive assumption is false, at least K of those H cells violate the additive prediction. Audit s unchecked cells uniformly without replacement.

The probability of missing every violation is

P_miss(s | H,K) = C(H-K,s) / C(H,s).

For a requested miss-risk delta, define the audit requirement as the smallest s satisfying

P_miss <= delta.

The total evidence cost is then

C = 21 + s.

This gives a finite-population assurance-cost curve between promised attribution and full exact certification.

## Interpretation boundary

This calculation is standard hypergeometric acceptance sampling. Observer121 does not claim the probability formula or its sample-size inversion as new.

The methodological value is diagnostic: the claimed evidence saving is meaningful only after stating the alternative class (here, at least K violating unchecked cells) and the tolerated miss risk delta.

If K=1 and delta tends to zero, the frontier returns to exhaustive certification. If violations must be numerous, useful probabilistic assurance can require substantially fewer observations.

## Relation to property testing

Property testing similarly obtains sublinear query complexity by replacing exact certification against arbitrary nearby alternatives with a promise that violations are sufficiently far from the target property. Observer121 uses this stage to make that relaxation explicit in evidence accounting rather than to propose a new property-testing algorithm.
