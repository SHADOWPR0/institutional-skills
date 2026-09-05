# Strategy Router

Use this file to decide which strategy family to activate.

## Inputs Required

- `objective_mode`: `QUALITY_COMPOUNDING` or `OPPORTUNITY_CAPTURE`
- `mandate_type`: `endowment`, `personal`, `corporate`, `trading_desk`, `venture_private`
- `horizon`: `intraday`, `swing`, `position`, `strategic`
- `regime`: `risk_on`, `risk_off`, `transition`
- `volatility_state`: `low`, `normal`, `high`
- `liquidity_state`: `ample`, `normal`, `tight`
- `data_edge`: `fundamental`, `quant_signal`, `flow_microstructure`, `hybrid`

## Router Logic (High Level)

1. Choose horizon lane.
   - `intraday` -> microstructure, market making, short-horizon technical/statistical setups, prediction-market micro alpha.
   - `swing` -> technical + tactical macro/factor overlays.
   - `position` -> fundamental + quant blended sleeves.
   - `strategic` -> multi-asset allocation, value/growth cycles, private pacing.

2. Apply regime filter.
   - `risk_on`:
     - favor momentum/growth/trend and selective carry.
     - reduce deep convex hedges unless mandated.
   - `risk_off`:
     - favor quality value, defensive factors, cash/liquidity buffers, convexity hedges.
     - reduce gross and crowded beta.
   - `transition`:
     - favor relative value, market neutral, event-driven, and selective optionality.

3. Apply objective mode.
   - `QUALITY_COMPOUNDING`:
     - diversify across low-correlation sleeves.
     - cap concentration and leverage.
     - avoid binary outcomes unless payoff asymmetry is exceptional.
   - `OPPORTUNITY_CAPTURE`:
     - concentrate in highest-conviction sleeve.
     - accept higher turnover and path volatility.
     - enforce tighter kill-switches.

4. Apply mandate overlay.
   - Endowment:
     - prioritize durability, correlation control, illiquidity pacing.
   - Personal:
     - prioritize tax-aware compounding and drawdown survivability.
   - Corporate:
     - prioritize liquidity ladder and policy constraints.
   - Trading desk:
     - prioritize fast edge capture and strict risk discipline.
   - Venture/private:
     - prioritize pacing, reserve strategy, and denominator risk control.

## Router Matrix

Use this table for initial routing:

| Condition | Primary Sleeve | Secondary Sleeves | Avoid |
|---|---|---|---|
| Intraday + high liquidity + risk_on | Technical momentum / microstructure | Market making, short-term stat arb | Illiquid deep value |
| Intraday + high vol + transition | Market making / dispersion / mean reversion | Tactical options overlays, prediction-market arb | Unhedged directional concentration |
| Intraday + transition + flow edge | Traditional market making (inventory-aware) | Cross-asset hedge overlays | Passive quoting without toxicity filters |
| Intraday + event-heavy tape | Prediction-market directional/arb | Crypto market making, technical tactical | Oversized binary exposure |
| Swing + risk_on + low vol | Trend/momentum | Growth quality, carry | Over-hedging |
| Swing + risk_off + high vol | Defensive factor rotation | Long convexity, relative value | Chasing breakouts late |
| Position + risk_on | Growth + quality + factor blend | Selective value, optionality | Pure deep value traps |
| Position + risk_off | Quality value + balance-sheet strength | Market-neutral factor sleeves | High-beta thematic concentration |
| Strategic + endowment | Multi-asset policy portfolio | Risk premia, private pacing | High-turnover tactical churn |
| Strategic + corporate | Liquidity ladder + high-grade carry | Selective beta overlays | Illiquid long-duration risk |

## Escalation Rules

- Escalate de-risking when all three are true:
  1. Regime turns `risk_off` or downside transition.
  2. Volatility state is `high` or rising fast.
  3. Correlation/concentration risk rises simultaneously.

- Escalate risk-on only when all three are true:
  1. Regime confirms `risk_on`.
  2. Breadth/liquidity improve.
  3. Strategy edge quality remains stable out-of-sample.

## Tie-Break Rules

If multiple sleeves are valid:

1. Choose higher expected edge stability.
2. Choose better downside asymmetry.
3. Choose lower implementation friction.
4. Choose sleeve with cleaner monitoring and faster invalidation.

## Output Contract

Every routing decision must produce:

- selected primary sleeve
- selected secondary sleeves
- explicit avoided sleeves
- risk budget allocation
- triggers for upgrade/downgrade
- invalidation conditions

## Additional Notes

- For traditional market making, apply `references/market-making-playbook.md`.
- For Polymarket/event strategies, apply `references/prediction-markets-playbook.md`.
