#!/usr/bin/env python3
"""Read-only packet/receipt checks. Never imports the live API route or writes CRM."""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


VERSION = "relationship_update.v1"
STATUSES = {
    "confirmed_owner", "confirmed_owner_instruction", "confirmed_warm_relationship",
    "confirmed_planned_joint_lunch", "planned_connector_ask", "pending_permission",
    "potential_path", "proposed_path_unconfirmed", "none_known",
}
GATES = {"linkedin_mutual_path_research", "verify_connector_permission",
         "verify_confidential_identity"}
HOLDS = {"blocked", "hard_block", "suppressed", "manual_hold", "pending"}


class InvalidHandoff(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise InvalidHandoff(message)


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def packet_digest(packet):
    """Local checkpoint hash, not a new packet field or an owner receipt field."""
    return digest(json.dumps(packet, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def _text(row, field, maximum, required=True):
    value = row.get(field)
    if value is None and not required:
        return
    require(isinstance(value, str) and len(value) <= maximum and
            (not required or bool(value.strip())), f"Invalid {field}")


def _minimal(packet):
    """Conservative authoring subset, NOT an implementation of the native parser."""
    require(isinstance(packet, dict), "Packet must be an object")
    require(packet.get("schemaVersion") == VERSION, "Invalid schemaVersion")
    _text(packet, "runId", 160)
    _text(packet, "observedAt", 100)
    try:
        date = datetime.fromisoformat(packet["observedAt"].replace("Z", "+00:00"))
        require(date.tzinfo is not None, "observedAt requires timezone")
    except ValueError as exc:
        raise InvalidHandoff("Invalid observedAt") from exc
    for field, maximum in (("sources", 20), ("updates", 50)):
        require(isinstance(packet.get(field), list) and
                1 <= len(packet[field]) <= maximum, f"Invalid {field} count")
    for source in packet["sources"]:
        require(isinstance(source, dict), "Source must be an object")
        _text(source, "namespace", 120)
        _text(source, "path", 1000)
        require(isinstance(source.get("sha256"), str) and
                re.fullmatch(r"[a-fA-F0-9]{64}", source["sha256"]), "Invalid SHA-256")
    aliases = set()
    for row in packet["updates"]:
        require(isinstance(row, dict), "Update must be an object")
        require(row.get("campaignId") in ("mortgage-partnerships", "capital-partnerships"), "Invalid campaignId")
        require(row.get("relationshipStatus") in STATUSES, "Invalid relationshipStatus")
        require(row.get("taskGate") is None or row.get("taskGate") in GATES,
                "Minimal mode requires a modern taskGate")
        for field, maximum in (("sourceNamespace", 120), ("sourceId", 500),
                               ("relationshipOwner", 300), ("relationshipStage", 120),
                               ("holdReason", 1000), ("nextAction", 1500)):
            _text(row, field, maximum)
        for field, maximum in (("canonicalId", 500), ("contactMode", 120),
                               ("nextActionOwner", 300), ("prerequisite", 1000)):
            _text(row, field, maximum, required=False)
        path = row.get("relationshipPath", [])
        require(isinstance(path, list) and len(path) <= 12 and
                all(isinstance(p, str) and p.strip() and len(p) <= 300 for p in path),
                "Invalid relationshipPath")
        require(isinstance(row.get("provenance", {}), dict), "Invalid provenance")
        alias = (row["campaignId"], row["sourceNamespace"], row["sourceId"])
        require(alias not in aliases, "Duplicate campaign alias")
        aliases.add(alias)
    return packet


def _source_reference(value, sources):
    if not isinstance(value, dict):
        return False
    allowed = {"namespace", "source_path", "sha256", "field_pointer", "observed_at"}
    return (set(value) <= allowed and
            isinstance(value.get("field_pointer"), str) and
            value["field_pointer"].startswith("/") and
            (value.get("namespace"), value.get("source_path"), value.get("sha256")) in sources)


def _safety(value, path=(), sources=frozenset()):
    # Inspect original input too: the native parser intentionally discards unknown keys.
    if isinstance(value, dict):
        for key, item in value.items():
            normalized = re.sub(r"[^a-z]", "", key.lower())
            if normalized in {"marketingeligible", "sendauthorized",
                              "activatecampaign", "clearsuppression", "contactmutation",
                              "sourcemutation", "confirmedintro"}:
                evidence_slot = path[-2:] == ("provenance", "field_evidence")
                require(item is False or item is None or
                        (evidence_slot and _source_reference(item, sources)),
                        f"Forbidden authority: {key}")
            if normalized in {"sendauthority", "activationauthority", "writebackauthority"}:
                require(item in (None, "none"), f"Forbidden authority: {key}")
            _safety(item, path + (key,), sources)
    elif isinstance(value, list):
        for item in value:
            _safety(item, path, sources)


def validate_packet(packet, schema_path=None, allow_minimal=False):
    require(isinstance(packet, dict), "Packet must be an object")
    sources = {(s.get("namespace"), s.get("path"), s.get("sha256"))
               for s in packet.get("sources", []) if isinstance(s, dict)
               and all(isinstance(s.get(k), str) for k in ("namespace", "path", "sha256"))}
    _safety(packet, sources=sources)
    if schema_path is None:
        require(allow_minimal, "Supply --schema-path or explicitly opt into --allow-minimal")
        return _minimal(packet), "minimal_contract_only"
    path = Path(schema_path).resolve(strict=True)
    require(path.name == "relationship-updates.ts", "Select the pure relationship-updates.ts parser")
    js = """
import {readFileSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
try {
  const {parseRelationshipUpdatePacket} = await import(pathToFileURL(process.argv[1]));
  process.stdout.write(JSON.stringify(parseRelationshipUpdatePacket(JSON.parse(readFileSync(0, 'utf8')))));
} catch { process.stderr.write('Native relationship parser rejected input.'); process.exit(1); }
"""
    result = subprocess.run(["node", "--input-type=module", "-e", js, str(path)],
                            input=json.dumps(packet), text=True, capture_output=True, timeout=15)
    require(result.returncode == 0, "Native parser failed; no silent fallback")
    return json.loads(result.stdout), "canonical_typescript_parser"


def validate_receipt(packet, envelope):
    """Verify native route.ts structure/binding, not owner authenticity or DB state."""
    require(isinstance(envelope, dict), "Receipt envelope must be an object")
    r = envelope.get("receipt", envelope)
    require(isinstance(r, dict), "Receipt must be an object")
    require(r.get("schema_version") == VERSION and r.get("run_id") == packet["runId"] and
            r.get("observed_at") == packet["observedAt"], "Receipt does not match packet")
    expected_audit = "aud_rel_" + digest(f"{VERSION}:{packet['runId']}")[:24]
    require(r.get("audit_id") == expected_audit, "Receipt audit_id mismatch")
    sources = ["src_" + digest(f"{s['namespace']}:{s['path']}:{s['sha256']}")[:24]
               for s in packet["sources"]]
    require(r.get("source_record_ids") == sources, "Receipt source binding mismatch")
    for field in ("outbound_actions", "source_mutations", "contact_mutations", "campaign_activations"):
        require(type(r.get(field)) is int and r[field] == 0, f"Receipt {field} must be zero")
    require(type(r.get("idempotent")) is bool, "Missing idempotent receipt state")
    results = r.get("results")
    require(isinstance(results, list) and len(results) == len(packet["updates"]),
            "Receipt result count mismatch")
    expected = {(u["campaignId"], u["sourceNamespace"], u["sourceId"]): u for u in packet["updates"]}
    seen, pending, nomination, gates = set(), 0, 0, 0
    for row in results:
        require(isinstance(row, dict), "Receipt result must be an object")
        key = (row.get("campaign_id"), row.get("source_namespace"), row.get("source_id"))
        require(key in expected and key not in seen, "Receipt alias mismatch or duplicate")
        seen.add(key)
        require(row.get("marketing_eligible") is False, "Receipt cannot grant eligibility")
        status = row.get("status")
        require(status in {"relationship_updated", "identity_pending_relationship_updated",
                           "awaiting_campaign_nomination"}, "Invalid receipt result status")
        u = expected[key]
        if u.get("canonicalId") is not None:
            require(row.get("canonical_id") == u["canonicalId"], "Canonical receipt identity conflict")
        if status == "awaiting_campaign_nomination":
            nomination += 1
            continue
        require(row.get("relationship_owner") == u["relationshipOwner"] and
                row.get("relationship_status") == u["relationshipStatus"] and
                row.get("task_gate") == u.get("taskGate"), "Receipt relationship mismatch")
        require(row.get("suppression_state") in HOLDS, "Receipt cannot clear suppression")
        gates += bool(row.get("task_gate"))
        if status == "identity_pending_relationship_updated":
            pending += 1
            require(row.get("canonical_id") is None and u.get("canonicalId") is None and
                    row.get("subject_id") == f"alias:{u['sourceNamespace']}:{u['sourceId']}",
                    "Identity-pending receipt is inconsistent")
        else:
            canonical = row.get("canonical_id")
            require(isinstance(canonical, str) and canonical and not canonical.startswith("alias:") and
                    row.get("subject_id") == canonical, "Missing canonical receipt identity")
            require(u.get("canonicalId") in (None, canonical), "Canonical receipt identity conflict")
    for field, count in (("updates_received", len(results)), ("updates_committed", len(results) - nomination),
                         ("identity_pending", pending), ("awaiting_campaign_nomination", nomination),
                         ("task_gates", gates)):
        require(type(r.get(field)) is int and r[field] == count, f"Receipt {field} mismatch")
    return "partial" if nomination else "complete"


def validate_handoff(packet, schema_path=None, allow_minimal=False, receipt=None):
    parsed, mode = validate_packet(packet, schema_path, allow_minimal)
    receipt_state = "awaiting_owner" if receipt is None else validate_receipt(parsed, receipt)
    return {"valid": True, "contract_mode": mode, "packet_sha256": packet_digest(packet),
            "receipt_state": receipt_state, "owner_authenticity_verified": False,
            "send_authority": "none", "graph_commit_verified": False}


def evaluate_invariants(case, output):
    """Flat equality assertions on forward-agent summary fields; no agent answers generated."""
    errors = []
    for key, expected in case["expected_invariants"].items():
        if key not in output or output[key] != expected or type(output[key]) is not type(expected):
            errors.append(key)
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path)
    parser.add_argument("--schema-path", type=Path)
    parser.add_argument("--allow-minimal", action="store_true")
    parser.add_argument("--owner-receipt", type=Path)
    args = parser.parse_args(argv)
    try:
        packet = json.loads(args.packet.read_text())
        receipt = json.loads(args.owner_receipt.read_text()) if args.owner_receipt else None
        result = validate_handoff(packet, args.schema_path, args.allow_minimal, receipt)
        print(json.dumps(result, sort_keys=True))
        return 0
    except (OSError, ValueError, TypeError, KeyError, subprocess.SubprocessError):
        # Private input values and native exception messages must not leak to shared logs.
        print(json.dumps({"valid": False, "error": "Relationship handoff validation failed"}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
