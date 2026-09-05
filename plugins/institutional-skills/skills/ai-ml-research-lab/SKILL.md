---
name: ai-ml-research-lab
description: Canonical AI, ML, RL, LLM, agent-evaluation, model-risk, and research-to-production lab skill. Use for machine learning experiment design, model evaluation, reinforcement learning, LLM building, tokenizer/data/architecture/pretraining/post-training plans, LLM/agent benchmarking, feature/data validation, MLOps, reproducibility, leakage checks, calibration, ablations, JAX/PyTorch research translation, and cross-domain AI systems. For investment capital decisions, investment-management remains decision owner and this skill is support.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# AI/ML Research Lab

## Quick Reference

### What It Does

Owns reusable AI, ML, RL, LLM, and agent-evaluation method design, validation,
reproducibility, and model-risk controls.

### Entrypoints

- ML/RL experiments, LLM building, research translation, agent evaluations, and model risk
- feature/label leakage, fold design, calibration, ablations, or MLOps questions
- financial time-series model validation, with `investment-management` as decision owner

### Inputs / Outputs

- Inputs: decision, owner, data lineage, as-of date, split policy, baseline, and promotion/kill gates.
- Outputs: experiment contract, evaluation plan, artifact manifest, model-risk review, and promote/iterate/kill decision.

### Dependencies / Tooling

Use the local references and deterministic validators. Domain skills retain
ownership of capital, banking, or growth decisions.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants

- No performance claim without a baseline, split policy, and leakage review.
- Fit transforms within folds; never treat incomplete labels as features.
- Missing artifact identity, version, or expiry fails closed.

## Role

Use this skill as the reusable AI research and model-engineering lab across the local skill library.

It does not replace domain owners:

- `investment-management` owns capital allocation, portfolio, trading, sizing, and risk decisions.
- `growth-operating-system` owns growth, marketing, funnel, and campaign decisions.
- `universal-banker` owns banking, credit, deal, underwriting, and capital-markets decisions.

This skill owns AI/ML/RL method design, experiments, model evaluation, reproducibility, leakage control, agent benchmarking, and research-to-production translation.

## Default Workflow

1. Classify the work.
   - `ML_EXPERIMENT`: supervised/unsupervised model, feature pipeline, forecast, classification, ranking.
   - `RL_EXPERIMENT`: policy learning, simulator, reward function, offline RL, online/paper deployment.
   - `LLM_BUILD`: tokenizer, dataset, Transformer architecture, pretraining, post-training, serving, model card, or LLM learning roadmap.
   - `LLM_AGENT_EVAL`: agent behavior, tool use, memory, benchmark, safety, or hallucination measurement.
   - `RESEARCH_TRANSLATION`: paper, notebook, model-guided research idea, JAX/PyTorch port, ablation plan.
   - `MODEL_RISK`: validation, monitoring, drift, calibration, governance, challenger model, kill switch.

2. Define the decision before modeling.
   - Target decision and user/domain owner.
   - Baseline, benchmark, and success metric.
   - Data source, as-of date, split policy, and forbidden leakage.
   - Promotion gate, rollback gate, and owner approval.

3. Load only the needed reference.
   - Experiment design: `references/experiment-design.md`
   - Financial time-series features, labels, and model artifacts: `references/time-series-feature-label-artifact-contract.md`
   - Databento market-data and predictive-ML work: `{SKILLS_ROOT}/_library/docs/DATABENTO_MARKET_DATA_ML_OPERATING_CONTRACT.md` (not bundled; recipient resource required)
   - Databento official docs and all examples: `{SKILLS_ROOT}/_library/docs/DATABENTO_OFFICIAL_DOCS_AND_EXAMPLES_CATALOG.md` (not bundled; recipient resource required)
   - LLM build roadmap: `references/llm-build-playbook.md`
   - RL and simulation: `references/rl-simulation.md`
   - LLM/agent evals: `references/llm-agent-evals.md`
   - Model risk/governance: `references/model-risk-governance.md`
   - Research translation: `references/research-translation.md`
   - Cross-agent ops, pass@k, worktree benchmarking, context budgets, and cost/runtime governance: `../agent-ops-control-plane`
   - Source map: `references/source-map.md`

4. Build the evaluation harness before interpreting results.
   - Baseline first.
   - Split policy before feature engineering.
   - Ablations before claims.
   - Confidence intervals or uncertainty bands when feasible.
   - Failure modes and negative controls.

5. Produce an audit-ready output.
   - Objective.
   - Dataset and as-of dates.
   - Baseline and benchmark.
   - Method.
   - Metrics and uncertainty.
   - Leakage controls.
   - Ablations.
   - Failure modes.
   - Promote / iterate / kill decision.

## Non-Negotiables

- No benchmark, no performance claim.
- No split policy, no modeling claim.
- No leakage analysis, no production promotion.
- No calibration check, no probability-as-decision claim.
- No cost/latency/resource estimate, no deployment recommendation.
- No online or capital-impacting rollout without kill switch and owner approval.
- No Databento predictive-model claim unless raw/derived lineage, point-in-time
  symbology, roll/session semantics, feature/label causality, historical/live
  parity, and the cache-to-cloud append contract satisfy the canonical
  Databento operating contract.

## Agentic Stack

Use the global `_library/docs/AGENTIC_OPERATING_LAYER.md` (not bundled; recipient resource required) when coordinating multiple agents.

Use `agent-ops-control-plane` as the support layer for cross-agent eval harnesses, pass@k reporting, worktree-isolated benchmarking, context-bloat audits, model/tool routing budgets, runtime governance, and continuous-learning promotion gates.

Recommended agents:

- Research Scout: source papers, repos, and prior art.
- Data Auditor: data contracts, splits, leakage, missingness, provenance.
- Experiment Designer: baseline, ablation matrix, metrics, sample size.
- Model Builder: implementation and training loop.
- Evaluation Lead: test harness, statistical readout, calibration, error analysis.
- Model Risk Officer: promotion gate, monitoring, drift, rollback.
- Production Integrator: packaging, reproducibility, runtime, cost, observability.

## Dispatch Rules

- Finance AI/RL/trading work: keep `investment-management` as decision owner; use this skill for experiments, model validation, RL simulation, and agent evals.
- For financial time-series ML, load `references/time-series-feature-label-artifact-contract.md` with `references/experiment-design.md`; `investment-management` remains the decision owner for capital allocation.
- Growth AI work: keep `growth-operating-system` as decision owner; use this skill for targeting models, causal experiments, uplift, attribution, and LLM campaign-agent evals.
- Banking/credit AI work: keep `universal-banker` as decision owner; use this skill for scorecards, model validation, challenger models, and explainability.
- Pure ML, RL, LLM, agent, or research work: this skill is the front door.
- LLM building or model ownership work: use `references/llm-build-playbook.md`; keep finance/trading applications under `investment-management` as decision owner.

## Scripts

- `scripts/ai_ml_router.py`: route task text to experiment type, references, agents, and required outputs.
- `scripts/experiment_gate.py`: validate that an experiment plan has the minimum fields for execution/promotion.
- `scripts/validate_time_series_contract.py`: validate a versioned financial time-series feature/label/model artifact contract.
