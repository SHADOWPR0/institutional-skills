# RL Market Simulation Lab

Use this for reinforcement learning, execution agents, market making, inventory control, event-market policies, and simulated market response.

`investment-management` owns the trading/risk decision. `ai-ml-research-lab` supports environment design, reward design, evaluation, and model-risk governance.

## Preferred Simulation Stack

- Limit-order-book or discrete-event market simulator when microstructure matters.
- ABIDES/ABIDES-Gym style environments for execution and daily investor agents.
- Offline replay only as a lower-confidence prefilter.
- Paper/live shadow only after simulator and historical evaluation survive gates.

## RL Environment Contract

- State: prices, order book, inventory, risk, regime, news/event features.
- Actions: quote, cancel, cross spread, size, hedge, no-op, de-risk.
- Reward: PnL net of costs, inventory penalty, drawdown penalty, toxicity penalty, latency penalty.
- Constraints: max position, max loss, leverage, order rate, venue exposure.
- Episode termination: risk breach, end of day/event, data fault, kill switch.
- Baselines: passive market making, TWAP/VWAP, heuristic inventory controller, no-trade.

## Finance-Specific Failure Modes

- Simulator overfit.
- Unrealistic fills.
- Missing adverse selection.
- Reward hacking.
- Latency blindness.
- Cost underestimation.
- Regime brittleness.
- Hidden leverage.
- Multi-agent collusion or unstable equilibria.

## Promotion Gates

- Outperforms strong heuristic baselines after costs.
- Stable across seeds, regimes, and volatility states.
- No tail-risk blowups under stress.
- Inventory and drawdown gates work.
- Human review before any live order permission.
- Live rollout starts in paper/shadow mode.

## Output Pattern

- Objective and instrument/venue.
- Environment contract.
- Reward formula.
- Baselines.
- Risk constraints.
- Evaluation protocol.
- Results and stress tests.
- Failure modes.
- Paper/live rollout gate.

