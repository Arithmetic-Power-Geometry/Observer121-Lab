# V1 real-data validation

## Purpose

Move beyond analytically constructed identification families and test whether the attribution discipline remains usable on a standard public classification dataset.

## Dataset

Wisconsin Diagnostic Breast Cancer dataset distributed with scikit-learn. The experiment uses its numeric diagnostic features and binary diagnosis target.

## Matched comparison

Random acquisition and uncertainty acquisition receive the same train/test split, initial labeled examples, label budget, feature representation, preprocessing rule, and logistic-regression learner. Only the rule selecting the next unlabeled example changes.

## Attribution rule

Under these controls, a reproducible performance difference is attributed to **selection policy within this design**. The experiment does not claim that uncertainty sampling, active learning, or the dataset is novel.

## Why this matters for Observer121

The earlier calibration stages used families constructed so the true source of productivity was analytically known. This stage asks whether the same matched-control logic remains interpretable on non-constructed observations.
