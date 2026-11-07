from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ecommerce_customers.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(DATA, parse_dates=["signup_date"])
    required = {
        "customer_id", "tenure_months", "customer_segment",
        "acquisition_channel", "region", "orders_count",
        "avg_order_value", "support_tickets", "days_since_last_order", "churned"
    }
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    # Basic data quality checks
    df = df.drop_duplicates(subset=["customer_id"])
    df = df.dropna(subset=["customer_id", "churned"])
    df["churned"] = df["churned"].astype(int)

    total_customers = df["customer_id"].nunique()
    churned_customers = int(df.loc[df["churned"] == 1, "customer_id"].nunique())
    overall = pd.DataFrame([{
        "total_customers": total_customers,
        "churned_customers": churned_customers,
        "churn_rate_pct": round(100 * churned_customers / total_customers, 2),
        "retention_rate_pct": round(100 * (1 - churned_customers / total_customers), 2),
        "average_order_value": round(df["avg_order_value"].mean(), 2),
        "average_recency_days": round(df["days_since_last_order"].mean(), 2)
    }])
    overall.to_csv(OUT / "overall_kpis.csv", index=False)

    for dimension, filename in [
        ("customer_segment", "customer_churn_by_segment.csv"),
        ("acquisition_channel", "customer_churn_by_channel.csv"),
        ("region", "customer_churn_by_region.csv")
    ]:
        report = (df.groupby(dimension, dropna=False)
                    .agg(customers=("customer_id", "nunique"),
                         churned_customers=("churned", "sum"),
                         avg_orders=("orders_count", "mean"),
                         avg_support_tickets=("support_tickets", "mean"))
                    .reset_index())
        report["churn_rate_pct"] = (100 * report["churned_customers"] / report["customers"]).round(2)
        report.to_csv(OUT / filename, index=False)

    behavior = (df.groupby("churned")
                  .agg(customers=("customer_id", "nunique"),
                       avg_orders=("orders_count", "mean"),
                       avg_recency_days=("days_since_last_order", "mean"),
                       avg_support_tickets=("support_tickets", "mean"),
                       avg_order_value=("avg_order_value", "mean"))
                  .reset_index())
    behavior.to_csv(OUT / "behavior_by_churn_status.csv", index=False)

    # A simple chart for quick review; Power BI dashboard is built separately.
    segment = pd.read_csv(OUT / "customer_churn_by_segment.csv")
    plt.figure(figsize=(8, 5))
    plt.bar(segment["customer_segment"], segment["churn_rate_pct"])
    plt.title("Churn Rate by Customer Segment")
    plt.xlabel("Customer Segment")
    plt.ylabel("Churn Rate (%)")
    plt.tight_layout()
    plt.savefig(OUT / "churn_by_segment.png", dpi=160)
    plt.close()

    print("Analysis complete. Reports saved to:", OUT)

if __name__ == "__main__":
    main()
