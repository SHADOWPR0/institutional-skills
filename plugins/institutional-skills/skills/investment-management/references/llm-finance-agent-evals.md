# LLM Finance Agent Evaluations

Use this when evaluating LLM agents for research, trading, risk, portfolio review, filings, news, prediction markets, or multi-agent investment workflows.

The goal is not to prove that an agent is smart. The goal is to find where it breaks before it can harm decisions.

## Evaluation Lanes

- Research agent: sources, thesis extraction, filing/news synthesis.
- Quant agent: hypothesis generation, code scaffolding, benchmark discipline.
- Trading agent: signal interpretation, risk constraints, trade proposal quality.
- Risk agent: exposure, drawdown, liquidity, regime, and invalidation checks.
- Portfolio agent: sizing, rebalance, tax/cost, concentration, mandate fit.
- Market-making agent: inventory, quote/pull, toxicity, latency, venue controls.

## Core Metrics

- Source fidelity.
- Numerical accuracy.
- Unsupported claim rate.
- Stale-data detection.
- Benchmark discipline.
- Risk-first behavior.
- Calibration.
- Tool-use correctness.
- Compliance with no-execution rules.
- Recovery after bad intermediate state.
- Role fidelity: each agent stays within its evidence, challenge, proposal, or decision authority.
- Handoff completeness and schema validity.
- Information isolation: no future or downstream-only data reaches an upstream role.
- Debate value: incremental errors caught or decisions improved per added round and token.
- Coordinator loss: material dissent and source caveats survive manager compression.

## Benchmark Design

- Static cases: frozen filings, frozen market snapshots, known answer keys.
- Historical cases: past regimes with known outcomes, no future leakage.
- Adversarial cases: bad data, contradictory sources, tempting overconfidence.
- Live shadow cases: current data, no trade authority, reviewed by human/domain owner.
- Team ablations: compare the full role graph with a strong single-agent baseline and smaller pods.
- Debate ablations: compare no debate, one challenge pass, and bounded multi-round debate.
- Resume tests: interrupt a run and prove that only state with matching instrument, date, data, prompt, role set, model, and graph identity can resume.

## Required Architecture Tests

- Exact prices, indicators, dates, returns, exposures, and limits come from deterministic tools or verified snapshots.
- Historical data adapters reject post-cutoff records and flag undated evidence.
- Decision roles use typed outputs with validation and explicit fallback behavior.
- Trader outputs remain proposals until the Portfolio Manager and deterministic risk rules accept them.
- Every decision records its benchmark, horizon, expected edge, requested size, costs, and invalidation condition.
- Outcome memory stores raw and benchmark-relative results plus one specific future decision rule.
- Prior memory cannot silently override current evidence.
- No role can call a broker, exchange, or capital action without separate explicit authority.

## Architecture Lessons From Recent Research

Recent LLM trading-agent work suggests agent framework and risk style can matter as much as model backbone. Treat model choice, prompt, memory, tools, and risk policy as separate variables.

Do not rely on headline returns from small preprint benchmarks. Require local replication or a conservative internal benchmark before promotion.

The public TradingAgents implementation is useful as a role-graph reference, especially its typed decision outputs, verified market snapshot, outcome-linked decision log, and graph-aware checkpointing. Use `references/investment-firm-agent-roster.md` for the locally hardened version. Do not import its claimed returns or connect the framework to capital.

## Promotion Gates

- Passes source/numerical fidelity gates.
- Flags stale/missing data.
- Does not invent prices, catalysts, filings, or risk metrics.
- Produces explicit invalidation conditions.
- Respects no-execution and capital-allocation guardrails.
- Improves human-reviewed research throughput or quality.
