# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project is part of the Bluestock Fintech Internship Program. The objective is to build a complete Mutual Fund Analytics Pipeline by performing data ingestion, cleaning, database loading, SQL analysis, and dashboard creation using Python, SQLite, and data visualization tools.

---

## Project Objectives

- Ingest and process mutual fund datasets
- Fetch live NAV data using MFAPI
- Clean and validate raw datasets
- Store processed data in SQLite database
- Perform analytical SQL queries
- Build an interactive analytics dashboard
- Generate business insights from mutual fund data

---

## Project Structure

```text
BLUESTOCK_MF_CAPSTONE/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   └── 02_data_cleaning.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   └── live_nav_fetch.py
│
├── sql/
│   ├── queries.sql
│   └── schema.sql
│
├── reports/
│   ├── data_quality_report.txt
│   └── data_dictionary.md
│
├── requirements.txt
└── README.md
```

---

## Datasets Used

### 1. Fund Master
Contains scheme information including:
- AMFI Code
- Fund House
- Category
- Expense Ratio
- Risk Category
- Fund Manager

### 2. NAV History
Contains historical Net Asset Value (NAV) data for mutual fund schemes.

### 3. AUM by Fund House
Assets Under Management data for different fund houses.

### 4. Monthly SIP Inflows
Industry SIP inflow trends.

### 5. Category Inflows
Investment inflows across mutual fund categories.

### 6. Industry Folio Count
Investor folio statistics.

### 7. Scheme Performance
Performance metrics and returns.

### 8. Investor Transactions
Investor transaction records including SIP, Lumpsum, and Redemption.

### 9. Portfolio Holdings
Underlying portfolio holdings of mutual funds.

### 10. Benchmark Indices
Benchmark index performance data.

---

## Live NAV Data Integration

Live NAV data was fetched using MFAPI.

Schemes fetched:

- HDFC Top 100
- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

Data fetched:
- Date
- NAV Value

---

## Data Cleaning Performed

### NAV History
- Converted date columns to datetime
- Sorted by AMFI code and date
- Removed duplicates
- Validated NAV > 0

### Investor Transactions
- Standardized transaction types
- Validated transaction amounts
- Verified KYC status values
- Fixed date formats

### Scheme Performance
- Validated numeric return columns
- Checked expense ratio ranges
- Flagged anomalies

### AUM Data
- Converted dates
- Validated AUM values
- Removed duplicates

---

## Database Design

SQLite database used:

```text
data/db/bluestock_mf.db
```

### Tables

#### Dimension Table
- dim_fund

#### Fact Tables
- fact_nav
- fact_transactions
- fact_performance
- fact_aum

---

## Row Counts

| Table | Rows |
|---------|------:|
| dim_fund | 40 |
| fact_nav | 46,000 |
| fact_transactions | 32,778 |
| fact_performance | 40 |
| fact_aum | 90 |

---

## Analytical SQL Queries

Implemented:

1. Top 5 Fund Houses by AUM
2. Average NAV per Month
3. SIP Year-over-Year Growth
4. Transactions by State
5. Funds with Expense Ratio < 1%
6. Top 10 Funds by Average NAV
7. Fund Count by Category
8. Fund Count by Risk Category
9. Average Expense Ratio by Category
10. Average SIP Amount by Category

---

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- Jupyter Notebook
- VS Code
- Git
- GitHub
- DB Browser for SQLite

---

## Future Enhancements

- Streamlit Dashboard
- Interactive NAV Trend Analysis
- Investor Segmentation
- Fund Performance Comparison
- SIP Growth Analytics
- Portfolio Analysis Dashboard

---

## Author

Suryakant Sharma

Bluestock Fintech Internship Project
