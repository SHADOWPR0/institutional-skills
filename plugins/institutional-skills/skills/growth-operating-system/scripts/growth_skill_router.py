#!/usr/bin/env python3
"""Route growth requests to layers, agents, and support skill clusters."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict


@dataclass
class Route:
    layers: list[str]
    agents: list[str]
    support_clusters: list[str]
    required_outputs: list[str]
    metrics: list[str]
    guardrails: list[str]


RULES = [
    (
        "market_intelligence",
        ["icp", "segment", "competitor", "review", "pain", "objection", "market", "customer research"],
        "Market Research Agent",
        ["ICP profiles", "pain library", "objection library", "competitor map"],
        ["qualified segment count", "objection frequency", "demand score"],
    ),
    (
        "offer_engineering",
        ["offer", "pricing", "guarantee", "risk reversal", "positioning", "value prop", "hormozi"],
        "Offer Architect Agent",
        ["offer ladder", "value stack", "risk reversal", "pricing test"],
        ["conversion rate", "gross margin", "payback period"],
    ),
    (
        "persuasion_copy",
        ["copy", "landing", "ad", "email", "sms", "script", "subject line", "objection reply"],
        "Copy Chief Agent",
        ["copy variants", "campaign assets", "CTA map"],
        ["CTR", "reply rate", "conversion rate", "spam complaints"],
    ),
    (
        "funnel_engineering",
        ["funnel", "lead capture", "qualification", "nurture", "appointment", "crm", "pipeline"],
        "Funnel Engineer Agent",
        ["funnel map", "lead scoring", "routing rules", "nurture sequence"],
        ["MQL rate", "SQL rate", "show rate", "opportunity rate"],
    ),
    (
        "growth_analytics",
        ["cac", "ltv", "payback", "attribution", "cohort", "experiment", "ab test", "analytics"],
        "Analytics Agent",
        ["metric tree", "experiment plan", "readout plan"],
        ["CAC", "LTV", "payback", "confidence interval"],
    ),
    (
        "referral_network",
        ["referral", "affiliate", "partner", "network effect", "viral", "community"],
        "Referral Growth Agent",
        ["referral loop", "partner map", "incentive design"],
        ["viral coefficient", "partner pipeline", "referral conversion"],
    ),
]


SUPPORT_CLUSTERS = {
    "crm": ["crm", "hubspot", "attio", "pipedrive", "salesforce", "close", "zoho", "capsule"],
    "email_sms": ["email", "sms", "sendgrid", "postmark", "twilio", "instantly", "lemlist"],
    "seo_content": ["seo", "ahrefs", "semrush", "keyword", "backlink", "content"],
    "lead_data": ["apollo", "hunter", "phantombuster", "lead", "prospect", "enrich"],
    "analytics": ["analytics", "ga4", "simple analytics", "attribution", "cohort"],
    "creative_social": ["social", "youtube", "reddit", "twitter", "canva", "brand"],
}


def route(text: str) -> Route:
    lower = text.lower()
    layers: list[str] = []
    agents: list[str] = []
    outputs: list[str] = []
    metrics: list[str] = []

    for layer, keywords, agent, layer_outputs, layer_metrics in RULES:
        if any(k in lower for k in keywords):
            layers.append(layer)
            agents.append(agent)
            outputs.extend(layer_outputs)
            metrics.extend(layer_metrics)

    if not layers:
        layers = ["market_intelligence", "offer_engineering", "growth_analytics"]
        agents = ["Market Research Agent", "Offer Architect Agent", "Analytics Agent"]
        outputs = ["ICP profiles", "offer ladder", "metric tree"]
        metrics = ["qualified pipeline", "CAC", "LTV", "payback"]

    clusters = [
        name for name, keywords in SUPPORT_CLUSTERS.items()
        if any(re.search(r"\b" + re.escape(k) + r"\b", lower) for k in keywords)
    ]

    guardrails = [
        "do not invent proof or urgency",
        "define metric and kill switch before execution",
        "reject vanity metrics unless tied to revenue, pipeline, retention, or referrals",
        "check consent/compliance before outreach",
    ]

    return Route(
        layers=sorted(set(layers)),
        agents=sorted(set(agents)),
        support_clusters=sorted(set(clusters)),
        required_outputs=sorted(set(outputs)),
        metrics=sorted(set(metrics)),
        guardrails=guardrails,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("request", nargs="*", help="Growth request text")
    parser.add_argument("--json", action="store_true", help="Emit JSON only")
    args = parser.parse_args()
    text = " ".join(args.request).strip()
    if not text:
        text = input().strip()
    result = route(text)
    if args.json:
        print(json.dumps(asdict(result), indent=2))
    else:
        print(json.dumps(asdict(result), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
