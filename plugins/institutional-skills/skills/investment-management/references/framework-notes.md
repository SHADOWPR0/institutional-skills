# Framework Notes

This note captures recurring logic observed across private local investment
research and preserved model/risk artifacts.

## 1) Evergreen Engine Model

- Regime-Throttle Module
  - Purpose: macro regime detection using liquidity and credit conditions.
  - Key outputs: regime net-liquidity diagnostics, transition-probability snapshots, exposure curves.
  - Hard override: if `residual_flag == 1`, posture moves to cash/defensive mode.

- Intraday Execution And Timing Gate
  - Purpose: intraday execution layer with signal/conviction logic.
  - Depends on regime-throttle state for macro permissioning and stance.
  - Typical output: premarket trade lists and execution manifests.

- Power-Law / Y-Engine
  - Purpose: structural convexity and tail-geometry diagnostics.
  - Core metrics: Y or Upsilon-style scores, high-order moments (`M5`, `M6`, `M7`), tail index.
  - Typical outputs: ranking tables with Kelly-like sizing fields.

## 2) Evidence-Weighted Scoring Pattern

From local docs and notebooks, the common composite form blends:

- structural convexity or tail-geometry diagnostics
- correlation and diversification fit
- persistence or repeatability
- survival and fragility penalties
- calibrated model probability when available
- Kelly-style sizing or risk-contribution fields
- theme/regime adjustments

Treat private formula names and exact weights as implementation-dependent. Verify
against the specific run artifact used and express the active decision in plain
institutional terms unless the user asks for the private project artifact.

## 3) Deterministic Kernel Pattern

Kernel output contract usually includes:

- `asOf`
- `regime` (`label`, `score/confidence`, `drivers`)
  - Optional full-cycle state posteriors (`risk_on`, `transition`, `risk_off`)
- `portfolio` summary
- `marketSnapshot`
- `eventsTop`
- `brief` and `decision`
- `meta` (deterministic/provider/fallback/warnings)

Key principle:

- Deterministic state remains authoritative.
- LLM narrative is optional annotation with deterministic fallback.

## 4) Risk Governance Pattern

Observed recurring desk constraints include:

- Max leverage caps
- Single-position caps
- Drawdown-triggered de-risk rules
- fail-safe pause/flatten rules on data or execution faults

When drafting recommendations, map each action to:

- trigger condition
- position scope
- urgency
- invalidation criterion

## 5) Decision-Gate Pattern

From legacy deterministic decision logic:

- Escalate action only when both are true:
  - regime stress is present, and
  - cross-asset confirmation exists.
- Default to hold/watch language when cross-asset confirmation is absent.
- Avoid tactical noise (short-horizon chatter) in full-cycle guidance.

## 6) Practical Validation Checks

Before using a run artifact:

1. Validate schema/columns against declared contracts.
2. Confirm as-of timestamp and data freshness.
3. Confirm there are no malformed headers (for example, shifted CSV header rows).
4. Check for missing fields required by downstream decisions (`alpha_final`, sizing, risk flags).
5. Record all assumptions when converting diagnostics into portfolio actions.
