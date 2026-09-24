# Observer121 V1 diagnostic benchmark

## Purpose

The benchmark asks why an observation strategy appears more productive while keeping the underlying exact-identification task fixed.

## Diagnostic axes and controls

1. **Selection:** same primitive experiment library, different ordering/selection.
2. **Adaptivity:** requires a matched experiment language before it can be isolated.
3. **Query language:** equality tests versus balanced subset tests.
4. **Representation:** explicitly materialized decision structure versus a compact procedural realization.
5. **Information:** achieved query count versus the exact binary information lower bound.

## Identifiability rule

An axis is reported as isolated only when all competing axes are held fixed. In the present synthetic family, moving from equality tests to adaptive balanced subset tests changes both the experiment language and the policy, so the resulting gain is labeled **query-language/adaptivity confounded**. It is not attributed to adaptivity alone.

Online generation is separately controlled by an equivalent pre-written procedural policy. Representation is separately exposed by comparing explicit materialization with that compact procedure. Information efficiency is assessed against the exact binary lower bound.

## Interpretation discipline

The benchmark does not assume that these ingredients are individually novel. Its research question is whether controlled attribution of apparent observation productivity is useful and distinguishable from existing single-axis analyses.

A claimed effect is retained only when its matched control does not explain it.
