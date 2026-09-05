# Technical Analysis

Canonical local support skill for professional technical analysis, CMT-style synthesis, causal strategy research, and replay-ready technical-analyst agents.

It combines:

- broad technical-analysis doctrine;
- explicit evidence grading and no-look-ahead controls;
- the distilled findings of `{RECIPIENT_RESOURCE}`;
- one typed proposal contract suitable for historical replay and live shadow evaluation.

It does not grant trade authority and does not represent that an AI agent holds a CMT charter.

## Canonical Location

`{SKILLS_ROOT}/technical-analysis`

Mirrors are synchronized to:

- `{SKILLS_ROOT}/technical-analysis`
- `{RECIPIENT_RESOURCE}`

## Validation

```bash
python3 scripts/validate_analysis_packet.py examples/technical_analysis_packet.json
python3 -m unittest discover -s tests -p 'test_*.py'
```
