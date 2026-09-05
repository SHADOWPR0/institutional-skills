#!/usr/bin/env python3
"""
Deterministic strategy router for investment mandate contexts.

Examples:
  python scripts/strategy_router.py --context '{"objective_mode":"OPPORTUNITY_CAPTURE","mandate_type":"trading_desk","horizon":"swing","regime":"risk_on","volatility_state":"normal","liquidity_state":"normal","data_edge":"quant_signal"}'
  python scripts/strategy_router.py --context-file context.json --top 5
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Strategy:
    name: str
    horizons: tuple[str, ...]
    regimes: tuple[str, ...]
    objectives: tuple[str, ...]
    mandates: tuple[str, ...]
    edges: tuple[str, ...]
    notes: str


STRATEGIES: tuple[Strategy, ...] = (
    Strategy(
        name="quality_value_core",
        horizons=("position", "strategic"),
        regimes=("risk_off", "transition", "risk_on"),
        objectives=("QUALITY_COMPOUNDING",),
        mandates=("endowment", "personal", "corporate"),
        edges=("fundamental", "hybrid"),
        notes="Defensive compounding sleeve with strong balance-sheet bias.",
    ),
    Strategy(
        name="growth_compounders",
        horizons=("position", "strategic"),
        regimes=("risk_on", "transition"),
        objectives=("QUALITY_COMPOUNDING", "OPPORTUNITY_CAPTURE"),
        mandates=("endowment", "personal", "trading_desk"),
        edges=("fundamental", "hybrid"),
        notes="Secular growth sleeve with durability filters.",
    ),
    Strategy(
        name="multi_factor_systematic",
        horizons=("swing", "position"),
        regimes=("risk_on", "risk_off", "transition"),
        objectives=("QUALITY_COMPOUNDING",),
        mandates=("endowment", "personal", "corporate", "trading_desk"),
        edges=("quant_signal", "hybrid"),
        notes="Diversified factor exposure with turnover control.",
    ),
    Strategy(
        name="trend_macro_systematic",
        horizons=("swing", "position", "strategic"),
        regimes=("risk_on", "risk_off", "transition"),
        objectives=("QUALITY_COMPOUNDING", "OPPORTUNITY_CAPTURE"),
        mandates=("endowment", "personal", "trading_desk"),
        edges=("quant_signal", "hybrid"),
        notes="Cross-asset trend sleeve with regime adaptability.",
    ),
    Strategy(
        name="market_neutral_stat_arb",
        horizons=("intraday", "swing"),
        regimes=("transition", "risk_off", "risk_on"),
        objectives=("QUALITY_COMPOUNDING",),
        mandates=("trading_desk", "personal"),
        edges=("quant_signal", "flow_microstructure"),
        notes="Relative-value sleeve for choppy/transition regimes.",
    ),
    Strategy(
        name="traditional_market_making",
        horizons=("intraday",),
        regimes=("risk_on", "transition", "risk_off"),
        objectives=("QUALITY_COMPOUNDING", "OPPORTUNITY_CAPTURE"),
        mandates=("trading_desk",),
        edges=("flow_microstructure", "hybrid"),
        notes="Inventory-aware two-sided quoting with toxicity filtering (Citadel-style pattern).",
    ),
    Strategy(
        name="technical_tactical",
        horizons=("intraday", "swing"),
        regimes=("risk_on", "transition", "risk_off"),
        objectives=("OPPORTUNITY_CAPTURE",),
        mandates=("trading_desk", "personal"),
        edges=("flow_microstructure", "hybrid"),
        notes="Discretionary technical execution with tight risk gates.",
    ),
    Strategy(
        name="options_convexity_overlay",
        horizons=("swing", "position"),
        regimes=("risk_off", "transition"),
        objectives=("QUALITY_COMPOUNDING", "OPPORTUNITY_CAPTURE"),
        mandates=("endowment", "personal", "trading_desk", "corporate"),
        edges=("quant_signal", "hybrid"),
        notes="Convex downside or asymmetric payoff overlay.",
    ),
    Strategy(
        name="polymarket_event_trading",
        horizons=("intraday", "swing", "position"),
        regimes=("risk_on", "transition", "risk_off"),
        objectives=("QUALITY_COMPOUNDING", "OPPORTUNITY_CAPTURE"),
        mandates=("trading_desk", "personal"),
        edges=("quant_signal", "hybrid", "flow_microstructure"),
        notes="Probability mispricing and cross-market consistency strategies for event markets.",
    ),
    Strategy(
        name="crypto_basis_relative_value",
        horizons=("intraday", "swing", "position"),
        regimes=("risk_on", "transition"),
        objectives=("QUALITY_COMPOUNDING", "OPPORTUNITY_CAPTURE"),
        mandates=("trading_desk", "personal"),
        edges=("flow_microstructure", "quant_signal", "hybrid"),
        notes="Crypto carry/basis sleeve with venue-risk controls.",
    ),
    Strategy(
        name="market_making_liquidity_provision",
        horizons=("intraday",),
        regimes=("risk_on", "transition", "risk_off"),
        objectives=("QUALITY_COMPOUNDING", "OPPORTUNITY_CAPTURE"),
        mandates=("trading_desk",),
        edges=("flow_microstructure",),
        notes="Spread capture and inventory management sleeve.",
    ),
)


REQUIRED_FIELDS = (
    "objective_mode",
    "mandate_type",
    "horizon",
    "regime",
    "volatility_state",
    "liquidity_state",
    "data_edge",
)


OBJECTIVE_ALIASES = {
    "PROFIT_MAX": "OPPORTUNITY_CAPTURE",
    "ABSOLUTE_RETURN": "OPPORTUNITY_CAPTURE",
    "COMPOUNDING": "QUALITY_COMPOUNDING",
}


def _load_context(args: argparse.Namespace) -> dict[str, Any]:
    if args.context and args.context_file:
        raise ValueError("Use either --context or --context-file, not both.")
    if args.context_file:
        data = Path(args.context_file).expanduser().resolve().read_text(encoding="utf-8")
        return json.loads(data)
    if args.context:
        return json.loads(args.context)
    raise ValueError("Provide --context or --context-file.")


def _validate_context(ctx: dict[str, Any]) -> list[str]:
    missing = [f for f in REQUIRED_FIELDS if f not in ctx or not str(ctx[f]).strip()]
    return missing


def _normalize_context(ctx: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(ctx)
    raw_objective = str(normalized.get("objective_mode", "")).strip().upper()
    if raw_objective:
        compact = re.sub(r"[^A-Z]", "", raw_objective)
        if compact.startswith("PNL") and "MAX" in compact:
            normalized["objective_mode"] = "OPPORTUNITY_CAPTURE"
        elif "SHARPE" in compact and "MAX" in compact:
            normalized["objective_mode"] = "QUALITY_COMPOUNDING"
        else:
            normalized["objective_mode"] = OBJECTIVE_ALIASES.get(raw_objective, raw_objective)
    return normalized


def _score(strategy: Strategy, ctx: dict[str, Any]) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []

    if ctx["horizon"] in strategy.horizons:
        score += 3
        reasons.append("horizon match")
    if ctx["regime"] in strategy.regimes:
        score += 3
        reasons.append("regime match")
    if ctx["objective_mode"] in strategy.objectives:
        score += 3
        reasons.append("objective match")
    if ctx["mandate_type"] in strategy.mandates:
        score += 2
        reasons.append("mandate match")
    if ctx["data_edge"] in strategy.edges:
        score += 2
        reasons.append("edge match")

    if ctx["liquidity_state"] == "tight" and ctx["horizon"] == "intraday":
        if strategy.name in {"market_making_liquidity_provision", "technical_tactical"}:
            score -= 2
            reasons.append("liquidity penalty")

    if ctx["volatility_state"] == "high" and strategy.name == "options_convexity_overlay":
        score += 1
        reasons.append("high-vol convexity boost")

    if ctx["horizon"] == "intraday" and strategy.name in {
        "traditional_market_making",
        "market_making_liquidity_provision",
    }:
        score += 1
        reasons.append("intraday mm boost")

    if strategy.name == "polymarket_event_trading" and ctx["regime"] == "transition":
        score += 1
        reasons.append("transition event-market boost")

    return score, reasons


def route_context(ctx: dict[str, Any], top_n: int) -> dict[str, Any]:
    ctx = _normalize_context(ctx)
    ranked: list[dict[str, Any]] = []
    for strategy in STRATEGIES:
        score, reasons = _score(strategy, ctx)
        ranked.append(
            {
                "strategy": strategy.name,
                "score": score,
                "reasons": reasons,
                "notes": strategy.notes,
            }
        )

    ranked.sort(key=lambda x: x["score"], reverse=True)
    selected = ranked[:top_n]
    avoided = [r for r in ranked if r["score"] <= 3][:5]

    return {
        "context": ctx,
        "selected": selected,
        "avoided": avoided,
        "decision": "Route to top strategy as primary; next two as secondary sleeves.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a mandate context to strategy families.")
    parser.add_argument("--context", help="Inline JSON context string")
    parser.add_argument("--context-file", help="Path to JSON context file")
    parser.add_argument("--top", type=int, default=3, help="Number of top strategies to return")
    args = parser.parse_args()

    try:
        context = _load_context(args)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"context_load_failed: {exc}"}))
        return 2

    missing = _validate_context(context)
    if missing:
        print(json.dumps({"ok": False, "error": f"missing_fields: {missing}"}))
        return 2

    result = route_context(context, top_n=max(1, args.top))
    print(json.dumps({"ok": True, **result}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
