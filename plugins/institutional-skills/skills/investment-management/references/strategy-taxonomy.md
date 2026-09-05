# Strategy Taxonomy

This taxonomy is for framework selection, not proprietary implementation.

For each family, define:
- use case
- expected edge source
- key metrics
- common failure modes
- preferred objective mode

## 1) Value Investing

### 1.1 Deep Value
- Use when:
  - valuation dispersion is wide
  - liquidity stress creates forced selling
  - balance sheet downside is survivable
- Edge source:
  - mean reversion from mispricing vs normalized earnings/assets
- Key metrics:
  - EV/EBIT, FCF yield, balance-sheet resilience, downside coverage
- Failure modes:
  - value traps, structural decline, leverage mismatch
- Best fit:
  - `QUALITY_COMPOUNDING` and strategic horizons

### 1.2 Quality Value
- Use when:
  - macro is uncertain and drawdown control matters
- Edge source:
  - paying reasonable multiples for durable cash flows
- Key metrics:
  - ROIC persistence, margin stability, reinvestment runway
- Failure modes:
  - overpaying for perceived safety
- Best fit:
  - `QUALITY_COMPOUNDING`

## 2) Growth Investing

### 2.1 Secular Compounders
- Use when:
  - earnings revision momentum + durable TAM expansion align
- Edge source:
  - long-duration compounding and operating leverage
- Key metrics:
  - revenue growth quality, unit economics, reinvestment efficiency
- Failure modes:
  - duration shocks, narrative crowding, decelerating growth
- Best fit:
  - both modes, with stricter drawdown gates in `QUALITY_COMPOUNDING`

### 2.2 Innovation/Thematic Growth
- Use when:
  - thematic adoption inflects with measurable evidence
- Edge source:
  - non-linear adoption and market share capture
- Key metrics:
  - adoption curves, ecosystem lock-in, balance sheet runway
- Failure modes:
  - hype without cash-flow conversion, thematic overcrowding
- Best fit:
  - `OPPORTUNITY_CAPTURE` unless hedged

## 3) Fundamental Discretionary (Long/Short)

- Use when:
  - issuer-specific information edge is strong
  - catalyst path is identifiable
- Edge source:
  - differentiated interpretation of fundamentals/catalysts
- Key metrics:
  - thesis hit rate, catalyst timing accuracy, idiosyncratic alpha
- Failure modes:
  - thesis drift, narrative anchoring, poor short construction
- Best fit:
  - both modes

## 4) Quant Factor and Systematic Equity

### 4.1 Multi-Factor
- Use when:
  - signal breadth is high and transaction costs are controlled
- Edge source:
  - persistent factor premia + disciplined rebalancing
- Key metrics:
  - IC/IR, turnover-adjusted alpha, factor crowding exposure
- Failure modes:
  - factor regime breaks, hidden beta, implementation slippage
- Best fit:
  - `QUALITY_COMPOUNDING`

### 4.2 Market-Neutral Statistical Arbitrage
- Use when:
  - cross-sectional dislocations are frequent
  - borrow and execution quality are sufficient
- Edge source:
  - relative mispricing convergence
- Key metrics:
  - spread half-life, residual volatility, borrow cost, capacity
- Failure modes:
  - crowding, structural breaks, borrow squeezes
- Best fit:
  - `QUALITY_COMPOUNDING` and transition regimes

## 5) Macro Systematic

### 5.1 Trend Following (CTAs)
- Use when:
  - macro dispersion and directional persistence increase
- Edge source:
  - capturing medium-term serial correlation across assets
- Key metrics:
  - trend persistence, diversification benefit, crisis convexity
- Failure modes:
  - choppy regimes, late signal reversals
- Best fit:
  - both modes

### 5.2 Carry and Relative Value
- Use when:
  - policy/risk premia are stable and liquidity is adequate
- Edge source:
  - harvesting compensated risk premia
- Key metrics:
  - carry-to-risk ratio, roll-down quality, correlation spikes
- Failure modes:
  - sudden regime shifts, liquidity air pockets
- Best fit:
  - `QUALITY_COMPOUNDING`

## 6) Technical and Tactical Discretionary

- Use when:
  - market structure and flow dominate fundamentals in short windows
- Edge source:
  - repeatable pattern behavior and execution timing
- Key metrics:
  - expectancy by setup class, slippage, adverse excursion
- Failure modes:
  - overtrading, regime mismatch, weak discipline
- Best fit:
  - `OPPORTUNITY_CAPTURE` with strict kill-switches

## 7) Options and Volatility

### 7.1 Convexity / Tail Hedges
- Use when:
  - downside convexity is underpriced relative to regime risk
- Edge source:
  - asymmetric payoff under stress
- Key metrics:
  - hedge efficiency, carry drag, crisis beta
- Failure modes:
  - persistent bleed in calm markets, poor strike selection
- Best fit:
  - risk overlay for both modes

### 7.2 Volatility Carry / Premium Harvest
- Use when:
  - implied vol rich to realized, with stable regime and strong risk controls
- Edge source:
  - volatility risk premium
- Key metrics:
  - IV-RV spread, tail exposure, gap risk
- Failure modes:
  - volatility regime break, gap events
- Best fit:
  - `QUALITY_COMPOUNDING` only with hard risk caps

## 8) Crypto (Spot + Derivatives)

### 8.1 Structural Crypto Beta
- Use when:
  - regime and liquidity support directional exposure
- Edge source:
  - adoption, reflexivity, network effects
- Key metrics:
  - on-chain/liquidity proxies, basis, market structure health
- Failure modes:
  - liquidity collapses, leverage cascades, venue risk
- Best fit:
  - both modes with higher governance requirements

### 8.2 Basis/Funding/Relative-Value
- Use when:
  - funding and basis dislocations are strong and executable
- Edge source:
  - cash-and-carry, basis mean reversion, cross-venue inefficiencies
- Key metrics:
  - annualized basis, funding variance, counterparty risk
- Failure modes:
  - exchange/custody risk, collateral stress
- Best fit:
  - `QUALITY_COMPOUNDING` if operational controls are institutional-grade

### 8.3 Crypto Market Making (CEX/DEX)
- Use when:
  - order flow is continuous, fee/rebate economics are favorable, and latency/infra is reliable
- Edge source:
  - spread capture, maker rebates, inventory skewing, and venue fragmentation arbitrage
- Key metrics:
  - realized spread, adverse-selection loss, queue-fill quality, inventory VaR, hedge latency
- Failure modes:
  - toxic flow, liquidation cascades, exchange downtime, stale quotes
- Best fit:
  - trading desk mandates; `OPPORTUNITY_CAPTURE` with hard risk rails, `QUALITY_COMPOUNDING` only with tight inventory constraints

### 8.4 Crypto Cross-Venue and On/Off-Chain Arb
- Use when:
  - pricing, funding, or liquidity differ materially across venues/chains
- Edge source:
  - basis/funding dislocations, fragmented order books, bridge timing mismatches
- Key metrics:
  - net arb spread after fees/latency, settlement reliability, collateral utilization
- Failure modes:
  - settlement delays, bridge risk, counterparty risk, quote fade
- Best fit:
  - both modes, with strong operational controls

### 8.5 Prediction Markets (Polymarket-Style)
- Use when:
  - event contract prices are misaligned vs calibrated probability estimates
- Edge source:
  - probabilistic mispricing, cross-market consistency breaks, event-resolution process edge
- Key metrics:
  - edge per contract (`model_prob - market_prob`), expected value net of fees, resolution risk premium
- Failure modes:
  - bad probability calibration, ambiguous resolution criteria, liquidity cliffs near event date
- Best fit:
  - tactical sleeves in both modes; position limits must reflect binary payoff risk

## 9) Market Making / Liquidity Provision

- Use when:
  - order flow is deep enough and execution stack is robust
- Edge source:
  - spread capture + inventory management
- Key metrics:
  - spread capture net of adverse selection, inventory VaR, fill quality
- Failure modes:
  - toxic flow, latency disadvantage, inventory runaway
- Best fit:
  - specialized trading desk mandates

### 9.1 Traditional Multi-Asset Market Making (Citadel-Style Pattern)
- Use when:
  - venue connectivity, latency discipline, and cross-hedging stack are institutional-grade
- Edge source:
  - continuous two-sided quoting, dynamic spread setting, inventory risk transfer, and cross-asset hedging
- Key metrics:
  - quoted vs realized spread, fill toxicity, inventory turnover, hedge slippage, quote uptime
- Failure modes:
  - adverse selection spikes, queue-position decay, hedging lag, concentration in one flow regime
- Best fit:
  - professional trading desks only

### 9.2 151-Strategies Paper Anchor (Market-Making)
- In `ssrn-3247865.pdf`, strategy 3.19 frames baseline market making as capturing bid-ask spread but warns this fails under toxic flow without short-horizon directional filtering and execution discipline.
- Practical implication:
  - raw spread capture is insufficient; add toxicity filters, signal-gated quoting, and inventory-aware skew.

## 10) Event-Driven / Special Situations

- Use when:
  - catalyst path and probability tree are quantifiable
- Edge source:
  - merger spreads, restructurings, spin-offs, legal/regulatory outcomes
- Key metrics:
  - deal break probability, downside floor, time-to-resolution
- Failure modes:
  - legal surprises, financing risk, timeline slippage
- Best fit:
  - both modes

## 11) Credit and Distressed

- Use when:
  - spreads compensate default/liquidity risk
- Edge source:
  - mispriced default risk, restructuring optionality
- Key metrics:
  - spread decomposition, recovery assumptions, covenant quality
- Failure modes:
  - hidden balance-sheet risks, liquidity freezes
- Best fit:
  - mostly `QUALITY_COMPOUNDING` with strong downside analytics

## 12) Endowment-Style Multi-Asset Allocation

- Use when:
  - long horizon and intergenerational capital preservation/growth goals dominate
- Edge source:
  - strategic diversification + illiquidity premia + disciplined rebalancing
- Key metrics:
  - policy tracking error, liquidity runway, regime stress tests
- Failure modes:
  - over-illiquidity, denominator effect, weak rebalancing discipline
- Best fit:
  - `QUALITY_COMPOUNDING`

## 13) Corporate Treasury and Balance-Sheet Investing

- Use when:
  - capital preservation, liquidity scheduling, and policy constraints are primary
- Edge source:
  - maturity ladder optimization, selective risk premia, hedging discipline
- Key metrics:
  - liquidity coverage, duration risk, policy compliance
- Failure modes:
  - yield chasing, mismatch vs liability timing
- Best fit:
  - `QUALITY_COMPOUNDING`

## 14) Private / Venture Portfolio Construction

- Use when:
  - portfolio is dominated by illiquid, long-duration assets
- Edge source:
  - selection, pacing, and reserve discipline
- Key metrics:
  - vintage diversification, reserve ratio, dilution path
- Failure modes:
  - overconcentration, follow-on misallocation, denominator shocks
- Best fit:
  - strategic mode with strict pacing discipline

## Selection Rule

Always select strategies by:
1. regime fit
2. edge validity
3. implementation quality
4. risk-adjusted performance persistence

Never select by narrative appeal alone.
