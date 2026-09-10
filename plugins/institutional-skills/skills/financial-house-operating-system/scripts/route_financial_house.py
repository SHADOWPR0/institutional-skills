#!/usr/bin/env python3
"""Deterministic mission router for the financial-house operating system."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Role:
    role_id: str
    title: str
    desk: str
    skills: tuple[str, ...]
    output: str


REGISTRY_PATH = Path(__file__).resolve().parents[1] / "references" / "capability-registry.json"


def load_registry(path: Path = REGISTRY_PATH) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        registry = json.load(handle)
    if registry["schema_version"] != 1:
        raise ValueError("Unsupported capability registry schema")
    return registry


ROLES: dict[str, Role] = {
    profile["id"]: Role(
        profile["id"], profile["title"], profile["desk"],
        tuple(profile["default_skills"]), profile["deliverable"],
    )
    for profile in load_registry()["execution_roles"]
}


CATEGORY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "investment": (
        "portfolio",
        "investment",
        "trade",
        "trading",
        "alpha",
        "quant",
        "risk budget",
        "position sizing",
        "market making",
        "macro",
        "equities",
        "stock",
        "stocks",
        "etf",
        "valuation",
        "dividend",
        "asset allocation",
        "equity",
        "public market",
        "crypto",
        "options",
    ),
    "banking": (
        "credit",
        "underwrite",
        "underwriting",
        "loan",
        "loans",
        "lender",
        "lenders",
        "capital markets",
        "debt",
        "financing",
        "mortgage",
        "mortgages",
        "securitization",
        "m&a",
        "deal",
        "term sheet",
        "covenant",
        "covenants",
        "borrower",
        "borrowers",
        "lbo",
        "banking",
        "alm",
        "syndication",
        "acquisition financing",
        "financial model",
        "three statement",
        "dscr",
        "dti",
        "ltv",
        "financial forecast",
        "numerical model",
        "tax strategy",
        "estate planning",
        "trust administration",
        "fiduciary",
        "cash flow model",
        "cash flows",
    ),
    "venture": (
        "venture",
        "vc",
        "seed",
        "series a",
        "series b",
        "series c",
        "growth equity",
        "pre-ipo",
        "crossover",
        "pro rata",
        "pro-rata",
        "secondaries",
        "cap table",
        "platform support",
    ),
    "growth": (
        "sales",
        "marketing",
        "growth",
        "lead",
        "lead gen",
        "leadgen",
        "leads",
        "crm",
        "outreach",
        "positioning",
        "offer",
        "funnel",
        "conversion",
        "referral",
        "partnership",
        "demand",
    ),
    "communications": (
        "email",
        "memo",
        "pitch",
        "copy",
        "prose",
        "persuasion",
        "narrative",
        "deck",
        "letter",
        "write",
        "rewrite",
        "copyedit",
        "biography",
    ),
    "product_design": (
        "app",
        "site",
        "dashboard",
        "software",
        "python",
        "api",
        "bug",
        "website",
        "frontend",
        "front-end",
        "react",
        "next.js",
        "gsap",
        "tailwind",
        "figma",
        "blender",
        "responsive",
        "accessibility",
        "screenshot reconstruction",
        "backend",
        "code",
        "ui",
        "ux",
        "product",
        "deploy",
    ),
    "ai": (
        "ai",
        "ml",
        "llm",
        "eval",
        "machine learning",
        "neural network",
        "model evaluation",
        "leakage",
        "rl",
        "simulation",
    ),
    "ops": (
        "security",
        "records",
        "audit",
        "receipt",
        "governance",
        "automation",
        "workflow",
        "ops",
    ),
}

MACRO_KEYWORDS = ("macro", "rates thesis", "fx thesis", "policy regime", "macro themes")
TECHNICAL_KEYWORDS = ("technical analysis", "ta", "chart", "chart analysis", "market structure", "breadth", "rsi", "macd", "price action", "causal replay")
QUANT_KEYWORDS = ("quant", "systematic", "backtest", "walk forward", "stat arb", "factor model", "signal research")
RISK_KEYWORDS = ("sizing", "portfolio construction", "risk budget", "drawdown", "stress test", "concentration", "allocation", "reserves")
CAPITAL_KEYWORDS = ("lender", "lenders", "capital markets", "syndication", "securitization", "distribution", "financing", "finance the deal")
UNDERWRITE_KEYWORDS = ("underwrite", "underwriting", "lbo", "m&a", "merger", "acquisition", "covenant", "covenants", "financial model", "three statement", "dscr", "cash flows", "diligence")
CRM_KEYWORDS = ("crm", "lead", "leads", "lead gen", "leadgen", "outreach", "follow up", "relationship", "referral", "contact enrichment", "contacts", "pipeline")


CATEGORY_ROLES: dict[str, tuple[str, ...]] = {
    "investment": ("cio",),
    "venture": ("venture_platform",),
    "banking": ("credit_committee",),
    "growth": ("growth",),
    "communications": ("communications",),
    "product_design": ("product_design",),
    "ai": ("ai_validation",),
    "ops": ("ops_security",),
}


def load_context(raw: str | None, path: str | None) -> dict[str, Any]:
    if path:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    if raw:
        return json.loads(raw)
    return {}


def classify(text: str, registry: dict[str, Any] | None = None) -> list[str]:
    hits = [category for category, keywords in CATEGORY_KEYWORDS.items() if matches(text, keywords)]
    registry = registry or load_registry()
    for capability in registry["capabilities"]:
        if capability["kind"] == "support_workflow" and matches(text, capability["keywords"]):
            hits.append(capability["category"])
        if capability["kind"] not in ("desk_family", "investment_role", "banker_specialist"):
            continue
        # Full named desks and specialist contracts remain addressable without
        # inferring investment work from a software or geography noun alone.
        if matches(text, (capability["title"],)):
            hits.append(capability["category"])
    if matches(text, MACRO_KEYWORDS + TECHNICAL_KEYWORDS + QUANT_KEYWORDS):
        hits.insert(0, "investment")
    if matches(text, CRM_KEYWORDS) and "growth" not in hits:
        hits.append("growth")
    meeting = next(cap for cap in registry["capabilities"] if cap["id"] == "ops.meeting-capture")
    if matches(text, meeting["keywords"]) and not matches(text, tuple(k for k in CRM_KEYWORDS if k != "follow up") + CATEGORY_KEYWORDS["growth"]):
        hits = [category for category in hits if category != "growth"]
    # A valuation inside a transaction is banker work; editing a founder bio
    # does not assign an investment committee or an AI team.
    if "banking" in hits and not matches(text, ("investment", "portfolio", "trading", "stocks", "equities")):
        hits = [category for category in hits if category != "investment"]
    if "venture" in hits and matches(text, ("growth equity",)) and not matches(text, ("marketing", "sales", "crm", "gtm", "funnel", "partnership")):
        hits = [category for category in hits if category != "growth"]
    if set(hits) & {"investment", "venture", "banking"} and not re.search(
        r"\b(?:build|fix|implement|debug|develop|deploy) (?:a |the )?(?:web |python )?(?:app|api|software|website|dashboard|frontend|backend)\b", normalize(text)
    ) and not matches(text, ("bug", "code", "ui", "ux", "frontend", "backend", "dashboard", "website")):
        hits = [category for category in hits if category != "product_design"]
    if matches(text, ("copyedit", "rewrite", "biography")) and not matches(text, ("investment", "underwrite", "underwriting", "diligence")):
        hits = [category for category in hits if category not in ("investment", "banking", "venture")]
    return unique(hits) or ["ops"]


def normalize(text: str) -> str:
    return re.sub(r"[\s_-]+", " ", text.casefold()).strip()


def matches(text: str, keywords: tuple[str, ...] | list[str]) -> bool:
    normalized = normalize(text)
    return any(re.search(rf"(?<!\w){re.escape(normalize(keyword))}(?!\w)", normalized)
               for keyword in keywords if keyword.strip())


def request_text(context: dict[str, Any]) -> str:
    # Constraints, sources, model IDs and forbidden actions are not intent.
    fields = ("objective", "request", "goal", "task", "mandate", "deal_type", "asset_class", "sector", "region", "geography")
    return " ".join(str(context[key]) for key in fields if key in context)


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item not in seen:
            out.append(item)
            seen.add(item)
    return out


def build_route(context: dict[str, Any]) -> dict[str, Any]:
    registry = load_registry()
    blob = request_text(context)
    categories = classify(blob, registry)
    role_ids: list[str] = []
    crm = "growth" in categories and matches(blob, CRM_KEYWORDS)
    coordination_only = matches(blob, ("financing follow up",)) and not matches(blob, UNDERWRITE_KEYWORDS + ("structure", "finance the deal", "rank lenders", "compare lenders"))
    banker_evidence_only = crm and "banking" in categories and (coordination_only or not matches(blob, ("underwrite", "underwriting", "financing", "finance the deal", "structure", "m&a", "lbo")))
    if "investment" in categories or "venture" in categories:
        role_ids.append("venture_platform" if "venture" in categories else "cio")
        if matches(blob, MACRO_KEYWORDS + TECHNICAL_KEYWORDS):
            role_ids.append("market_structure")
        if matches(blob, QUANT_KEYWORDS):
            role_ids.append("systematic_research_pm")
        if matches(blob, RISK_KEYWORDS):
            role_ids.append("portfolio_risk")
    if "banking" in categories:
        role_ids.append("credit_committee")
        if not banker_evidence_only:
            if matches(blob, UNDERWRITE_KEYWORDS):
                role_ids.append("deal_diligence")
            if matches(blob, CAPITAL_KEYWORDS):
                role_ids.append("capital_markets")
    for category in ("growth", "communications", "product_design", "ai", "ops"):
        if category in categories:
            role_ids.extend(CATEGORY_ROLES[category])
    if "growth" in categories:
        role_ids.append("communications")

    explicit_ids = context.get("capability_ids", [])
    if not isinstance(explicit_ids, list) or any(not isinstance(item, str) for item in explicit_ids):
        raise ValueError("capability_ids must be a list of registry IDs")
    by_id = {capability["id"]: capability for capability in registry["capabilities"]}
    unknown = set(explicit_ids) - by_id.keys()
    if unknown:
        raise ValueError(f"Unknown capability IDs: {sorted(unknown)}")
    selected = []
    for capability in registry["capabilities"]:
        explicit = capability["id"] in explicit_ids
        domain = capability.get("category")
        eligible = domain in categories or (domain == "investment" and "venture" in categories)
        if capability["kind"] in ("sector", "region") and "banking" in categories:
            eligible = True
        searchable = capability["kind"] != "execution_profile" and not capability["id"].startswith("package.")
        if explicit or (eligible and searchable and matches(blob, capability["keywords"])):
            selected.append(capability)
            # Sector/geographic lenses enrich the owner packet, not a new team.
            if capability["kind"] not in ("sector", "region") and not banker_evidence_only:
                role_ids.append(capability["execution_role"])
    if explicit_ids and not blob:
        role_ids = [capability["execution_role"] for capability in selected]
        categories = unique([capability.get("category", "ops") for capability in selected])
    for capability in selected:
        if capability["id"] not in explicit_ids:
            continue
        if capability["category"] not in categories:
            categories.append(capability["category"])
        if capability["owner"] == "investment-management":
            role_ids.insert(0, "venture_platform" if capability["execution_role"] == "venture_platform" else "cio")
        elif capability["owner"] == "universal-banker":
            role_ids.insert(0, "credit_committee")
    if "support.relationship-os-handoff" in explicit_ids:
        crm = True
        role_ids.extend(("growth", "communications"))
    if crm:
        if not any(cap["id"] == "support.relationship-os-handoff" for cap in selected):
            selected.append(by_id["support.relationship-os-handoff"])
    substantial_domains = set(categories) & {"investment", "venture", "banking", "growth", "product_design", "ai"}
    if "venture" in substantial_domains:
        substantial_domains.discard("investment")
    if banker_evidence_only:
        substantial_domains.discard("banking")
    if len(substantial_domains) > 1 or matches(blob, ("run the firm", "full firm", "staff a workforce")):
        role_ids.insert(0, "chief_of_staff")
    role_ids = unique(role_ids)
    roles = [ROLES[role_id] for role_id in role_ids]
    selected_ids = {capability["id"] for capability in selected}
    for role_id in role_ids:
        capability = by_id[f"profile.{role_id}"]
        if capability["id"] not in selected_ids:
            selected.append(capability)

    # Overlay lenses belong to the selected financial owner for this packet.
    packet_capabilities = []
    for capability in selected:
        packet = dict(capability)
        if capability["kind"] in ("sector", "region"):
            packet["registry_owner"] = capability["owner"]
            packet["registry_execution_role"] = capability["execution_role"]
            packet["owner"] = "universal-banker" if "banking" in categories and "investment" not in categories and "venture" not in categories else "investment-management"
            packet["execution_role"] = "credit_committee" if packet["owner"] == "universal-banker" else ("venture_platform" if "venture" in categories else "cio")
            packet["skills"] = [packet["owner"]]
        if banker_evidence_only and packet["category"] == "banking":
            packet["registry_execution_role"] = capability["execution_role"]
            packet["execution_role"] = "credit_committee"
        packet_capabilities.append(packet)

    role_packets = []
    for role in roles:
        caps = [capability for capability in packet_capabilities if capability["execution_role"] == role.role_id]
        role_skills = list(role.skills)
        if role.role_id == "ops_security" and any(cap["id"] == "ops.meeting-capture" for cap in caps) and not matches(blob, ("security", "incident", "threat", "vulnerability")):
            role_skills = ["agent-ops-control-plane"]
        if role.role_id == "market_structure":
            role_skills = ["investment-management"]
            if matches(blob, MACRO_KEYWORDS) or any("global-macro-theme-picker" in cap["skills"] for cap in caps if cap["kind"] != "execution_profile"):
                role_skills.append("global-macro-theme-picker")
            if matches(blob, TECHNICAL_KEYWORDS) or any("technical-analysis" in cap["skills"] for cap in caps if cap["kind"] != "execution_profile"):
                role_skills.append("technical-analysis")
        role_packets.append({
            "id": role.role_id, "title": role.title, "desk": role.desk,
            "skills": unique(role_skills + [skill for cap in caps if cap["kind"] != "execution_profile" for skill in cap["skills"]]),
            "output": role.output, "capability_ids": [cap["id"] for cap in caps],
            "references": unique([ref for cap in caps for ref in cap["references"]]),
            "tools": unique([tool for cap in caps for tool in cap["tools"]]),
        })
    skills = unique([skill for role in role_packets for skill in role["skills"]])

    decision_owners: list[str] = []
    if "investment" in categories:
        decision_owners.append("investment-management")
    if "venture" in categories:
        decision_owners.append("investment-management")
    if "banking" in categories:
        decision_owners.append("universal-banker")
    if "growth" in categories:
        decision_owners.append("growth-operating-system")
    if "communications" in categories:
        decision_owners.append("ethical-supersuader")
    for capability in packet_capabilities:
        if capability["id"] in explicit_ids:
            decision_owners.append(capability["owner"])
    if not decision_owners:
        decision_owners.append("ai-ml-research-lab" if "ai" in categories else "visual-design-operating-system" if "product_design" in categories else "agent-ops-control-plane")

    mission_owner = "chief_of_staff" if "chief_of_staff" in role_ids else "growth" if banker_evidence_only else roles[0].role_id

    return {
        "mission_owner": mission_owner,
        "categories": categories,
        "decision_owners": unique(decision_owners),
        "roles": role_packets,
        "skill_stack": skills,
        "handoff": "Mission owner reconciles specialists into the relevant decision owner packet. Relationship changes require the external Relationship OS owner receipt.",
        "registry_schema_version": registry["schema_version"],
        "capability_ids": [cap["id"] for cap in packet_capabilities],
        "capabilities": packet_capabilities,
        "resource_refs": unique([ref for role in role_packets for ref in role["references"]]),
        "external_handoffs": [registry["external_owners"]["relationship_os"]] if crm else [],
        "invocation_status": "planned_not_invoked",
        "forbidden_without_approval": [
            "trade execution",
            "loan commitment or lender submission",
            "external outreach send",
            "filing/signing/payment",
            "production deployment",
            "secret movement or disclosure",
        ],
        "stop_condition": "All assigned outputs are delivered, evidence gaps are explicit, and the decision owner can act or decline.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a mission to the financial-house workforce graph.")
    parser.add_argument("--context", help="Inline JSON context")
    parser.add_argument("--context-file", help="Path to JSON context")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    args = parser.parse_args()

    context = load_context(args.context, args.context_file)
    route = build_route(context)
    print(json.dumps(route, indent=None if args.compact else 2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
