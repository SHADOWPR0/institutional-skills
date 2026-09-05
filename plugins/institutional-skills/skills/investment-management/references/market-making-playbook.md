# Market-Making Playbook (Private)

This playbook covers traditional and crypto market-making frameworks.

## 1) Core Objective

Earn durable spread/flow alpha while controlling inventory and adverse selection risk.

## 2) Traditional Market-Making (Citadel-Style Operating Pattern)

Use this framework for equities/options/futures/ETFs where infrastructure supports low-latency quoting.

### 2.1 Core Components

- Quote engine:
  - dynamic two-sided quotes based on volatility, depth, queue rank, and toxicity
- Inventory engine:
  - target inventory bands and skew quotes to mean-revert inventory
- Toxicity engine:
  - detect informed flow and widen/pull quotes when toxicity spikes
- Hedge engine:
  - hedge inventory with correlated instruments or options/futures overlays
- Risk governor:
  - hard loss limits, max inventory, max quote width, and kill-switches

### 2.2 Metrics

- quoted spread vs realized spread
- adverse-selection loss
- fill ratio by quote rank
- inventory VaR and inventory half-life
- hedge slippage and hedge latency
- quote uptime and reject rate

### 2.3 Control Rules

- when toxicity rises sharply:
  - widen spreads and reduce quote size
- when inventory breaches upper band:
  - skew quotes toward inventory reduction and hedge immediately
- when liquidity evaporates:
  - reduce participation and prioritize risk transfer over spread capture

### 2.4 151-Strategies Anchor

- `references/corpus/drive/Academic_Papers/ssrn-3247865.pdf` (not bundled; recipient resource required)
  - strategy 3.19 describes market making as bid-ask capture and explicitly warns about adverse selection under informed flow.
- operational implication:
  - pure passive quoting is not enough; use short-horizon signal gating and toxicity controls.

## 3) Crypto Market-Making

Apply traditional framework with crypto-specific constraints.

### 3.1 Added Constraints

- venue reliability and API stability
- liquidation cascade risk
- funding/basis interaction with spot inventory
- custody/transfer and counterparty risk

### 3.2 Crypto-Specific Metrics

- maker rebate contribution vs spread PnL
- liquidation-event drawdown
- cross-venue quote sync error
- basis drift vs hedge effectiveness

### 3.3 Crypto Controls

- event-mode profile for high-vol windows
- per-venue inventory caps
- hard throttle on quote size during exchange incidents

## 4) Deployment Checklist

Before enabling market making:

1. confirm latency and execution stack health
2. validate toxicity model behavior on recent data
3. set inventory and loss kill-switches
4. define fallback mode for venue failures
5. run paper/live-shadow validation before scaling
