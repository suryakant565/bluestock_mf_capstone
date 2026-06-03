--  top 5 funds by AUM
SELECT fund_house,
       MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- avg nav 
SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- SIP YoY Growth

WITH yearly_sip AS (
    SELECT
        strftime('%Y', transaction_date) AS year,
        SUM(amount_inr) AS total_sip_amount
    FROM fact_transactions
    WHERE transaction_type = 'SIP'
    GROUP BY strftime('%Y', transaction_date)
)

SELECT
    year,
    total_sip_amount,
    ROUND(
        (
            total_sip_amount -
            LAG(total_sip_amount) OVER (ORDER BY year)
        ) * 100.0 /
        LAG(total_sip_amount) OVER (ORDER BY year),
        2
    ) AS yoy_growth_pct
FROM yearly_sip
ORDER BY year;

-- state transactions

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    fund_house,
    category,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;

-- Top 10 Funds by Average NAV

SELECT
    amfi_code,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC
LIMIT 10;