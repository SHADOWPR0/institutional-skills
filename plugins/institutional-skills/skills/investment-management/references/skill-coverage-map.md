# Investment Skill Coverage Map

This file answers the practical question: what can the investment-management org see and call?

`investment-management` is the capital-decision owner. The packages below are globally discoverable support capabilities. They are not all loaded by default; the Portfolio Manager or CIO selects the smallest relevant stack for the decision.

## Macro Folder Decision

Keep `global-macro-theme-picker` as a separate callable package because locked consumers and fresh Codex tasks need one stable name and path. Treat it as the Macro Desk operating manual inside `investment-management`, not as a peer capital-allocation owner.

## Every Canonical Package

| Skill | Status | Desk | Investment-org relation | Required deps | Callable roles |
|---|---|---|---|---|---|
| `skill-creator` | support | Specialist Support | platform/system support; invoke only when relevant | none | as routed |
| `skill-installer` | support | Specialist Support | platform/system support; invoke only when relevant | none | as routed |
| `agent-ops-control-plane` | production owner | Executive Control | firm-level operating support | none | `chief_of_staff`, `data_ai_model_validation` |
| `ai-ml-research-lab` | production owner | Data AI and Model Validation | direct investment desk/support | none | `systematic_research_pm`, `data_ai_model_validation` |
| `atlas` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `atropos-command` | support | Executive Control | selective support | none | `chief_of_staff` |
| `beautiful-prose` | archive | Communications | firm-level operating support | `ethical-supersuader` | as routed |
| `cloudflare-deploy` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `corporate-counsel` | production owner | Fiduciary Legal and Tax | adjacent finance/legal/fiduciary support | none | `deal_underwriting_diligence`, `fiduciary_legal_tax` |
| `develop-web-game` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `doc` | support | Operations Security and Records | records, security, documentation, or operational support | none | `deal_underwriting_diligence`, `persuasive_writing_communications`, `operations_security_records` |
| `ethical-supersuader` | production owner | Communications | firm-level operating support | none | `capital_markets_lender_routing`, `growth_partnerships`, `persuasive_writing_communications` |
| `figma` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `figma-implement-design` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `financial-house-operating-system` | production owner | Executive Control | firm-level operating support | `agent-ops-control-plane` | `chief_of_staff` |
| `financial-planner` | support | Fiduciary Legal and Tax | adjacent finance/legal/fiduciary support | none | `fiduciary_legal_tax` |
| `gh-address-comments` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `gh-fix-ci` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `global-macro-theme-picker` | research-only | Investment Committee | direct investment desk/support | `investment-management` | `cio_investment_committee` |
| `growth-operating-system` | production owner | Growth and Partnerships | firm-level operating support | none | `growth_partnerships` |
| `imagegen` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `investment-management` | production owner | Investment Committee | direct investment desk/support | none | `cio_investment_committee`, `systematic_research_pm`, `portfolio_construction_risk` |
| `jupyter-notebook` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `systematic_research_pm`, `data_ai_model_validation` |
| `linear` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `netlify-deploy` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `notion-knowledge-capture` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `notion-meeting-intelligence` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `notion-research-documentation` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `notion-spec-to-implementation` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `openai-docs` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `pdf` | support | Operations Security and Records | records, security, documentation, or operational support | none | `deal_underwriting_diligence`, `persuasive_writing_communications`, `operations_security_records` |
| `playwright` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `render-deploy` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `risk-wall-ui` | parked | Specialist Support | platform/system support; invoke only when relevant | none | as routed |
| `screenshot` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `security-best-practices` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `security-bluebook-builder` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `security-ownership-map` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `security-threat-model` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `sentry` | support | Operations Security and Records | records, security, documentation, or operational support | none | `operations_security_records` |
| `sora` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `speech` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `spreadsheet` | support | Operations Security and Records | records, security, documentation, or operational support | none | `deal_underwriting_diligence`, `data_ai_model_validation`, `operations_security_records` |
| `tax-strategy` | support | Banking Credit and Capital Markets | adjacent finance/legal/fiduciary support | `universal-banker` | `fiduciary_legal_tax` |
| `technical-analysis` | support | Investment Committee | direct investment desk/support | `investment-management` | `market_structure_technical` |
| `transcribe` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `trust-officer` | support | Fiduciary Legal and Tax | adjacent finance/legal/fiduciary support | none | `fiduciary_legal_tax` |
| `universal-banker` | production owner | Banking Credit and Capital Markets | adjacent finance/legal/fiduciary support | none | `universal_banker_credit_committee`, `deal_underwriting_diligence`, `capital_markets_lender_routing` |
| `vercel-deploy` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |
| `visual-design-operating-system` | production owner | Product Engineering and Design | firm-level operating support | none | `product_engineering_design` |
| `yeet` | support | Product Engineering and Design | artifact, product, deployment, or verification support | none | `product_engineering_design` |

## Routing Rule

- Investment, portfolio, trading, sizing, macro, risk, and capital judgment starts in `investment-management`.
- Macro research uses `global-macro-theme-picker` as a child desk with no independent execution authority.
- Credit, underwriting, lending, and deal structuring route to `universal-banker`.
- AI/ML/RL method questions route to `ai-ml-research-lab` unless the final decision is a capital decision.
- Prose, growth, design, product, deployment, security, records, and platform packages are support layers selected only when they improve the actual deliverable.

## Runtime Boundary

Canonical source: `{SKILLS_ROOT}`. Global Codex runtime: `{SKILLS_ROOT}`. Drive and private Git are mirrors. Availability is global; invocation is selective.
