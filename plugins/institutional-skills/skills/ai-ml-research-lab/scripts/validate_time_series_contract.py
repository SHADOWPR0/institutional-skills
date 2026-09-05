#!/usr/bin/env python3
"""Validate a financial time-series feature, label, and model artifact contract."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


REQUIRED = (
    "prediction_unit", "event_time", "available_at", "features", "feature_order",
    "source_and_revision_policy", "fit_fold_id", "fit_start", "fit_end", "label_name",
    "label_complete_at", "overlap_span", "transform_type", "transform_hash", "serializer",
    "model_hash", "code_hash", "config_hash", "training_data_hash", "evaluation_data_hash",
    "expires_at", "forbidden_uses",
)
UNTRUSTED_SERIALIZERS = {"pickle", "joblib", "cloudpickle", "marshal"}


def _parse(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def validate(contract: Any, now: str = "2026-07-20T00:00:00+00:00") -> list[str]:
    if not isinstance(contract, dict):
        return ["contract must be an object"]
    errors = [
        f"{key} is required"
        for key in REQUIRED
        if key not in contract
        or contract[key] is None
        or (isinstance(contract[key], str) and not contract[key].strip())
        or (isinstance(contract[key], (list, dict)) and not contract[key])
    ]
    if errors:
        return errors
    order = contract["feature_order"]
    features = contract["features"]
    if not isinstance(order, list) or not isinstance(features, list) or order != [item.get("name") for item in features]:
        errors.append("feature_order must exactly match features")
    event_time = _parse(contract["event_time"])
    available_at = _parse(contract["available_at"])
    label_complete = _parse(contract["label_complete_at"])
    if not event_time or not available_at or not label_complete:
        errors.append("event_time, available_at, and label_complete_at must be ISO timestamps")
    elif available_at > event_time:
        errors.append("available_at cannot be after event_time")
    elif label_complete <= event_time:
        errors.append("label_complete_at must be after event_time")
    if contract.get("fit_scope") != "fold_local":
        errors.append("fit_scope must be fold_local")
    if _parse(contract["fit_end"]) is None or _parse(contract["fit_start"]) is None:
        errors.append("fit_start and fit_end must be ISO timestamps")
    elif _parse(contract["fit_end"]) >= event_time:
        errors.append("fit_end must precede event_time")
    if contract["serializer"].lower() in UNTRUSTED_SERIALIZERS:
        errors.append("serializer is executable or untrusted")
    expiry = _parse(contract["expires_at"])
    current = _parse(now)
    if expiry is None or current is None or expiry <= current:
        errors.append("model artifact is expired")
    if contract.get("overlap_span") and contract.get("purged_or_embargoed") is not True:
        errors.append("overlapping labels require purged_or_embargoed true")
    if contract.get("asset_class") == "derivative":
        missing = [field for field in ("funding_complete", "mark_complete", "index_complete") if contract.get(field) is not True]
        if missing:
            errors.append("derivative fold incomplete: " + ", ".join(missing))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--as-of", default="2026-07-20T00:00:00+00:00")
    args = parser.parse_args()
    errors = validate(json.loads(args.contract.read_text(encoding="utf-8")), args.as_of)
    if errors:
        print("INVALID: " + "; ".join(errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
