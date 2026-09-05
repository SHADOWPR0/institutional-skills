#!/usr/bin/env python3
"""Validate a minimal AI/ML/RL experiment plan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = [
    "objective",
    "owner",
    "decision",
    "data_sources",
    "as_of_date",
    "split_policy",
    "baseline",
    "primary_metric",
    "leakage_controls",
    "promotion_gate",
    "kill_switch",
]


OPTIONAL_BUT_STRONGLY_RECOMMENDED = [
    "cost_model",
    "latency_budget",
    "ablation_plan",
    "monitoring_plan",
    "rollback_plan",
    "security_review",
]


def load_plan(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return json.loads(text)


def validate(plan: dict) -> dict:
    missing = [key for key in REQUIRED if not plan.get(key)]
    recommended_missing = [key for key in OPTIONAL_BUT_STRONGLY_RECOMMENDED if not plan.get(key)]
    return {
        "ok": not missing,
        "missing_required": missing,
        "missing_recommended": recommended_missing,
        "decision": "ready_for_experiment" if not missing else "blocked_until_required_fields_exist",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_json", type=Path)
    args = parser.parse_args()
    result = validate(load_plan(args.plan_json))
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
