# Mandate Playbooks

Use these overlays after selecting a strategy family.

## 1) Endowment / OCIO Style

Primary objective:
- compound real purchasing power with high survivability

Mode selection:
- `QUALITY_COMPOUNDING` for policy capital and drawdown-sensitive sleeves
- `OPPORTUNITY_CAPTURE` only for explicitly approved opportunistic sleeves with
  capped risk and clear exit rules

Core sleeve structure:
- policy portfolio (global beta, diversifiers, real assets)
- alternative risk premia
- selective private exposure with pacing
- explicit liquidity reserve and rebalancing budget

Governance:
- investment committee cadence and policy bands
- strict liquidity stress testing
- no tactical overtrading

## 2) Personal / Family Office

Primary objective:
- compound wealth and optionality without taking ruin risk

Mode selection:
- prefer `OPPORTUNITY_CAPTURE` for alpha-seeking, tactical, venture/growth, and
  special-situation sleeves when risk is bounded
- use `QUALITY_COMPOUNDING` for core capital, liquidity reserves, tax-sensitive
  compounding, and drawdown-sensitive mandates

Core controls:
- tax-aware implementation
- concentration limits per theme/name
- drawdown survivability and cash runway
- behavior-aware guardrails (avoid panic and FOMO loops)

## 3) Corporate Treasury

Primary objective:
- preserve capital and maintain liability coverage

Default mode:
- `QUALITY_COMPOUNDING`

Core controls:
- policy-compliant duration ladder
- liquidity bucket segmentation (operating, reserve, strategic)
- strict counterparty and concentration controls

Allowed tactical risk:
- small, explicitly approved overlays only

## 4) Trading Desk / Prop

Primary objective:
- high-quality edge capture at controlled risk

Mode selection:
- `OPPORTUNITY_CAPTURE` with strict governance

Core controls:
- hard intraday and daily loss limits
- kill-switches for slippage, latency, liquidity deterioration
- real-time inventory and exposure controls
- mandatory post-trade review

## 5) Venture / Private Holdings

Primary objective:
- capture power-law upside while surviving illiquidity, dilution, and follow-on
  risk

Mode selection:
- `OPPORTUNITY_CAPTURE` for new investments, asymmetric follow-ons, secondaries,
  and growth-equity opportunities with hard portfolio caps
- `QUALITY_COMPOUNDING` for pacing, reserve policy, denominator risk, and
  vintage diversification

Core controls:
- pacing discipline by vintage
- reserve policy for follow-ons
- scenario stress by funding environment

## Mandate Conversion Rules

When a user asks for one style but constraints imply another:

- explain constraint mismatch
- propose a base mandate and tactical sleeve split
- assign risk budgets explicitly

Example:
- request: aggressive trading
- reality: corporate cash mandate
- conversion: preserve treasury policy core and allocate a tiny tactical sleeve with strict risk cap
