# Import libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
# Create path for visualization outputs
OUTPUT_DIR = Path("outputs/visualizations")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

print("Visualization output directory created successfully.")
# Load final monthly performance data
monthly_performance = pd.read_csv(
    "outputs/final_monthly_analysis_dashboard.csv"
)

print("\nMonthly performance data loaded successfully.")
print(monthly_performance.head())
# Load monthly growth data
monthly_growth = pd.read_csv(
    "outputs/combined_monthly_growth.csv"
)

print("\nMonthly growth data loaded successfully.")
print(monthly_growth.head())
# Load top 5 monthly performance data
top_5_performance = pd.read_csv(
    "outputs/top_5_monthly_performance.csv"
)

print("\nTop 5 monthly performance data loaded successfully.")
print(top_5_performance.head())
# Load bottom 5 monthly performance data
bottom_5_performance = pd.read_csv(
    "outputs/bottom_5_monthly_performance.csv"
)

print("\nBottom 5 monthly performance data loaded successfully.")
print(bottom_5_performance.head())
# Load monthly performance comparison data
performance_comparison = pd.read_csv(
    "outputs/monthly_performance_comparison.csv"
)

print("\nMonthly performance comparison data loaded successfully.")
print(performance_comparison.head())
# Load monthly statistical summary data
statistical_summary = pd.read_csv(
    "outputs/monthly_statistical_summary.csv"
)

print("\nMonthly statistical summary data loaded successfully.")
print(statistical_summary.head())
# Load final monthly outlier summary data
outlier_summary = pd.read_csv(
    "outputs/final_monthly_outlier_summary.csv"
)

print("\nMonthly outlier summary data loaded successfully.")
print(outlier_summary.head())
# Load final project KPI summary data
kpi_summary = pd.read_csv(
    "outputs/final_project_kpi_summary.csv"
)

print("\nFinal project KPI summary data loaded successfully.")
print(kpi_summary.head(8))
# Set visualization theme
sns.set_theme(
    style="whitegrid",
    context="notebook"
)

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["figure.dpi"] = 100

print("\nVisualization theme configured successfully.")
# Create Mean vs Median comparison chart
plt.figure(figsize=(10, 6))

x = range(len(statistical_summary["Metric"]))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    statistical_summary["Mean"],
    width=width,
    label="Mean"
)

plt.bar(
    [i + width / 2 for i in x],
    statistical_summary["Median"],
    width=width,
    label="Median"
)

plt.xticks(
    list(x),
    statistical_summary["Metric"]
)

plt.title("Monthly Mean vs Median Comparison")
plt.xlabel("Metric")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_mean_vs_median.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nMonthly Mean vs Median chart saved successfully.")
# Create monthly standard deviation comparison chart
plt.figure(figsize=(10, 6))

plt.bar(
    statistical_summary["Metric"],
    statistical_summary["Standard_Deviation"]
)

plt.title("Monthly Standard Deviation by Metric")
plt.xlabel("Metric")
plt.ylabel("Standard Deviation")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_standard_deviation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nMonthly standard deviation chart saved successfully.")# Create coefficient of variation comparison chart
plt.figure(figsize=(10, 6))

plt.bar(
    statistical_summary["Metric"],
    statistical_summary["Coefficient_of_Variation_Percentage"]
)

plt.title("Monthly Coefficient of Variation by Metric")
plt.xlabel("Metric")
plt.ylabel("Coefficient of Variation (%)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_coefficient_of_variation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nMonthly coefficient of variation chart saved successfully.")# Create monthly outlier count chart
plt.figure(figsize=(10, 6))

plt.bar(
    outlier_summary["Metric"],
    outlier_summary["Outlier_Count"]
)

plt.title("Monthly Outlier Count by Metric")
plt.xlabel("Metric")
plt.ylabel("Number of Outliers")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_outlier_count.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nMonthly outlier count chart saved successfully.")# Create monthly outlier percentage chart
plt.figure(figsize=(10, 6))

plt.bar(
    outlier_summary["Metric"],
    outlier_summary["Outlier_Percentage"]
)

plt.title("Monthly Outlier Percentage by Metric")
plt.xlabel("Metric")
plt.ylabel("Outlier Percentage (%)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_outlier_percentage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nMonthly outlier percentage chart saved successfully.")# Create best vs worst monthly performance chart
plt.figure(figsize=(10, 6))

x = range(len(performance_comparison["Metric"]))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    performance_comparison["Best_Value"],
    width=width,
    label="Best Value"
)

plt.bar(
    [i + width / 2 for i in x],
    performance_comparison["Worst_Value"],
    width=width,
    label="Worst Value"
)

plt.xticks(
    list(x),
    performance_comparison["Metric"]
)

plt.title("Best vs Worst Monthly Performance")
plt.xlabel("Metric")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "best_vs_worst_monthly_performance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBest vs worst monthly performance chart saved successfully.")# Create top 5 revenue months chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_5_performance["Revenue_Month"].astype(str),
    top_5_performance["Revenue"]
)

plt.title("Top 5 Months by Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_5_revenue_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 revenue months chart saved successfully.")# Create top 5 orders months chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_5_performance["Orders_Month"].astype(str),
    top_5_performance["Orders"]
)

plt.title("Top 5 Months by Orders")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_5_orders_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 orders months chart saved successfully.")# Create top 5 customers months chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_5_performance["Customers_Month"].astype(str),
    top_5_performance["Customers"]
)

plt.title("Top 5 Months by Customers")
plt.xlabel("Month")
plt.ylabel("Customers")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_5_customers_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 customers months chart saved successfully.")# Create top 5 quantity months chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_5_performance["Quantity_Month"].astype(str),
    top_5_performance["Quantity"]
)

plt.title("Top 5 Months by Quantity")
plt.xlabel("Month")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_5_quantity_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 quantity months chart saved successfully.")# Create bottom 5 revenue months chart
plt.figure(figsize=(10, 6))

plt.bar(
    bottom_5_performance["Revenue_Month"].astype(str),
    bottom_5_performance["Revenue"]
)

plt.title("Bottom 5 Months by Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "bottom_5_revenue_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBottom 5 revenue months chart saved successfully.")# Create bottom 5 orders months chart
plt.figure(figsize=(10, 6))

plt.bar(
    bottom_5_performance["Orders_Month"].astype(str),
    bottom_5_performance["Orders"]
)

plt.title("Bottom 5 Months by Orders")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "bottom_5_orders_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBottom 5 orders months chart saved successfully.")
# Create bottom 5 customers months chart
plt.figure(figsize=(10, 6))

plt.bar(
    bottom_5_performance["Customers_Month"].astype(str),
    bottom_5_performance["Customers"]
)

plt.title("Bottom 5 Months by Customers")
plt.xlabel("Month")
plt.ylabel("Customers")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "bottom_5_customers_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBottom 5 customers months chart saved successfully.")# Create bottom 5 quantity months chart
plt.figure(figsize=(10, 6))

plt.bar(
    bottom_5_performance["Quantity_Month"].astype(str),
    bottom_5_performance["Quantity"]
)

plt.title("Bottom 5 Months by Quantity")
plt.xlabel("Month")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "bottom_5_quantity_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBottom 5 quantity months chart saved successfully.")# Create top 5 vs bottom 5 revenue comparison chart
plt.figure(figsize=(10, 6))

x = range(len(top_5_performance))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    top_5_performance["Revenue"],
    width=width,
    label="Top 5 Revenue"
)

plt.bar(
    [i + width / 2 for i in x],
    bottom_5_performance["Revenue"],
    width=width,
    label="Bottom 5 Revenue"
)

plt.xticks(
    list(x),
    ["Rank 1", "Rank 2", "Rank 3", "Rank 4", "Rank 5"]
)

plt.title("Top 5 vs Bottom 5 Monthly Revenue")
plt.xlabel("Performance Rank")
plt.ylabel("Revenue")
plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_vs_bottom_5_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 vs bottom 5 revenue chart saved successfully.")# Create top 5 vs bottom 5 orders comparison chart
plt.figure(figsize=(10, 6))

x = range(len(top_5_performance))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    top_5_performance["Orders"],
    width=width,
    label="Top 5 Orders"
)

plt.bar(
    [i + width / 2 for i in x],
    bottom_5_performance["Orders"],
    width=width,
    label="Bottom 5 Orders"
)

plt.xticks(
    list(x),
    ["Rank 1", "Rank 2", "Rank 3", "Rank 4", "Rank 5"]
)

plt.title("Top 5 vs Bottom 5 Monthly Orders")
plt.xlabel("Performance Rank")
plt.ylabel("Orders")
plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_vs_bottom_5_orders.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 vs bottom 5 orders chart saved successfully.")# Create top 5 vs bottom 5 customers comparison chart
plt.figure(figsize=(10, 6))

x = range(len(top_5_performance))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    top_5_performance["Customers"],
    width=width,
    label="Top 5 Customers"
)

plt.bar(
    [i + width / 2 for i in x],
    bottom_5_performance["Customers"],
    width=width,
    label="Bottom 5 Customers"
)

plt.xticks(
    list(x),
    ["Rank 1", "Rank 2", "Rank 3", "Rank 4", "Rank 5"]
)

plt.title("Top 5 vs Bottom 5 Monthly Customers")
plt.xlabel("Performance Rank")
plt.ylabel("Customers")
plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_vs_bottom_5_customers.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 vs bottom 5 customers chart saved successfully.")# Create top 5 vs bottom 5 quantity comparison chart
plt.figure(figsize=(10, 6))

x = range(len(top_5_performance))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    top_5_performance["Quantity"],
    width=width,
    label="Top 5 Quantity"
)

plt.bar(
    [i + width / 2 for i in x],
    bottom_5_performance["Quantity"],
    width=width,
    label="Bottom 5 Quantity"
)

plt.xticks(
    list(x),
    ["Rank 1", "Rank 2", "Rank 3", "Rank 4", "Rank 5"]
)

plt.title("Top 5 vs Bottom 5 Monthly Quantity")
plt.xlabel("Performance Rank")
plt.ylabel("Quantity")
plt.legend()
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_vs_bottom_5_quantity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nTop 5 vs bottom 5 quantity chart saved successfully.")# Create monthly outlier severity chart
severity_mapping = {
    "None": 0,
    "Low": 1,
    "Moderate": 2,
    "High": 3
}

outlier_severity_values = (
    outlier_summary["Outlier_Severity"]
    .map(severity_mapping)
)

plt.figure(figsize=(10, 6))

plt.bar(
    outlier_summary["Metric"],
    outlier_severity_values
)

plt.title("Monthly Outlier Severity by Metric")
plt.xlabel("Metric")
plt.ylabel("Outlier Severity")

plt.yticks(
    [0, 1, 2, 3],
    ["None", "Low", "Moderate", "High"]
)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_outlier_severity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nMonthly outlier severity chart saved successfully.")# Create final visualization index
visualization_index = pd.DataFrame({
    "Visualization": [
        "Monthly Mean vs Median",
        "Monthly Standard Deviation",
        "Monthly Coefficient of Variation",
        "Monthly Outlier Count",
        "Monthly Outlier Percentage",
        "Best vs Worst Monthly Performance",
        "Top 5 Revenue Months",
        "Top 5 Orders Months",
        "Top 5 Customers Months",
        "Top 5 Quantity Months",
        "Bottom 5 Revenue Months",
        "Bottom 5 Orders Months",
        "Bottom 5 Customers Months",
        "Bottom 5 Quantity Months",
        "Top vs Bottom 5 Revenue",
        "Top vs Bottom 5 Orders",
        "Top vs Bottom 5 Customers",
        "Top vs Bottom 5 Quantity",
        "Monthly Outlier Severity"
    ],
    "File_Name": [
        "monthly_mean_vs_median.png",
        "monthly_standard_deviation.png",
        "monthly_coefficient_of_variation.png",
        "monthly_outlier_count.png",
        "monthly_outlier_percentage.png",
        "best_vs_worst_monthly_performance.png",
        "top_5_revenue_months.png",
        "top_5_orders_months.png",
        "top_5_customers_months.png",
        "top_5_quantity_months.png",
        "bottom_5_revenue_months.png",
        "bottom_5_orders_months.png",
        "bottom_5_customers_months.png",
        "bottom_5_quantity_months.png",
        "top_vs_bottom_5_revenue.png",
        "top_vs_bottom_5_orders.png",
        "top_vs_bottom_5_customers.png",
        "top_vs_bottom_5_quantity.png",
        "monthly_outlier_severity.png"
    ]
})

visualization_index.to_csv(
    OUTPUT_DIR / "visualization_index.csv",
    index=False
)

print("\nVisualization index saved successfully.")# Create visualization completion status
visualization_completion_status = pd.DataFrame({
    "Project_Stage": [
        "Data Visualization"
    ],
    "Status": [
        "Completed"
    ],
    "Total_Visualizations": [
        len(visualization_index)
    ]
})

visualization_completion_status.to_csv(
    OUTPUT_DIR / "visualization_completion_status.csv",
    index=False
)

print("\n========================================")
print("DATA VISUALIZATION COMPLETED")
print("========================================")
print("Visualization completion status saved successfully.")