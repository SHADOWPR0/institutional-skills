# Model Risk Governance

Use this for production model validation, challenger models, monitoring, drift, incident response, and audit readiness.

## Governance Layers

- Intended use and prohibited use.
- Model owner and approver.
- Data lineage and permissions.
- Training/evaluation reproducibility.
- Performance threshold.
- Fairness/compliance where relevant.
- Security and prompt-injection exposure for LLM systems.
- Monitoring and alerting.
- Kill switch and rollback.

## Model Card Minimums

- Model purpose.
- Training data summary.
- Evaluation data summary.
- Split policy.
- Metrics and uncertainty.
- Known limitations.
- Failure modes.
- Monitoring metrics.
- Human review conditions.
- Rollback procedure.

## Monitoring

- Input drift.
- Label drift.
- Calibration drift.
- Performance drift.
- Cost/latency drift.
- Tool/API failure rate.
- Distribution shift by segment/regime.
- Incident log and root cause.

## Kill Switches

Stop or degrade the model when:

- data freshness breaches threshold
- drift exceeds threshold
- model fails high-severity examples
- unsupported claims rise above limit
- cost/latency blows through budget
- security/compliance issue appears
- live performance violates guardrail

