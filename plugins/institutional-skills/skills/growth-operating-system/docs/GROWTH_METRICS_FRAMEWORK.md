# Growth Metrics Framework

## Metric Hierarchy

### Business Metrics

- revenue
- gross profit
- qualified pipeline
- net revenue retention
- expansion revenue
- contribution margin

### Acquisition Metrics

- CAC
- CAC payback
- cost per qualified lead
- cost per sales accepted opportunity
- channel conversion rate
- pipeline per dollar

### Conversion Metrics

- landing page conversion
- lead-to-MQL
- MQL-to-SQL
- SQL-to-opportunity
- opportunity-to-close
- no-show rate
- sales cycle length

### Retention Metrics

- cohort retention
- churn
- renewal rate
- activation
- repeat purchase
- product-qualified expansion

### Referral Metrics

- referral invite rate
- referral acceptance rate
- referral conversion
- viral coefficient
- partner-sourced pipeline
- fraud/low-quality referral rate

## Core Equations

```text
LTV = Gross Margin per Customer x Average Customer Lifetime
CAC Payback = CAC / Monthly Gross Profit per Customer
Growth Efficiency = Net New ARR / Sales and Marketing Spend
Qualified Pipeline Efficiency = Sales Accepted Pipeline / Demand Spend
Expected Value per Lead = P(close) x Gross Profit - Acquisition Cost
Viral Coefficient = Invites per Customer x Invite Conversion Rate
```

## Experiment Standard

Every test must define:

- hypothesis
- segment
- metric
- baseline
- minimum detectable effect when possible
- sample caveats
- decision rule
- duration
- owner
- kill switch

## Kill Switches

Stop or roll back when:

- CAC payback exceeds mandate
- qualified rate collapses
- unsubscribe/spam/complaint rates breach limits
- conversion lift is not material after enough signal
- sales feedback shows poor-fit leads
- claims are unsupported
- brand/trust damage appears
- legal/compliance risk is unresolved

## Causal Discipline

Do not treat correlation as proof. Prefer:

- randomized A/B tests
- geo or time-based holdouts
- cohort comparisons
- pre/post with explicit confounders
- source-of-truth CRM reconciliation
- confidence intervals or bootstrap intervals when sample size permits
