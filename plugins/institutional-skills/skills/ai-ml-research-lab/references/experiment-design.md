# Experiment Design

Use this for ML/AI experiments, signal research, ranking models, forecasters, classifiers, embeddings, and model comparisons.

## Minimum Experiment Contract

- Decision: what action changes if the model works.
- Owner: domain owner and approver.
- Unit of prediction: row/entity/time grain.
- Label/target: exact definition and timestamp.
- Data: sources, as-of date, permissions, lineage.
- Split: train/validation/test or walk-forward policy.
- Baseline: simple model, rule, or dumb prior.
- Metric: primary, secondary, and guardrail metrics.
- Cost model: runtime, data cost, labeling cost, API/tool cost.
- Promotion gate: threshold versus baseline and uncertainty.
- Kill gate: failure conditions and rollback.

## Leakage Checklist

- Target is not included directly or through future-derived features.
- Feature timestamps are earlier than prediction timestamp.
- Cross-sectional normalization uses only information available at the prediction time.
- Entity leakage is controlled when the same entity appears across train/test.
- Hyperparameters are selected only on validation, not test.
- Test set is not reused as a development loop.
- Data revisions and survivorship bias are documented.

## Evaluation Standards

- Start with a dumb baseline.
- Add one complexity layer at a time.
- Report confidence intervals, bootstraps, or dispersion across folds where feasible.
- Run ablations for features, model class, prompt/tool policy, memory, and retrieval.
- Separate statistical lift from economic or business lift.
- Measure degradation under realistic costs, latency, missing data, stale data, and adversarial inputs.

## Output Pattern

- Objective
- Dataset and as-of dates
- Split policy
- Baseline
- Candidate models
- Metrics
- Leakage controls
- Ablations
- Results
- Failure modes
- Promote / iterate / kill decision

