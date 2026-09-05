# Prediction Markets Playbook (Private)

Framework for trading and market making in binary/event markets (for example, Polymarket-style venues).

## 1) Objective

Exploit mispricing between market-implied probabilities and calibrated event probabilities while controlling binary resolution risk.

## 2) Strategy Families

### 2.1 Directional Probability Edge

- Buy when model probability > market probability by threshold.
- Sell/short (or buy NO) when model probability < market probability by threshold.
- Position sizing must scale with confidence and event uncertainty.

### 2.2 Cross-Market Consistency Arbitrage

- Identify logically related contracts with inconsistent probability sums.
- Trade basket to lock positive expected value after fees and slippage.

### 2.3 Time-Decay and Information Flow

- As event date approaches, estimate expected probability convergence speed.
- Trade underreaction/overreaction around high-impact information windows.

### 2.4 Event Market Making

- Quote both sides around fair probability.
- Manage inventory around neutral probability exposure.
- Pull or widen quotes when resolution ambiguity spikes.

## 3) Data and Modeling Requirements

- explicit resolution criteria parsing
- event base-rate priors
- calibrated probability model (not raw score)
- liquidity and order-book monitoring
- fee/slippage model

## 4) Risk Controls

- cap per-event exposure
- cap correlated-event aggregate exposure
- apply ambiguity haircut when resolution language is unclear
- force-close/reduce risk before event cutoff if liquidity deteriorates

## 5) Failure Modes

- model overconfidence on sparse events
- hidden correlation between “independent” events
- ambiguous or delayed resolution
- liquidity vacuum near event close

## 6) Output Template

For each event trade idea, provide:

- event contract
- market implied probability
- model probability and confidence band
- expected value net of fees
- sizing and max loss
- invalidation trigger
- resolution-risk note
