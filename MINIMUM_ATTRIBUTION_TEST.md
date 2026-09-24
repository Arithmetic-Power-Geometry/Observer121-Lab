# Minimum attribution-set kill test

## Question

For an m x n system-observer grid, what is the smallest observed-cell set sufficient for a declared attribution model?

## Exact boundaries

For the additive model

y_ij = mu + alpha_i + beta_j,

the model has m+n-1 free parameters under standard reference constraints. Treating observed cells as edges between m system vertices and n observer vertices, connectedness of the observation graph is the estimability condition. A spanning tree has exactly m+n-1 edges, so the minimum is

kappa_additive = m+n-1.

For the unrestricted saturated cell model, every cell mean is independent, hence

kappa_unrestricted = mn.

For 11 x 11 this gives 21 versus 121 cells.

A single unrestricted 2 x 2 interaction contrast requires its four participating cells.

## AESHO result

This is a productive boundary for Observer121 but not a new general theorem. In the natural linear-model formulation it is an instance of classical estimability/design-matrix rank and connected incomplete-design logic. Minimum measurement selection under observability/rank constraints is also an established optimization problem.

Therefore Observer121 should use these results as calibration controls. A novelty claim would require an attribution constraint not reducible to the declared model's ordinary estimability/observability condition.
