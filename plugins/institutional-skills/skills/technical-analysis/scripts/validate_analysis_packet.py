#!/usr/bin/env python3
"""Validate a technical-analysis proposal packet.

The validator deliberately owns only packet integrity and fail-closed admission.
A valid packet is still a research or shadow proposal; it is never execution
authorization.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any


MODES = {"DESCRIPTIVE_TA", "RESEARCH_TA", "AGENT_REPLAY", "LIVE_SHADOW"}
DECISIONS = {"LONG", "SHORT", "FLAT"}
EVIDENCE_GRADES = {
    "A_VALIDATED",
    "B_RESEARCH_CANDIDATE",
    "C_DESCRIPTIVE",
    "D_DOCTRINE",
    "F_REJECTED",
}
RISK_STATUSES = {"PASS", "FAIL", "BLOCKED"}
REQUIRED_STRING_FIELDS = (
    "schema_version",
    "mode",
    "as_of",
    "data_cutoff",
    "instrument",
    "venue",
    "snapshot_id",
    "skill_version",
    "model_id",
    "role",
    "candidate_set_id",
    "decision",
    "evidence_grade",
    "continuation_case",
    "reversal_case",
    "risk_status",
)


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _parse_timestamp(value: Any, field: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty ISO-8601 timestamp")
        return None
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        errors.append(f"{field} must be a valid ISO-8601 timestamp")
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        errors.append(f"{field} must include a UTC offset or Z suffix")
        return None
    return parsed


def _decimal(value: Any, field: str, errors: list[str]) -> Decimal | None:
    if not _is_number(value):
        errors.append(f"{field} must be a finite number")
        return None
    try:
        return Decimal(str(value))
    except InvalidOperation:
        errors.append(f"{field} must be decimal-compatible")
        return None


def _validate_positive_number(packet: dict[str, Any], field: str, errors: list[str]) -> None:
    value = packet.get(field)
    if not _is_number(value) or value <= 0:
        errors.append(f"{field} must be a positive finite number")


def _validate_costs(value: Any, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append("costs must be an object")
        return

    round_trip = value.get("round_trip_points")
    if not _is_number(round_trip) or round_trip < 0:
        errors.append("costs.round_trip_points must be a non-negative finite number")

    slippage_model = value.get("slippage_model")
    if not isinstance(slippage_model, str) or not slippage_model.strip():
        errors.append("costs.slippage_model must be a non-empty string")

    if type(value.get("adverse_gap_through")) is not bool:
        errors.append("costs.adverse_gap_through must be a boolean")


def _validate_lookahead_audit(
    value: Any,
    data_cutoff: datetime | None,
    decision: Any,
    errors: list[str],
) -> None:
    if not isinstance(value, dict):
        errors.append("lookahead_audit must be an object")
        return

    passed = value.get("passed")
    future_data_used = value.get("future_data_used")
    if type(passed) is not bool:
        errors.append("lookahead_audit.passed must be a boolean")
    if type(future_data_used) is not bool:
        errors.append("lookahead_audit.future_data_used must be a boolean")

    confirmed_at = _parse_timestamp(
        value.get("signal_confirmed_at"), "lookahead_audit.signal_confirmed_at", errors
    )
    if confirmed_at is not None and data_cutoff is not None and confirmed_at > data_cutoff:
        errors.append("lookahead_audit.signal_confirmed_at cannot exceed data_cutoff")

    if passed is True and future_data_used is True:
        errors.append("lookahead_audit cannot pass when future_data_used is true")
    if passed is False and decision != "FLAT":
        errors.append("a failed lookahead audit requires decision FLAT")
    if future_data_used is True and decision != "FLAT":
        errors.append("future data detection requires decision FLAT")


def _validate_price_geometry(packet: dict[str, Any], errors: list[str]) -> None:
    decision = packet.get("decision")
    selected_candidate_id = packet.get("selected_candidate_id")
    price_fields = ("entry", "target", "stop")

    if decision == "FLAT":
        if selected_candidate_id is not None:
            errors.append("selected_candidate_id must be null for decision FLAT")
        for field in price_fields:
            if packet.get(field) is not None:
                errors.append(f"{field} must be null for decision FLAT")
        return

    if decision not in {"LONG", "SHORT"}:
        return

    if not isinstance(selected_candidate_id, str) or not selected_candidate_id.strip():
        errors.append("selected_candidate_id must be a non-empty string for LONG or SHORT")

    tick_size = _decimal(packet.get("tick_size"), "tick_size", errors)
    if tick_size is not None and tick_size <= 0:
        errors.append("tick_size must be greater than zero")

    prices: dict[str, Decimal] = {}
    for field in price_fields:
        parsed = _decimal(packet.get(field), field, errors)
        if parsed is not None:
            prices[field] = parsed
            if tick_size is not None and tick_size > 0 and parsed % tick_size != 0:
                errors.append(f"{field} must align to tick_size")

    if len(prices) != 3:
        return
    entry = prices["entry"]
    target = prices["target"]
    stop = prices["stop"]
    if decision == "LONG" and not (stop < entry < target):
        errors.append("LONG geometry must satisfy stop < entry < target")
    if decision == "SHORT" and not (target < entry < stop):
        errors.append("SHORT geometry must satisfy target < entry < stop")


def validate_packet(packet: Any) -> list[str]:
    """Return all validation errors; an empty list means the packet is valid."""

    errors: list[str] = []
    if not isinstance(packet, dict):
        return ["packet must be a JSON object"]

    for field in REQUIRED_STRING_FIELDS:
        value = packet.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field} must be a non-empty string")

    mode = packet.get("mode")
    if isinstance(mode, str) and mode not in MODES:
        errors.append(f"mode must be one of {sorted(MODES)}")

    decision = packet.get("decision")
    if isinstance(decision, str) and decision not in DECISIONS:
        errors.append(f"decision must be one of {sorted(DECISIONS)}")

    evidence_grade = packet.get("evidence_grade")
    if isinstance(evidence_grade, str) and evidence_grade not in EVIDENCE_GRADES:
        errors.append(f"evidence_grade must be one of {sorted(EVIDENCE_GRADES)}")

    risk_status = packet.get("risk_status")
    if isinstance(risk_status, str) and risk_status not in RISK_STATUSES:
        errors.append(f"risk_status must be one of {sorted(RISK_STATUSES)}")

    as_of = _parse_timestamp(packet.get("as_of"), "as_of", errors)
    data_cutoff = _parse_timestamp(packet.get("data_cutoff"), "data_cutoff", errors)
    if as_of is not None and data_cutoff is not None and data_cutoff > as_of:
        errors.append("data_cutoff cannot exceed as_of")

    _validate_positive_number(packet, "horizon_minutes", errors)
    _validate_positive_number(packet, "ttl_minutes", errors)

    confidence = packet.get("confidence")
    if not _is_number(confidence) or not 0 <= confidence <= 1:
        errors.append("confidence must be a finite number between 0 and 1")

    observations = packet.get("verified_observations")
    if not isinstance(observations, list) or not observations:
        errors.append("verified_observations must be a non-empty list")
    elif any(not isinstance(item, (str, dict)) for item in observations):
        errors.append("verified_observations entries must be strings or objects")

    timeframe_state = packet.get("timeframe_state")
    if not isinstance(timeframe_state, dict) or not timeframe_state:
        errors.append("timeframe_state must be a non-empty object")

    invalidation_conditions = packet.get("invalidation_conditions")
    if not isinstance(invalidation_conditions, list) or not invalidation_conditions:
        errors.append("invalidation_conditions must be a non-empty list")
    elif any(not isinstance(item, str) or not item.strip() for item in invalidation_conditions):
        errors.append("invalidation_conditions entries must be non-empty strings")

    stale_data = packet.get("stale_data")
    if type(stale_data) is not bool:
        errors.append("stale_data must be a boolean")
    elif stale_data and decision != "FLAT":
        errors.append("stale_data requires decision FLAT")

    if risk_status in {"FAIL", "BLOCKED"} and decision != "FLAT":
        errors.append("risk_status FAIL or BLOCKED requires decision FLAT")

    execution_authority = packet.get("execution_authority")
    if execution_authority is not False or type(execution_authority) is not bool:
        errors.append("execution_authority must be boolean false")

    _validate_costs(packet.get("costs"), errors)
    _validate_lookahead_audit(packet.get("lookahead_audit"), data_cutoff, decision, errors)
    _validate_price_geometry(packet, errors)
    return errors


def load_packet(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="Path to the JSON proposal packet")
    parser.add_argument("--quiet", action="store_true", help="Print only validation errors")
    args = parser.parse_args(argv)

    try:
        packet = load_packet(args.packet)
    except FileNotFoundError:
        print(f"INVALID: packet not found: {args.packet}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: unable to read packet: {exc}", file=sys.stderr)
        return 2

    errors = validate_packet(packet)
    if errors:
        for error in errors:
            print(f"INVALID: {error}", file=sys.stderr)
        return 1
    if not args.quiet:
        print(f"VALID: {args.packet}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
