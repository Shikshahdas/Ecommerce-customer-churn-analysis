# Power BI Dashboard Build Guide

## 1. Import
Import `data/ecommerce_customers.csv` into Power BI Desktop. Confirm `signup_date` is Date and numeric columns are numeric.

## 2. Create measures (DAX)
```DAX
Total Customers = DISTINCTCOUNT(ecommerce_customers[customer_id])

Churned Customers =
CALCULATE(
    DISTINCTCOUNT(ecommerce_customers[customer_id]),
    ecommerce_customers[churned] = 1
)

Churn Rate % = DIVIDE([Churned Customers], [Total Customers], 0)

Retention Rate % = 1 - [Churn Rate %]

Average Order Value = AVERAGE(ecommerce_customers[avg_order_value])

Average Recency (Days) = AVERAGE(ecommerce_customers[days_since_last_order])

Average Orders = AVERAGE(ecommerce_customers[orders_count])
```

## 3. Suggested one-page layout
- KPI cards: Total Customers, Churned Customers, Churn Rate %, Retention Rate %.
- Clustered bar chart: Churn Rate % by Customer Segment.
- Bar chart: Churn Rate % by Acquisition Channel.
- Column chart: Churn Rate % by Region.
- Stacked column: Customer count by Churn Status and Segment.
- Table: Segment, Customers, Churned Customers, Churn Rate %, Average Orders.
- Slicers: Region, Customer Segment, Acquisition Channel.

## 4. Design
Use a consistent restrained theme, clear titles, percentage formatting, and descriptive tooltips. Label the dashboard as an analysis of synthetic demonstration data.
