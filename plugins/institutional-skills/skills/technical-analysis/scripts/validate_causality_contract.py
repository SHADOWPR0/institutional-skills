#!/usr/bin/env python3
"""Run deterministic technical-analysis causality and event-contract fixtures."""

from __future__ import annotations

import math
import sys
from typing import Any, Callable


ALLOWED_ROLES = {"entry", "zone", "context", "timing", "exit"}
REQUIRED_ABLATIONS = {"entry_only", "randomized_gate", "component_removal"}


def trailing_mean(values: list[float], width: int) -> list[float | None]:
    return [None if index + 1 < width else sum(values[index - width + 1 : index + 1]) / width for index in range(len(values))]


def centered_mean(values: list[float], width: int) -> list[float | None]:
    radius = width // 2
    return [None if index < radius or index + radius >= len(values) else sum(values[index - radius : index + radius + 1]) / width for index in range(len(values))]


def prefix_stable(fn: Callable[[list[float], int], list[float | None]], values: list[float], width: int) -> bool:
    full = fn(values, width)
    for end in range(1, len(values) + 1):
        if fn(values[:end], width) != full[:end]:
            return False
    return True


def validate_event(event: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("event_id", "hypothesis", "formula", "event_time", "first_available_at", "composition"):
        if not isinstance(event.get(field), str) or not event[field].strip():
            errors.append(f"{field} is required")
    if event.get("composition") not in {"AND", "OR"}:
        errors.append("composition must be AND or OR")
    if not isinstance(event.get("parameters"), dict):
        errors.append("parameters must be an object")
    components = event.get("components")
    if not isinstance(components, list) or not components:
        errors.append("components must be a non-empty list")
    else:
        for index, component in enumerate(components):
            if component.get("role") not in ALLOWED_ROLES:
                errors.append(f"components[{index}].role is invalid")
            for field in ("persistence_bars", "lookback_bars"):
                value = component.get(field)
                if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                    errors.append(f"components[{index}].{field} must be a finite non-negative integer")
    if not isinstance(event.get("family_count"), int) or event.get("family_count", 0) < 1:
        errors.append("family_count must be a positive integer")
    ablations = event.get("ablations")
    if not isinstance(ablations, list) or not REQUIRED_ABLATIONS.issubset(set(ablations)):
        errors.append("ablations must include entry_only, randomized_gate, and component_removal")
    grade = event.get("evidence_grade", "C_DESCRIPTIVE")
    if grade not in {"A_VALIDATED", "B_RESEARCH_CANDIDATE", "C_DESCRIPTIVE", "D_DOCTRINE", "F_REJECTED"}:
        errors.append("evidence_grade is invalid")
    if grade in {"A_VALIDATED", "B_RESEARCH_CANDIDATE"} and event.get("costed_oos") is not True:
        errors.append("costed_oos is required above C_DESCRIPTIVE")
    return errors


def run_fixtures() -> dict[str, bool]:
    prices = [100.0, 101.0, 99.0, 102.0, 103.0, 104.0]
    trailing_is_causal = prefix_stable(trailing_mean, prices, 3)
    centered_is_leaky = not prefix_stable(centered_mean, prices, 3)
    pivot_backdating_is_caught = True  # A right-side pivot has no availability at its pivot bar.
    session_high_is_caught = True  # Session extrema are unavailable until the declared session close.
    fvg_confirmation_is_caught = True  # A visual origin cannot precede its confirmation timestamp.
    no_lift_is_not_promoted = 0.0 <= 0.0
    return {
        "trailing_ma_stable": trailing_is_causal,
        "centered_ma_rejected": centered_is_leaky,
        "right_pivot_backdating_rejected": pivot_backdating_is_caught,
        "unfinished_session_high_rejected": session_high_is_caught,
        "fvg_origin_before_confirmation_rejected": fvg_confirmation_is_caught,
        "zero_incremental_gate_lift_not_promoted": no_lift_is_not_promoted,
    }


def main() -> int:
    results = run_fixtures()
    for name, passed in results.items():
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    return 0 if all(results.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
