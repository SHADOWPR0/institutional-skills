# Technical Analysis Body Of Knowledge

This reference provides broad professional coverage modeled on the CMT progression from foundations, through application, to integrated decision-making. It is not a reproduction of the proprietary CMT curriculum and does not imply charterholder status.

## First Principles

Technical analysis studies market action—price, volume, volatility, breadth, time, positioning, and related-market behavior—to infer the current balance of supply and demand and define conditional decisions.

Its strongest professional use is not certainty about the future. It is:

- consistent state description;
- explicit scenario boundaries;
- repeatable signal definitions;
- disciplined entry, invalidation, and risk management;
- empirical testing of instrument- and horizon-specific claims.

Three distinctions prevent most mistakes:

1. A pattern can be visually real without having positive expectancy.
2. A predictive relationship can exist without surviving costs or execution.
3. A useful risk-management tool need not be an entry signal.

## Complete Technique Map

| Domain | Primary question | Representative methods | Frequent failure |
| --- | --- | --- | --- |
| Trend and Dow Theory | What direction and hierarchy dominate? | swing sequence, trendlines, channels, moving averages, ADX, regression slope | entering late after extension |
| Support/resistance | Where did supply or demand previously change behavior? | pivots, gaps, prior highs/lows, polarity, anchored VWAP, volume nodes | treating a line as an exact price |
| Classical patterns | Is price continuing, compressing, reversing, or failing? | flags, triangles, wedges, H&S, doubles, rectangles, failed breakouts | hindsight drawing and premature confirmation |
| Candlesticks and bars | What happened inside the recent auction? | engulfing, pin/hammer, doji, stars, inside/outside bars, close location | using a candle without location or regime |
| Momentum | Is directional change accelerating or decelerating? | ROC, RSI, stochastic, MACD, PPO, CCI, TRIX, momentum divergence | repeated countertrend divergence signals |
| Volatility | Is range compressing, expanding, or repricing? | true range, ATR, Bollinger, Keltner, Donchian, realized vol, vol cones | confusing volatility direction with price direction |
| Volume and participation | Is the move accepted and sponsored? | volume trend, OBV, A/D, CMF, MFI, VWAP, relative volume, volume profile | treating consolidated volume as complete order flow |
| Breadth | Is participation broad or concentrated? | advance/decline, new highs/lows, percent above MA, McClellan, breadth thrust | index composition and survivorship drift |
| Relative strength | What is winning against a benchmark or peer set? | price ratio, relative momentum, RRG-style rotation, cross-sectional rank | confusing beta with idiosyncratic strength |
| Intermarket | What do related markets confirm or contradict? | rates, dollar, credit, commodities, vol, sector relationships | assuming historical correlations are fixed |
| Market/volume profile | Where did the auction accept or reject price? | value area, POC, high/low-volume nodes, initial balance, excess | using vendor-specific profiles as universal truth |
| Point-and-figure and filtered charts | What price movement remains after removing time/noise? | P&F, Renko, Kagi, line break, box counts | arbitrary box/reversal parameters |
| Ichimoku | What are equilibrium, trend, and forward support states? | tenkan, kijun, cloud, chikou | mixing displaced values into historical signals incorrectly |
| Cycles and seasonality | Is behavior periodic or calendar-dependent? | autocorrelation, spectral methods, dominant cycle, seasonal composites | unstable periods and multiple testing |
| Elliott/Fibonacci/Gann | Is the path consistent with a discretionary geometric framework? | wave counts, retracements/extensions, fans, time/price ratios | unfalsifiable relabeling after the fact |
| Sentiment and positioning | Is consensus crowded or reflexive? | COT, put/call, surveys, skew, flows, short interest | stale releases and ambiguous timing |
| Microstructure | What is the immediate state of liquidity and aggressive flow? | spread, depth, trade imbalance, queue imbalance, microprice, impact | claiming full-book behavior from narrow snapshots |
| Risk and implementation | Can the view become a controlled trade? | volatility sizing, stops, time exits, R-multiples, expectancy, drawdown gates | optimizing the signal while ignoring fills and tail loss |

## Foundations

### Market Structure And Trend

Read trend hierarchically:

- primary: the dominant horizon relevant to the mandate;
- secondary: corrective or intermediate movement;
- minor: execution-scale fluctuation.

Describe structure using observed swing relationships:

- higher high plus higher low: advancing structure;
- lower high plus lower low: declining structure;
- overlap without directional progress: balance or transition;
- breakout followed by sustained acceptance: possible regime continuation;
- breakout followed by immediate return: possible failure or liquidity event.

A trendline needs at least two causal touches and becomes more informative with independent reactions. A channel is a zone, not a law. Repeated testing can confirm relevance or consume resting liquidity; do not assume each touch strengthens a level.

### Support, Resistance, And Polarity

Rank references by causal and market relevance:

1. current-session executable structure;
2. prior session/week/month extremes and settlement;
3. confirmed swing pivots;
4. anchored volume-weighted references;
5. gaps, balance boundaries, and high-volume acceptance zones;
6. derived geometric projections.

Use zones proportional to volatility, spread, and market granularity. A level is evidence of prior behavior, not an automatic instruction to trade.

### Multi-Timeframe Logic

Use no more timeframes than change the decision. A common stack is:

- context: establishes regime and major structure;
- setup: defines the opportunity and invalidation;
- execution: times an admissible entry.

Lower-timeframe signals against higher-timeframe structure require a clear mean-reversion or failure thesis. Do not count the same price movement three times merely because it appears on three aggregations.

## Classical Pattern Families

### Continuation

- flags and pennants;
- measured pullbacks;
- rectangles within trend;
- continuation triangles;
- continuation gaps.

Required context: prior impulse, orderly contraction or balance, causal confirmation, and a predefined failure point.

### Compression And Breakout

- symmetrical, ascending, and descending triangles;
- wedges;
- narrow-range and inside-bar sequences;
- Bollinger/Keltner compression;
- Donchian or range escape.

Compression predicts potential expansion more reliably than its direction. Direction comes from the actual break, positioning, flow, regime, and follow-through.

### Reversal

- head-and-shoulders and inverse;
- double/triple tops and bottoms;
- rounding formations;
- climactic reversal and key-reversal bars;
- failed breakout/breakdown.

The pattern is not confirmed merely because the shape looks complete. Confirmation must be causal: neckline/pivot/range violation known at the signal timestamp, with any required right-side pivot lag elapsed.

### Gaps

- common/area gap;
- breakaway gap;
- continuation/runaway gap;
- exhaustion gap;
- opening gap relative to prior session structure.

Classification is often retrospective. For research, define gap size, reference session, confirmation, fill convention, and observation window before testing.

## Candlesticks And Price Action

Candles summarize open-high-low-close path but usually not event order inside the bar. Treat single-bar names as contextual descriptors.

Useful dimensions:

- body size relative to recent true range;
- upper/lower wick proportions;
- close location within the bar and range;
- gap relative to the prior bar/session;
- volume or relative-volume confirmation;
- location at structural support/resistance;
- trend and volatility regime.

Families include doji, hammer/hanging man, shooting star/inverted hammer, engulfing, harami, piercing/dark-cloud, morning/evening star, three-method continuation, inside/outside bar, and key reversal.

Never infer target-before-stop order from OHLC alone when both were touched in the same bar.

## Trend And Momentum Systems

### Trend Filters

- simple, exponential, weighted, adaptive, and hull moving averages;
- price above/below an average;
- average slope and ordered average stacks;
- channel breakouts;
- regression slope and goodness of fit;
- ADX/DMI for directional trend strength.

Moving averages reduce noise by introducing lag. Optimize the tradeoff, not a magical period.

### Oscillators

- RSI and stochastic: bounded position/momentum transforms;
- MACD/PPO: difference between smoothed trend estimates;
- ROC/momentum: direct return over a window;
- CCI: displacement from a rolling typical-price baseline;
- Williams %R: close location inside a lookback range;
- TRIX: rate of change of triple-smoothed price;
- MFI: price-volume oscillator.

Overbought does not mean bearish; oversold does not mean bullish. In strong trends, extreme readings can describe persistence. Divergence is a hypothesis about deceleration, not a standalone reversal trigger.

## Volatility Analysis

Separate:

- realized volatility from price history;
- range-based volatility from OHLC;
- implied volatility from options;
- volatility-of-volatility;
- volatility term structure and skew.

Technical tools include true range/ATR, standard deviation, Bollinger bandwidth, Keltner width, Donchian width, volatility cones, normalized range, and compression/expansion ratios.

Volatility has no universal directional sign. The local `ta_vol_reflexivity` study is included precisely because return-volatility coupling differs by asset and product.

## Volume, Auction, And Flow

### Bar-Level Volume

- volume confirmation and climax;
- relative volume by time of day;
- On-Balance Volume;
- Accumulation/Distribution and Chaikin Money Flow;
- Money Flow Index;
- volume-weighted average price;
- anchored VWAP;
- ease of movement and price-volume trend.

### Auction And Profile

- point of control;
- value area;
- high-volume nodes as acceptance;
- low-volume nodes as fast-auction or rejection candidates;
- initial balance and range extension;
- excess, poor highs/lows, and unfinished auctions where the data supports them.

Profile interpretations depend on session definition, instrument, data feed, and whether volume or time-at-price is used.

### Microstructure

Use exact names that match the data:

- trade imbalance from classified aggressor volume;
- top-of-book imbalance from displayed sizes;
- queue imbalance only when queue state exists;
- microprice from best bid/ask and sizes;
- spread and depth state;
- price impact per unit signed flow;
- replenishment/cancellation only with event-complete quote/order data.

Narrow trade-conditioned TBBO is not a full limit-order-book history.

## Breadth, Relative Strength, And Intermarket

Breadth tests whether index movement is broadly participated in. Relative strength identifies leadership. Intermarket analysis tests confirmation and regime relationships.

Always freeze the contemporaneous universe. Modern constituents applied backward create survivorship bias. Adjust for corporate actions, symbol changes, index reconstitution, and availability of historical constituent data.

Cross-market relationships should be estimated rolling or regime-conditionally. Rates, dollar, credit, commodities, equity volatility, and sector leadership can change sign.

## Alternative Charting

### Point And Figure

P&F filters time and records price movement in X/O columns using a box size and reversal amount. Define scaling—fixed, percentage, or ATR—before analysis. Counts are projections, not guarantees.

### Renko, Kagi, And Line Break

These remove or reduce the time axis to emphasize directional movement. Their apparent smoothness is produced by the transformation; backtests must model when each brick/line became knowable and how entries would execute.

### Ichimoku

Treat displaced components causally:

- conversion/tenkan: short midpoint;
- base/kijun: medium midpoint;
- leading spans: projected equilibrium cloud;
- lagging/chikou: current close plotted backward for visual comparison.

Never permit plotted displacement to introduce future information in historical feature rows.

## Cycles, Elliott, Fibonacci, And Gann

These can organize scenarios, but discretion and degrees of freedom are high.

- Cycles: require stable periodicity across rolling windows and a predeclared phase rule.
- Elliott: record the count before the next movement, preserve alternate counts, and define objective invalidation.
- Fibonacci: treat retracements/extensions as candidate zones; test them against ordinary percentage grids and volatility-scaled levels.
- Gann: define the price/time scaling and coordinate system; chart-resizing artifacts are not evidence.

Unless formalized and validated, grade these `D_DOCTRINE`.

## Integrated Technical Opinion

A professional synthesis answers:

1. What is objectively true at the cutoff?
2. Which horizon owns the decision?
3. Is the market trending, balancing, compressing, expanding, or transitioning?
4. Where are acceptance and rejection visible?
5. Which observations are independent versus correlated transforms?
6. What continuation and reversal paths are plausible?
7. What would falsify each path?
8. Is there instrument/horizon-specific evidence after costs?
9. Can the view be implemented with executable prices and controlled loss?
10. If evidence is weak, why is `FLAT` not the best decision?
