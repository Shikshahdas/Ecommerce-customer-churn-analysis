# E-Commerce Customer Churn Analysis & KPI Dashboard

A portfolio project demonstrating customer-level data preparation, exploratory analysis, SQL KPI reporting, and a Power BI dashboard specification.

## Project goals
- Measure customer churn and retention.
- Identify customer groups associated with higher churn.
- Track business KPIs by segment, region, and acquisition channel.
- Translate analysis into practical retention recommendations.

## Tools
Python, Pandas, Matplotlib, SQL (PostgreSQL-compatible), Power BI.

## Dataset
`data/ecommerce_customers.csv` contains 2,500 **synthetic** customer records generated for this portfolio project. It contains no real customer or personally identifiable information. The churn labels are simulated for demonstration, so findings are illustrative and must not be presented as real-world business outcomes.

## Repository structure
```text
ecommerce-customer-churn-analysis/
├── data/
│   └── ecommerce_customers.csv
├── outputs/
│   ├── customer_churn_by_segment.csv
│   ├── customer_churn_by_channel.csv
│   └── monthly_kpis.csv
├── powerbi/
│   └── dashboard_build_guide.md
├── sql/
│   └── analysis.sql
├── src/
│   └── analysis.py
├── requirements.txt
└── README.md
```

## Run locally
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis from the repository root:
   ```bash
   python src/analysis.py
   ```
4. Review the generated CSV reports in `outputs/`.

## Key metric definitions
- **Customers:** distinct customer IDs.
- **Churned customers:** customers with `churned = 1`.
- **Churn rate:** churned customers / total customers.
- **Average order value (AOV):** mean of `avg_order_value`.
- **Average recency:** mean `days_since_last_order`.
- **Retention rate:** 1 - churn rate.

## Business questions
1. What proportion of customers are marked as churned?
2. Which customer segments have the highest churn rate?
3. Does churn differ across acquisition channels and regions?
4. How do order frequency, support tickets, and recency vary by churn status?
5. Which customer groups should a retention team investigate first?

## Important interpretation note
This project uses a synthetic dataset and simulated churn labels. The analysis demonstrates a workflow and does not establish causal relationships. Avoid claiming that any intervention reduced churn or improved revenue unless you conduct and document a valid experiment.

## Suggested GitHub description
Exploratory customer churn analysis using Python, Pandas, SQL and Power BI, with KPI reporting and retention-focused business insights.
