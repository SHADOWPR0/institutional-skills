---
name: growth-operating-system
description: Canonical growth, marketing, sales, lead-generation, CRM, outreach, funnel, conversion, referral, content, offer, positioning, and growth-analytics operating system. Use for demand generation, market intelligence, offer engineering, persuasive copy, sales systems, CRM workflows, funnel optimization, lifecycle marketing, referrals, partnerships, and compounding growth strategy.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Growth Operating System

## Quick Reference

### What It Does

Owns measurable growth strategy across market intelligence, offers, demand,
sales, CRM, conversion, retention, referrals, and partnerships.

### Entrypoints

- growth strategy, marketing, sales, CRM, funnel, conversion, or partnerships

### Inputs / Outputs

- Inputs: business model, customer evidence, economics, channel data, and constraint.
- Outputs: measurable growth decision, artifact, experiment, metric, and kill rule.

### Dependencies / Tooling

Use connector skills for execution, `ethical-supersuader` for prose quality,
`visual-design-operating-system` for presentation, and
`agent-ops-control-plane` for recurring-agent controls.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants

- Optimize qualified demand and durable economics, not vanity metrics.
- Do not launch or send without explicit authority.
- Every repeated campaign needs measurement and a stop rule.

## Purpose

This is the single canonical front door for growth work. It consolidates marketing, sales, lead generation, CRM, outreach, copywriting, funnel design, growth analytics, referral systems, and business development into one measurable operating system.

This is not a branding exercise. The objective is qualified demand, trust, conversion efficiency, retention, referrals, customer lifetime value, and compounding business growth.

## Ownership

Use this skill as decision owner when the task involves:

- market intelligence
- ICP and segmentation
- offer creation
- positioning
- direct response copy
- landing pages
- outbound and inbound campaigns
- CRM and sales pipeline operations
- nurture flows
- conversion-rate optimization
- growth analytics
- referral, affiliate, partnership, or network-effect systems

Use connector/automation skills only as execution tools after this skill defines strategy, message, metrics, and constraints.

The bundled Sales plugin can be used as a support library for account research,
meeting prep, CRM hygiene, pipeline review, call feedback, contact enrichment,
business-case packaging, and deal-strategy structure. Keep this skill as the
decision owner. Load `references/plugin-support-map.md` only when a Sales plugin
workflow improves the deliverable. Do not edit plugin-cache files or replace the
growth operating system with plugin-native routing.

Use `visual-design-operating-system` as support when a campaign, content system, landing page, deck, email, report, social asset, or other growth artifact needs visual direction, art direction, UI/UX polish, layout, or generated-media guidance. This skill remains decision owner for growth strategy and metrics.

Use `agent-ops-control-plane` as support for growth-agent swarms, campaign evals, cost/runtime budgets, CRM/outreach kill switches, context-bloat control, and continuous learning from campaign results. This skill remains decision owner for growth strategy and metrics.

For mortgage-partnerships, capital-partnerships, or relationship-workforce acceptance, load
`references/relationship-workforce.md`. Growth owns research, qualification,
offer, channel, and pipeline strategy; `ethical-supersuader` owns prose and
`universal-banker` owns financing substance. Relationship OS alone owns canonical
identity, suppression, factual dossiers, and committed CRM outcomes. Use its
existing `relationship_update.v1` contract; a staged packet is not a commit.

## Layered Architecture

1. Market Intelligence
   - ICP, segmentation, competitor map, pain mining, objection mining, demand analysis.
2. Offer Engineering
   - offer stack, pricing, risk reversal, guarantee, positioning, value communication.
3. Persuasion And Copy
   - direct response, landing pages, ads, email/SMS, sales scripts, objection replies.
4. Funnel Engineering
   - lead capture, qualification, nurture, appointment setting, conversion paths.
5. Growth Analytics
   - CAC, LTV, payback, conversion rates, attribution, cohorts, channel efficiency.
6. Referral And Network Effects
   - referral loops, partner systems, affiliates, virality, community/network amplification.

## Multiplicative Growth Rule

Prefer systems that compound:

- retention before acquisition scale
- LTV/CAC before raw lead volume
- qualified pipeline before vanity engagement
- referral loops before one-off campaigns
- cohort improvement before top-line claims
- measured experiments before opinion

Every substantive plan should state the growth equation it improves.

## Agent Roles

- Market Research Agent: ICP, competitor, review, customer, and objection mining.
- Offer Architect Agent: offer ladder, value stack, risk reversal, pricing tests.
- Copy Chief Agent: messaging, copy, scripts, emails, ads, landing pages.
- Funnel Engineer Agent: lead capture, qualification, nurture, routing, conversion.
- Analytics Agent: metrics, cohorts, attribution, experiment design, causal checks.
- Referral Growth Agent: referral, affiliate, partnership, and network loops.
- CRO Agent: landing page tests, funnel friction, objections, forms, calls-to-action.

## Workflow

1. Define business model, customer, economics, and current bottleneck.
2. Select the layer that owns the bottleneck.
3. Inventory sources: customer calls, CRM, site analytics, ad data, email/SMS data, sales notes, reviews, competitors, landing pages, and market research.
4. Separate facts, customer language, assumptions, and creative judgment.
5. Build one measurable growth artifact.
6. Define experiment, metric, threshold, duration, and kill switch.
7. Hand off execution to connector skills only after the strategy is measurable.
8. Log results and update the playbook.

When a campaign or growth agent will run repeatedly, add an agent-ops ledger entry: hypothesis, baseline, variant, cost, conversion metric, failure mode, patch, retest, and promote / iterate / retire decision.

## Output Contracts

Market intelligence:

- ICP segments, pains, objections, triggers, alternatives, buying committee, qualification rules.

Offer:

- promise, audience, mechanism, value stack, proof, guarantee/risk reversal, price, constraints.

Copy/campaign:

- audience, message, offer, proof, CTA, variants, channel fit, compliance notes, success metric.

Funnel:

- journey map, stages, conversion events, owner, tooling, lead scoring, routing, nurture, SLA.

Analytics:

- metric tree, baseline, target, experiment design, sample caveats, readout plan, kill criteria.

Referral:

- loop trigger, incentive, invite moment, recipient value, fraud controls, loop metric, compounding logic.

## Guardrails

- Do not invent traction, scarcity, testimonials, customer proof, or urgency.
- Do not optimize for vanity metrics.
- Do not scale a campaign without CAC/LTV/payback or qualified-pipeline logic.
- Do not use manipulative copy, dark patterns, fake consensus, or misleading guarantees.
- Do not let connector availability determine strategy.
- Do not run regulated outreach without consent/compliance checks.

## References

- `docs/GROWTH_SYSTEM_AUDIT.md`
- `docs/GROWTH_SKILL_CONSOLIDATION_REPORT.md`
- `docs/GROWTH_ARCHITECTURE.md`
- `docs/DEPRECATED_GROWTH_SKILLS.md`
- `docs/GROWTH_AGENT_HANDOFFS.md`
- `docs/GROWTH_METRICS_FRAMEWORK.md`
- `references/plugin-support-map.md`

## Scripts

- `scripts/growth_skill_audit.py` (not bundled; recipient resource required)
- `scripts/growth_skill_router.py`
