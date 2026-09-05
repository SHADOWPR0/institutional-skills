# Global Macro Research Framework

## Mandate Boundary

This framework runs a vendor-neutral global macro research process for a
6-to-18-month horizon. It can produce thesis cards, expression comparisons,
price-aware entry states, and paper portfolio recommendations for human review.
It cannot execute, place orders, mutate a live book, infer approval from silence,
or override `investment-management`, which remains the parent capital-decision
owner.

The skill distinguishes five decisions that must not be collapsed:

1. a structurally attractive theme;
2. a trade with an identifiable causal mechanism;
3. an instrument or expression that transmits the mechanism cleanly;
4. an entry that is attractive at the current price; and
5. a paper position that fits aggregate portfolio risk.

Use no named-investor branding, attribution hooks, or copied holdings. Any
recovered reference book is a generic validation fixture only, not an instruction
to trade and not a seed for future idea generation.

## Source Hierarchy

Use current information on every live run. Every time-sensitive claim needs a
source URL or local source ID, publication date, event date, retrieval timestamp,
and as-of cutoff. Missing data is `UNAVAILABLE`; never invent prices, policy
rates, financial metrics, contract specifications, citations, or vintage data.

Priority:

1. central banks, finance ministries, statistical agencies, regulators, official
   budgets, exchanges, and treaty organizations;
2. company filings, earnings calls, investor materials, and official index or
   contract methodology;
3. exchange, futures, rates, FX, credit, commodity, and market-structure data;
4. multilateral institutions and high-quality academic or institutional research;
5. reputable reporting for events not yet reflected in primary documents;
6. sell-side, independent research, newsletters, and social posts as nomination
   or interpretation only, never sole factual foundation.

Conflicting high-priority sources are preserved as conflicts, not silently
resolved.

## Required Data Surface

Each quarterly rebuild examines at minimum:

- growth and labor momentum across the US, euro area, China, Japan, and major
  emerging markets;
- headline, core, and wage inflation;
- policy rates, expected paths, balance sheets, and central-bank reaction
  functions;
- fiscal impulse, debt issuance, and term-premium pressure;
- nominal and real sovereign curves;
- FX valuation, carry, reserves, intervention risk, and reserve policy;
- commodity supply, inventories, marginal cost, project pipeline, and demand;
- credit spreads, lending conditions, default expectations, and refinancing risk;
- equity valuation, earnings expectations, breadth, and cyclicality by region
  and industry;
- positioning, flows, volatility, liquidity, and crowding;
- geopolitical commitments that create durable expenditure or supply changes.

## Shared Market-State Snapshot

Every run creates one immutable `market_state.snapshot_id`. Required dimensions:

- liquidity;
- inflation;
- monetary and fiscal policy;
- business cycle.

Each dimension contains:

- `state`: concise factual view;
- `direction`: `RISING`, `FALLING`, `STABLE`, `MIXED`, or `UNAVAILABLE`;
- `confidence`: `LOW`, `MEDIUM`, `HIGH`, or `UNAVAILABLE`;
- `status`: `AVAILABLE`, `STALE`, `CONFLICTED`, or `UNAVAILABLE`;
- `evidence_ids`: source-manifest references;
- `notes`: bounded interpretation or unavailable-data reason.

Every theme must reference this same snapshot and declare its relationship to
each dimension as `ALIGNED`, `NEUTRAL`, `CONDITIONAL`, or `CONTRADICTED`.

## Quarterly Zero-Based Rebuild

Command form: `macro quarterly-rebuild --as-of YYYY-MM-DD`.

### Stage A - Freeze The Information Set

- Record `as_of`, `evidence_cutoff`, retrieval timestamps, revisions, and data
  vintages.
- Archive source manifest entries and mark stale or unavailable series.
- Historical simulations may not access later documents, revisions, or market
  data.

### Stage B - Build The World-State Table

For each region and asset class, report level, 3-month change, 12-month change,
market expectation, and directional surprise where available. Keep facts,
estimates, and interpretation separate.

### Stage C - Generate Imbalances

Generate 8 to 15 candidate macro imbalances without reference to the existing
portfolio. Start with pressures that cannot persist indefinitely:

`imbalance -> decision maker -> likely response -> economic transmission -> asset-class impact -> possible expression`

Examples of pressures: monetary-policy divergence, fiscal dominance, underbuilt
supply, forced capital spending, reserve depletion, unsustainable external
balance, institutional rearmament, or a price that blocks required investment.

### Stage D - Develop Thesis Cards

Promote no more than eight candidates. Each card requires:

- title, status, geography, asset class, sub-asset class, and horizon;
- full causal chain;
- variant view or explicit statement that no variant view is established;
- 6-, 12-, and 18-month base, bull, and bear scenarios;
- catalysts and expected time window;
- strongest disconfirming evidence;
- thesis invalidation;
- at least three candidate expressions when feasible;
- relevant price/valuation evidence as of the run;
- crowding and positioning assessment;
- confidence score and evidence quality;
- source list and explicit data gaps.

Every thesis separately labels:

- `THESIS`: `INVALID`, `WEAKENING`, `INTACT`, or `STRENGTHENING`;
- `VALUATION_OR_PRICE`: `CHEAP`, `FAIR`, `RICH`, `EXTREME`, or `UNAVAILABLE`;
- `TIMING`: `EARLY`, `ACTIONABLE`, `CROWDED`, `LATE`, or `UNAVAILABLE`;
- `PORTFOLIO_ACTION`: `REJECT`, `WATCH`, `STAGE`, `HOLD`, `ADD`, `TRIM`,
  `EXIT`, `NO_CHANGE`, or `FULL_REBUILD`.

A strong theme at a bad price is `WATCH` or `WAIT_PRICE`, not an automatic
paper position.

### Stage E - Adversarial Review

Run a separate critic pass before sizing. The critic tests:

- hidden consensus assumptions;
- duplicated factor exposures;
- reflexive or circular logic;
- stale evidence;
- thesis drift;
- narrative appeal with no near-term transmission;
- valid theme already reflected in price;
- implementation risks that dominate the macro edge.

The research pass must answer every material objection. Unresolved objections
reduce confidence or block promotion.

### Stage F - Select Expression And Entry State

For each thesis, compare at least three expressions when feasible. Score:

- causal purity;
- valuation or price;
- liquidity;
- carry;
- convexity;
- governance and jurisdiction risk;
- currency exposure;
- path dependency;
- implementation cost;
- ordinary downside and thesis-break downside;
- downside under a thesis-neutral scenario.

Assign one entry state:

- `NOW`: price and evidence justify initial paper exposure;
- `STAGE`: use predefined tranches;
- `WAIT_PRICE`: thesis valid, entry unattractive;
- `WAIT_EVIDENCE`: mechanism not confirmed;
- `REJECT`: inadequate asymmetry or unreliable expression;
- `UNAVAILABLE`: required data missing.

### Stage G - Construct The Paper Book

Paper recommendations are sized by independent risk contribution, not ticker
count or raw dollars. Required outputs:

- cash weight;
- gross and net notional;
- expected annualized volatility;
- one-day 99 percent historical or filtered VaR;
- expected shortfall;
- position and theme risk contributions;
- exposure by growth, inflation, USD, real-rate, duration, commodity, credit,
  and geopolitical factors;
- stress loss under at least eight historical or synthetic scenarios;
- liquidity and gap-risk flags.

No single thesis may contribute more than 30 percent of forecast portfolio
volatility at inception without explicit human override. Initial deployment
should normally be 50 to 70 percent of target paper risk, with remaining
capacity tied to predefined evidence or price triggers.

Rates-spread paper positions must be DV01-normalized. Raw matching contract
counts are prohibited. FX paper positions must report native notional, USD
notional, margin, and 5, 10, and 15 percent adverse-move loss.

### Stage H - Compare With The Existing Book

Only after the zero-based proposed book is complete may the process load the
existing book. Classify every difference as new thesis, thesis removed,
expression changed, size changed, unchanged despite price movement, or held for
tax, liquidity, or implementation reasons.

### Stage I - Human Approval

All recommendations remain `PROPOSED` or `RESEARCH_ONLY` until the principal explicitly
approves them. The skill never infers approval from silence and never places or
implies an order.

## Monthly Evidence Check

Command form: `macro monthly-check --as-of YYYY-MM-DD`.

This is not a new forecast. For every active and watch-list thesis:

1. list genuinely new evidence;
2. map each item to the causal chain;
3. classify whether it strengthens, weakens, or does not affect the thesis;
4. update price, valuation, carry, crowding, and entry state;
5. test every catalyst and invalidation condition;
6. recommend `NO_CHANGE`, `ADD`, `TRIM`, `EXIT`, or `FULL_REBUILD`;
7. identify the next scheduled evidence date.

Default behavior is `NO_CHANGE`. News volume alone is not a reason to trade.

## Event-Driven Review

Trigger immediate review on:

- unexpected central-bank action or material reaction-function change;
- fiscal-policy change that affects the thesis mechanism;
- war, intervention, sanction, export restriction, or treaty commitment;
- a 10 percent move in an individual paper position or comparable theme move;
- a 2 percent paper-book drawdown attributable to one thesis;
- company guidance, backlog, capital-allocation, or governance break;
- explicit thesis invalidation;
- loss, corruption, or supersession of required data.

An event review may recommend action but cannot execute it.

## Ranking Method

Score each positive component from 0 to 4:

| Component | Weight | Question |
|---|---:|---|
| Regime coherence | 20 | Does the thesis fit the shared state without hidden contradictions? |
| Causal strength | 20 | Is every link from pressure to asset impact explicit and plausible? |
| Evidence quality | 15 | Are claims current, causal, sourced, and cross-checked? |
| Catalyst and timing | 15 | Is there a visible transmission window within the horizon? |
| Cross-asset confirmation | 10 | Do independent markets or data domains confirm the mechanism? |
| Bear-case resilience | 10 | Does the thesis survive the strongest alternative explanation? |
| Market structure | 5 | Can the theme be observed without unstable/reflexive signals dominating? |
| Independence | 5 | Does it add a distinct driver rather than relabeling existing risk? |

`base_score = sum(weight * component_score / 4)`

Penalties:

- contradiction: 0 to 25;
- stale or unavailable data: 0 to 15;
- crowding/reflexivity: 0 to 15;
- duplicate driver: 0 to 20;
- unresolved critic: 0 to 25.

`final_score = max(0, base_score - total_penalties)`

The score is a research rank, not expected return, probability, risk budget, or
portfolio weight.

## Conflict-Resolution Hierarchy

Resolve conflicts in this order:

1. as-of integrity and source vintage;
2. immutable shared market-state snapshot;
3. verified official and primary evidence;
4. timestamped market and exchange evidence;
5. broad cross-asset confirmation;
6. model estimates with declared uncertainty;
7. qualitative interpretation and narrative.

Later items cannot silently override earlier items. If a theme conflicts with
the snapshot, reject it when the mechanism requires the opposite current state,
or mark it `CONDITIONAL` if it depends on a falsifiable state transition.

## Machine-Readable State

Use this local structure when a project needs persistent state:

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

All numerical fields must declare units. A validation failure blocks report
publication.

## Output Modes

### Full Macro Paper Recommendation

Use `mode: PAPER_PORTFOLIO_RECOMMENDATION` for quarterly rebuilds, monthly
checks, and event reviews that compare expressions or propose paper book
changes. Required top-level controls:

```json
{
  "mode": "PAPER_PORTFOLIO_RECOMMENDATION",
  "parent_owner": "investment-management",
  "review_type": "QUARTERLY_REBUILD",
  "research_only": true,
  "human_approval_required": true,
  "execution_authority": false,
  "live_trading": false,
  "existing_book_loaded_before_zero_based_book": false
}
```

The packet also requires `source_manifest`, `market_state`, `thesis_cards`,
`expression_comparisons`, `proposed_book`, `conflicts`, `unavailable_data`, and
`audit`. See `examples/example_paper_book_packet.json`.

### Sanitized Theme Handoff

Use `mode: THEME_HANDOFF` or `RESEARCH_ONLY` when exporting to any system that needs theme-level research only. This mode strips every
instrument, ticker, security, allocation, weight, size, entry, stop, target,
order, execution, and measurement-proxy field. See
`examples/example_theme_packet.json`.

## Required Reports

`PORTFOLIO_LATEST.md` style reports begin with:

1. as-of timestamp and data freshness;
2. one-paragraph portfolio conclusion;
3. current approved book versus proposed book;
4. actions requiring human approval;
5. aggregate risk and top three ways the book can lose;
6. thesis cards;
7. watch list and explicit entry triggers;
8. scheduled catalysts;
9. source appendix.

Use direct language:

- "The thesis is intact, but the price is unattractive."
- "The evidence changed; the price merely moved."
- "These are three securities but one macro risk."
- "I cannot size this spread safely without current DV01."

Avoid unsupported phrases such as "likely to outperform", "strong fundamentals",
or "favorable macro backdrop" unless the evidence and mechanism are explicit.

## Locked Consumer Integration Contract

Module: `Favored Macro Themes`.

A locked consumer receives only the sanitized theme handoff. It does not receive the full
paper book, expression list, instrument identities, sizing, weights, entry
levels, or execution language.

Input:

- immutable shared `market_state.snapshot_id`;
- as-of and evidence cutoff;
- validated `THEME_HANDOFF` packet.

Published payload:

```json
{
  "module": "favored_macro_themes",
  "snapshot_id": "same-as-market-state",
  "as_of": "ISO-8601",
  "themes": [
    {
      "rank": 1,
      "theme_id": "THEME_ID",
      "title": "Asset-class theme",
      "origin": "CORE_BOOK",
      "asset_class": "RATES",
      "sub_asset_class": "SOVEREIGN_DURATION",
      "geography": "GLOBAL",
      "horizon": "6-18M",
      "disposition": "FAVORED",
      "confidence": "MEDIUM",
      "thesis_short": "...",
      "catalysts": ["..."],
      "invalidation": ["..."],
      "data_gaps": []
    }
  ],
  "research_only": true
}
```

A locked consumer may display or consume these themes but may not infer allocations. Any
portfolio, security, or capital action is a separate request to
`investment-management`.

## Acceptance Criteria

- Historical as-of runs cannot access future documents or revisions.
- Every market-sensitive statement has a resolvable citation and timestamp.
- Missing current price prevents an actionable entry recommendation.
- Multiple expressions driven by the same macro variable are identified as
  common risk.
- A valid thesis at an extreme price produces `WAIT_PRICE`.
- Existing holdings do not contaminate quarterly zero-based idea generation.
- Futures exposures show notional, margin, and stress loss.
- Curve trades are DV01-normalized.
- The critic can block a thesis.
- Monthly runs default to `NO_CHANGE` absent material evidence.
- Event triggers create review records but no orders.
- All proposed changes require explicit human approval.
- Generated JSON passes schema validation and markdown reports reconcile to it.
