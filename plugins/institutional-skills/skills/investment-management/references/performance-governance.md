# Performance Governance

This file defines the anti-underperformance operating standard.

## Principle

Underperformance is tolerated only as transient noise inside predefined limits. Persistent underperformance triggers immediate intervention.

## Required Baseline Metrics

Track at strategy and portfolio levels:

- absolute return
- benchmark-relative alpha
- Sharpe and Sortino
- max drawdown and drawdown duration
- hit rate and expectancy
- turnover-adjusted return
- slippage/implementation shortfall
- concentration and correlation drift

## Benchmark and Hurdle Setup

Before deploying or scaling any sleeve:

1. define benchmark or peer hurdle
2. define target objective (`QUALITY_COMPOUNDING` or `OPPORTUNITY_CAPTURE`)
3. define review windows (short, medium, long)
4. define explicit kill-switch thresholds

No benchmark -> no capital scaling decision.

## Kill-Switch Framework

Use tiered responses:

- Tier 1 (warning)
  - mild degradation
  - action: reduce size, intensify monitoring

- Tier 2 (de-risk)
  - repeated misses or drawdown acceleration
  - action: cut gross/net, suspend weakest sleeves

- Tier 3 (shutdown)
  - structural breakdown or risk controls breached
  - action: stop strategy, run root-cause process before restart

## Root-Cause Analysis Template

When a strategy degrades, classify cause:

- regime mismatch
- signal decay
- execution degradation
- leverage/position sizing error
- data quality failure
- governance override error

Each RCA must produce:
- diagnosis
- patch plan
- re-test plan
- go/no-go restart decision

## Override Policy

Discretionary overrides are allowed only if:

- rationale is explicit and testable
- time-bounded expiry is set
- override owner is named
- rollback trigger is pre-defined

No open-ended overrides.

## Reporting Cadence

- Daily:
  - PnL, risk, key limit utilization, abnormal events
- Weekly:
  - strategy attribution, degradation checks, edge stability
- Monthly:
  - mandate compliance, capacity review, strategy keep/retire decisions

## Keep, Scale, Retire Rules

- Keep:
  - edge stable, governance clean, risk in range
- Scale:
  - edge stable across regimes and capacity supports larger deployment
- Retire:
  - repeated underperformance with unresolved root cause

## Anti-Drift Checklist

At every review:

- Is this still the same strategy?
- Is edge source still valid?
- Has implementation quality changed?
- Are we taking hidden beta unintentionally?
- Are we still aligned to mandate objective?
