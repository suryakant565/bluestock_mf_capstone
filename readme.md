# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone is an end-to-end data analytics project focused on mutual fund performance evaluation, investor behavior analysis, risk assessment, and business intelligence reporting.

The project combines Python, SQL, SQLite, and Power BI to transform raw mutual fund data into actionable insights through advanced analytics and interactive dashboards.

---

## Objectives

* Build a centralized mutual fund analytics database.
* Perform data cleaning and transformation using Python.
* Analyze mutual fund performance using financial metrics.
* Study investor behavior and SIP trends.
* Calculate advanced risk measures such as VaR and CVaR.
* Develop a risk-based mutual fund recommendation system.
* Create interactive Power BI dashboards for decision-making.

---

## Technology Stack

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Data Sources

The project utilizes the following datasets:

* Fund Master Data
* NAV History Data
* Investor Transactions Data
* Portfolio Holdings Data
* Benchmark Index Data

---

## Project Structure

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   └── recommender.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── dashboards/
│   └── bluestock_mf.pbix
├── reports/
│   ├── var_cvar_report.csv
│   ├── sip_continuity_report.csv
│   ├── sector_hhi_report.csv
│   ├── rolling_sharpe_chart.png
│   └── Final_Report.pdf
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Database Design

The project uses a SQLite database with a star-schema-inspired design.

### Dimension Table

* dim_fund

### Fact Tables

* fact_nav
* fact_aum
* fact_performance
* fact_transactions

---

## Exploratory Data Analysis

EDA was conducted to:

* Validate data quality
* Analyze investor demographics
* Examine AUM trends
* Study SIP inflows
* Understand transaction patterns

---

## Performance Analytics

The following metrics were calculated:

* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* CAGR
* Volatility
* Maximum Drawdown

---

## Advanced Analytics

### Historical VaR & CVaR

* Computed 95% Value at Risk (VaR)
* Computed Conditional Value at Risk (CVaR)

Output:

* `var_cvar_report.csv`

### Rolling Sharpe Ratio

* Calculated 90-Day Rolling Sharpe Ratio
* Evaluated consistency of risk-adjusted returns

Output:

* `rolling_sharpe_chart.png`

### Investor Cohort Analysis

* Grouped investors by first transaction year
* Analyzed investment behavior by cohort

### SIP Continuity Analysis

* Calculated average gaps between SIP transactions
* Identified At-Risk investors

Output:

* `sip_continuity_report.csv`

### Sector HHI Analysis

* Calculated Herfindahl-Hirschman Index (HHI)
* Measured portfolio concentration risk

Output:

* `sector_hhi_report.csv`

### Fund Recommendation System

Developed a recommendation engine that suggests mutual funds based on:

* Low Risk
* Moderate Risk
* High Risk

---

## Power BI Dashboard

A four-page interactive dashboard was developed.

### Page 1 – Market Overview

* Total AUM
* SIP Inflows
* Fund Count
* Investor Count
* Industry AUM Trend
* Fund House Comparison

### Page 2 – Fund Performance & Risk

* Return vs Risk Analysis
* Sharpe Ratio
* Sortino Ratio
* Alpha Ranking
* Maximum Drawdown
* Fund Scorecard

### Page 3 – Investor Analytics

* Transaction Volume Analysis
* Investment Type Distribution
* State-wise Investment Trends
* Age Group Analysis

### Page 4 – SIP & Market Trends

* SIP Inflow vs NIFTY50 Trend
* Category Inflow Heatmap
* Category-wise Investment Flows

---

## Key Findings

* The mutual fund industry demonstrated strong AUM growth during the analysis period.
* SIP participation increased steadily, indicating growing investor confidence.
* Equity-oriented schemes attracted significantly higher investments than debt schemes.
* Risk-adjusted performance varied across mutual fund categories.
* Investor activity was concentrated within the 26–45 age group.
* Leading fund houses managed a substantial share of total industry assets.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute notebooks in the following order:

```text
01_data_ingestion.ipynb
02_data_cleaning.ipynb
03_eda_analysis.ipynb
04_performance_analytics.ipynb
05_advanced_analytics.ipynb
```

Open the Power BI dashboard:

```text
dashboards/bluestock_mf.pbix
```

---

## Author

**Suryakant Sharma**

Bluestock Mutual Fund Analytics Capstone Project

2026
