# Institutional Workforce

Reusable skills and bounded employees for investment management, banking, growth,
communications, research, design and operations. Two financial decision owners:
`investment-management` and `universal-banker`. The workforce router chooses the
smallest relevant team; 14 profiles cover the complete capability registry.

## Install And Run

Python 3.11+ on macOS/Linux, no paid API calls or third-party dependencies:

```bash
python3 install.py --target "$HOME/institutional-skills"
python3 -B examples/run_demo.py --output /tmp/workforce-demo
python3 -B -m unittest discover -s tests
codex plugin marketplace add "$PWD"
codex plugin add institutional-skills@institutional-skills
```

The first command installs an isolated copy, not credentials or global aliases.
Run plugin commands from the installed directory to use that copy. Optional
`--agents-dir "$HOME/.codex/agents"` installs native custom-agent TOMLs, refusing
to overwrite different files. The plugin alone supplies skills; custom profiles
require a host that supports that agent configuration. Use one active owner copy,
not duplicate standalone and plugin skill front doors.

Ask normally: "Underwrite this financing and draft a professional partner note"
or "Research the portfolio mandate and produce a risk review." The orchestrator
reads source evidence, assigns roles through an available native agent tool (or
works inline), validates artifacts, and records actual receipts. Router output
alone is not execution. The local demo is a deterministic inline execution test,
not a claim that a model or custom agent was invoked.

## Coverage And Boundaries

The registry retains 38 desk families, 11 sectors, 10 regions, 19 investment
roles, 20 banker specialties, and adjacent specialist supports. Read the
financial-house org chart and capability-registry.json for exact mappings.
Methods and operational checklists are included; private source archives,
client records, personal writing samples and unlicensed papers are not.
SOURCE_GATES.json records every source disposition and content hash.

Copy bindings.example.json to bindings.json and supply your own approved data,
CRM contract, tools and voice samples. No broker, CRM, email, database, paid API,
or cloud integration is enabled by installation. Native editable XLS/PPT output
requires a compatible execution tool; unavailable tools must be reported.

Standalone skills/custom profiles work only on compatible local hosts. Chat/Work
web/mobile access requires importing this marketplace into a supported workspace,
installing the plugin there, and testing a fresh conversation. A GitHub checkout
or local install does not establish account-wide discovery or tool availability.

## Evidence And Learning

The demo writes a model calculation, credit memo, internal outreach draft,
assignment journal, recovery checkpoint and outcome-linked lesson candidate.
Actual jobs use the same journal with saved native dispatch/validation/owner
receipts. Evidence hashes detect changed artifacts; retry IDs are stable.
Learning candidates do not silently modify formulas, risk policy or underwriting.
No new scheduler, CRM or trading executor is created.

See UPDATE.md, PUBLIC_BUILD.json and SOURCE_GATES.json. Original donor notices
remain under the plugin's LICENSES directory; referenced publications are not
relicensed or bundled. MIT covers the authorized authored core and export code.
