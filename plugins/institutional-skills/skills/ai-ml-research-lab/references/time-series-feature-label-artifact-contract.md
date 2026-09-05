# Time-Series Feature, Label, And Artifact Contract

Use this contract with `experiment-design.md` for financial time-series ML.
It makes feature availability, label completion, fold-local transforms, and
model artifact identity testable. `investment-management` remains the capital
decision owner.

## Required Record

Every prediction artifact records:

```text
prediction_unit
event_time
available_at
feature_name / feature_order
source_and_revision_policy
fit_fold_id / fit_start / fit_end
label_name / label_complete_at / overlap_span
transform_type / transform_hash / serializer
model_hash / code_hash / config_hash
training_data_hash / evaluation_data_hash
expires_at
forbidden_uses
```

Use a structured manifest, not prose, for the record. Missing hashes, feature
order, version, expiry, source revision policy, or timestamp fields fail
closed.

## Fold And Label Rules

- Fit imputation, scaling, winsorization, feature selection, calibration, and
  balancing inside the training fold only.
- A label is unavailable until `label_complete_at`; it cannot be used as a
  contemporaneous feature or decision input.
- Purge or embargo overlapping forward-return, barrier, and holding-period
  labels.
- For derivatives, record point-in-time funding, mark, index, contract, and
  settlement completeness for each fold.
- Treat executable serializers as untrusted input. Allow only reviewed,
  non-executable formats unless a separately approved sandboxed loader exists.

## Metrics And Promotion

F1, MCC, and Cohen's kappa can describe classification behavior. They do not
substitute for calibration, decision utility, cost, turnover, fill assumptions,
or net economics. Promotion requires the domain owner's benchmark and a
fold-level comparison under the same executable assumptions.

## Deterministic Regression Cases

The local validator must accept a correct lagged, fold-local feature contract
and reject: a full-sample scaler; a future-return feature disguised as a
feature; unpurged triple-barrier overlap; reordered columns; expired model
artifact; and a derivative fold missing funding, mark, or index coverage.

## Provenance Boundary

This is an independently written local contract informed by public
methodological review: Jesse commit `fa63531c` (MIT), nateemma commit `a132ecd`
(GPL concepts only), and Freqtrade commit `d433b1b` (GPL concepts only). No
external code, saved models, or datasets are imported by this reference.
