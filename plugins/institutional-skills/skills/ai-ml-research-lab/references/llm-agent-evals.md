# LLM and Agent Evaluations

Use this for LLM agents, tool-use agents, multi-agent workflows, memory systems, finance/growth/coding agents, and autonomous research loops.

## Evaluation Axes

- Task success.
- Source fidelity.
- Tool correctness.
- Numerical accuracy.
- Calibration and uncertainty.
- Hallucination and unsupported claim rate.
- Policy/guardrail compliance.
- Memory usefulness vs contamination.
- Latency and cost.
- Recoverability after bad intermediate state.

## Agent Benchmark Design

- Define the task universe.
- Separate easy, medium, hard, adversarial, and live tasks.
- Freeze inputs for deterministic comparison where possible.
- Add live tasks only after static benchmark sanity checks.
- Score outputs with human-reviewed rubrics or deterministic validators.
- Track model, prompt, tools, memory state, and run timestamp.

## Multi-Agent Controls

- Assign owner and reviewers.
- Use file leases or advisory reservations when editing shared files.
- Use a task graph for dependencies.
- Require audit logs for irreversible actions.
- Benchmark agent architecture separately from model backbone.

## Output Pattern

- Benchmark name and task set.
- Agent architecture.
- Tools and permissions.
- Memory/retrieval setup.
- Metrics and scoring rubric.
- Results by task bucket.
- Failure examples.
- Recommended changes.
- Promote / iterate / kill decision.

