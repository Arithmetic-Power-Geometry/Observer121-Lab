# Observer121 Attribution Matrix

Observer121 is a controlled diagnostic benchmark for determining why an observation strategy appears more productive. Version labels belong to software releases and artifact provenance; the scientific components below are intentionally unversioned in prose.

| Diagnostic source | Matched control | What is held fixed | Observable contrast | Current status |
|---|---|---|---|---|
| Selection policy | random vs uncertainty acquisition | data, learner, features, initial labels, label budget | predictive performance | real-data validation completed |
| Adaptivity | adaptive vs non-adaptive threshold policy | target family, threshold-query language, answer alphabet, exact-ID objective | query count | isolated exactly |
| Query language | equality vs fixed bit-query language | target family, objective; no online generation required | query count | calibrated |
| Online generation | generated balanced policy vs equivalent procedural compiled policy | induced decisions and query sequence | query count | no unique advantage |
| Representation | explicit materialization vs compact procedural realization | query behavior and decision policy | representation size | benefit survives; not a new theorem |
| Information efficiency | achieved queries vs binary lower bound | target cardinality and binary answer model | excess above lower bound | calibrated |

## Interpretation

The benchmark does not claim that selection, adaptivity, active learning, query-language complexity, information bounds, or succinct representation are new. Its candidate methodological contribution is the use of matched controls to attribute an apparent observation advantage rather than reporting only that one strategy outperforms another.

## Current boundary

The strongest surviving claim is methodological: Observer121 provides a common laboratory in which candidate gains can be attacked by matched controls and assigned to an identifiable source when the design permits it. A source is left confounded when the available control does not isolate it.

AESHO is retained as an internal research discipline and need not be presented as a scientific theory in the manuscript.
