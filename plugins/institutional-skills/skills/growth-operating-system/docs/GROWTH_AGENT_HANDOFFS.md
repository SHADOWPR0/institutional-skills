# Growth Agent Handoffs

## Universal Handoff Fields

- objective
- layer
- owner agent
- source paths
- customer segment
- offer
- constraints
- assumptions
- metric target
- evidence
- output format
- deadline
- kill switch

## Agents

### Market Research Agent

Inputs: business description, customer data, reviews, competitors, CRM notes, sales calls, search/social data.

Outputs: ICPs, pains, objections, buying triggers, competitor map, demand map.

Handoff to: Offer Architect, Copy Chief, Analytics Agent.

### Offer Architect Agent

Inputs: ICP, pains, alternatives, willingness-to-pay, proof, constraints.

Outputs: offer stack, guarantee/risk reversal, price test, value map.

Handoff to: Copy Chief, Funnel Engineer, Analytics Agent.

### Copy Chief Agent

Inputs: ICP, offer, proof, objections, channel, compliance limits.

Outputs: copy variants, landing page sections, emails, SMS, scripts, ads.

Handoff to: Funnel Engineer, CRO Agent.

### Funnel Engineer Agent

Inputs: offer, copy, traffic source, CRM, qualification criteria, sales process.

Outputs: funnel map, lead capture, lead scoring, routing, nurture, appointment path, SLA.

Handoff to: Analytics Agent, Sales/CRM connector skills.

### Analytics Agent

Inputs: event data, CRM, spend, revenue, cohorts, experiments.

Outputs: metric tree, baseline, experiment design, readout, causal caveats, kill/scale decision.

Handoff to: all agents.

### Referral Growth Agent

Inputs: customer success moments, NPS/reviews, partner map, incentives, fraud constraints.

Outputs: referral loop, partner loop, invite timing, incentive economics, loop metric.

Handoff to: Funnel Engineer, Analytics Agent.

### CRO Agent

Inputs: page/funnel data, heatmaps, form analytics, recordings, conversion rates, objections.

Outputs: friction map, test backlog, page variants, prioritization.

Handoff to: Copy Chief, Funnel Engineer, Analytics Agent.

## Mail/Beads/CASS Pattern

When MCP Agent Mail and Beads are available:

1. Create a Beads issue for each workstream.
2. Use the Beads issue ID as the Agent Mail thread ID.
3. Reserve files before editing.
4. Post artifacts and metrics into the thread.
5. Sync Beads JSONL before git or Drive sync.
6. Use CASS to retrieve prior campaign lessons before major strategy changes.
