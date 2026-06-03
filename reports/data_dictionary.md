# Data Dictionary

## dim_fund

| Column             | Description                                  |
| ------------------ | -------------------------------------------- |
| amfi_code          | Unique AMFI code for mutual fund scheme      |
| fund_house         | Asset Management Company (AMC) name          |
| scheme_name        | Name of the mutual fund scheme               |
| category           | Fund category (Equity, Debt, etc.)           |
| sub_category       | Fund sub-category (Large Cap, Mid Cap, etc.) |
| plan               | Direct or Regular plan                       |
| launch_date        | Fund launch date                             |
| benchmark          | Benchmark index used for comparison          |
| expense_ratio_pct  | Annual expense ratio (%)                     |
| exit_load_pct      | Exit load charged on redemption (%)          |
| min_sip_amount     | Minimum SIP investment amount                |
| min_lumpsum_amount | Minimum lump-sum investment amount           |
| fund_manager       | Name of fund manager                         |
| risk_category      | Risk level of scheme                         |
| sebi_category_code | SEBI classification code                     |

## fact_nav

| Column           | Description               |
| ---------------- | ------------------------- |
| amfi_code        | Mutual fund scheme code   |
| date             | NAV date                  |
| nav              | Net Asset Value of scheme |
| daily_return_pct | Daily percentage return   |

## fact_transactions

| Column             | Description                  |
| ------------------ | ---------------------------- |
| investor_id        | Unique investor identifier   |
| transaction_date   | Date of transaction          |
| amfi_code          | Mutual fund scheme code      |
| transaction_type   | SIP, Lumpsum, or Redemption  |
| amount_inr         | Transaction amount in INR    |
| state              | Investor state               |
| city               | Investor city                |
| city_tier          | Tier classification of city  |
| age_group          | Investor age group           |
| gender             | Investor gender              |
| annual_income_lakh | Annual income in lakh rupees |
| payment_mode       | Payment method used          |
| kyc_status         | KYC verification status      |

## fact_performance

| Column         | Description                  |
| -------------- | ---------------------------- |
| amfi_code      | Mutual fund scheme code      |
| return_1yr_pct | One-year return percentage   |
| return_3yr_pct | Three-year return percentage |
| return_5yr_pct | Five-year return percentage  |
| sharpe_ratio   | Risk-adjusted return metric  |
| alpha          | Excess return over benchmark |
| beta           | Market sensitivity measure   |
| max_drawdown   | Maximum historical decline   |

## fact_aum

| Column         | Description                           |
| -------------- | ------------------------------------- |
| date           | Reporting date                        |
| fund_house     | Asset Management Company              |
| aum_lakh_crore | Assets Under Management in lakh crore |
| aum_crore      | Assets Under Management in crore      |
| num_schemes    | Number of schemes managed             |
