#!/usr/bin/env python3
"""Fail closed on incomplete or contaminated external quant-repository intake records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


PROHIBITED_DIRECT_ADOPT_LICENSES = {"GPL", "AGPL", "UNLICENSED", "UNKNOWN"}
REQUIRED_TACTIC_FIELDS = {"source_files", "test_evidence", "benchmark", "ablation", "effort", "impact", "decision"}
REQUIRED_ADAPTER_CHECKS = {"websocket_recovery", "rest_reconciliation", "duplicate_intent", "rate_limit", "outage", "stale_data"}


def validate(record: Any) -> list[str]:
    if not isinstance(record, dict):
        return ["record must be an object"]
    errors: list[str] = []
    for field in ("objective", "domain_owner", "repository", "target_system", "review_date", "license", "cleanup_proof"):
        if not record.get(field):
            errors.append(f"{field} is required")
    sha = record.get("commit_sha")
    if not isinstance(sha, str) or len(sha) != 40:
        errors.append("commit_sha must be a full 40-character SHA")
    budget = record.get("review_budget", {})
    if not isinstance(budget, dict) or not isinstance(budget.get("agents"), int) or not isinstance(budget.get("rechecks"), int):
        errors.append("declared agent and recheck budget is required")
    if record.get("external_code_executed") is not False:
        errors.append("external code execution is prohibited during intake")
    if record.get("protected_paths_read_only") is not True:
        errors.append("protected paths must remain read-only")
    for index, tactic in enumerate(record.get("tactics", [])):
        missing = [field for field in REQUIRED_TACTIC_FIELDS if not tactic.get(field)]
        if missing:
            errors.append(f"tactics[{index}] missing " + ", ".join(sorted(missing)))
        if tactic.get("evidence_type") == "README_ONLY":
            errors.append(f"tactics[{index}] README-only evidence is insufficient")
        license_name = str(record.get("license", "")).upper()
        if tactic.get("decision") == "ADOPT" and license_name in PROHIBITED_DIRECT_ADOPT_LICENSES:
            errors.append(f"tactics[{index}] direct ADOPT blocked by license")
    adapter = record.get("adapter")
    if adapter is not None:
        for field in ("official_api_version", "as_of", "least_privilege_auth", "event_order", "capability_status"):
            if not adapter.get(field):
                errors.append(f"adapter.{field} is required")
        if adapter.get("capability_status") not in {"SUPPORTED", "UNSUPPORTED", "UNVERIFIED"}:
            errors.append("adapter.capability_status is invalid")
        checks = adapter.get("chaos_checks", {})
        missing = [name for name in REQUIRED_ADAPTER_CHECKS if checks.get(name) is not True]
        if missing:
            errors.append("adapter chaos checks incomplete: " + ", ".join(sorted(missing)))
        if adapter.get("manual_approval_before_credentials_or_orders") is not True:
            errors.append("adapter requires manual approval before credentials or orders")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    errors = validate(json.loads(args.record.read_text(encoding="utf-8")))
    if errors:
        print("INVALID: " + "; ".join(errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
