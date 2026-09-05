# RL and Simulation

Use this for reinforcement learning, contextual bandits, market simulators, execution agents, pricing/auction simulations, robotics-style control, and policy optimization.

## RL Contract

- Environment: real, simulated, offline replay, or hybrid.
- State: observable features and hidden-state caveats.
- Action space: discrete/continuous, constraints, invalid actions.
- Reward: exact formula, horizon, discount, penalties.
- Policy class: rule, bandit, RL, planner, model-based, or hybrid.
- Baseline policies: random, heuristic, supervised imitation, current production policy.
- Risk limits: hard constraints and termination conditions.
- Evaluation: offline validation, simulator validation, paper/live shadow, production.

## Finance-Specific Warning

RL policies often overfit simulator quirks, ignore market impact, and fail under transaction costs or regime shifts. For finance, require:

- walk-forward or time-blocked evaluation
- transaction costs and slippage
- market impact model or conservative penalty
- capacity estimate
- stress regimes
- inventory and leverage constraints
- action throttles
- paper-trading shadow period before any live use

## Simulator Guidance

For market microstructure work, prefer ABIDES/ABIDES-Gym style simulation or an explicit limit-order-book simulator over toy price-series environments. Use simulation to reject bad policies, not to prove deployment readiness.

## Promotion Gates

- Beats dumb and strong heuristic baselines.
- Survives transaction costs and latency.
- Stable across seeds and regimes.
- No hidden leverage or tail-risk blowup.
- Human/domain owner signs off before live use.

