#!/usr/bin/env python3
"""Deterministic synthetic inline execution and interrupted-state recovery demo."""
import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins/institutional-skills/skills"
sys.path.insert(0, str(SKILLS / "financial-house-operating-system/scripts"))
from workforce_runtime import new_mission, apply_event, recovery

def run(output):
    output.mkdir(parents=True, exist_ok=True)
    mandate = json.loads((ROOT / "examples/mandate.json").read_text())
    facts = mandate["facts"]
    def write(name, value):
        p = output / name
        p.write_text(json.dumps(value, indent=2) if not isinstance(value, str) else value)
        return str(p)
    model = {"dscr": facts["ebitda"] / facts["annual_debt_service"],
             "debt_to_ebitda": facts["existing_debt"] / facts["ebitda"],
             "stress_dscr": facts["ebitda"] * 0.7 / facts["annual_debt_service"],
             "source": "synthetic_fixture", "status": "illustrative_not_approval"}
    model_path = write("model.json", model)
    memo_path = write("credit-memo.md", "# Synthetic Credit Review\n\nBase DSCR 2.0x; 30% EBITDA decline gives 1.4x. Debt/EBITDA 1.25x. Request verified statements, debt schedule, collateral valuation and lien search before terms. No loan commitment.\n")
    draft_path = write("internal-draft.md", "# Internal Draft, Not Sent\n\nWould a short equipment-financing checklist help your team qualify referrals? It covers cash flow, collateral and the documents needed before discussing terms.\n\nRecipient and contact eligibility remain unverified.\n")
    state = new_mission({**mandate, "source_paths": [str(ROOT / "examples/mandate.json")]})
    dispatch = write("inline-execution.json", {"executor": "parent_inline", "synthetic": True})
    validation = write("validation.json", {"passed": model["dscr"] == 2 and abs(model["stress_dscr"] - 1.4) < 1e-9, "external_actions": 0})
    for role_id, assignment in state["assignments"].items():
        apply_event(state, {"event_id": role_id + "-start", "kind": "assigned", "role_id": role_id, "executor": "parent_inline", "receipt_path": dispatch})
        reads = [str(SKILLS / s / "SKILL.md") for s in assignment["packet"]["skills"] if (SKILLS / s / "SKILL.md").exists()]
        # The deterministic demo reads the actual contracts; it does not claim model interpretation.
        for path in reads: Path(path).read_text()
        apply_event(state, {"event_id": role_id + "-done", "kind": "completed", "role_id": role_id,
            "artifact_paths": [model_path, memo_path, draft_path], "skill_read_paths": reads,
            "validations": [{"command": "synthetic ratio and no-external-action check", "exit_code": 0, "receipt_path": validation}]})
    owner = write("synthetic-owner.json", {"decision": "accepted_for_demo_only"})
    apply_event(state, {"event_id": "owner", "kind": "owner_decision", "role_ids": list(state["assignments"]), "decision": "accepted", "receipt_path": owner})
    packet = write("handoff.json", {"runId": "demo-recovery-1", "data": "synthetic; no CRM submission"})
    event = {"event_id": "stage", "kind": "handoff", "handoff_id": "demo", "run_id": "demo-recovery-1", "owner": "recipient-crm", "packet_path": packet}
    apply_event(state, event)
    checkpoint = write("mission.json", state)
    restored = json.loads(Path(checkpoint).read_text())
    revision = restored["revision"]
    apply_event(restored, event)
    assert restored["revision"] == revision
    resumed = recovery(restored)
    assert resumed["pending_handoffs"]["demo"]["run_id"] == "demo-recovery-1"
    write("recovery.json", resumed)
    apply_event(restored, {"event_id": "observed", "kind": "outcome", "outcome_type": "synthetic_calculation_checked", "observed_at": "2026-01-01T00:00:00Z", "receipt_path": validation})
    apply_event(restored, {"event_id": "lesson", "kind": "lesson_candidate", "outcome_id": "observed", "canonical_owner": "universal-banker", "hypothesis": "An explicit stressed coverage line makes the synthetic review easier to verify.", "baseline_path": memo_path, "challenger_path": model_path, "evaluation_path": validation})
    write("mission.json", restored)
    result = {"demo_passed": True, "executor": "deterministic_inline", "native_agent_invoked": False,
              "roles_executed": list(restored["assignments"]), "ratios": model,
              "recovery_verified": True, "lesson_state": restored["lessons"][0]["status"], "external_actions": 0}
    write("RESULT.json", result)
    return result

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    print(json.dumps(run(p.parse_args().output), indent=2))
