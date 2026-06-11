# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project is an end-to-end Mutual Fund Analytics platform developed as part of the Bluestock Fintech Capstone Program. The project covers data ingestion, cleaning, exploratory analysis, database design, risk analytics, investor behavior analysis, and interactive dashboard development using Power BI.

## Objectives

* Build a centralized mutual fund analytics database.
* Analyze fund performance and risk metrics.
* Study investor transaction behavior and SIP trends.
* Create interactive Power BI dashboards.
* Develop advanced analytics and fund recommendation capabilities.

---

## Tech Stack

* Python (Pandas, NumPy, Matplotlib)
* SQLite
* SQL
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Structure

bluestock_mf_capstone/

├── data/

│ ├── raw/

│ ├── processed/

│ └── db/bluestock_mf.db

├── notebooks/

│ ├── 01_data_ingestion.ipynb

│ ├── 02_data_cleaning.ipynb

│ ├── 03_eda_analysis.ipynb

│ ├── 04_performance_analytics.ipynb

│ └── 05_advanced_analytics.ipynb

├── scripts/

│ ├── data_ingestion.py

│ ├── live_nav_fetch.py

│ └── recommender.py

├── sql/

│ ├── schema.sql

│ └── queries.sql

├── dashboards/

│ └── bluestock_mf.pbix

├── reports/

│ ├── var_cvar_report.csv

│ ├── sip_continuity_report.csv

│ ├── sector_hhi_report.csv

│ ├── rolling_sharpe_chart.png

│ └── Final_Report.pdf

├── README.md

└── requirements.txt

---

## Database Design

Implemented a star-schema style structure using SQLite:

### Dimension Table

* dim_fund

### Fact Tables

* fact_aum
* fact_nav
* fact_performance
* fact_transactions

Database schema is available in `sql/schema.sql`.

---

## Exploratory Data Analysis (EDA)

Performed:

* Missing value analysis
* Data quality checks
* Distribution analysis
* Category-wise fund analysis
* AUM trend analysis
* Investor transaction analysis

---

## Risk & Performance Analytics

Computed key performance metrics:

* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* CAGR
* Volatility

---

## Advanced Analytics

### Historical VaR & CVaR

* Computed 95% Value at Risk (VaR)
* Computed Conditional Value at Risk (CVaR)
* Generated `var_cvar_report.csv`

### Rolling Sharpe Ratio

* Calculated 90-Day Rolling Sharpe Ratio
* Visualized performance stability across funds
* Generated `rolling_sharpe_chart.png`

### Investor Cohort Analysis

* Grouped investors by first investment year
* Analyzed investment patterns by cohort

### SIP Continuity Analysis

* Calculated transaction gaps
* Identified At-Risk investors
* Generated `sip_continuity_report.csv`

### Fund Recommendation System

* Risk-based recommendation engine
* Supports:

  * Low Risk
  * Moderate Risk
  * High Risk

### Sector Concentration Analysis

* Calculated Herfindahl-Hirschman Index (HHI)
* Measured portfolio concentration across sectors
* Generated `sector_hhi_report.csv`

---

## Power BI Dashboard

Developed a 4-page interactive dashboard.

### Page 1 – Market Overview

* Total AUM
* SIP Inflows
* Investor Count
* Fund Count
* Industry AUM Trend
* Fund House Comparison

### Page 2 – Fund Performance & Risk

* Return vs Risk Analysis
* Alpha Ranking
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Fund Scorecard

### Page 3 – Investor Analytics

* Investor Demographics
* Transaction Analysis
* State-wise Investment Trends
* Cohort Insights

### Page 4 – SIP & Market Trends

* SIP Inflow Trends
* Benchmark Comparison
* Category-wise Flows
* Market Trend Analysis

---

## Key Insights

* Risk-adjusted performance varies significantly across fund categories.
* Several funds exhibit strong Sharpe and Sortino ratios despite moderate risk.
* Investor cohorts formed in recent years contribute a substantial share of investments.
* SIP continuity analysis identified investors with irregular contribution patterns.
* HHI analysis revealed varying levels of portfolio concentration across schemes.

---

## Author

Suryakant Sharma

Bluestock Mutual Fund Analytics Capstone Project
