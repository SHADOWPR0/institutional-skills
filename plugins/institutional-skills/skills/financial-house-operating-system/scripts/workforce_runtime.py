#!/usr/bin/env python3
"""Small, local work-packet journal. Dispatch stays with the host's native agent tool."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any

from route_financial_house import build_route


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def evidence(path: str) -> dict[str, str]:
    item = Path(path).expanduser().resolve(strict=True)
    if not item.is_file():
        raise ValueError(f"Evidence must be a file: {item}")
    return {"path": str(item), "sha256": hashlib.sha256(item.read_bytes()).hexdigest()}


def verify(ref: dict[str, str]) -> None:
    if evidence(ref["path"])["sha256"] != ref["sha256"]:
        raise ValueError(f"Evidence changed: {ref['path']}")


def new_mission(context: dict[str, Any]) -> dict[str, Any]:
    if not str(context.get("objective", "")).strip():
        raise ValueError("A concrete objective is required")
    route = build_route(context)
    roles = route.get("staffed_roles", route.get("roles", []))
    assignments = {}
    for role in roles:
        role_id = role.get("role_id", role.get("id"))
        if not role_id:
            raise ValueError("Router returned a role without an id")
        assignments[role_id] = {"packet": role, "status": "planned", "attempts": []}
    return {
        "schema_version": "workforce_mission.v1", "revision": 0,
        "created_at": now(), "objective": context["objective"],
        "context": context, "route": route, "status": "planned",
        "sources": [evidence(p) for p in context.get("source_paths", [])],
        "assignments": assignments, "handoffs": {}, "outcomes": [],
        "lessons": [], "events": [],
        "authority": "A plan or journal entry grants no external action authority.",
    }


def apply_event(state: dict[str, Any], event: dict[str, Any]) -> dict[str, Any]:
    """Advance only on explicit receipts; replaying an event is a no-op."""
    event_id = event.get("event_id")
    if not isinstance(event_id, str) or not event_id.strip():
        raise ValueError("event_id is required for replay safety")
    digest = hashlib.sha256(json.dumps(event, sort_keys=True).encode()).hexdigest()
    for prior in state["events"]:
        if prior["event_id"] == event_id:
            if prior["sha256"] != digest:
                raise ValueError("event_id reused with different content")
            return state
    if event.get("expected_revision", state["revision"]) != state["revision"]:
        raise ValueError("Stale revision; reload the mission before changing it")
    kind = event.get("kind")
    role_id = event.get("role_id")
    assignment = state["assignments"].get(role_id)
    if kind in {"assigned", "completed", "failed"} and not assignment:
        raise ValueError("Unknown role")

    if kind == "assigned":
        if assignment["status"] not in {"planned", "failed", "rework"}:
            raise ValueError("Role already assigned; reconcile before redispatch")
        executor = event.get("executor")
        if executor not in {"native_agent", "parent_inline"}:
            raise ValueError("Executor must describe actual host execution")
        receipt = evidence(event["receipt_path"])
        if executor == "native_agent":
            agent_id = event.get("native_agent_id")
            if not agent_id or agent_id not in Path(receipt["path"]).read_text():
                raise ValueError("Native agent id must appear in the dispatch receipt")
        assignment["attempts"].append({"executor": executor,
            "native_agent_id": event.get("native_agent_id"), "dispatch": receipt})
        assignment["status"] = "running"
        state["status"] = "running"
    elif kind == "completed":
        if assignment["status"] != "running":
            raise ValueError("Completion requires an actual assignment")
        artifacts = [evidence(p) for p in event.get("artifact_paths", [])]
        checks = event.get("validations", [])
        reads = [evidence(p) for p in event.get("skill_read_paths", [])]
        if not artifacts or not checks or not reads:
            raise ValueError("Artifacts, validation receipts, and loaded skills are required")
        known = set(assignment["packet"].get("skills", []))
        for ref in reads:
            path = Path(ref["path"])
            if path.name != "SKILL.md" or path.parent.name not in known:
                raise ValueError("Loaded skill must resolve to an assigned canonical capability")
        validation_receipts = []
        for check in checks:
            if check.get("exit_code") != 0 or not check.get("command"):
                raise ValueError("Failed or unspecified validation")
            validation_receipts.append({"command": check["command"], "exit_code": 0,
                "receipt": evidence(check["receipt_path"])})
        assignment.update(status="validated", artifacts=artifacts, loaded_skills=reads,
                          validations=validation_receipts)
        state["status"] = "awaiting_owner"
    elif kind == "failed":
        if assignment["status"] != "running" or not event.get("reason"):
            raise ValueError("Failure requires a running assignment and reason")
        assignment.update(status="failed", failure=event["reason"])
        state["status"] = "needs_recovery"
    elif kind == "owner_decision":
        selected = event.get("role_ids", [])
        if not selected or any(r not in state["assignments"] for r in selected):
            raise ValueError("Owner decision requires known roles")
        if any(state["assignments"][r]["status"] != "validated" for r in selected):
            raise ValueError("Owner cannot accept unvalidated work")
        if event.get("decision") not in {"accepted", "rework"}:
            raise ValueError("Decision must be accepted or rework")
        receipt = evidence(event["receipt_path"])
        for r in selected:
            for ref in state["assignments"][r]["artifacts"]:
                verify(ref)
            state["assignments"][r].update(status=event["decision"], owner_receipt=receipt)
        state["status"] = ("accepted" if all(a["status"] == "accepted"
            for a in state["assignments"].values()) else "running")
    elif kind == "handoff":
        handoff_id = event["handoff_id"]
        packet = evidence(event["packet_path"])
        if handoff_id in state["handoffs"]:
            if state["handoffs"][handoff_id]["packet"] != packet:
                raise ValueError("Handoff id reused for different packet")
            raise ValueError("Handoff already pending; reconcile its existing run id")
        if not event.get("run_id") or not event.get("owner"):
            raise ValueError("Handoff requires the receiving owner and stable run id")
        state["handoffs"][handoff_id] = {"owner": event["owner"],
            "run_id": event["run_id"], "packet": packet, "status": "awaiting_owner"}
    elif kind == "handoff_receipt":
        handoff = state["handoffs"][event["handoff_id"]]
        verify(handoff["packet"])
        receipt = evidence(event["receipt_path"])
        payload = json.loads(Path(receipt["path"]).read_text())
        native = payload.get("receipt", payload)
        ids = {value for value in (payload.get("runId"), native.get("runId"), native.get("run_id")) if value}
        if ids != {handoff["run_id"]}:
            raise ValueError("Owner receipt does not match the submitted run id")
        if event.get("result") not in {"accepted", "rejected", "needs_review"}:
            raise ValueError("Explicit owner result required")
        # Domain adapters validate owner-specific semantics before this checkpoint.
        check = event.get("validation", {})
        if check.get("exit_code") != 0 or not check.get("command"):
            raise ValueError("Domain receipt validation is required")
        handoff.update(status=event["result"], receipt=receipt,
            validation={"command": check["command"], "receipt": evidence(check["receipt_path"])},
            owner_authenticity_verified=False, graph_commit_verified=False,
            receipt_scope="Input receipt checked; the owning system remains the commit authority")
    elif kind == "outcome":
        if not event.get("observed_at") or not event.get("outcome_type"):
            raise ValueError("Observed outcome type and timestamp required")
        state["outcomes"].append({"id": event_id, "type": event["outcome_type"],
            "observed_at": event["observed_at"], "receipt": evidence(event["receipt_path"]),
            "note": "Evidence pointer only; the source system owns operational facts."})
    elif kind == "lesson_candidate":
        if event.get("outcome_id") not in {o["id"] for o in state["outcomes"]}:
            raise ValueError("A lesson requires an observed outcome")
        if not event.get("hypothesis") or not event.get("canonical_owner"):
            raise ValueError("Lesson requires a falsifiable hypothesis and existing owner")
        state["lessons"].append({"id": event_id, "status": "candidate_not_promoted",
            "outcome_id": event["outcome_id"], "hypothesis": event["hypothesis"],
            "canonical_owner": event["canonical_owner"],
            "baseline": evidence(event["baseline_path"]),
            "challenger": evidence(event["challenger_path"]),
            "evaluation": evidence(event["evaluation_path"])})
    else:
        raise ValueError(f"Unknown event kind: {kind}")
    state["revision"] += 1
    state["events"].append({"event_id": event_id, "kind": kind, "sha256": digest, "at": now()})
    return state


def recovery(state: dict[str, Any]) -> dict[str, Any]:
    return {"revision": state["revision"], "status": state["status"],
        "assignments": {r: {"status": a["status"], "last_attempt": a["attempts"][-1:]}
                        for r, a in state["assignments"].items() if a["status"] != "accepted"},
        "pending_handoffs": {k: v for k, v in state["handoffs"].items()
                             if v["status"] == "awaiting_owner"},
        "instruction": "Inspect running native ids and pending owner run ids before redispatch."}


@contextmanager
def locked(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o600)
    with os.fdopen(fd, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def save(path: Path, state: dict[str, Any]) -> None:
    fd, temp = tempfile.mkstemp(dir=path.parent, prefix=".workforce-", suffix=".json")
    try:
        with os.fdopen(fd, "w") as handle:
            json.dump(state, handle, indent=2)
            handle.write("\n")
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["init", "record", "resume"])
    parser.add_argument("--state", type=Path, required=True,
                        help="Private mission state in the owning project, never the skill library")
    parser.add_argument("--input", type=Path, help="Context (init) or event (record) JSON")
    args = parser.parse_args()
    try:
        with locked(args.state):
            if args.action == "init":
                if args.state.exists():
                    raise ValueError("Mission exists; resume it rather than replacing evidence")
                state = new_mission(json.loads(args.input.read_text()))
            else:
                state = json.loads(args.state.read_text())
                if args.action == "record":
                    apply_event(state, json.loads(args.input.read_text()))
            if args.action != "resume":
                save(args.state, state)
            print(json.dumps(recovery(state), indent=2))
    except (ValueError, KeyError, OSError, TypeError) as error:
        parser.exit(1, f"ERROR: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
