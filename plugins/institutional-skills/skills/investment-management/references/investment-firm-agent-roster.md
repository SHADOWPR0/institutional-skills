# Investment Firm Agent Roster

Use this module when staffing a temporary research pod, trading desk, risk
review, or full investment-firm simulation. It is an employee roster inside
`investment-management`, not a separate skill or trading system.

For the full evergreen asset-management org chart, use
`references/asset-management-operating-org.md`. This file gives the compact
packet contract and deployment presets.

## Command Structure

The CIO / Investment Committee owns final capital judgment. The Portfolio
Manager owns mandate fit, sizing, and portfolio construction. Specialist desks
supply evidence or challenge. The Trader converts an approved thesis into a
trade proposal. No agent receives execution authority by default.

### Evidence Team

- Market Data Verifier: produces the as-of snapshot, source timestamps, stale-data flags, corporate-action checks, and look-ahead audit.
- Fundamental Analyst: statements, unit economics, quality, valuation, revisions, and accounting risks.
- Market and Technical Analyst: invokes `technical-analysis` for causal price structure, volatility, liquidity, positioning, trend, mean reversion, and microstructure where the supplied data supports it; emits its typed proposal packet and never receives execution authority.
- Macro Desk: invokes `global-macro-theme-picker` for growth, inflation, policy,
  liquidity, rates/curves, FX, commodities, credit, country/regional equity
  themes, reserve assets, structural/fiscal themes, expression comparison, and
  paper-book macro work. The macro package remains separately callable for
  locked downstream integrations.
- Public Equity Analyst: listed-company fundamentals, estimates, valuation,
  catalysts, factor exposure, and thesis tracking.
- Systematic Research Analyst: signal design, causal timestamps, baselines,
  walk-forward evidence, costs, turnover, and capacity.
- Derivatives and Volatility Analyst: options, convexity, volatility carry,
  hedges, greeks, scenario loss, and hedge failure.
- Crypto and Event Markets Analyst: basis, funding, probability edge,
  resolution risk, venue capability, connector boundaries, and market making.
- News and Event Analyst: dated catalysts, filings, earnings, legal or regulatory events, and event-path scenarios.
- Sentiment and Positioning Analyst: crowding, flows, options positioning, surveys, and source-quality limits.

### Challenge Team

- Bull Researcher: states the strongest evidence-backed upside case and identifies what would make it larger.
- Bear and Falsification Researcher: attacks assumptions, searches for disconfirming evidence, and defines thesis-break conditions.
- Research Manager: scores evidence quality, resolves material disagreements, and produces the research recommendation.

### Portfolio Team

- Trader: converts the research view into a proposed instrument, direction, entry logic, horizon, exit logic, and implementation alternatives.
- Upside Risk Analyst: tests convexity, missed-opportunity cost, and whether caution understates asymmetric upside.
- Capital Preservation Analyst: tests ruin, drawdown, liquidity, gap, leverage, correlation, and model-risk paths.
- Scenario Risk Analyst: compares base, bull, bear, transition, and black-swan paths without advocacy.
- Portfolio Manager: owns mandate fit, benchmark, expected edge, sizing method, covariance, capital budget, and the final `PROMOTE / ITERATE / KILL / NO TRADE` decision.
- Performance and Memory Analyst: resolves decisions against outcomes and compresses specific lessons into the decision ledger.

## Required Handoff

Every role returns a compact structured packet:

- `as_of` and `data_cutoff`
- `instrument_or_universe`
- `objective_mode` and `horizon`
- `sources` with timestamps
- `verified_facts`
- `estimates_and_assumptions`
- `thesis_or_role_view`
- `edge_and_benchmark`, when applicable
- `costs_liquidity_and_capacity`
- `failure_modes`
- `invalidation_conditions`
- `confidence_and_calibration_basis`
- `recommended_next_action`

The Trader additionally returns instrument, action, entry condition, exit condition, stop or risk limit, size requested, expected holding period, and implementation costs. The Portfolio Manager must accept, modify, reject, or defer each field explicitly.

## Deployment Presets

- Fast screen: Market Data Verifier, one relevant specialist, Bear/Falsification Researcher, Portfolio Manager.
- Public-equity pod: verifier, fundamental, market, macro, news, sentiment, bull, bear, research manager, trader, three risk views, portfolio manager.
- Quant review: verifier, quant researcher, leakage auditor, benchmark analyst, execution-cost analyst, risk analyst, portfolio manager.
- Event desk: verifier, event analyst, fundamental analyst, bull, bear, trader, scenario risk, portfolio manager.
- Macro book: Macro Desk, Portfolio Construction, Falsification, Performance
  Attribution, CIO / Investment Committee.
- Full firm: add strategy-specific pods only after the mandate and evidence justify the cost.

Do not deploy every role by habit. Add a role only when it brings distinct data, method, or decision authority.

## Debate Rules

- Debate only a material disagreement with identifiable evidence on both sides.
- Cap rounds before launch. Default to one claim, one rebuttal, and one manager synthesis.
- Preserve each side's evidence separately; do not compress away dissent before the manager sees it.
- Score whether debate changed the decision or exposed a failure mode. Retire debates that add words but not information.
- Use a fresh-context falsification pass for high-consequence decisions.

## Production Controls

- Deterministic data beats agent prose for prices, indicators, dates, returns, exposures, and limits.
- Historical runs must reject records after the stated cutoff, including undated news when provenance cannot be proved.
- Checkpoints must include instrument, as-of date, data version, role set, prompt version, model, and graph shape. Never resume incompatible state.
- Store decision records append-only. Resolve them later against raw return, benchmark-relative return, costs, and the original horizon.
- Memory may inform a new decision but cannot override current evidence or risk rules.
- Broker, exchange, email, filing, deployment, and capital actions require separate explicit authority.

## Source Provenance

Concepts were adapted from the public TradingAgents architecture and hardened for the user's existing investment-management system.

- Source: https://github.com/TauricResearch/TradingAgents
- Inspected commit: `01477f9afb7a47b849ed4c9259d3a9a4738d9fda`
- License observed: Apache-2.0
- Local snapshot: `{RECIPIENT_RESOURCE}`
