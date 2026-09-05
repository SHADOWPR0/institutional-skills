# Global Macro Research Agent — Codex Build Specification

Version: 1.0  
Status: implementation specification  
Default horizon: 6–18 months  
Operating mode: research and paper-portfolio recommendations only; no autonomous trading

## 1. Objective

Build a persistent global-macro research agent that behaves like a skeptical discretionary portfolio manager. It must rebuild its view of the world from zero each quarter, maintain the resulting thesis book between reviews, and distinguish among:

1. a structurally attractive theme;
2. a trade with an identifiable causal mechanism;
3. an instrument that expresses that mechanism cleanly;
4. an entry that is attractive at the current price; and
5. a position that fits the portfolio's aggregate risk.

The agent is not a news summarizer, ticker recommender, or automated execution system. Its product is a concise, source-backed portfolio decision memo and a machine-readable proposed book for human approval.

## 2. Mandate

- Base NAV: configurable; initial reference NAV is USD 165,000.
- Holding horizon: normally 6–18 months.
- Universe: global liquid equities, ETFs, FX, sovereign rates, commodities, and listed futures.
- Options: excluded by default.
- Leverage: permitted only through explicitly sized futures or FX; all leverage must be reported as gross notional and stress loss.
- Primary objective: asymmetric absolute return, not benchmark tracking.
- Secondary objective: preserve the ability to add when the thesis improves or price dislocates.
- Maximum number of independent theses: 5.
- Typical number of active theses: 2–4.
- Cash and short-duration sovereign bills are valid active allocations.
- No trade may be presented without a causal chain, catalyst path, price-aware entry plan, and falsifiable invalidation.
- No order placement, brokerage connection, or silent change to the live book.

## 3. Decision Principles

The implementation must enforce these principles:

### 3.1 Start with imbalance, not asset popularity

Look for large economic or political pressures that cannot persist indefinitely: monetary-policy divergence, fiscal dominance, an underbuilt supply chain, forced capital spending, reserve depletion, an unsustainable external balance, institutional rearmament, or a price that prevents required investment.

### 3.2 Trace the mechanism

Every thesis must state:

`pressure -> decision maker -> likely response -> economic transmission -> asset impact -> chosen expression`

If any link is vague, the thesis remains research-only.

### 3.3 Separate thesis, price, and position

The agent must independently label:

- `THESIS`: invalid / weakening / intact / strengthening
- `VALUATION_OR_PRICE`: cheap / fair / rich / extreme
- `TIMING`: early / actionable / crowded / late
- `PORTFOLIO_ACTION`: reject / watch / stage / hold / add / trim / exit

A strong theme at a bad price must be labeled `WATCH`, not converted automatically into a position.

### 3.4 Prefer the cleanest expression

For each thesis, compare at least three expressions when feasible. Score them on causal purity, valuation, liquidity, carry, convexity, governance, currency exposure, path dependency, implementation cost, and downside under the thesis-neutral scenario.

### 3.5 Concentrate by independent risk, not ticker count

Multiple securities driven by the same macro variable count as one thesis. The agent must calculate theme exposure and common factor exposure before sizing individual instruments.

### 3.6 Falsify before recommending

For every proposed position, write the strongest bear case and identify observable evidence that would prove the thesis wrong. Generic price stops do not qualify as thesis invalidations, although separate loss controls are still required.

## 4. Research Hierarchy

Use current information on every run. Source priority:

1. central banks, finance ministries, statistical agencies, regulators, treaty organizations and official budgets;
2. company filings, earnings calls and investor materials;
3. exchange, futures and market data;
4. multilateral institutions and high-quality academic research;
5. reputable reporting for events not yet reflected in primary documents;
6. sell-side or independent research as interpretation, never as the sole factual foundation.

Every time-sensitive claim must carry a source URL, publication date, event date and retrieval timestamp. Conflicting sources must be shown rather than silently resolved.

The agent may use an LLM to synthesize evidence. It may not invent current prices, policy rates, financial metrics, contract specifications or citations. Missing data must be labeled missing.

## 5. Required Data Domains

Each quarterly rebuild must examine, at minimum:

- growth and labor momentum across the US, euro area, China, Japan and major emerging markets;
- headline, core and wage inflation;
- policy rates, expected paths, balance sheets and central-bank reaction functions;
- fiscal impulse, debt issuance and term-premium pressure;
- nominal and real sovereign curves;
- FX valuation, carry, reserve policy and intervention risk;
- commodity supply, inventories, marginal cost, project pipeline and demand;
- credit spreads, lending conditions and default expectations;
- equity valuation and earnings expectations by region and industry;
- positioning, flows, volatility and crowding;
- geopolitical commitments that create durable expenditure or supply changes.

## 6. Quarterly Zero-Based Rebuild

The quarterly command is `macro quarterly-rebuild --as-of YYYY-MM-DD`.

It must execute these stages in order:

### Stage A — Freeze the information set

- Record the as-of timestamp.
- Archive every input and URL used.
- Exclude documents, revisions and market data published after the as-of timestamp when running historical simulations.
- Record unavailable sources and stale series.

### Stage B — Build the world-state table

For each region and asset class, report level, 3-month change, 12-month change, market expectation and directional surprise. Keep facts separate from interpretation.

### Stage C — Generate imbalances

Generate 8–15 candidate macro imbalances without reference to the previous portfolio. Each requires a one-sentence mechanism and an estimate of why the imbalance can persist or resolve within 18 months.

### Stage D — Develop thesis cards

Promote no more than eight candidates. Each thesis card must contain:

- title and status;
- causal chain;
- variant perception: what the market appears to believe and what the agent believes instead;
- 6-, 12- and 18-month base, bull and bear scenarios;
- catalysts and expected time window;
- strongest disconfirming evidence;
- thesis invalidation;
- candidate expressions;
- relevant prices and valuation as of the run;
- crowding and positioning assessment;
- confidence score from 0–100 with a written justification;
- evidence quality score from 0–100;
- source list.

### Stage E — Adversarial review

Run a separate critic pass that cannot see the proposed sizing. It must identify:

- hidden consensus assumptions;
- duplicated factor exposures;
- reflexive or circular logic;
- stale evidence;
- thesis drift;
- an attractive narrative with no near-term transmission mechanism;
- a valid theme already fully reflected in price;
- implementation risks that dominate the macro edge.

The research pass must answer every material objection. Unresolved objections reduce confidence or block promotion.

### Stage F — Select expression and entry state

Rank candidate instruments. Report expected upside, ordinary downside, thesis-break downside, carry, liquidity, correlation to the intended driver, and key idiosyncratic risks.

Assign one entry state:

- `NOW`: price and evidence justify initial exposure;
- `STAGE`: initiate in predefined tranches;
- `WAIT_PRICE`: thesis valid, entry unattractive;
- `WAIT_EVIDENCE`: mechanism not yet confirmed;
- `REJECT`: inadequate asymmetry or unreliable expression.

### Stage G — Construct the proposed book

Size by risk contribution, not dollars alone. Required portfolio statistics:

- cash weight;
- gross and net notional;
- expected annualized volatility;
- one-day 99% historical or filtered VaR;
- expected shortfall;
- position and theme risk contributions;
- exposure by growth, inflation, USD, real-rate, duration, commodity and geopolitical factors;
- stress loss under at least eight historical or synthetic scenarios;
- liquidity and gap-risk flags.

No single thesis may contribute more than 30% of forecast portfolio volatility at inception. No individual equity may exceed 7.5% of NAV without explicit human override. Initial deployment should normally be 50–70% of target risk, with remaining capacity tied to stated evidence or price triggers.

Rates-spread positions must be sized by DV01. Raw matching contract counts are prohibited. FX futures must report native notional, USD notional, margin and a 5%, 10% and 15% adverse-move loss.

### Stage H — Compare with the existing book

Only after the zero-based proposed book is complete, load the existing book and classify every difference as:

- new thesis;
- thesis removed;
- expression changed;
- size changed;
- unchanged despite price movement;
- held for tax, liquidity or implementation reasons.

Do not anchor the new analysis to existing holdings.

### Stage I — Human approval

Publish recommendations only. Changes remain `PROPOSED` until the user approves them. The agent must never infer approval from silence.

## 7. Monthly Evidence Check

The monthly command is `macro monthly-check --as-of YYYY-MM-DD`.

This is not a new forecast. For every active and watch-list thesis:

1. list genuinely new evidence;
2. map each item to the causal chain;
3. show whether it strengthens, weakens or does not affect the thesis;
4. update price, valuation, carry and crowding;
5. test every catalyst and invalidation condition;
6. recommend `NO_CHANGE`, `ADD`, `TRIM`, `EXIT`, or `FULL_REBUILD`;
7. identify the next scheduled evidence date.

Default behavior is `NO_CHANGE`. News volume alone is not a reason to trade.

## 8. Event-Driven Review

Trigger an immediate review on any of the following:

- an unexpected central-bank action or material reaction-function change;
- fiscal-policy change that affects the thesis mechanism;
- war, intervention, sanction, export restriction or treaty commitment;
- a 10% move in an individual position or a theme-specific comparable move;
- a 2% portfolio NAV drawdown attributable to one thesis;
- company guidance cut, backlog failure, capital-allocation change or governance event;
- an explicit thesis invalidation;
- loss or corruption of required data.

An event review may recommend an action but cannot execute it.

## 9. Entry and Rebalancing Rules

- Never recommend full target size immediately unless the thesis is event-defined and delay materially worsens asymmetry.
- Default staging: 50% initial, 30% on confirmation or a better price, 20% on final confirmation.
- Define every tranche before the first proposed entry.
- Systematic or calendar-dependent components must be tested over alternative rebalance dates.
- Report best, median and worst net outcomes across timing offsets.
- Reject apparent edge that depends on one fortunate rebalance date.
- Use actual commissions, bid/ask, slippage, financing, roll and withholding assumptions.

## 10. Current Reference Book

This is the recovered August 2, 2026 target book. It is a reference test fixture, not an instruction to trade and not a seed for future quarterly idea generation.

| Theme | Target exposure | Reference expression | Current implementation state |
|---|---:|---|---|
| Long Japanese yen | +24% FX notional | 5 Micro JPY futures at the reference NAV | `WAIT/STAGE`; re-price after intervention volatility |
| Copper producers | 20% NAV | COPX 10%, Antofagasta 6%, Ivanhoe Mines 4% | `WAIT_PRICE`; structural thesis intact but spot copper is near record territory |
| Grid and power equipment | 13% NAV | GE Vernova 6%, Eaton 4%, Hitachi 3% | `WATCH/STAGE`; verify valuation and backlog conversion company by company |
| European defense | 15% NAV | Leonardo 5%, BAE Systems 5%, Hensoldt 5% | `WATCH/STAGE`; spending mechanism strengthened, entry price still required |
| Short-duration reserve | 20% NAV | SHY or 1–2 year US Treasuries | `HOLD_CASH_EQUIVALENT`; this means short maturity, not short the securities |
| Cash/T-bills | 32% NAV | Treasury bills or equivalent cash | `HOLD_RESERVE` |
| US 2s30s steepener overlay | risk-sized, not NAV-weighted | short 2-year duration / long 30-year duration | `RESEARCH_ONLY`; replace the old equal-contract placeholder with DV01-neutral sizing |

Because the equity sleeves total 48%, the short-duration reserve 20%, and cash 32%, the cash-funded portfolio totals 100% of NAV. The yen position is an overlay and must be reported separately as gross notional and stress risk. The curve overlay must not be activated until its DV01, carry, roll and stress loss are calculated.

## 11. Machine-Readable State

Maintain these files:

```text
macro/
  config/
    mandate.yaml
    instruments.yaml
    sources.yaml
    risk_limits.yaml
  state/
    current_book.json
    watchlist.json
    thesis_registry.json
    event_log.jsonl
  snapshots/YYYY-MM-DD/
    source_manifest.json
    world_state.parquet
    candidate_imbalances.json
    thesis_cards.json
    expression_scores.json
    risk_report.json
    proposed_book.json
    decision_memo.md
    critic_memo.md
  reports/
    PORTFOLIO_LATEST.md
    WATCHLIST_LATEST.md
```

Minimum position schema:

```json
{
  "position_id": "JPY_LONG_2026Q3",
  "thesis_id": "JAPAN_NORMALIZATION",
  "status": "PROPOSED",
  "direction": "LONG",
  "instrument": "M6J",
  "asset_class": "FX_FUTURE",
  "target_nav_weight": null,
  "target_usd_notional": 39600,
  "target_risk_pct": 0.18,
  "entry_state": "STAGE",
  "tranches": [],
  "catalysts": [],
  "invalidation": [],
  "market_data_as_of": "2026-08-02T00:00:00-04:00",
  "sources": []
}
```

All numerical fields must include units in the schema definition. A validation failure blocks report publication.

## 12. Required Reports

### `PORTFOLIO_LATEST.md`

Must begin with:

1. as-of timestamp and data freshness;
2. one-paragraph portfolio conclusion;
3. current approved book versus proposed book;
4. actions requiring human approval;
5. aggregate risk and top three ways the book can lose;
6. thesis cards;
7. watch list and explicit entry triggers;
8. scheduled catalysts;
9. source appendix.

### Decision language

The agent must use direct language:

- “The thesis is intact, but the price is unattractive.”
- “The evidence changed; the price merely moved.”
- “These are three tickers but one copper risk.”
- “I cannot size this spread safely without current DV01.”

It must not use unsupported phrases such as “likely to outperform,” “strong fundamentals,” or “favorable macro backdrop.”

## 13. Core Agent Prompt

Use the following as the project agent's controlling instruction:

> You are the portfolio research lead for a concentrated global-macro book with a 6–18 month horizon. Rebuild the world view from current primary evidence, reason from causal imbalances, and propose the cleanest liquid expressions. Treat thesis validity, price attractiveness, entry timing and portfolio fit as separate decisions. Prefer no position to a weakly causal or fully priced position. Concentrate only in independent risks, preserve cash for better asymmetry, and make every thesis falsifiable. Cite every current claim. Never fabricate data, never hide conflicting evidence, never size a rates spread without DV01, and never place or imply an order. Your output is an auditable recommendation for human approval. On quarterly runs, do not inspect the existing portfolio until the zero-based candidate book is complete. On monthly runs, update evidence rather than reinventing the forecast. On event runs, determine whether the causal chain changed and recommend the minimum necessary response.

## 14. Tests and Acceptance Criteria

The build is accepted only when:

- a historical as-of run cannot access future documents or revisions;
- every market-sensitive statement has a resolvable citation and timestamp;
- a missing current price prevents an actionable entry recommendation;
- the same theme held through three securities is identified as common risk;
- a valid thesis at an extreme price produces `WAIT_PRICE`;
- an existing holding does not contaminate the zero-based candidate generation stage;
- futures exposures show notional, margin and stress loss;
- curve trades are DV01-normalized;
- the critic can block a thesis;
- monthly runs default to no change absent material evidence;
- event triggers create a review record but no order;
- all proposed portfolio changes require explicit human approval;
- generated JSON passes schema validation and the markdown report reconciles exactly to it.

## 15. Suggested Build Sequence

1. Implement schemas, configuration and source manifest.
2. Implement current market-data adapters and freshness checks.
3. Implement thesis registry and evidence mapping.
4. Implement quarterly, monthly and event workflows.
5. Implement instrument comparison and portfolio risk aggregation.
6. Implement independent critic pass.
7. Generate reports and reconciliation tests.
8. Run a paper-only shadow quarter before relying on recommendations.

## 16. Explicit Non-Goals

- high-frequency or intraday prediction;
- automatic trade execution;
- optimizing a backtest to reproduce the reference book;
- daily narrative churn;
- copying a named investor's holdings;
- treating LLM confidence as a probability;
- substituting price stops for economic invalidation;
- using the existing portfolio as the idea-generation universe.
