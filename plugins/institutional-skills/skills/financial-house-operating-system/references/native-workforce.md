# Native Workforce

Ordinary requests are enough. Select the owner and relevant capability from
`capability-registry.json`; the user need not name a skill or employee.
The registry is the source for the router, org chart, roster, and native profiles.
Desk coverage is broader than the small set of execution profiles.

## Execution

1. Read the raw request and source evidence. Route by the decision being made,
   not incidental words, desired file format, or every noun in the source.
2. Do short single-owner work inline. For genuinely separable work, select only
   the required profiles, give each a bounded work packet, and invoke the host's
   native agent tool. Do not create another user task for a subtask.
3. If the host exposes only generic `spawn_agent`, use bounded role packets instead of a custom role selector.
   Pass the selected role's mandate, skills, references, allowed tools, output,
   checks, and stop condition in that native spawn message. Record its returned
   id. Do not claim that a named TOML was invoked when only this fallback ran.
4. Validate the artifact and have the domain owner accept it. A work plan,
   agent's self-report, or file's existence is not proof of task completion.
5. For interrupted work, inspect the existing native id and pending owner receipt
   before redispatch. CRM work retains the same packet/run identity. Relationship
   OS remains the identity, suppression, eligibility, and committed-graph owner.

## Local State

`scripts/workforce_runtime.py` is a small journal, not a scheduler, CRM, or
trading database. Use `init`, `record`, and `resume` with an explicit `--state`
file in the owning project's private working directory. Never put live client
packets or outcomes in the distributed skills library.

Supported events: `assigned`, `completed`, `failed`, `owner_decision`, `handoff`,
`handoff_receipt`, `outcome`, `lesson_candidate`. Every event has a unique
`event_id`; `expected_revision` prevents stale writes. Replays are idempotent.
State is written atomically with owner-only permissions. Receipts preserve
source/artifact hashes, actual native ids, validation commands, and owner run ids.

`completed` needs `artifact_paths`, `skill_read_paths`, and `validations`
(`command`, `exit_code`, `receipt_path`). A handoff receipt also needs the matching
`runId` and a passing domain validator. The generic journal never invents the
meaning of a CRM acceptance, delivery, trade, or performance metric.

## Learning

An observed outcome points to evidence in its owning system. A candidate lesson
links that outcome, baseline, challenger, evaluation, and canonical owner.
The existing Skill Intelligence cycle reviews these candidates. Promote only a
tested, source-backed improvement within current authority. Financial formulas,
risk/credit policy, production behavior, and ownership remain unchanged without
explicit approval. No outcome means no claimed learning; zero promotion is valid.

## Model And Discovery

Profiles inherit the caller's model, reasoning, sandbox and tools. Preserve recipient manual settings; no model or service tier is forced by this package.

Optional TOMLs are under the plugin's agents/ directory. Install them using the public install.py --agents-dir option on compatible hosts. The plugin supplies skills through the supported marketplace install. A fresh task must demonstrate discovery and actual execution; file copies alone do not prove either. Workspace/cloud installation is separate.

## Official Basis

Accessed 2026-09-05:

- [Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents):
  standalone TOMLs, inherited configuration, bounded delegation.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): progressive loading,
  standalone local discovery, plugin distribution to supported products.
- [GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra):
  clear instruction hierarchy, proportional tools and delegation, measured evals.
