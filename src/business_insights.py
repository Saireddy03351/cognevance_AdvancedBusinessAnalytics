# Import required libraries
import pandas as pd
from pathlib import Path
# Create output directory for business insights
OUTPUT_DIR = Path("outputs/business_insights")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

print("Business insights output directory created successfully.")# Load final monthly analysis dashboard
monthly_dashboard = pd.read_csv(
    "outputs/final_monthly_analysis_dashboard.csv"
)

print("\nFinal monthly analysis dashboard loaded successfully.")
print(monthly_dashboard.head())
# Load final project KPI summary
kpi_summary = pd.read_csv(
    "outputs/final_project_kpi_summary.csv"
)

print("\nFinal project KPI summary loaded successfully.")
print(kpi_summary)
# Load final project summary
project_summary = pd.read_csv(
    "outputs/final_project_summary.csv"
)

print("\nFinal project summary loaded successfully.")
print(project_summary)
# Load monthly performance comparison
performance_comparison = pd.read_csv(
    "outputs/monthly_performance_comparison.csv"
)

print("\nMonthly performance comparison loaded successfully.")
print(performance_comparison)# Load combined growth highlights
growth_highlights = pd.read_csv(
    "outputs/combined_growth_highlights.csv"
)

print("\nCombined growth highlights loaded successfully.")
print(growth_highlights)# Extract variability insights from project summary
most_variable_metric = project_summary.loc[
    project_summary["Summary_Item"] == "Most Variable Metric",
    "Value"
].iloc[0]

most_stable_metric = project_summary.loc[
    project_summary["Summary_Item"] == "Most Stable Metric",
    "Value"
].iloc[0]

print("\nVariability insights extracted successfully.")
print("Most Variable Metric:", most_variable_metric)
print("Most Stable Metric:", most_stable_metric)# Extract outlier insights from project summary
metric_with_most_outliers = project_summary.loc[
    project_summary["Summary_Item"] == "Metric With Most Outliers",
    "Value"
].iloc[0]

highest_outlier_percentage_metric = project_summary.loc[
    project_summary["Summary_Item"] == "Highest Outlier Percentage Metric",
    "Value"
].iloc[0]

lowest_outlier_percentage_metric = project_summary.loc[
    project_summary["Summary_Item"] == "Lowest Outlier Percentage Metric",
    "Value"
].iloc[0]

print("\nOutlier insights extracted successfully.")
print("Metric With Most Outliers:", metric_with_most_outliers)
print(
    "Highest Outlier Percentage Metric:",
    highest_outlier_percentage_metric
)
print(
    "Lowest Outlier Percentage Metric:",
    lowest_outlier_percentage_metric
)# Extract best and worst revenue performance
revenue_performance = performance_comparison[
    performance_comparison["Metric"] == "Revenue"
].iloc[0]

best_revenue_month = revenue_performance["Best_Month"]
best_revenue_value = revenue_performance["Best_Value"]

worst_revenue_month = revenue_performance["Worst_Month"]
worst_revenue_value = revenue_performance["Worst_Value"]

print("\nRevenue performance insights extracted successfully.")
print("Best Revenue Month:", best_revenue_month)
print("Best Revenue Value:", best_revenue_value)
print("Worst Revenue Month:", worst_revenue_month)
print("Worst Revenue Value:", worst_revenue_value)# Extract best and worst orders performance
orders_performance = performance_comparison[
    performance_comparison["Metric"] == "Orders"
].iloc[0]

best_orders_month = orders_performance["Best_Month"]
best_orders_value = orders_performance["Best_Value"]

worst_orders_month = orders_performance["Worst_Month"]
worst_orders_value = orders_performance["Worst_Value"]

print("\nOrders performance insights extracted successfully.")
print("Best Orders Month:", best_orders_month)
print("Best Orders Value:", best_orders_value)
print("Worst Orders Month:", worst_orders_month)
print("Worst Orders Value:", worst_orders_value)# Extract best and worst customers performance
customers_performance = performance_comparison[
    performance_comparison["Metric"] == "Customers"
].iloc[0]

best_customers_month = customers_performance["Best_Month"]
best_customers_value = customers_performance["Best_Value"]

worst_customers_month = customers_performance["Worst_Month"]
worst_customers_value = customers_performance["Worst_Value"]

print("\nCustomers performance insights extracted successfully.")
print("Best Customers Month:", best_customers_month)
print("Best Customers Value:", best_customers_value)
print("Worst Customers Month:", worst_customers_month)
print("Worst Customers Value:", worst_customers_value)# Extract best and worst quantity performance
quantity_performance = performance_comparison[
    performance_comparison["Metric"] == "Quantity"
].iloc[0]

best_quantity_month = quantity_performance["Best_Month"]
best_quantity_value = quantity_performance["Best_Value"]

worst_quantity_month = quantity_performance["Worst_Month"]
worst_quantity_value = quantity_performance["Worst_Value"]

print("\nQuantity performance insights extracted successfully.")
print("Best Quantity Month:", best_quantity_month)
print("Best Quantity Value:", best_quantity_value)
print("Worst Quantity Month:", worst_quantity_month)
print("Worst Quantity Value:", worst_quantity_value)# Create best vs worst performance insights summary
performance_insights = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Best_Month": [
        best_revenue_month,
        best_orders_month,
        best_customers_month,
        best_quantity_month
    ],
    "Best_Value": [
        best_revenue_value,
        best_orders_value,
        best_customers_value,
        best_quantity_value
    ],
    "Worst_Month": [
        worst_revenue_month,
        worst_orders_month,
        worst_customers_month,
        worst_quantity_month
    ],
    "Worst_Value": [
        worst_revenue_value,
        worst_orders_value,
        worst_customers_value,
        worst_quantity_value
    ]
})

performance_insights.to_csv(
    OUTPUT_DIR / "performance_insights.csv",
    index=False
)

print("\nPerformance insights summary saved successfully.")# Create variability business insights summary
variability_insights = pd.DataFrame({
    "Insight": [
        "Most Variable Metric",
        "Most Stable Metric"
    ],
    "Metric": [
        most_variable_metric,
        most_stable_metric
    ],
    "Business_Interpretation": [
        f"{most_variable_metric} shows the greatest relative month-to-month variability.",
        f"{most_stable_metric} shows the most consistent month-to-month performance."
    ]
})

variability_insights.to_csv(
    OUTPUT_DIR / "variability_insights.csv",
    index=False
)

print("\nVariability business insights saved successfully.")# Create outlier business insights summary
outlier_insights = pd.DataFrame({
    "Insight": [
        "Metric With Most Outliers",
        "Highest Outlier Percentage Metric",
        "Lowest Outlier Percentage Metric"
    ],
    "Metric": [
        metric_with_most_outliers,
        highest_outlier_percentage_metric,
        lowest_outlier_percentage_metric
    ],
    "Business_Interpretation": [
        f"{metric_with_most_outliers} recorded the highest number of unusual monthly observations.",
        f"{highest_outlier_percentage_metric} has the highest proportion of months classified as outliers.",
        f"{lowest_outlier_percentage_metric} has the lowest proportion of months classified as outliers."
    ]
})

outlier_insights.to_csv(
    OUTPUT_DIR / "outlier_insights.csv",
    index=False
)

print("\nOutlier business insights saved successfully.")# Create performance gap insights
performance_gap_insights = performance_insights.copy()

performance_gap_insights["Performance_Gap"] = (
    performance_gap_insights["Best_Value"]
    - performance_gap_insights["Worst_Value"]
)

performance_gap_insights["Performance_Gap_Percentage"] = (
    performance_gap_insights["Performance_Gap"]
    / performance_gap_insights["Worst_Value"]
    * 100
).round(2)

performance_gap_insights.to_csv(
    OUTPUT_DIR / "performance_gap_insights.csv",
    index=False
)

print("\nPerformance gap insights saved successfully.")# Identify metric with the largest performance gap
largest_gap_row = performance_gap_insights.loc[
    performance_gap_insights["Performance_Gap_Percentage"].idxmax()
]

largest_gap_metric = largest_gap_row["Metric"]
largest_gap_percentage = largest_gap_row["Performance_Gap_Percentage"]

print("\nLargest performance gap identified successfully.")
print("Metric:", largest_gap_metric)
print("Performance Gap Percentage:", largest_gap_percentage)# Create largest performance gap insight
largest_gap_insight = pd.DataFrame({
    "Insight": [
        "Largest Performance Gap Metric"
    ],
    "Metric": [
        largest_gap_metric
    ],
    "Performance_Gap_Percentage": [
        largest_gap_percentage
    ],
    "Business_Interpretation": [
        f"{largest_gap_metric} shows the largest percentage difference "
        "between its best and worst monthly performance."
    ]
})

largest_gap_insight.to_csv(
    OUTPUT_DIR / "largest_performance_gap_insight.csv",
    index=False
)

print("\nLargest performance gap insight saved successfully.")# Create actionable business recommendations
business_recommendations = pd.DataFrame({
    "Recommendation_ID": [
        "R1",
        "R2",
        "R3",
        "R4"
    ],
    "Focus_Area": [
        "Performance Variability",
        "Outlier Monitoring",
        "Performance Gap",
        "Best Month Strategy"
    ],
    "Recommendation": [
        f"Monitor {most_variable_metric} closely because it shows the greatest month-to-month variability.",
        f"Investigate unusual changes in {metric_with_most_outliers} because it recorded the highest number of outliers.",
        f"Develop improvement strategies for {largest_gap_metric} because it shows the largest gap between best and worst monthly performance.",
        f"Study the factors contributing to the strong performance in {best_revenue_month} and use them to improve weaker revenue months."
    ]
})

business_recommendations.to_csv(
    OUTPUT_DIR / "business_recommendations.csv",
    index=False
)

print("\nBusiness recommendations saved successfully.")# Create final business insights report
final_business_insights = pd.DataFrame({
    "Insight_Category": [
        "Most Variable Metric",
        "Most Stable Metric",
        "Metric With Most Outliers",
        "Highest Outlier Percentage",
        "Lowest Outlier Percentage",
        "Largest Performance Gap",
        "Best Revenue Month",
        "Worst Revenue Month"
    ],
    "Finding": [
        most_variable_metric,
        most_stable_metric,
        metric_with_most_outliers,
        highest_outlier_percentage_metric,
        lowest_outlier_percentage_metric,
        largest_gap_metric,
        best_revenue_month,
        worst_revenue_month
    ]
})

final_business_insights.to_csv(
    OUTPUT_DIR / "final_business_insights.csv",
    index=False
)

print("\nFinal business insights report saved successfully.")# Create business insights completion status
business_insights_status = pd.DataFrame({
    "Project_Stage": [
        "Business Insights"
    ],
    "Status": [
        "Completed"
    ],
    "Total_Insight_Files": [
        6
    ]
})

business_insights_status.to_csv(
    OUTPUT_DIR / "business_insights_completion_status.csv",
    index=False
)

print("\n========================================")
print("BUSINESS INSIGHTS COMPLETED")
print("========================================")
print("Business insights completion status saved successfully.")