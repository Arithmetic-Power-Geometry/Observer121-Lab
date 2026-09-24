# Justified attribution: attribution cost plus assumption-certification cost

## Setup

For the 11 x 11 Observer121 grid, a connected spanning-tree design uses 21 cells. Under the trusted additive model

Y_ij = mu + alpha_i + beta_j,

those 21 observations determine every cell.

## Certification attack

Now remove the promise that the world is additive. Allow an unrestricted alternative that differs from an additive matrix at even one previously unobserved cell.

After any proper subset of the 121 cells has been inspected, choose an unobserved cell and alter only that value. The additive world and the defective world agree on the entire observed transcript but disagree on whether additivity is globally valid.

Hence no proper subset can certify exact global additivity against this unrestricted alternative.

For Observer121:

- economical attribution under the promise: 21 cells;
- hidden cells after attribution: 100;
- exact worst-case certification against unrestricted alternatives: 121 cells;
- exact worst-case observational saving after certification: 0.

## Boundary with property testing

This statement concerns exact certification against an unrestricted single-cell deviation. It does not contradict property testing, which weakens the task by distinguishing a property from objects that are epsilon-far from it, usually with probabilistic guarantees. Sublinear additivity/linearity testers are known under those weaker objectives.

## AESHO interpretation

The productive result is a distinction between **promised attribution cost** and **justified attribution cost**. The numerical 21-to-121 collapse follows from classical additive-model estimability plus an elementary adversarial certification argument; it is not claimed as a new property-testing lower bound.
