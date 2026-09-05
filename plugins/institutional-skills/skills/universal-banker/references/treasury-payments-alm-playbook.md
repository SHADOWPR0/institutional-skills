# Treasury, Payments, and ALM Playbook

Framework for liquidity/funding strategy, payment rails, and balance-sheet risk control.

## 1) Coverage

- liquidity and funding stack optimization
- cash concentration and working-capital design
- FX and interest-rate hedge policy
- payment-rail selection and fraud/chargeback controls
- bank relationship and contingency funding architecture

## 2) Core Formulas

- **Liquidity Coverage (internal)** = High-Quality Liquid Assets / Net Cash Outflows (horizon)
- **Cash Conversion Cycle (CCC)** = DSO + DIO - DPO
- **Net Interest Margin (NIM)** = (Interest Income - Interest Expense) / Average Earning Assets
- **Duration Gap (simplified)** = Duration(Assets) - Duration(Liabilities)
- **Hedge Ratio** = Notional Hedged Exposure / Total Exposure
- **Payment Loss Rate** = Fraud and Chargeback Losses / Gross Payment Volume

## 3) Underwriting/Decision Priorities

- funding concentration and rollover risk
- intraday and stressed liquidity sufficiency
- payment-rail reliability, settlement windows, and reconciliation quality
- fraud controls and operational resilience
- hedge effectiveness and basis risk under stress

## 4) Structural Controls

- minimum liquidity buffers by stress horizon
- diversified funding maturity ladder
- dual-authorization controls for treasury operations
- payment exception queues with SLA governance
- counterparty and settlement-bank concentration caps

## 5) Stress Testing

- deposit/funding outflow shock
- payment outage and settlement delay scenario
- abrupt rate and FX regime shift
- counterparty downgrade/default scenario
