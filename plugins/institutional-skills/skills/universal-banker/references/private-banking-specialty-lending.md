# Private Banking and Specialty Lending Playbook

Framework for collateral-led loans outside plain-vanilla bank credit.

## 1) Product Coverage

- securities-backed lines (Lombard, margin-secured private lines)
- crypto-backed loans (spot collateral and staked-asset variants)
- hard money real-estate bridge loans
- merchant cash advance (MCA) and revenue-based financing
- bespoke UHNW short-term bridge loans
- yacht and private aircraft secured facilities (loan or lease-style economics)

## 2) Core Formulas

- **LTV** = Loan Balance / Collateral Value
- **Advance Rate** = Maximum Loan / Eligible Collateral Value
- **Borrowing Base** = Sum(Eligible Collateral_i * Advance Rate_i)
- **Excess Collateral Ratio** = Eligible Collateral Value / Loan Balance
- **MCA Effective APR (approx.)**:
  - APR ≈ ((Factor Rate - 1) * Advance) / (Average Outstanding Balance * Term in Years)
- **Liquidation Coverage** = Net Liquidation Proceeds / Loan Balance
- **Margin Call Buffer** = (Current Collateral Value - Maintenance Requirement) / Loan Balance

## 3) Metric Bands (Policy Defaults, Not Law)

### Securities-Backed Lines
- base advance rates:
  - cash/T-bills: 90-98%
  - large-cap index ETFs: 60-75%
  - single-name liquid equities: 40-60%
  - concentrated/small-cap: 20-40%
- margin maintenance trigger: typically 5-15% above minimum collateral requirement
- single-name concentration cap: typically 10-25% of collateral pool

### Crypto-Backed Loans
- conservative starting advance:
  - BTC/ETH majors: 25-50%
  - altcoins: 0-30% (or ineligible)
- liquidation trigger often set near 70-85% collateral utilization by product design
- intraday monitoring cadence required due to volatility clustering

### Hard Money Bridge (Real Estate)
- as-is LTV often targeted: <= 60-70%
- as-complete LTARV/LTV often targeted: <= 65-75%
- LTC guardrail often targeted: <= 80-90%
- minimum debt-service or interest-reserve coverage required before close

### Merchant Cash Advance
- remittance as % of daily card/sales flow often set to preserve borrower operating capacity
- loss trigger: sustained remittance shortfall plus sales trend deterioration
- require transparent effective-cost disclosure and state-level legal review

### Yacht and Private Aircraft Lending
- conservative LTV guardrails based on age, condition, and resale depth
- require independent appraisal plus broker/liquidation cross-check
- maintenance reserve and insurance covenant package is mandatory
- tighten tenor as asset age and obsolescence risk increase

## 4) Structure and Controls

- daily/near-real-time collateral valuation for fast-moving assets
- contractual right to margin call and liquidate without delay
- concentration and wrong-way-risk caps
- jurisdiction-specific usury, disclosure, and collection compliance checks
- operational controls: dual authorization for liquidations and exception handling

## 5) Stress Tests

- gap-down collateral shocks (single-day and multi-day)
- liquidity haircut expansion under stressed volumes
- correlated borrower + collateral stress (wrong-way risk)
- operational outage stress: exchange/custodian/broker downtime

## 6) Red Flags and Auto-Decline Conditions

- unverifiable collateral ownership/perfection
- concentrated collateral with no executable unwind path
- borrower cash-flow that only works under refinance assumption
- pricing/fee terms likely non-compliant in jurisdiction
- unlicensed/predatory lending patterns (loan-sharking behavior)

## 7) Monitoring

- mark-to-market and maintenance headroom dashboard
- collateral concentration and liquidity score trend
- exception queue aging and margin-call response time
- realized liquidation slippage vs modeled liquidation value
