-- PostgreSQL-compatible SQL analysis
-- Load data/ecommerce_customers.csv into a table named ecommerce_customers.
-- Suggested table types: dates as DATE, metrics as INTEGER/NUMERIC.

-- 1. Overall business KPIs
SELECT
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT CASE WHEN churned = 1 THEN customer_id END) AS churned_customers,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN churned = 1 THEN customer_id END)
        / NULLIF(COUNT(DISTINCT customer_id), 0), 2
    ) AS churn_rate_pct
FROM ecommerce_customers;

-- 2. Churn by customer segment
SELECT
    customer_segment,
    COUNT(DISTINCT customer_id) AS customers,
    COUNT(DISTINCT CASE WHEN churned = 1 THEN customer_id END) AS churned_customers,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN churned = 1 THEN customer_id END)
        / NULLIF(COUNT(DISTINCT customer_id), 0), 2
    ) AS churn_rate_pct
FROM ecommerce_customers
GROUP BY customer_segment
ORDER BY churn_rate_pct DESC;

-- 3. Churn by acquisition channel
SELECT
    acquisition_channel,
    COUNT(DISTINCT customer_id) AS customers,
    ROUND(100.0 * AVG(churned), 2) AS churn_rate_pct
FROM ecommerce_customers
GROUP BY acquisition_channel
ORDER BY churn_rate_pct DESC;

-- 4. Compare behavior by churn status
SELECT
    churned,
    COUNT(*) AS customers,
    ROUND(AVG(orders_count), 2) AS avg_orders,
    ROUND(AVG(days_since_last_order), 2) AS avg_days_since_last_order,
    ROUND(AVG(support_tickets), 2) AS avg_support_tickets,
    ROUND(AVG(avg_order_value), 2) AS avg_order_value
FROM ecommerce_customers
GROUP BY churned
ORDER BY churned;

-- 5. Regional KPI view
SELECT
    region,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(churned), 2) AS churn_rate_pct,
    ROUND(AVG(avg_order_value), 2) AS average_order_value
FROM ecommerce_customers
GROUP BY region
ORDER BY churn_rate_pct DESC;
