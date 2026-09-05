# Pattern And Indicator Catalog

Use this catalog to make technical-analysis language reproducible. It is a definition library, not an edge registry. A technique becomes a trading claim only after the causal and economic tests in `evidence-and-walk-forward.md`.

## Normalization Conventions

- `O_t, H_t, L_t, C_t, V_t`: open, high, low, close, and volume of the completed bar at `t`.
- `TR_t = max(H_t-L_t, |H_t-C_{t-1}|, |L_t-C_{t-1}|)`.
- Normalize price distances by ATR, realized volatility, price, or tick size as appropriate.
- Normalize intraday volume against the same instrument, weekday, session, and clock bucket.
- A close-confirmed signal at bar `t` cannot execute before the next admissible observation unless an executable quote at or after confirmation is retained.
- Any pivot requiring `k` right-side bars becomes known only after those `k` bars close.

## Classical Geometry

For every pattern, freeze the pivot algorithm, tolerance, minimum/maximum duration, trend context, confirmation rule, invalidation rule, and target method before evaluation.

| Family | Causal definition | Confirmation | Common failure |
| --- | --- | --- | --- |
| Bull flag | Up impulse followed by bounded, usually downward or lateral consolidation | Break above the frozen flag boundary after it is knowable | Chasing a late, overextended impulse |
| Bear flag | Down impulse followed by bounded, usually upward or lateral consolidation | Break below the frozen flag boundary | Shorting after exhaustion |
| Pennant | Impulse followed by converging short-duration consolidation | Break in a declared direction after both boundaries are fixed | Relabeling any small triangle as a pennant |
| Symmetrical triangle | Lower highs and higher lows under frozen pivot tolerances | Close or executable break outside a boundary | Assuming direction before the break |
| Ascending triangle | Approximately flat highs with rising lows | Upside break for the classic thesis; downside break is a separate failure event | Ignoring repeated failed highs or declining participation |
| Descending triangle | Approximately flat lows with falling highs | Downside break for the classic thesis; upside break is a separate failure event | Treating horizontal lows as guaranteed support failure |
| Rising wedge | Rising convergent boundaries | Predeclared boundary break; bearish interpretation requires context | Calling every narrow uptrend bearish |
| Falling wedge | Falling convergent boundaries | Predeclared boundary break; bullish interpretation requires context | Calling every narrow downtrend bullish |
| Head-and-shoulders | Three causal peaks with a higher middle peak and a frozen neckline | Neckline violation after the right shoulder and pivot lags complete | Drawing the neckline after the outcome |
| Inverse head-and-shoulders | Three causal troughs with a lower middle trough and frozen neckline | Upside neckline violation after completion | Premature entry before right-side confirmation |
| Double top | Two separated causal highs within a frozen tolerance | Intervening trough violation | Treating equal highs alone as reversal proof |
| Double bottom | Two separated causal lows within a frozen tolerance | Intervening peak violation | Treating equal lows alone as reversal proof |
| Rectangle | Repeated reactions inside frozen horizontal zones | Close or executable break beyond the zone | Overfitting boundaries to every touch |
| Failed breakout | Confirmed excursion beyond a frozen boundary followed by a defined return inside | Return threshold and deadline fixed ex ante | Defining failure only after a loss is visible |

Other common formations—triple tops/bottoms, rounding bases/tops, cups and handles, broadening formations, diamonds, islands, gaps, measured moves, and key reversals—use the same causal template. Their names do not exempt them from frozen geometry.

## Candlestick And Bar Features

Prefer numeric anatomy over names:

- body: `|C_t-O_t|`;
- upper wick: `H_t-max(O_t,C_t)`;
- lower wick: `min(O_t,C_t)-L_t`;
- close location value: `((C_t-L_t)-(H_t-C_t))/(H_t-L_t)` when range is nonzero;
- body, wick, and gap components divided by ATR or recent median range;
- inside/outside status relative to the prior completed bar;
- gap relative to the correct session boundary.

Named families include doji, hammer/hanging man, shooting star/inverted hammer, engulfing, harami, piercing/dark-cloud cover, morning/evening star, three-soldiers/crows, three-method continuation, inside bars, outside bars, and key reversals.

A candle is not an independent edge. Record trend, location, volatility, participation, session, and causal execution. OHLC cannot reveal target-versus-stop order when both occur inside one bar.

## Trend And Momentum

- `SMA_n(t) = mean(C_{t-n+1:t})`.
- `EMA_n(t) = alpha*C_t + (1-alpha)*EMA_n(t-1)`, `alpha=2/(n+1)`.
- Wilder smoothing uses `alpha=1/n` after a declared seed.
- moving-average slope: `(MA_t-MA_{t-k})/normalizer`.
- rate of change: `ROC_n = C_t/C_{t-n}-1`.
- log momentum: `ln(C_t/C_{t-n})`.
- MACD: `EMA_fast-EMA_slow`; signal is an EMA of MACD; histogram is their difference.
- PPO: MACD-like difference divided by the slow EMA.
- RSI: `100-100/(1+RS)`, where `RS` is Wilder-smoothed positive change divided by smoothed absolute negative change.
- stochastic `%K = 100*(C_t-LL_n)/(HH_n-LL_n)`; `%D` is a declared smoothing.
- Williams `%R = -100*(HH_n-C_t)/(HH_n-LL_n)`.
- CCI: `(typical_price-SMA(typical_price))/(c*mean_deviation)` with `c` declared, commonly `0.015`.
- TRIX: rate of change of a triple-smoothed EMA.
- DMI/ADX: Wilder-smoothed directional movement and true range; ADX measures trend strength, not direction.
- regression trend: rolling slope plus fit quality; use errors robust to autocorrelation when making statistical claims.

Overbought/oversold is a state, not a trade direction. Divergence must define its pivots and confirmation without hindsight.

## Volatility And Range

- ATR: Wilder or simple average of true range; state the convention.
- close-to-close realized volatility: standard deviation of returns, annualized only with a stated factor.
- range estimators: Parkinson, Garman-Klass, Rogers-Satchell, and Yang-Zhang require their specific assumptions and session treatment.
- Bollinger bands: rolling mean plus/minus `k` rolling standard deviations; bandwidth is width divided by the center or price.
- Keltner channel: declared central average plus/minus an ATR multiple.
- Donchian channel: rolling high/low excluding or including the current bar as explicitly stated.
- compression: current band/range width divided by its causal historical distribution.
- realized-volatility ratio: short-horizon volatility divided by long-horizon volatility.

Realized volatility, implied volatility, volatility indices, skew, and volatility-of-volatility are distinct data products. Never substitute one silently for another.

## Volume, VWAP, And Participation

- session VWAP: `sum(price_i*volume_i)/sum(volume_i)` over a causally defined session; specify trade price or typical-price bars.
- anchored VWAP: the same calculation from a predeclared event timestamp.
- relative volume: current cumulative or bucket volume divided by comparable historical buckets.
- OBV: cumulative signed volume using close-to-close direction.
- Accumulation/Distribution: cumulative volume weighted by close location.
- Chaikin Money Flow: rolling sum of money-flow volume divided by rolling volume.
- Money Flow Index: RSI-like ratio of positive and negative typical-price money flow.
- volume-price trend: cumulative volume weighted by percentage price change.
- ease of movement: price displacement relative to volume and range, with scaling declared.

Consolidated bar volume is not order flow. Futures volume, equity venue volume, crypto venue volume, and tick count are not interchangeable.

## Breadth And Relative Strength

- advance/decline line and ratio;
- advancing minus declining volume;
- new-high/new-low series;
- percent of a frozen universe above moving averages;
- McClellan oscillator/summation index using declared EMA conventions;
- breadth thrust and cumulative breadth variants;
- benchmark price ratio and its return/slope;
- cross-sectional momentum percentile or z-score;
- RRG-style relative strength and momentum coordinates, with vendor-independent formulas documented.

Historical breadth requires point-in-time constituents. Modern constituents applied backward create survivorship bias.

## Auction, Profile, And Alternative Charts

- Volume profile: volume allocated by price; define session, binning, and source.
- Market/TPO profile: time or opportunity at price; do not call it volume profile.
- POC: the declared maximum-volume or maximum-TPO price bin.
- Value area: a declared fraction and expansion algorithm around POC.
- Initial balance: the exact session and opening duration.
- P&F: box size, scaling, reversal count, and price source must be frozen.
- Renko, Kagi, and line break: record the price movement that actually created each new element; visual charts often repaint the apparent history.
- Ichimoku: tenkan, kijun, leading spans, and chikou follow standard midpoint formulas, but plotted displacement must not become feature leakage.

## Cycles, Waves, Ratios, And Geometry

Cycle studies may use autocorrelation, spectral density, wavelets, Hilbert transforms, seasonal composites, and phase estimates. Require stable out-of-sample periodicity; the strongest in-sample frequency is not automatically forecastable.

Elliott Wave, Fibonacci retracements/extensions, Gann angles, harmonic patterns, and geometric ratios may structure scenarios. Preserve the pre-outcome count, alternate counts, anchors, tolerances, and invalidation. If a method permits unlimited relabeling, grade it as doctrine rather than evidence.

## Sentiment, Positioning, And Intermarket

Possible inputs include COT positioning, put/call ratios, volatility term structure/skew, dealer positioning estimates, surveys, short interest, fund flows, options volume, rates, dollar, credit, commodities, sector leadership, and cross-asset relative strength.

Every field needs an availability timestamp, revision policy, product mapping, and causal lag. Correlations must be estimated rolling or conditionally; historical sign is not permanent.

## Microstructure

- quoted spread: `ask-bid`, normalized by tick or mid.
- top-of-book imbalance: `(bid_size-ask_size)/(bid_size+ask_size)`.
- microprice: `(ask*bid_size + bid*ask_size)/(bid_size+ask_size)`.
- signed trade imbalance: `(buy_initiated_volume-sell_initiated_volume)/total_classified_volume`.
- order-flow imbalance: event-by-event change in displayed bid/ask quantities under a declared formulation.
- price impact: subsequent price change per unit signed flow.
- sweep velocity: distance, levels, or volume consumed divided by elapsed event time, requiring event-complete data.
- replenishment, cancellation, queue position, and exhaustion require the corresponding book events; they cannot be inferred faithfully from sparse snapshots.

Call the input what it is. Trade-conditioned top-of-book data is not a full order book, and top-of-book imbalance is not queue imbalance.

## Pattern Research Record

Any researched setup should be represented as:

```text
setup_id
instrument_universe
bar_or_event_schema
session_and_timezone
causal_formula_version
confirmation_timestamp_rule
entry_and_fill_rule
target_stop_or_horizon
cost_and_slippage_model
development_dates
walk_forward_folds
event_count
expectancy_and_uncertainty
baseline_and_multiple_test_result
failure_regimes
evidence_grade
```

If these fields are missing, describe the setup but do not promote it as edge.
