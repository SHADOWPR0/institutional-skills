# Quant AI Benchmarking

Use this when `investment-management` evaluates ML, LLM, or AI-assisted alpha research.

`investment-management` remains decision owner. Use `ai-ml-research-lab` for experiment design, leakage checks, model-risk gates, and agent eval mechanics.

## Benchmark Contract

- Investment decision: rank, size, hedge, trade, avoid, monitor, or research.
- Universe: assets, venues, eligibility, liquidity filters, survivorship policy.
- Prediction unit: asset/date/time horizon.
- Data timestamp: point-in-time where possible.
- Baseline: equal weight, cap weight, naive momentum/value, current process, or random policy.
- Cost model: fees, spread, slippage, borrow, funding, taxes when relevant.
- Capacity: ADV, market impact, turnover, rebalance constraints.
- Metric hierarchy: economic utility first, statistical metric second.
- Kill switch: drawdown, turnover, drift, stale data, failed sanity test.

## Required Checks

- Walk-forward or time-blocked validation.
- No future-derived features.
- Point-in-time fundamentals and membership if available.
- Out-of-sample Sharpe and turnover-adjusted alpha.
- Hit rate and payoff asymmetry.
- Factor/beta attribution.
- Capacity and crowding.
- Stress regimes.
- Feature ablations.
- Dumb baseline comparison.

## LLM Quant Research Controls

Use LLMs for:

- literature triage
- code scaffolding
- hypothesis generation
- feature dictionary construction
- source extraction
- report drafting

Do not treat LLM prose as:

- price data
- execution instruction
- validated signal
- proof of edge

Every LLM-generated hypothesis must become a measurable experiment before capital scaling.

## Promotion Standard

Promote only if the strategy:

- beats baseline after realistic costs
- survives leakage review
- is stable across time blocks or regimes
- has explicit capacity limits
- has a clear failure mode and kill gate
- maps to Kelly/risk budget without overstating confidence

