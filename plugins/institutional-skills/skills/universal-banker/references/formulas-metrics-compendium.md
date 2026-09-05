# Formulas and Metrics Compendium

Reusable quantitative toolkit across credit, underwriting, securitization, market making, and portfolio governance.

## 1) Credit and Cash-Flow Coverage

- **Leverage (Net Debt / EBITDA)** = (Total Debt - Cash) / EBITDA
- **Interest Coverage** = EBITDA / Cash Interest Expense
- **Fixed Charge Coverage (FCCR)** = (EBITDA - Capex - Cash Taxes) / (Interest + Scheduled Principal + Fixed Charges)
- **DSCR** = Cash Flow Available for Debt Service / Debt Service
- **Debt Yield (CRE)** = NOI / Loan Balance

## 2) Collateral and Structure

- **LTV** = Loan Balance / Collateral Value
- **LTC** = Loan Amount / Total Project Cost
- **Haircut** = 1 - Advance Rate
- **Borrowing Base** = Sum(Eligible Collateral_i * Advance Rate_i) - Reserves
- **Liquidation Coverage** = Net Liquidation Value / Outstanding Exposure

## 3) Pricing and Risk-Adjusted Return

- **Expected Loss (EL)** = PD * LGD * EAD
- **Unexpected Loss Proxy** = Stress Loss - EL
- **RAROC** = (Risk-Adjusted Return) / Economic Capital
- **Risk-Adjusted Return (simple)** = (Spread + Fees - EL - Funding Cost - OpEx) / Exposure
- **Breakeven Spread** = Funding Cost + EL + Target Return + OpEx - Fee Offset

## 4) Project and Infrastructure

- **LLCR** = NPV(Project Cash Flows Available for Debt Service) / Outstanding Debt
- **PLCR** = NPV(Project-Life CFADS) / Outstanding Debt
- **DSRA Coverage** = Debt Service Reserve Balance / Next Debt Service
- **Completion Buffer** = (Committed Sources - Remaining Uses) / Remaining Uses

## 5) Securitization and Structured Credit

- **Credit Enhancement (%)** = (Subordination + Reserve + Excess Spread Support) / Pool Balance
- **OC Ratio** = Collateral Balance / Notes Balance
- **IC Ratio** = Interest Collections / Note Interest Due
- **WAL (weighted average life)** = Sum(Principal_t * t) / Total Principal
- **Excess Spread** = Asset Yield - (Funding Cost + Servicing + Charge-offs + Other Fees)

## 6) Mortgage and Real Estate

- **Front-End DTI** = Housing Expense / Gross Income
- **Back-End DTI** = Total Debt Obligations / Gross Income
- **Debt Yield (CRE)** = NOI / Loan Balance
- **Breakeven Occupancy** = (Operating Expenses + Debt Service) / Potential Gross Income
- **Cap Rate Implied Value** = NOI / Market Cap Rate

## 7) Municipal and Public Finance

- **Revenue DSCR** = Net Revenue for Debt Service / Annual Debt Service
- **Debt Burden (AV-based)** = Net Direct Debt / Taxable Assessed Value
- **Cash Days on Hand** = Unrestricted Cash / (Operating Expense / 365)
- **Pension Burden** = Unfunded Pension Liability / Revenue

## 8) Microfinance and Inclusive Finance

- **PAR30** = Portfolio >30 DPD / Gross Loan Portfolio
- **PAR90** = Portfolio >90 DPD / Gross Loan Portfolio
- **Write-Off Ratio** = Write-Offs / Average Gross Loan Portfolio
- **Collection Efficiency** = Collections / Amount Due
- **FSS** = Adjusted Operating Revenue / (Financial Expense + Loan Loss Provision + Operating Expense)

## 9) Asset and Equipment Finance / Leasing

- **Lease Rate Factor** = Periodic Lease Payment / Asset Cost
- **Residual Value Ratio** = Expected Residual Value / Original Asset Cost
- **LTOLV** = Loan Balance / Orderly Liquidation Value
- **Net Investment in Lease (simplified)** = PV(Lease Cash Flows + Residual) - Initial Outlay
- **Break-Even Utilization** = (Fixed Costs + Debt/Lease Obligation) / Contribution Margin per Utilization Unit
- **Repossession Recovery Rate** = Net Recovery After Costs / Exposure at Default

## 10) M&A and Corporate Advisory

- **Enterprise Value (EV)** = Equity Value + Net Debt + Preferred + Minority Interest
- **Equity Value** = EV - Net Debt - Senior Claims
- **Synergy NPV** = PV(Post-Tax Synergies) - Integration Costs
- **Accretion/(Dilution)** = (Pro Forma EPS - Standalone EPS) / Standalone EPS
- **Implied Deal Multiple** = Purchase Consideration / Target EBITDA (or EBIT)
- **IRR (deal equity)** = Rate where NPV(Equity Cash Flows) = 0

## 11) Treasury and Payments

- **Cash Conversion Cycle (CCC)** = DSO + DIO - DPO
- **NIM** = (Interest Income - Interest Expense) / Average Earning Assets
- **Duration Gap (simplified)** = Duration(Assets) - Duration(Liabilities)
- **Hedge Ratio** = Notional Hedged Exposure / Total Exposure
- **Payment Loss Rate** = Fraud and Chargeback Losses / Gross Payment Volume

## 12) Insurance and Risk Transfer

- **Loss Ratio** = Incurred Losses / Earned Premium
- **Expense Ratio** = Underwriting Expenses / Earned Premium
- **Combined Ratio** = Loss Ratio + Expense Ratio
- **Retention Ratio** = Net Retained Risk / Gross Risk Written
- **Reserve Adequacy Gap** = Required Reserves - Booked Reserves

## 13) Market Making and Liquidity

- **Realized Spread** = Signed Trade Price - Midprice after Horizon
- **Effective Spread** = 2 * |Trade Price - Midprice at Execution|
- **Inventory Turnover** = Gross Traded Volume / Average Inventory
- **Adverse Selection Cost** = Midprice Move Against Position after Fill
- **Slippage** = Executed Hedge Price - Target Hedge Price

## 14) Portfolio and Concentration

- **Single-Name Concentration** = Exposure to Name / Total Portfolio Exposure
- **Sector Concentration** = Sector Exposure / Total Portfolio Exposure
- **Top-10 Concentration** = Sum(Top 10 Exposures) / Total Portfolio Exposure
- **Vintage Loss Rate** = Cumulative Losses by Vintage / Original Vintage Balance
- **Migration Rate** = Obligors Downgraded in Period / Total Obligors
- **Sharpe Ratio** = (Portfolio Return - Risk-Free Rate) / Volatility
- **Information Ratio** = Active Return / Tracking Error
- **Tracking Error** = StdDev(Portfolio Return - Benchmark Return)
- **Max Drawdown** = Max(Peak-to-Trough Decline)

## 15) Stress Testing Templates

- **Rate Shock**: +100/+200/+300 bps, reprice financing and debt service.
- **Cash-Flow Shock**: -10%/-20%/-30% revenue with margin compression.
- **Collateral Shock**: -10%/-20%/-40% collateral value and reduced liquidity.
- **Refinance Shock**: no takeout window for 6-18 months.
- **Correlation Shock**: simultaneous borrower weakness + collateral markdown.

## 16) Policy Notes

- Metric thresholds must be policy-set and jurisdiction-specific.
- Do not rely on static market spread assumptions; refresh current market inputs before final recommendation.
- Keep formulas constant; update assumptions and data feeds each run.
