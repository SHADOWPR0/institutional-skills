---
name: investment-management
description: Canonical asset-management team skill for investment research, portfolio management, capital allocation, risk, public/private markets, macro, quant/systematic research, AI/ML-assisted investing, derivatives, crypto, event markets, market structure, position sizing, performance review, and investment decision governance. Use as the sole investment decision owner; macro, technical analysis, AI/ML, plugins, and legacy model packs are support layers.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Investment Management

## Quick Reference

### What It Does

Operates as a full asset-management team: CIO, PM, research director, macro
desk, public equity desk, systematic research, portfolio construction, risk,
execution, performance attribution, falsification, and research operations.

### Entrypoints

- investment research, trade thesis, portfolio, risk, regime, or sizing work
- global macro rebuilds, macro thesis books, paper macro books, monthly checks,
  event reviews, or favored macro themes
- deep quant, crypto, market making, prediction markets, AI finance, or RL trading
- full asset-management team staffing or investment committee work
- private local research, preserved model/risk provenance, or house investment
  archives when the user explicitly asks for those artifacts

### Inputs / Outputs

- Inputs: mandate, objective mode, disclosure mode, as-of data, constraints, and risk limits.
- Outputs: source-backed decision memo, research packet, strategy route, risk
  brief, portfolio action proposal, org-staffed analysis, or
  `PROMOTE / ITERATE / KILL / WAIT / NO TRADE` decision.

### Dependencies / Tooling

Use `global-macro-theme-picker`, `technical-analysis`, `ai-ml-research-lab`,
`agent-ops-control-plane`, and curated plugins as support where applicable.
This skill remains the investment decision owner.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants

- No capital scaling without a benchmark, net economics, and explicit risk limits.
- Venue/framework evidence is not alpha evidence.
- A valid research packet never grants execution authority.

## Overview

This is the single canonical app-level investment-management skill. It
supersedes the formerly separate `investment-management-private`,
`investment-management-public`, production, and private-regime active skills
while preserving their source material inside this skill.

Use it to build evidence-based investment outputs in the user's house style:
compound capital, respect benchmarks, separate thesis from price and action,
prefer post-cost edge, preserve optionality, attack fragility, and never confuse
narrative confidence with a scalable investment decision. Private project names,
internal scores, and productized engines are provenance; active guidance should
translate them into evergreen institutional concepts unless the user asks for a
specific private artifact.

Start with `references/house-investment-philosophy.md` for doctrine and
`references/asset-management-operating-org.md` when the task needs a real
asset-management org chart or employee graph. Use
`references/full-cycle-investing-preference-model.md` when the task needs the
user's durable investment taste: debasement/liquidity awareness, power-law
growth, reflexivity, long/short horizon pluralism, and strong opinions loosely
held.

Use `references/skill-coverage-map.md` when the task asks which canonical
skills, desks, support functions, or adjacent operators are available from the
investment-management org.

For crypto venue, platform, connector, or market-making claims, load
`references/crypto-platform-and-venue-due-diligence.md` before selecting a
framework, adapter, or strategy. Platform capability is never inferred from a
framework or a similar venue.

## Alias Routing

Route all of these requests here:

- `investment-management`
- `investment-management-private`
- `investment-management-public`
- `investment-management-production`
- `investment-management-private-regime`
- "deep quant"
- "private local research archive"
- "preserved model risk stack"
- "portfolio construction"
- "position sizing"
- "market regime"
- "factor model"
- "risk wall"
- "trade memo"
- "crypto trading"
- "prediction markets"
- "market making"
- "AI quant"
- "ML alpha"
- "RL trading"
- "LLM finance agent"
- "favored macro themes"
- "global macro theme picker"
- "global macro"
- "macro quarterly-rebuild"
- "macro monthly-check"
- "macro event review"
- "paper global macro book"

Former top-level investment-management skills are consolidated under
`references/source-skill-index/legacy-packages/` (not bundled; recipient resource required), but they are no longer
separate front doors. If an older thread or agent mentions one of the old names,
route to this canonical skill and inspect `references/source-skill-index/README.md` (not bundled; recipient resource required)
only for provenance.

The Macro Desk sits inside this asset-management team through the unchanged
`global-macro-theme-picker` package. Keep that package separately callable for
locked downstream integrations. Use `references/macro-desk-integration.md`
for the boundary.

For recursive research intake and source maintenance, load
`references/owned-research-lifecycle.md`. Existing analytics are frozen; safe
reference, fixture, routing, and failure-detection improvements may promote only
after deterministic tests, while analytical changes remain staged challengers.

## Classification Modes

Always set the disclosure mode first:

- `PRIVATE_INTERNAL`
  - Use private local research corpus, preserved model/risk provenance, formulas, implementation details, private run artifacts, and internal governance logic.
  - This is the default for the user's private workflows.
- `PUBLIC_SAFE`
  - Use public-safe strategy frameworks and sanitized abstractions.
  - Do not expose proprietary formulas, tuned private coefficients, private prompts, private data, or confidential execution logic.

If the user does not specify the mode, default to `PRIVATE_INTERNAL` for local/private work and `PUBLIC_SAFE` for external deliverables.

## Operating Modes

Always set one objective mode:

- `QUALITY_COMPOUNDING`
  - Durable compounding mode. Optimize risk-adjusted return and consistency.
  - Prefer stable edges, lower turnover, lower correlation, tight drawdown governance, and strong benchmark discipline.
- `OPPORTUNITY_CAPTURE`
  - Opportunity-capture mode. Optimize absolute return subject to hard risk limits.
  - Allow higher turnover, concentration, tactical expression, and convex payoff structures.

If the user does not specify a mode:

- default to `OPPORTUNITY_CAPTURE` when the mandate is alpha-seeking,
  tactical, event-driven, crypto, options, venture/growth, exotics, trading
  desk, or otherwise explicitly profit-maximizing and the risk limits are known
- default to `QUALITY_COMPOUNDING` when the mandate is fiduciary, strategic,
  defensive, benchmark-sensitive, drawdown-sensitive, or missing a clear risk
  budget
- maintain both modes; when in doubt, show the `OPPORTUNITY_CAPTURE` route first
  and the `QUALITY_COMPOUNDING` route as the risk-disciplined comparison

## Deep Quant Coverage

This skill includes deep quant and systematic capability through the merged
private/public/production materials and support links:

- multi-factor systematic equity
- market-neutral statistical arbitrage
- macro systematic trend, carry, and relative value
- technical/statistical short-horizon trading
- options convexity, tail hedging, and volatility carry
- crypto basis, funding, cross-venue relative value, and market making
- prediction-market probability edge, consistency arbitrage, time-decay, and event market making
- inventory-aware traditional market making with toxicity, fill-quality, realized-spread, and hedge-latency controls
- regime detection and regime-throttle governance
- Kelly-style sizing, Sortino/Sharpe/Calmar-style diagnostics, drawdown gates, turnover-adjusted alpha, factor crowding checks, correlation drift, and capacity review
- out-of-sample skepticism, benchmark discipline, and underperformance incident handling
- AI/ML/RL-assisted alpha research, LLM finance-agent evaluation, market-simulation/RL support, and model-risk gates through `ai-ml-research-lab`

Quant outputs must separate:

- measured facts
- model estimates
- assumptions
- inference
- action
- invalidation condition

No benchmark means no capital scaling decision.

## Workflow

1. Define the decision before analysis.
   - Confirm objective, horizon, constraints, and risk tolerance.
   - Confirm whether the task is exploratory research, portfolio decision support, or execution planning.
   - Confirm what must be delivered (memo, ranked list, risk brief, action plan).
   - Set `PRIVATE_INTERNAL` vs `PUBLIC_SAFE`.
   - Set `QUALITY_COMPOUNDING` vs `OPPORTUNITY_CAPTURE`.

2. Load only the relevant corpus slices.
   - Start with `references/house-investment-philosophy.md`.
   - Use `references/full-cycle-investing-preference-model.md` for user
     preference/context when selecting lenses, horizons, benchmarks, or
     decision packet fields.
   - Use `references/asset-management-operating-org.md` for org-chart staffing.
   - Use `references/skill-coverage-map.md` when the user asks whether the
     investment org can see every canonical skill or support capability.
   - Start source retrieval with `references/source-map.md` and open the smallest set of files needed.
   - Use repo docs/contracts before large notebooks.
   - Use `references/strategy-router.md` to select the investment lane.
   - Use `references/strategy-taxonomy.md` for the framework and metrics.
   - Use `references/performance-governance.md` for kill-switches and underperformance handling.
   - Use `references/outcome-linked-decision-ledgers.md` when a recurring research, trade, allocation, private-deal, or strategy-review loop needs decision memory tied to observed outcomes.
   - Use `references/investment-firm-agent-roster.md` when staffing an analyst pod, trading desk, risk committee, or full investment-firm agent team.
   - Use `references/quant-ai-benchmarking.md`, `references/rl-market-simulation-lab.md`, or `references/llm-finance-agent-evals.md` when AI/ML/RL or finance-agent evaluation is involved.
   - Use `{SKILLS_ROOT}/global-macro-theme-picker` as the
     default Macro Desk operating package for zero-based macro rebuilds, thesis
     books, expression comparison, price-aware entry states, paper-book
     recommendations, monthly checks, event reviews, and sanitized theme
     handoffs. Do not relocate or rename it.
   - Use `{SKILLS_ROOT}/_library/docs/DATABENTO_MARKET_DATA_ML_OPERATING_CONTRACT.md` (not bundled; recipient resource required) for Databento-backed futures research, predictive modeling, execution data, point-in-time roll/session handling, and hosted data continuity.
   - Use `{SKILLS_ROOT}/_library/docs/DATABENTO_OFFICIAL_DOCS_AND_EXAMPLES_CATALOG.md` (not bundled; recipient resource required) to select the exact official Databento schema, API, venue, or example page; tutorials remain implementation references, never alpha or promotion evidence.
   - Use `scripts/pdf_excerpt.py` (not bundled; recipient resource required) for PDF triage before deep reading.

3. Anchor on deterministic state.
   - For preserved model/risk outputs, anchor on contracts, regime outputs,
     diagnostics, ranking outputs, run metadata, and manifest artifacts.
   - Record data freshness (as-of date/time) and mark stale inputs explicitly.

4. Synthesize into an actionable view.
   - Separate facts, inferences, and assumptions.
   - Quantify risks first: concentration, leverage, drawdown paths, liquidity, and regime mismatch.
   - Map any recommendation to explicit triggers and invalidation conditions.
   - Include expected edge source, benchmark, risk budget, sizing logic, and stop/scale rules.

5. Deliver in an audit-ready structure.
   - Include source-backed evidence and file paths.
   - Include decision logic, not just a conclusion.
   - Include what would change the recommendation.
   - Include stale/missing-data flags.

6. Install the performance control loop.
   - Register hypothesis, benchmark, hurdle, review window, and stop conditions.
   - Use `references/recursive-improvement.md` when a strategy needs diagnosis, patching, retesting, or retirement.

## Strategy Routing

Use `scripts/strategy_router.py` or `references/strategy-router.md` when the task needs strategy selection.

Required routing fields:

- `objective_mode`: `QUALITY_COMPOUNDING` or `OPPORTUNITY_CAPTURE`
- `mandate_type`: `endowment`, `personal`, `corporate`, `trading_desk`, `venture_private`
- `horizon`: `intraday`, `swing`, `position`, `strategic`
- `regime`: `risk_on`, `risk_off`, `transition`
- `volatility_state`: `low`, `normal`, `high`
- `liquidity_state`: `ample`, `normal`, `tight`
- `data_edge`: `fundamental`, `quant_signal`, `flow_microstructure`, `hybrid`

Every routing decision must produce:

- selected primary sleeve
- selected secondary sleeves
- avoided sleeves
- risk budget allocation
- triggers for upgrade/downgrade
- invalidation conditions

## Vertical Coverage

- value and quality value
- growth, compounders, innovation themes
- fundamental discretionary long-only and long/short
- sector research across technology, internet/media/telecom, consumer,
  healthcare, financials, industrials, energy, materials, real estate,
  utilities/infrastructure, small/mid cap, developed international, emerging,
  and frontier markets
- quant factor and systematic equity
- market-neutral statistical arbitrage
- macro systematic trend/carry/relative value
- discretionary global macro research through the default
  `global-macro-theme-picker` child skill
- technical and tactical discretionary trading
- options, volatility, convexity, and tail-risk overlays
- crypto spot, derivatives, basis, funding, cross-venue, and market making
- prediction markets and Polymarket-style event strategies
- traditional multi-asset market making and liquidity provision
- AI/ML-assisted alpha research and signal evaluation
- RL market simulation, execution-policy testing, and market-making policy research
- LLM finance-agent benchmarking for research, risk, trading, and portfolio workflows
- global investment opportunities, cross-asset dislocations, exotics, forced
  selling, capital-structure relative value, structured notes, insurance-linked
  risk, and opportunistic special situations
- venture capital and growth equity across seed, Series A/B/C, growth,
  pre-IPO/crossover, secondaries, fund/manager diligence, platform support,
  company-building, reserve strategy, and VC-to-banking handoffs
- composable investment-firm agent teams spanning evidence, challenge, trade construction, independent risk, portfolio decision, and performance memory
- endowment/OCIO allocation
- corporate treasury and liquidity management
- private/venture pacing and reserve strategy
- SEC filing and financial statement analysis when paired with EdgarTools or ratio/DCF skills
- Alpha Vantage or other market-data workflows when current data is required

## Adjacent Skill Dispatch

Keep this skill as the decision owner. Dispatch to adjacent skills only when their specific tooling is needed:

- `EdgarTools` for SEC filings, XBRL, company filings, and multi-company filing analysis.
- `alpha-vantage-automation` for Alpha Vantage market data workflows.
- `creating-financial-models` for DCF, sensitivity tables, Monte Carlo valuation, and scenario models.
- `financial-analyst` or `analyzing-financial-statements` for ratios, statements, DCF reports, rolling forecasts, and benchmark analysis.
- `crypto-research` for broad crypto market research, news, sentiment, and coin-specific work.
- `technical-analysis` for CMT-curriculum-aligned market structure, indicators, patterns, multi-timeframe synthesis, scoped empirical edge, and causal analyst replay. Use legacy imported `stock-analyzer` only for lightweight compatibility utilities.
- `bankr` for crypto wallet/trading/Polymarket/DeFi operations when the user explicitly wants execution or account actions.
- `moon-dev-trading-agents` for Moon Dev trading-agent repository work, autonomous crypto agents, and its backtesting agent.
- `ai-ml-research-lab` for AI/ML/RL experiment design, leakage checks, LLM/agent evals, model-risk governance, research translation, simulation design, and reusable AI lab methods. Keep this skill as decision owner for investment and capital-allocation judgment.
- `agent-ops-control-plane` for investment-agent swarms, context budgets, pass@k evals, worktree-isolated benchmark variants, runtime/cost governance, recursive decision ledgers, and kill-switch discipline around long-running research agents. Keep this skill as decision owner for capital-allocation judgment.
- `universal-banker` for underwriting, credit, capital markets, securitization, M&A, covenant design, deal structuring, or banking work.
  Venture debt, M&A, structured finance, credit/lender terms, covenants, and
  closing conditions for VC/growth companies route there; this skill keeps
  portfolio fit, ownership, reserve, and investment judgment.

## Curated Plugin Support

The bundled Public Equity Investing and Investment Banking plugins can be used as support libraries for polished trackers, model updates, model audits, earnings/event workflows, risk reports, valuation scaffolds, memo/deck QC, and banking-adjacent artifact discipline.

Keep this skill as the decision owner. Load `references/plugin-support-map.md` only when a plugin workflow improves the deliverable. Do not edit plugin-cache files or replace the user's private local investment logic with plugin router rules.

## Output Patterns

Use one of these structures unless the user requests another format:

- Decision memo
  - Objective
  - Current regime and evidence
  - Portfolio impacts
  - Recommended action
  - Tripwires and invalidation

- Trade thesis review
  - Thesis summary
  - Supporting evidence
  - Failure modes
  - Position sizing and risk budget notes
  - Monitoring plan

- Portfolio checkpoint
  - Exposures and concentration
  - Macro alignment vs holdings
  - Hedging/sizing adjustments
  - Priority actions (now, next, later)

- Quant research memo
  - Hypothesis
  - Universe and data freshness
  - Benchmark and dumb baseline
  - Signal construction
  - Backtest and out-of-sample checks
  - Costs, slippage, turnover, and capacity
  - Factor and beta attribution
  - Failure modes and kill criteria
  - Promote / iterate / kill decision

- Strategy routing brief
  - Mandate and objective mode
  - Current regime/liquidity/volatility state
  - Primary sleeve
  - Secondary sleeves
  - Avoided sleeves
  - Risk budget
  - Upgrade/downgrade triggers

- Market-making or event-market brief
  - Instrument/venue/event
  - Fair value or calibrated probability
  - Edge net of fees/slippage
  - Inventory or max-loss limits
  - Toxicity/resolution/venue-risk controls
  - Quote/pull/scale rules

## Guardrails

- Do not claim certainty from narrative-only documents.
- Do not invent prices, returns, or metrics when data is missing.
- Do not present raw model prose as execution instructions without risk checks.
- Do not expose secrets or private credentials discovered in notebooks or documents.
- Do not treat this workflow as legal, tax, or licensed brokerage advice.
- Do not export proprietary internals in `PUBLIC_SAFE` mode.
- In `PRIVATE_INTERNAL` mode, use proprietary internals only for the user's local/private analysis.
- Treat any strategy with missing benchmark, stale data, or untested transaction costs as incomplete.
- For Databento-backed trading research, require the canonical Databento
  operating contract before accepting any model, OOS, sizing, or deployment
  claim; the vendor's example notebooks are methodological starting points, not
  economic promotion evidence.

## Data Hygiene

- Prefer canonical contracts/specs when notebook outputs conflict with docs.
- Surface schema anomalies and malformed exports before interpretation.
- Flag duplicate or inconsistent files (for example, multiple similarly named drafts).
- Record as-of dates for market data, portfolio state, and model outputs.
- Validate required columns before using CSV/parquet/model exports.
- Redact secrets or credentials if source notebooks contain them.

## References

- Source routing and corpus map: `references/source-map.md`
- House investment philosophy: `references/house-investment-philosophy.md`
- Full-cycle investing preference model: `references/full-cycle-investing-preference-model.md`
- Asset-management operating org: `references/asset-management-operating-org.md`
- Macro Desk integration: `references/macro-desk-integration.md`
- Venture Capital operating desk: `references/venture-capital-operating-desk.md`
- Engine and contract notes: `references/framework-notes.md`
- Strategy router: `references/strategy-router.md`
- Strategy taxonomy: `references/strategy-taxonomy.md`
- Performance governance: `references/performance-governance.md`
- Outcome-linked decision ledgers: `references/outcome-linked-decision-ledgers.md`
- Investment-firm agent roster: `references/investment-firm-agent-roster.md`
- Recursive improvement: `references/recursive-improvement.md`
- Market-making playbook: `references/market-making-playbook.md`
- Crypto platform and venue due diligence: `references/crypto-platform-and-venue-due-diligence.md`
- Prediction-markets playbook: `references/prediction-markets-playbook.md`
- Mandate playbooks: `references/mandate-playbooks.md`
- Curated paper index: `references/paper-index.md`
- Curated plugin support map: `references/plugin-support-map.md`
- AI/ML finance source map: `references/ai-ml-source-map.md`
- Quant AI benchmarking: `references/quant-ai-benchmarking.md`
- RL market simulation: `references/rl-market-simulation-lab.md`
- LLM finance-agent evals: `references/llm-finance-agent-evals.md`
- Local private corpus: `references/corpus/` (not bundled; recipient resource required)
- Preserved source skill archive: `references/source-skill-index/` (not bundled; recipient resource required)

## Scripts

Use `scripts/pdf_excerpt.py` (not bundled; recipient resource required) to extract metadata and short excerpts from PDFs for fast triage.
Use `scripts/strategy_router.py` to route mandate context to strategy families.
Use `scripts/build_corpus.py` (not bundled; recipient resource required) to refresh local corpus copies when source material changes.
