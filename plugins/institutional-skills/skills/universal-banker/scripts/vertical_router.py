#!/usr/bin/env python3
"""
Route a banking/underwriting context to lead vertical and specialist sub-agent lanes.

Examples:
  python scripts/vertical_router.py --context '{"deal_type":"rmbs","asset_class":"resi_mortgage","mandate_side":"arrange","size_bucket":"large","complexity":"high"}'
  python scripts/vertical_router.py --context-file deal.json --top 5
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Lane:
    name: str
    deal_types: tuple[str, ...]
    asset_classes: tuple[str, ...]
    mandate_sides: tuple[str, ...]
    keywords: tuple[str, ...]
    notes: str
    mandatory: bool = False


LANES: tuple[Lane, ...] = (
    Lane(
        name="Capital Markets Underwriter",
        deal_types=(
            "ipo",
            "follow_on",
            "ig_bond",
            "hy_bond",
            "leveraged_loan",
            "convertible",
            "preferred",
            "structured_note",
        ),
        asset_classes=("equity", "corporate_credit", "leveraged_finance", "public_markets"),
        mandate_sides=("originate", "arrange", "syndicate", "invest"),
        keywords=("bookbuild", "ecm", "dcm", "distribution", "flex", "stabilization"),
        notes="Leads ECM/DCM/LF underwriting and distribution risk.",
    ),
    Lane(
        name="Mortgage Underwriter",
        deal_types=("resi_mortgage", "non_qm", "jumbo", "rmbs", "dscr_mortgage"),
        asset_classes=("resi_mortgage",),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=("borrower", "ltv", "dti", "servicer", "appraisal"),
        notes="Covers borrower-level mortgage and collateral quality.",
    ),
    Lane(
        name="CRE Underwriter",
        deal_types=("cre_loan", "sasb", "cmbs", "construction_loan", "bridge_loan"),
        asset_classes=("cre",),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=("noi", "lease", "debt_yield", "tenant", "cap_rate"),
        notes="Underwrites property cash flows, sponsor support, and structure.",
    ),
    Lane(
        name="C&I Credit Officer",
        deal_types=("ci_revolver", "ci_term_loan", "abl", "sbl"),
        asset_classes=("corporate_lending", "sbl"),
        mandate_sides=("originate", "invest"),
        keywords=("ebitda", "working_capital", "borrowing_base", "guarantor"),
        notes="Handles regional/community-bank style commercial underwriting.",
    ),
    Lane(
        name="Asset & Equipment Finance Underwriter",
        deal_types=(
            "equipment_term_loan",
            "equipment_lease",
            "finance_lease",
            "operating_lease",
            "sale_leaseback",
            "aircraft_finance",
            "aircraft_lease",
            "truck_fleet_finance",
            "marine_asset_finance",
            "yacht_finance",
            "private_jet_finance",
        ),
        asset_classes=("equipment_finance", "leasing", "aircraft", "transport_assets"),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=(
            "lease_rate_factor",
            "residual_value",
            "utilization",
            "maintenance_reserve",
            "repossession",
            "remarketing",
        ),
        notes="Underwrites equipment, aircraft, fleet, and lease structures with residual-value controls.",
    ),
    Lane(
        name="Private Banking & Specialty Lending Underwriter",
        deal_types=(
            "private_sbl",
            "lombard_line",
            "crypto_backed_loan",
            "hard_money_loan",
            "merchant_cash_advance",
            "revenue_based_advance",
            "private_bridge_loan",
        ),
        asset_classes=("private_banking", "specialty_lending", "crypto_collateral"),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=(
            "margin_call",
            "haircut",
            "factor_rate",
            "ltc",
            "liquidation",
            "collateral",
        ),
        notes="Leads collateral-led specialty lending including SBL, crypto-backed, hard money, and MCA.",
    ),
    Lane(
        name="M&A and Corporate Advisory Lead",
        deal_types=(
            "ma_buy_side",
            "ma_sell_side",
            "merger",
            "carve_out",
            "spin_off",
            "fairness_opinion",
            "strategic_review",
        ),
        asset_classes=("m_and_a", "corporate_advisory"),
        mandate_sides=("advise", "arrange", "originate", "invest"),
        keywords=("synergy", "accretion", "dilution", "integration", "valuation", "antitrust"),
        notes="Leads transaction process design, valuation discipline, and closing-risk management.",
    ),
    Lane(
        name="Industry Vertical Specialist",
        deal_types=("any",),
        asset_classes=("any",),
        mandate_sides=("advise", "originate", "arrange", "syndicate", "invest", "market_make"),
        keywords=(
            "healthcare",
            "technology",
            "energy",
            "industrials",
            "consumer",
            "telecom",
            "financials",
        ),
        notes="Applies sector-specific assumptions and downside drivers across all deal types.",
    ),
    Lane(
        name="Treasury & Payments Strategist",
        deal_types=(
            "treasury_risk_program",
            "alm_optimization",
            "payments_program",
            "working_capital_program",
            "fx_hedging_program",
        ),
        asset_classes=("treasury", "payments", "liquidity_management"),
        mandate_sides=("advise", "arrange", "originate", "invest"),
        keywords=("cash_pooling", "payment_rails", "chargeback", "fraud", "duration_gap", "hedge_ratio"),
        notes="Designs liquidity, funding, payment-rail, and hedge policy frameworks.",
    ),
    Lane(
        name="Insurance & Risk Transfer Specialist",
        deal_types=("insurance_program", "captive_program", "reinsurance_program", "ils_program"),
        asset_classes=("insurance", "risk_transfer"),
        mandate_sides=("advise", "arrange", "originate", "invest"),
        keywords=("loss_ratio", "combined_ratio", "reserve", "cat_model", "retention", "treaty"),
        notes="Designs insurance and reinsurance structures and transfer efficiency controls.",
    ),
    Lane(
        name="Asset Management and Portfolio Strategy Lead",
        deal_types=("portfolio_mandate", "asset_allocation_program", "risk_budget_program", "manager_selection"),
        asset_classes=("asset_management", "multi_asset"),
        mandate_sides=("advise", "invest"),
        keywords=("sharpe", "tracking_error", "drawdown", "risk_budget", "attribution", "ips"),
        notes="Leads portfolio construction, risk budget governance, and manager/factor oversight.",
    ),
    Lane(
        name="Securitization Engineer",
        deal_types=("rmbs", "cmbs", "abs", "clo"),
        asset_classes=("structured_credit",),
        mandate_sides=("arrange", "syndicate", "invest"),
        keywords=("waterfall", "tranche", "oc", "ic", "enhancement", "warehouse"),
        notes="Designs waterfalls, triggers, and tranche structures.",
    ),
    Lane(
        name="Syndication Lead",
        deal_types=(
            "rmbs",
            "cmbs",
            "abs",
            "clo",
            "leveraged_loan",
            "hy_bond",
            "ig_bond",
            "ipo",
            "follow_on",
        ),
        asset_classes=("structured_credit", "corporate_credit", "leveraged_finance"),
        mandate_sides=("arrange", "syndicate"),
        keywords=("placement", "book", "anchor", "investor", "takeout"),
        notes="Owns distribution strategy and market-clearing execution.",
    ),
    Lane(
        name="Private Credit/PE Underwriter",
        deal_types=("unitranche", "mezzanine", "lbo_financing", "nav_lending", "specialty_finance"),
        asset_classes=("private_credit", "private_equity"),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=("sponsor", "lbo", "value_creation", "covenant", "exit"),
        notes="Underwrites sponsor-backed deals and private capital structures.",
    ),
    Lane(
        name="Project & Real Assets Underwriter",
        deal_types=(
            "project_finance",
            "infrastructure_finance",
            "aviation_finance",
            "shipping_finance",
            "trade_finance",
            "commodity_finance",
        ),
        asset_classes=("project_finance", "real_assets", "trade_finance"),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=("offtake", "construction", "residual_value", "utilization", "llcr", "dsra"),
        notes="Covers project cash-flow reliability, completion risk, and real-asset downside.",
    ),
    Lane(
        name="Public Finance Specialist",
        deal_types=("municipal_bond", "revenue_bond", "go_bond", "public_authority_finance"),
        asset_classes=("public_finance",),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=("tax_base", "intercept", "authority", "appropriation", "essentiality"),
        notes="Underwrites municipal and public-credit legal/revenue structures.",
    ),
    Lane(
        name="Microfinance Specialist",
        deal_types=("microloan", "group_microloan", "mfi_facility", "village_banking"),
        asset_classes=("microfinance",),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=("par30", "par90", "collection", "cohort", "field_ops"),
        notes="Underwrites micro-borrower and MFI portfolio exposures with conduct controls.",
    ),
    Lane(
        name="Esoteric/Structured Collateral Specialist",
        deal_types=(
            "royalty_finance",
            "litigation_finance",
            "carbon_credit_finance",
            "ip_finance",
            "insurance_linked_structure",
        ),
        asset_classes=("esoteric", "fringe_collateral"),
        mandate_sides=("originate", "arrange", "invest"),
        keywords=("scarce_data", "model_risk", "enforceability", "correlation", "concentration"),
        notes="Underwrites data-sparse or non-standard collateral with conservative controls.",
    ),
    Lane(
        name="Market Making Risk Lead",
        deal_types=("market_making_program", "liquidity_provision", "crypto_mm", "etf_mm"),
        asset_classes=("market_making", "crypto"),
        mandate_sides=("invest", "market_make"),
        keywords=("inventory", "toxicity", "latency", "quote", "hedge"),
        notes="Controls inventory/toxicity/latency risk in quoting businesses.",
    ),
    Lane(
        name="Enterprise Risk Governor",
        deal_types=("any",),
        asset_classes=("any",),
        mandate_sides=("advise", "originate", "arrange", "syndicate", "invest", "market_make"),
        keywords=("stress", "governance", "limits", "concentration"),
        notes="Independent risk gate; mandatory in all material transactions.",
        mandatory=True,
    ),
)


REQUIRED_FIELDS = ("deal_type", "asset_class", "mandate_side")
PROHIBITED_PATTERNS = (
    "loan_sharking",
    "loan sharking",
    "unlicensed lending",
    "extortionate lending",
    "predatory collection",
)


def _load_context(args: argparse.Namespace) -> dict[str, Any]:
    if args.context and args.context_file:
        raise ValueError("Use either --context or --context-file, not both.")
    if args.context_file:
        text = Path(args.context_file).expanduser().resolve().read_text(encoding="utf-8")
        return json.loads(text)
    if args.context:
        return json.loads(args.context)
    raise ValueError("Provide --context or --context-file.")


def _validate(ctx: dict[str, Any]) -> list[str]:
    return [f for f in REQUIRED_FIELDS if not str(ctx.get(f, "")).strip()]


def _text_blob(ctx: dict[str, Any]) -> str:
    keys = ("deal_type", "asset_class", "mandate_side", "goal", "notes", "collateral")
    return " ".join(str(ctx.get(k, "")).strip().lower() for k in keys if str(ctx.get(k, "")).strip())


def _prohibited_hits(text_blob: str) -> list[str]:
    return [p for p in PROHIBITED_PATTERNS if p in text_blob]


def _keyword_hits(keywords: tuple[str, ...], text_blob: str) -> list[str]:
    token_set = set(re.findall(r"[a-z0-9_]+", text_blob))
    hits: list[str] = []
    for kw in keywords:
        kw_norm = kw.lower().strip()
        if not kw_norm:
            continue
        if " " in kw_norm:
            if kw_norm in text_blob:
                hits.append(kw)
            continue
        if kw_norm in token_set:
            hits.append(kw)
    return hits


def _score(lane: Lane, ctx: dict[str, Any]) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    deal_type = str(ctx.get("deal_type", "")).strip().lower()
    asset_class = str(ctx.get("asset_class", "")).strip().lower()
    mandate_side = str(ctx.get("mandate_side", "")).strip().lower()
    complexity = str(ctx.get("complexity", "normal")).strip().lower()
    text_blob = _text_blob(ctx)

    if "any" in lane.deal_types or deal_type in lane.deal_types:
        if lane.deal_types == ("any",):
            score += 1
            reasons.append("generic deal scope")
        else:
            score += 5
            reasons.append("deal type match")
    if "any" in lane.asset_classes or asset_class in lane.asset_classes:
        if lane.asset_classes == ("any",):
            score += 1
            reasons.append("generic asset scope")
        else:
            score += 4
            reasons.append("asset class match")
    if mandate_side in lane.mandate_sides:
        score += 3
        reasons.append("mandate side match")

    keyword_hits = _keyword_hits(lane.keywords, text_blob)
    if keyword_hits:
        score += min(3, len(keyword_hits))
        reasons.append(f"keyword hits: {', '.join(keyword_hits[:3])}")

    if complexity == "high":
        if lane.name in {
            "Securitization Engineer",
            "Syndication Lead",
            "Enterprise Risk Governor",
            "Esoteric/Structured Collateral Specialist",
            "Private Banking & Specialty Lending Underwriter",
            "M&A and Corporate Advisory Lead",
            "Treasury & Payments Strategist",
            "Insurance & Risk Transfer Specialist",
            "Asset Management and Portfolio Strategy Lead",
        }:
            score += 2
            reasons.append("high complexity boost")
    elif complexity == "elevated":
        if lane.name in {"Enterprise Risk Governor", "Syndication Lead"}:
            score += 1
            reasons.append("elevated complexity boost")

    return score, reasons


DELIVERABLES: dict[str, str] = {
    "Capital Markets Underwriter": "Market-read memo with launch conditions, price/flex bands, and hold-risk plan.",
    "Mortgage Underwriter": "Borrower/collateral memo with LTV/DTI/DSCR stress and reps/warrants risk.",
    "CRE Underwriter": "NOI durability memo with tenant rollover, capex, DSCR/debt-yield, and sponsor support.",
    "C&I Credit Officer": "Cash-flow and covenant package with borrowing-base controls and downgrade triggers.",
    "Asset & Equipment Finance Underwriter": "Asset-value and lease-structure memo with residual stress and repossession controls.",
    "Private Banking & Specialty Lending Underwriter": "Collateral-led lending memo with advance rates, margin calls, liquidation controls, and legal checks.",
    "M&A and Corporate Advisory Lead": "Process + valuation memo with synergy quality, integration risk, and financing certainty.",
    "Industry Vertical Specialist": "Sector-adjusted assumptions memo with KPI sensitivities and downside drivers.",
    "Treasury & Payments Strategist": "Liquidity/funding and payment-control memo with hedge and contingency policy.",
    "Insurance & Risk Transfer Specialist": "Coverage/reserve and transfer-efficiency memo with counterparty and tail-risk controls.",
    "Asset Management and Portfolio Strategy Lead": "Portfolio construction memo with risk-budget, drawdown controls, and attribution plan.",
    "Securitization Engineer": "Waterfall + trigger design note with tranche stress outcomes and reserve mechanics.",
    "Syndication Lead": "Distribution strategy with investor map, fallback pricing, and execution timeline.",
    "Private Credit/PE Underwriter": "Downside sponsor/capital-structure memo with control rights and exit risks.",
    "Project & Real Assets Underwriter": "Completion/offtake/residual-value memo with contingency structure.",
    "Public Finance Specialist": "Revenue/legal-priority memo with policy shock and reserve-intercept stress.",
    "Microfinance Specialist": "Portfolio-quality memo with PAR trends, collection behavior, and conduct-risk controls.",
    "Esoteric/Structured Collateral Specialist": "Data-credibility and enforceability memo with concentration controls.",
    "Market Making Risk Lead": "Quote/inventory framework with toxicity limits, hedge policy, and kill-switches.",
    "Enterprise Risk Governor": "Independent challenge note with concentration, liquidity, and failure-trigger gates.",
}


def _brief_for(lane_name: str, ctx: dict[str, Any]) -> dict[str, Any]:
    return {
        "specialist": lane_name,
        "scope": f"Analyze {ctx['deal_type']} in {ctx['asset_class']} context.",
        "deliverable": DELIVERABLES.get(
            lane_name,
            "One-page memo: thesis, structure risks, pricing/terms recommendation, red flags.",
        ),
        "hard_constraints": [
            "No unstated assumptions.",
            "Stress downside explicitly.",
            "Name decline/restructure triggers.",
            "Separate model output from judgment.",
        ],
    }


def route(ctx: dict[str, Any], top_n: int) -> dict[str, Any]:
    text_blob = _text_blob(ctx)
    blocked = _prohibited_hits(text_blob)
    if blocked:
        lead = "Enterprise Risk Governor"
        briefs = [
            _brief_for(lead, ctx),
            {
                "specialist": "Legal/Compliance Specialist",
                "scope": "Assess jurisdictional legality and consumer-protection risk.",
                "deliverable": "Decline or lawful restructuring path memo.",
                "hard_constraints": [
                    "No illegal structure recommendations.",
                    "Document jurisdiction-specific risks and prohibitions.",
                ],
            },
        ]
        return {
            "context": ctx,
            "compliance_block": True,
            "block_reasons": blocked,
            "lead_lane": lead,
            "support_lanes": ["Legal/Compliance Specialist"],
            "selected_lanes": [
                {
                    "lane": lead,
                    "score": 999,
                    "reasons": ["compliance block"],
                    "notes": "Mandatory risk gate triggered by prohibited lending pattern.",
                    "mandatory": True,
                }
            ],
            "subagent_briefs": briefs,
            "decision": "Decline illegal/predatory structure and propose lawful alternatives only.",
        }

    ranked: list[dict[str, Any]] = []
    for lane in LANES:
        score, reasons = _score(lane, ctx)
        ranked.append(
            {
                "lane": lane.name,
                "score": score,
                "reasons": reasons,
                "notes": lane.notes,
                "mandatory": lane.mandatory,
            }
        )

    ranked.sort(key=lambda x: x["score"], reverse=True)
    selected = ranked[: max(1, top_n)]

    # Ensure mandatory lanes are always present.
    selected_lanes = {item["lane"] for item in selected}
    for item in ranked:
        if item["mandatory"] and item["lane"] not in selected_lanes:
            selected.append(item)
            selected_lanes.add(item["lane"])

    # Build sub-agent briefs
    briefs = []
    for item in selected:
        briefs.append(_brief_for(item["lane"], ctx))

    lead = selected[0]["lane"]
    support = [item["lane"] for item in selected[1:]]

    return {
        "context": ctx,
        "lead_lane": lead,
        "support_lanes": support,
        "selected_lanes": selected,
        "subagent_briefs": briefs,
        "decision": "Assign lead lane ownership, run mandatory support lanes in parallel, and reconcile in IC memo.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Universal banker vertical router.")
    parser.add_argument("--context", help="Inline JSON context")
    parser.add_argument("--context-file", help="Path to JSON context")
    parser.add_argument("--top", type=int, default=4, help="Number of lanes to return")
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Emit compact JSON output",
    )
    args = parser.parse_args()

    try:
        ctx = _load_context(args)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"context_load_failed: {exc}"}))
        return 2

    missing = _validate(ctx)
    if missing:
        print(json.dumps({"ok": False, "error": f"missing_fields: {missing}"}))
        return 2

    result = route(ctx, top_n=max(1, args.top))
    if args.compact:
        print(json.dumps({"ok": True, **result}))
    else:
        print(json.dumps({"ok": True, **result}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
