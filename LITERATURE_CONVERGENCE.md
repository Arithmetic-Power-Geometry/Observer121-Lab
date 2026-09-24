# Observer121 Literature Convergence Gate

Date: 2026-09-24

## Question

Does prior work already provide the same integrated task as Observer121: diagnose an observed productivity gain across selection policy, adaptivity, query-language expressivity, representation, and information efficiency, while explicitly reporting whether the proposed source is isolated, confounded, eliminated, interaction-dependent, or unresolved?

## Nearest literatures

### Optimal experimental design and model discrimination
Classical and modern model-discrimination work optimizes experimental designs or inputs so rival models become distinguishable. This directly overlaps Observer121's experiment-selection setting, but its primary target is informative design/model recovery rather than post-hoc attribution of the source of an observed efficiency gain.

Representative sources:
- Myung & Pitt (2009), Optimal Experimental Design for Model Discrimination, Psychological Review, DOI 10.1037/a0016104.
- Cavagnaro et al. (2011), Model discrimination through adaptive experimentation.
- optimal-input/model-discrimination literature in control and biochemical systems.

### Active learning and query-language complexity
Kontonis, Ma & Tzamos (COLT 2024) explicitly quantify a trade-off between number of queries and complexity of the query language. This substantially overlaps Observer121's query-language axis and prevents any novelty claim for that trade-off itself.

### Ablation and causal/component attribution
Ablation studies and causal-attribution methods isolate contributions of model components by controlled removal/intervention. This substantially overlaps the matched-control principle and prevents claiming single-factor attribution itself as new.

### Factorial experimental design
Factorial designs already separate main effects and interactions when intervention cells are sufficiently observed. Observer121's interaction contrast and endpoint-confounding argument are applications of this logic, not new factorial theory.

### Knowledge compilation / representation
Succinctness differences between explicit and procedural representations are established. Observer121 uses this as a control against misattributing representation savings to online information generation.

## Provisional gap after targeted search

The searched neighboring literatures contain the individual ingredients, but this audit did not identify a directly matching framework whose declared benchmark output jointly diagnoses observation-productivity gains across all five Observer121 axes and assigns the diagnostic states isolated/confounded/eliminated/interaction-dependent/unresolved.

This is a provisional literature gap, not proof of global novelty. It supports proceeding to manuscript preparation only with a narrow methodological claim.

## Paper gate

The paper may now be drafted because:
1. the central claim has converged;
2. major alternative novelty claims have been eliminated and documented;
3. synthetic positive and negative controls exist;
4. real-data validation exists;
5. exact promised-versus-certified evidence boundaries exist;
6. the nearest prior-art categories and claim boundaries are explicit.

Before submission, add one external model-discrimination validation using a published benchmark or model family and perform a manuscript-specific reference audit.

## Allowed novelty language

Prefer:
"Observer121 introduces a controlled diagnostic benchmark that integrates matched interventions across several distinct sources of observation productivity."

Avoid:
"first ever", "new theory of information", "new active-learning theorem", "new experimental-design theorem", or claims that the constituent axes are individually novel.
