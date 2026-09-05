# Crypto Platform And Venue Due Diligence

Use this reference before any crypto venue, product, connector, framework, or
market-making recommendation. It is an evidence contract, not exchange
instructions and not an alpha claim.

## 1. Decision Order

Resolve in this order: mandate -> venue and product -> point-in-time data ->
adapter -> framework -> strategy. A framework can describe a strategy class;
it cannot establish venue support, current API behavior, net economics, or
operational readiness.

## 2. Capability Matrix

Keep one row for each claimed capability with these fields:

| Scope | Capability | Status | Evidence | As-of | Blocker |
| --- | --- | --- | --- | --- | --- |
| venue/product/adapter/framework/strategy | precise supported action | `SUPPORTED`, `UNSUPPORTED`, or `UNVERIFIED` | official source, test, or run record | timestamp | next proof required |

`SUPPORTED` requires direct evidence for the exact venue, product, adapter,
and requested operation. `UNSUPPORTED` means a documented limitation,
negative test, or missing required interface. `UNVERIFIED` is the default and
blocks promotion. Do not infer Coinbase perpetual support from Coinbase spot
support, or one connector's behavior from another connector.

## 3. Product Data And Risk Fields

| Area | Spot | Perpetual |
| --- | --- | --- |
| market identity | symbol, base/quote, tick/lot, fees | contract, settlement asset, tick/lot, fees |
| executable state | bid/ask, depth, trades, order status | bid/ask, depth, trades, mark/index, order status |
| carrying risk | custody, transfer, borrow where applicable | funding, basis, leverage, margin tier, liquidation, mark/index divergence |
| lifecycle | listing/delisting, halts, deposits/withdrawals | expiry if applicable, funding schedule, maintenance margin, liquidation rules |

Missing point-in-time fees, precision, order-state semantics, or derivative
mark/index/funding fields makes net economic or risk claims incomplete.

## 4. Connector Evidence Grades

- `SOURCE_ONLY`: documented interface or source inspection only.
- `MOCKED_TEST`: deterministic mocked request/response tests.
- `PAPER`: venue-supported paper or sandbox behavior.
- `LIVE_DATA_SHADOW`: live market/order-state data with no capital or orders.
- `CAPPED_LIVE`: separately authorized, capped capital under reconciled logs.

Each grade is scoped to a specific venue, product, adapter version, and
operation. Higher grades do not transfer to another product or venue.

## 5. Directional Platform Scorecard

Score each candidate separately on: product availability, data completeness,
adapter evidence grade, order-state reconciliation, fee/slippage model,
liquidity/capacity, operational incident handling, legal/compliance fit, and
net economics. Record the evidence and as-of timestamp next to each score.
The score compares diligence completeness; it does not authorize a trade.

## 6. Market-Making Scorecard

For every venue/product, report at minimum:

- realized spread after fees/rebates and hedge costs;
- adverse-selection loss and toxicity behavior;
- inventory VaR and inventory half-life;
- quote uptime, rejects, cancels, and cancel/replace latency;
- hedge slippage, latency, and basis/funding exposure;
- stale-book, disconnect, duplicate-intent, and reconciliation incidents.

Gross quoted spread is not PnL. A market-making framework with no measured
net economics remains research only.

## 7. License And Clean-Room Gate

Keep source provenance, commit, license, and concept/code boundary in the
research record. The reviewed public references are:

| Source | Observed commit | License boundary | Permitted local use |
| --- | --- | --- | --- |
| Freqtrade | `d433b1b` | GPL; concepts only | leakage and research-process concepts |
| Hummingbot | `816b8ab` | Apache-2.0 | interface/process concepts after independent review |
| Jesse | `fa63531c` | MIT | testing and research-process concepts after independent review |
| TradersPost | `7217833` | unlicensed/unclear | factual observations only |

No copied strategy, adapter, or execution code enters proprietary systems from
this reference. Reimplement only from an independently written specification
after license, API, and contamination review.

## 8. No Alpha From Framework

Framework availability, an open-source backtest, a connector README, and a
passing mock are implementation evidence only. They do not demonstrate edge.
Promotion requires a frozen hypothesis, causal data, venue-specific execution
assumptions, net-of-fee/slippage economics, comparable baseline, and OOS or
forward-paper evidence.

## 9. Promotion And Venue Retirement

Promote only when the exact capability matrix row is `SUPPORTED`, connector
evidence reaches the predeclared grade, reconciliation and incident behavior
are tested, economics are net, and the capital owner approves the risk limit.
Retire or downgrade a venue/product when support changes, data becomes stale,
reconciliation fails, reject/cancel behavior breaches limits, incidents repeat,
or net economics fail their predeclared hurdle. Default state on missing proof
is `UNVERIFIED` and no capital action.

## 10. Minimum Evaluation Matrix

Evaluate each separately: Coinbase spot directional, Coinbase perpetual
directional, Coinbase spot market making, and non-Coinbase perpetual
directional. A pass requires a distinct platform, connector, venue, product,
and strategy evidence record; unsupported capabilities block the case;
Coinbase perpetual is never inferred from Coinbase spot; and every viable case
includes net economics. This contract intentionally contains no
exchange-specific operational directions.
