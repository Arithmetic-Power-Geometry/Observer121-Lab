# Observer121 Convergence Audit

## Research question

When one observation strategy appears more productive than another, can the source of that gain be identified rather than merely reported?

Observer121 treats an observation procedure as a controlled configuration

C = (W, Q, P, R, B),

with world/hypothesis family W, admissible query language Q, observation-selection policy P, representation R, and resource/accounting rule B. A source is attributed only when the relevant comparison changes that source while the competing sources required by the claim are held fixed or factorially resolved.

## Classification of results

| Result | Classification | Role in paper |
|---|---|---|
| 11 x 11 system-observer laboratory | benchmark architecture | introduce controlled observation space; do not claim matrix novelty |
| matched-control attribution labels: isolated, confounded, eliminated, interaction-dependent, unresolved | candidate methodological contribution | central framework |
| configuration C=(W,Q,P,R,B) | candidate organizing formalism | formalize attribution target |
| endpoint non-identifiability when multiple factors change | established factorial/control logic specialized to benchmark | proposition/control, not foundational novelty |
| additive minimum m+n-1 | established estimability/connected-design result | calibration only |
| unrestricted minimum mn | elementary saturated-model boundary | calibration only |
| 21-cell additive versus 121-cell exact certification | derived Observer121 boundary using established machinery | motivating evidence-accounting result |
| finite-population assurance frontier | established hypergeometric sampling | assurance calibration, not novelty |
| generated-query vs procedural compilation equivalence | negative control | eliminates unique online-generation claim |
| ZGTC and rectangle strategies losing to disagreement greedy | negative control | compressed provenance/supplement |
| matched-language adaptive threshold experiment | established adaptivity separation used as positive calibration | validates diagnostic |
| fixed-bit vs equality language | established query-language effect used as positive calibration | validates diagnostic |
| explicit vs procedural realization | established representation/succinctness phenomenon | validates representation axis |
| real-data random vs uncertainty acquisition | empirical validation | tests matched-control attribution outside constructed families |

## Surviving candidate contribution

The surviving contribution is methodological rather than a new search algorithm or new information-theoretic law:

> Observer121 is a controlled attribution benchmark for testing whether an apparent observation-productivity gain is identifiable with a declared experimental freedom, confounded with other freedoms, reproduced without the proposed source, or dependent on interactions among freedoms.

The contribution must be evaluated against prior work in experimental design, ablation methodology, active learning, query complexity, model discrimination, and benchmarking. None of the constituent classical results is claimed as new.

## Claims explicitly eliminated

Observer121 should not claim:
- novelty of the 11 x 11 matrix itself;
- a new general search algorithm;
- a new adaptivity theorem;
- a new query-language theorem;
- a new succinctness theorem;
- a new minimum-sensor/estimability theorem;
- a new hypergeometric or property-testing bound;
- a unique information advantage from online query generation.

## Evidence hierarchy for the paper

Main text should retain:
1. attribution formalism and identifiability rule;
2. one clean synthetic calibration per attribution axis;
3. the 21-to-121 promised-versus-certified boundary;
4. assurance relaxation as a short bridge, explicitly classical;
5. real-data validation;
6. prior-art boundary and limitations.

Earlier failed mechanisms and redundant benchmarks belong in supplementary material or repository provenance.

## Current AESHO decision

SURVIVES AS A METHODOLOGICAL CANDIDATE.

It has not survived as a new foundational theory. The next decisive requirement is a comprehensive literature comparison of the integrated attribution framework, followed by one additional external model-discrimination validation only if that comparison shows it is necessary.
