#!/usr/bin/env python3
"""Validate a crypto venue/platform diligence packet without granting execution authority."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


STATUSES = {"SUPPORTED", "UNSUPPORTED", "UNVERIFIED"}
GRADES = {"SOURCE_ONLY", "MOCKED_TEST", "PAPER", "LIVE_DATA_SHADOW", "CAPPED_LIVE"}


def validate(packet: Any) -> list[str]:
    if not isinstance(packet, dict):
        return ["packet must be an object"]
    errors: list[str] = []
    for field in ("platform", "venue", "product", "strategy", "adapter", "as_of", "status", "connector_grade"):
        if not isinstance(packet.get(field), str) or not packet[field].strip():
            errors.append(f"{field} is required")
    if packet.get("status") not in STATUSES:
        errors.append("status is invalid")
    if packet.get("connector_grade") not in GRADES:
        errors.append("connector_grade is invalid")
    if packet.get("status") != "SUPPORTED":
        errors.append("unsupported or unverified capability blocks promotion")
    if packet.get("framework_only") is True:
        errors.append("framework evidence cannot establish platform capability")
    if packet.get("net_economics") is not True:
        errors.append("net economics are required")
    if not isinstance(packet.get("capability_evidence"), str) or not packet.get("capability_evidence", "").strip():
        errors.append("exact capability evidence is required")
    if packet.get("product") == "perpetual":
        required = ("funding", "mark", "index", "margin", "liquidation")
        missing = [field for field in required if packet.get("product_fields", {}).get(field) is not True]
        if missing:
            errors.append("perpetual evidence incomplete: " + ", ".join(missing))
    if packet.get("strategy") == "market_making":
        required = ("realized_spread", "adverse_selection", "inventory_var", "inventory_half_life", "quote_uptime", "cancel_latency", "hedge_slippage")
        missing = [field for field in required if packet.get("mm_metrics", {}).get(field) is not True]
        if missing:
            errors.append("market-making scorecard incomplete: " + ", ".join(missing))
    if packet.get("execution_authority") is not False:
        errors.append("execution_authority must be false")
    return errors


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
