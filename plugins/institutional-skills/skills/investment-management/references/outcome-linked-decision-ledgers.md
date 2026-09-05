# Outcome-Linked Decision Ledgers

Use this reference when investment research or capital decisions should compound through memory instead of ending as one-off analysis.

The purpose is simple: connect the original hypothesis to the later result, then compress the lesson into reusable decision memory.

## When To Use

Use for recurring or reviewable decisions:

- public equity theses and trade memos;
- quant signal promotion, demotion, or retirement;
- options, volatility, crypto, prediction-market, or market-making hypotheses;
- private deals, SPVs, reserve pacing, follow-on decisions, and valuation marks;
- manager, strategy, or mandate reviews;
- AI/LLM finance-agent research loops where the agent makes a recommendation that can be scored later.

Do not use a ledger as trade authorization. The ledger improves memory and review quality; it never bypasses human approval, risk rules, legal/tax constraints, or execution controls.

## Minimum Ledger Record

Each entry should capture:

- `date`
- `asset_or_deal`
- `decision_type`
- `objective_mode`: `QUALITY_COMPOUNDING` or `OPPORTUNITY_CAPTURE`
- `hypothesis`
- `recommended_action`
- `size_or_exposure_requested`
- `actual_action_taken`, if different
- `benchmark`
- `hurdle_or_expected_edge`
- `time_horizon`
- `invalidation_condition`
- `risk_budget_or_max_loss`
- `key_sources`
- `owner`
- `review_date`
- `status`: `pending`, `resolved`, `retired`, or `superseded`

No benchmark means no scaling decision. If a benchmark is hard to define, write the benchmark problem explicitly rather than hiding it.

## Outcome Review

At review time, append:

- `raw_result`
- `benchmark_result`
- `alpha_or_relative_result`
- `holding_or_review_period`
- `costs_slippage_fees_or_dilution`
- `what_worked`
- `what_failed`
- `base_rate_update`
- `next_decision_rule`
- `promote_iterate_or_retire`

For private investments, the "result" may be qualitative or marked-to-model. Mark that clearly:

- realized cash return;
- third-party priced round;
- internal mark;
- milestone progress;
- failure, delay, dilution, or write-down;
- no reliable mark yet.

## Reflection Standard

Keep reflections short enough to be injected into future work:

- Was the directional or allocation call right relative to the chosen benchmark?
- Which part of the thesis held or failed?
- What concrete lesson should influence the next similar decision?

Avoid generic lessons like "do more research." A useful lesson changes a future filter, sizing rule, diligence step, timing rule, benchmark choice, or kill condition.

## Anti-Theater Rules

- Do not log research that never led to a decision unless it killed a bad idea for a clear reason.
- Do not let narrative confidence override stale data, missing costs, or an undefined benchmark.
- Do not count activity as learning until the entry has an outcome or an explicit retired status.
- Do not promote an agent, model, signal, or strategy from a single attractive example.
- Do not reuse private/proprietary reasoning in public-safe outputs.

## Local Integration

Use this alongside:

- `references/performance-governance.md` for kill switches and underperformance response;
- `references/recursive-improvement.md` for patch/retest/retire loops;
- `references/llm-finance-agent-evals.md` when an LLM agent produced or influenced the recommendation.

Capital memory should remain source-backed and human-readable. Prefer append-only markdown or structured YAML/CSV with stable fields over scattered chat summaries.

## Provenance

Source reviewed: https://github.com/TauricResearch/TradingAgents

Observed commit: `c15200dc286b66abce3f1bcf09b298dc06b8539d`

Fresh snapshot reviewed on 2026-07-12: `01477f9afb7a47b849ed4c9259d3a9a4738d9fda` (`v0.3.1`). The newer implementation retains the append-only outcome loop and adds typed decision outputs, verified market snapshots, look-ahead controls, benchmark mapping, and graph-aware checkpoint recovery.

License observed: Apache-2.0.

Useful pattern: append a pending decision, resolve it later with raw result and benchmark-relative result, then store a terse reflection that future analysis can reuse.

Local integration decision: concept-only. Do not run or install TradingAgents as a trading system and do not connect it to private-execution-system, private-execution-system, mortgage-partnerships, brokers, exchanges, or capital execution workflows without a separate explicit approval and sandboxed evaluation.
