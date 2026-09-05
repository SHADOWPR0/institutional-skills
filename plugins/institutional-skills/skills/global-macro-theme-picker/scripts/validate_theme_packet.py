#!/usr/bin/env python3
"""Fail-closed validator for global macro research packets."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


VERSION = "1.1.0"
STATE_KEYS = ("liquidity", "inflation", "policy", "business_cycle")
DATA_STATUSES = {"AVAILABLE", "STALE", "CONFLICTED", "UNAVAILABLE"}
DIRECTIONS = {"RISING", "FALLING", "STABLE", "MIXED", "UNAVAILABLE"}
CONFIDENCE = {"LOW", "MEDIUM", "HIGH", "UNAVAILABLE"}
ORIGINS = {"CORE_BOOK", "MODEL_ADDITION"}
RELATIONS = {"ALIGNED", "NEUTRAL", "CONDITIONAL", "CONTRADICTED"}
DISPOSITIONS = {"FAVORED", "CONDITIONAL", "WATCH", "REJECT"}
ASSET_CLASSES = {
    "RATES", "FX", "COMMODITIES", "EQUITIES", "CREDIT", "RESERVE_ASSETS",
    "STRUCTURAL_FISCAL",
}
REVIEW_TYPES = {"QUARTERLY_REBUILD", "MONTHLY_CHECK", "EVENT_REVIEW"}
THESIS_STATES = {"INVALID", "WEAKENING", "INTACT", "STRENGTHENING"}
PRICE_STATES = {"CHEAP", "FAIR", "RICH", "EXTREME", "UNAVAILABLE"}
TIMING_STATES = {"EARLY", "ACTIONABLE", "CROWDED", "LATE", "UNAVAILABLE"}
ACTIONS = {"REJECT", "WATCH", "STAGE", "HOLD", "ADD", "TRIM", "EXIT", "NO_CHANGE", "FULL_REBUILD"}
ENTRY_STATES = {"NOW", "STAGE", "WAIT_PRICE", "WAIT_EVIDENCE", "REJECT", "UNAVAILABLE"}
APPROVAL_STATES = {"PROPOSED", "RESEARCH_ONLY", "REJECTED"}

THEME_HANDOFF_FORBIDDEN_KEYS = {
    "ticker", "tickers", "symbol", "symbols", "security", "securities",
    "instrument", "instruments", "weight", "weights", "allocation",
    "position", "positions", "position_size", "sizing", "shares", "units",
    "contracts", "notional", "nav", "entry", "entry_price", "target",
    "target_price", "stop", "stop_loss", "order", "orders", "execution",
    "trade", "trades", "measurement_proxies", "proxy_symbols",
}
FULL_PACKET_FORBIDDEN_KEYS = {
    "order", "orders", "live_order", "live_orders", "broker_order_id",
    "account_id", "account_number", "api_key", "secret", "password",
}
REQUIRED_THEME_FIELDS = {
    "rank", "theme_id", "title", "origins", "snapshot_id", "asset_class",
    "sub_asset_class", "geography", "horizon", "thesis", "causal_chain",
    "catalysts", "evidence", "bear_case", "invalidation",
    "crowding_positioning", "market_structure", "state_reconciliation",
    "data_gaps", "scores", "penalties", "final_score", "confidence",
    "disposition",
}
REQUIRED_FULL_THESIS_FIELDS = REQUIRED_THEME_FIELDS | {
    "thesis_state", "valuation_or_price", "timing", "portfolio_action",
    "variant_view", "scenarios", "candidate_expressions", "critic_objections",
}
SCORE_KEYS = {
    "regime_coherence", "causal_strength", "evidence_quality",
    "catalyst_timing", "cross_asset_confirmation", "bear_case_resilience",
    "market_structure", "independence",
}
SCORE_WEIGHTS = {
    "regime_coherence": 20,
    "causal_strength": 20,
    "evidence_quality": 15,
    "catalyst_timing": 15,
    "cross_asset_confirmation": 10,
    "bear_case_resilience": 10,
    "market_structure": 5,
    "independence": 5,
}
PENALTY_KEYS = {
    "contradiction", "stale_or_unavailable_data", "crowding_reflexivity",
    "duplicate_driver", "unresolved_critic",
}
PENALTY_LIMITS = {
    "contradiction": 25,
    "stale_or_unavailable_data": 15,
    "crowding_reflexivity": 15,
    "duplicate_driver": 20,
    "unresolved_critic": 25,
}


def _present(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _walk_forbidden(value: Any, forbidden: set[str], path: str = "packet") -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            normalized = key.lower().replace("-", "_")
            if normalized in forbidden:
                errors.append(f"{path}.{key} is forbidden in this packet mode")
            errors.extend(_walk_forbidden(child, forbidden, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(_walk_forbidden(child, forbidden, f"{path}[{index}]"))
    return errors


def _validate_state(name: str, state: Any) -> list[str]:
    if not isinstance(state, dict):
        return [f"market_state.{name} must be an object"]
    errors: list[str] = []
    if not _present(state.get("state")):
        errors.append(f"market_state.{name}.state is required")
    if state.get("direction") not in DIRECTIONS:
        errors.append(f"market_state.{name}.direction is invalid")
    if state.get("confidence") not in CONFIDENCE:
        errors.append(f"market_state.{name}.confidence is invalid")
    if state.get("status") not in DATA_STATUSES:
        errors.append(f"market_state.{name}.status is invalid")
    if not isinstance(state.get("evidence_ids"), list):
        errors.append(f"market_state.{name}.evidence_ids must be a list")
    if state.get("status") == "UNAVAILABLE" and state.get("confidence") != "UNAVAILABLE":
        errors.append(f"market_state.{name} unavailable data needs unavailable confidence")
    return errors


def _expected_score(theme: dict[str, Any]) -> float | None:
    scores = theme.get("scores")
    penalties = theme.get("penalties")
    if not isinstance(scores, dict) or not isinstance(penalties, dict):
        return None
    try:
        base = sum(SCORE_WEIGHTS[key] * float(scores[key]) / 4 for key in SCORE_KEYS)
        total_penalty = sum(float(penalties[key]) for key in PENALTY_KEYS)
    except (KeyError, TypeError, ValueError):
        return None
    return round(max(0.0, base - total_penalty), 2)


def _validate_theme(theme: Any, snapshot_id: str, index: int, full: bool = False) -> list[str]:
    prefix = f"themes[{index}]" if not full else f"thesis_cards[{index}]"
    if not isinstance(theme, dict):
        return [f"{prefix} must be an object"]
    errors: list[str] = []
    required = REQUIRED_FULL_THESIS_FIELDS if full else REQUIRED_THEME_FIELDS
    missing = sorted(required - theme.keys())
    if missing:
        errors.append(f"{prefix} missing fields: {', '.join(missing)}")
        return errors
    if theme.get("snapshot_id") != snapshot_id:
        errors.append(f"{prefix}.snapshot_id must match market_state.snapshot_id")
    origins = theme.get("origins")
    if not isinstance(origins, list) or not origins or not set(origins) <= ORIGINS:
        errors.append(f"{prefix}.origins is invalid")
    if theme.get("asset_class") not in ASSET_CLASSES:
        errors.append(f"{prefix}.asset_class is invalid")
    for key in ("theme_id", "title", "sub_asset_class", "geography", "horizon", "thesis", "bear_case"):
        if not _present(theme.get(key)):
            errors.append(f"{prefix}.{key} is required")
    for key in ("causal_chain", "catalysts", "evidence", "invalidation"):
        if not isinstance(theme.get(key), list) or not theme[key]:
            errors.append(f"{prefix}.{key} must be a non-empty list")
    if not isinstance(theme.get("data_gaps"), list):
        errors.append(f"{prefix}.data_gaps must be a list")
    for key in ("crowding_positioning", "market_structure"):
        block = theme.get(key)
        if not isinstance(block, dict) or block.get("status") not in DATA_STATUSES:
            errors.append(f"{prefix}.{key}.status is invalid")
    reconciliation = theme.get("state_reconciliation")
    if not isinstance(reconciliation, dict):
        errors.append(f"{prefix}.state_reconciliation must be an object")
    else:
        for key in STATE_KEYS:
            if reconciliation.get(key) not in RELATIONS:
                errors.append(f"{prefix}.state_reconciliation.{key} is invalid")
    scores = theme.get("scores")
    if not isinstance(scores, dict) or set(scores) != SCORE_KEYS:
        errors.append(f"{prefix}.scores must contain the exact score components")
    else:
        for key, value in scores.items():
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 4:
                errors.append(f"{prefix}.scores.{key} must be between 0 and 4")
    penalties = theme.get("penalties")
    if not isinstance(penalties, dict) or set(penalties) != PENALTY_KEYS:
        errors.append(f"{prefix}.penalties must contain the exact penalty components")
    else:
        for key, value in penalties.items():
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= PENALTY_LIMITS[key]:
                errors.append(f"{prefix}.penalties.{key} is outside its allowed range")
    expected = _expected_score(theme)
    actual = theme.get("final_score")
    if expected is None or not isinstance(actual, (int, float)) or isinstance(actual, bool):
        errors.append(f"{prefix}.final_score is invalid")
    elif abs(float(actual) - expected) > 0.01:
        errors.append(f"{prefix}.final_score does not reconcile; expected {expected}")
    if theme.get("confidence") not in CONFIDENCE:
        errors.append(f"{prefix}.confidence is invalid")
    disposition = theme.get("disposition")
    if disposition not in DISPOSITIONS:
        errors.append(f"{prefix}.disposition is invalid")
    if isinstance(reconciliation, dict) and "CONTRADICTED" in reconciliation.values() and disposition == "FAVORED":
        errors.append(f"{prefix} cannot be favored while contradicted by market state")
    if disposition == "FAVORED" and isinstance(actual, (int, float)) and actual < 75:
        errors.append(f"{prefix} favored themes require final_score >= 75")
    if full:
        if theme.get("thesis_state") not in THESIS_STATES:
            errors.append(f"{prefix}.thesis_state is invalid")
        if theme.get("valuation_or_price") not in PRICE_STATES:
            errors.append(f"{prefix}.valuation_or_price is invalid")
        if theme.get("timing") not in TIMING_STATES:
            errors.append(f"{prefix}.timing is invalid")
        if theme.get("portfolio_action") not in ACTIONS:
            errors.append(f"{prefix}.portfolio_action is invalid")
        scenarios = theme.get("scenarios")
        if not isinstance(scenarios, dict) or not all(k in scenarios for k in ("6m", "12m", "18m")):
            errors.append(f"{prefix}.scenarios requires 6m, 12m, and 18m cases")
        expressions = theme.get("candidate_expressions")
        if not isinstance(expressions, list) or len(expressions) < 3:
            errors.append(f"{prefix}.candidate_expressions needs at least three expressions when feasible")
    return errors


def _validate_common(packet: dict[str, Any]) -> tuple[list[str], str]:
    errors: list[str] = []
    for field in ("schema_version", "as_of", "evidence_cutoff"):
        if not _present(packet.get(field)):
            errors.append(f"{field} is required")
    if packet.get("parent_owner") != "investment-management":
        errors.append("parent_owner must be investment-management")
    market_state = packet.get("market_state")
    snapshot_id = ""
    if not isinstance(market_state, dict):
        errors.append("market_state must be an object")
    else:
        snapshot_id = market_state.get("snapshot_id", "")
        if not _present(snapshot_id):
            errors.append("market_state.snapshot_id is required")
        for key in STATE_KEYS:
            errors.extend(_validate_state(key, market_state.get(key)))
    for field in ("conflicts", "unavailable_data"):
        if field in packet and not isinstance(packet.get(field), list):
            errors.append(f"{field} must be a list")
    audit = packet.get("audit")
    if not isinstance(audit, dict) or not all(_present(audit.get(k)) for k in ("run_id", "generated_at", "validator_version")):
        errors.append("audit requires run_id, generated_at, and validator_version")
    return errors, snapshot_id


def _validate_theme_handoff(packet: dict[str, Any]) -> list[str]:
    errors = _walk_forbidden(packet, THEME_HANDOFF_FORBIDDEN_KEYS)
    common_errors, snapshot_id = _validate_common(packet)
    errors.extend(common_errors)
    if packet.get("mode") not in {"RESEARCH_ONLY", "THEME_HANDOFF"}:
        errors.append("mode must be RESEARCH_ONLY or THEME_HANDOFF")
    if packet.get("research_only") is not True:
        errors.append("research_only must be true")
    if packet.get("portfolio_construction") is not False:
        errors.append("portfolio_construction must be false for theme handoff")
    if packet.get("execution_authority") is not False:
        errors.append("execution_authority must be false")
    themes = packet.get("themes")
    if not isinstance(themes, list):
        errors.append("themes must be a list")
    else:
        errors.extend(_validate_ranked_themes(themes, snapshot_id, full=False))
    cadence = packet.get("cadence")
    if not isinstance(cadence, dict) or not all(_present(cadence.get(k)) for k in ("daily_next", "monthly_next", "quarterly_next")):
        errors.append("cadence requires daily_next, monthly_next, and quarterly_next")
    return errors


def _validate_ranked_themes(themes: list[Any], snapshot_id: str, full: bool) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    ranks: list[int] = []
    for index, theme in enumerate(themes):
        errors.extend(_validate_theme(theme, snapshot_id, index, full=full))
        if isinstance(theme, dict):
            theme_id = theme.get("theme_id")
            if theme_id in seen:
                errors.append(f"themes[{index}].theme_id is duplicated")
            if isinstance(theme_id, str):
                seen.add(theme_id)
            rank = theme.get("rank")
            if not isinstance(rank, int) or isinstance(rank, bool) or rank < 1:
                errors.append(f"themes[{index}].rank must be a positive integer")
            else:
                ranks.append(rank)
    if ranks and sorted(ranks) != list(range(1, len(ranks) + 1)):
        errors.append("theme ranks must be unique and contiguous from 1")
    return errors


def _validate_expression_comparisons(packet: dict[str, Any]) -> list[str]:
    comparisons = packet.get("expression_comparisons")
    if not isinstance(comparisons, list) or not comparisons:
        return ["expression_comparisons must be a non-empty list"]
    errors: list[str] = []
    for index, comparison in enumerate(comparisons):
        prefix = f"expression_comparisons[{index}]"
        if not isinstance(comparison, dict):
            errors.append(f"{prefix} must be an object")
            continue
        if not _present(comparison.get("theme_id")):
            errors.append(f"{prefix}.theme_id is required")
        expressions = comparison.get("expressions")
        if not isinstance(expressions, list) or len(expressions) < 3:
            errors.append(f"{prefix}.expressions needs at least three alternatives when feasible")
            continue
        for expr_index, expression in enumerate(expressions):
            expr_prefix = f"{prefix}.expressions[{expr_index}]"
            if not isinstance(expression, dict):
                errors.append(f"{expr_prefix} must be an object")
                continue
            for field in ("expression_id", "asset_class", "causal_purity", "liquidity", "carry", "implementation_cost", "thesis_neutral_downside"):
                if field not in expression:
                    errors.append(f"{expr_prefix}.{field} is required")
            if expression.get("asset_class") not in ASSET_CLASSES:
                errors.append(f"{expr_prefix}.asset_class is invalid")
    return errors


def _validate_proposed_book(packet: dict[str, Any]) -> list[str]:
    book = packet.get("proposed_book")
    if not isinstance(book, dict):
        return ["proposed_book must be an object"]
    errors: list[str] = []
    if book.get("approval_status") not in APPROVAL_STATES:
        errors.append("proposed_book.approval_status must remain proposed/research-only/rejected")
    required = {
        "cash_weight", "gross_notional", "net_notional", "expected_annualized_volatility",
        "var_99_1d", "expected_shortfall", "theme_risk_contributions",
        "factor_exposures", "stress_tests", "liquidity_gap_flags",
    }
    missing = sorted(required - book.keys())
    if missing:
        errors.append("proposed_book missing fields: " + ", ".join(missing))
    if not isinstance(book.get("theme_risk_contributions"), list):
        errors.append("proposed_book.theme_risk_contributions must be a list")
    if not isinstance(book.get("stress_tests"), list) or len(book.get("stress_tests", [])) < 8:
        errors.append("proposed_book.stress_tests requires at least eight scenarios")
    positions = book.get("positions", [])
    if positions is not None and not isinstance(positions, list):
        errors.append("proposed_book.positions must be a list when present")
    if isinstance(positions, list):
        for index, position in enumerate(positions):
            prefix = f"proposed_book.positions[{index}]"
            if not isinstance(position, dict):
                errors.append(f"{prefix} must be an object")
                continue
            if position.get("status") not in APPROVAL_STATES:
                errors.append(f"{prefix}.status must remain proposed/research-only/rejected")
            if not _present(position.get("theme_id")):
                errors.append(f"{prefix}.theme_id is required")
            if position.get("entry_state") not in ENTRY_STATES:
                errors.append(f"{prefix}.entry_state is invalid")
            if position.get("asset_class") == "RATES" and position.get("rate_spread") is True and "dv01" not in position:
                errors.append(f"{prefix}.dv01 is required for rates-spread positions")
            if position.get("asset_class") == "FX" and any(k not in position for k in ("native_notional", "usd_notional", "margin", "stress_loss_5pct", "stress_loss_10pct", "stress_loss_15pct")):
                errors.append(f"{prefix} FX positions require notional, margin, and 5/10/15 pct stress losses")
    return errors


def _validate_full_macro_book(packet: dict[str, Any]) -> list[str]:
    errors = _walk_forbidden(packet, FULL_PACKET_FORBIDDEN_KEYS)
    common_errors, snapshot_id = _validate_common(packet)
    errors.extend(common_errors)
    if packet.get("mode") != "PAPER_PORTFOLIO_RECOMMENDATION":
        errors.append("mode must be PAPER_PORTFOLIO_RECOMMENDATION")
    if packet.get("review_type") not in REVIEW_TYPES:
        errors.append("review_type is invalid")
    if packet.get("research_only") is not True:
        errors.append("research_only must be true")
    if packet.get("human_approval_required") is not True:
        errors.append("human_approval_required must be true")
    if packet.get("execution_authority") is not False:
        errors.append("execution_authority must be false")
    if packet.get("live_trading") is not False:
        errors.append("live_trading must be false")
    if not isinstance(packet.get("source_manifest"), list) or not packet["source_manifest"]:
        errors.append("source_manifest must be a non-empty list")
    theses = packet.get("thesis_cards")
    if not isinstance(theses, list) or not theses:
        errors.append("thesis_cards must be a non-empty list")
    elif len(theses) > 8:
        errors.append("thesis_cards may not exceed eight promoted candidates")
    elif packet.get("review_type") == "QUARTERLY_REBUILD" and len(theses) > 5:
        errors.append("quarterly rebuild should promote at most five active independent theses")
    if isinstance(theses, list):
        errors.extend(_validate_ranked_themes(theses, snapshot_id, full=True))
    errors.extend(_validate_expression_comparisons(packet))
    errors.extend(_validate_proposed_book(packet))
    if packet.get("review_type") == "QUARTERLY_REBUILD" and packet.get("existing_book_loaded_before_zero_based_book") is not False:
        errors.append("quarterly rebuild must not load existing book before zero-based proposed book")
    return errors


def validate(packet: Any) -> list[str]:
    if not isinstance(packet, dict):
        return ["packet must be an object"]
    mode = packet.get("mode")
    if mode in {"RESEARCH_ONLY", "THEME_HANDOFF"}:
        return _validate_theme_handoff(packet)
    if mode == "PAPER_PORTFOLIO_RECOMMENDATION":
        return _validate_full_macro_book(packet)
    return ["mode must be RESEARCH_ONLY, THEME_HANDOFF, or PAPER_PORTFOLIO_RECOMMENDATION"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()
    errors = validate(json.loads(args.packet.read_text(encoding="utf-8")))
    if errors:
        print("INVALID: " + "; ".join(errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
