from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "Online_Retail_Processed.csv"

# Load processed dataset
print("Loading processed dataset...")

df = pd.read_csv(DATA_FILE)

print("Processed dataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()
# Calculate overall business KPIs
total_revenue = df["TotalPrice"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()
total_products = df["StockCode"].nunique()

print("\n--- OVERALL BUSINESS KPIs ---")
print(f"Total Revenue: £{total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Total Products: {total_products:,}")
# Calculate Average Order Value
order_values = df.groupby("InvoiceNo")["TotalPrice"].sum()
average_order_value = order_values.mean()

print("\n--- AVERAGE ORDER VALUE ---")
print(f"Average Order Value: £{average_order_value:,.2f}")
# Calculate Average Items per Order
items_per_order = df.groupby("InvoiceNo")["Quantity"].sum()
average_items_per_order = items_per_order.mean()

print("\n--- AVERAGE ITEMS PER ORDER ---")
print(f"Average Items per Order: {average_items_per_order:,.2f}")
# Calculate Average Revenue per Customer
customer_revenue = df.groupby("CustomerID")["TotalPrice"].sum()
average_revenue_per_customer = customer_revenue.mean()

print("\n--- AVERAGE REVENUE PER CUSTOMER ---")
print(f"Average Revenue per Customer: £{average_revenue_per_customer:,.2f}")
# Top 10 products by revenue
top_products_revenue = (
    df.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 PRODUCTS BY REVENUE ---")
print(top_products_revenue)
# Top 10 products by quantity sold
top_products_quantity = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 PRODUCTS BY QUANTITY SOLD ---")
print(top_products_quantity)
# Top 10 countries by revenue
top_countries_revenue = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 COUNTRIES BY REVENUE ---")
print(top_countries_revenue)
# Top 10 customers by revenue
top_customers_revenue = (
    df.groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 CUSTOMERS BY REVENUE ---")
print(top_customers_revenue)
# Calculate monthly revenue trend
monthly_revenue = (
    df.groupby("YearMonth")["TotalPrice"]
    .sum()
    .sort_index()
)

print("\n--- MONTHLY REVENUE TREND ---")
print(monthly_revenue)
# Calculate revenue by day of week
day_revenue = (
    df.groupby("DayOfWeek")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY DAY OF WEEK ---")
print(day_revenue)
# Calculate revenue by time of day
time_of_day_revenue = (
    df.groupby("TimeOfDay")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY TIME OF DAY ---")
print(time_of_day_revenue)
# Calculate revenue by season
season_revenue = (
    df.groupby("Season")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY SEASON ---")
print(season_revenue)
# Calculate revenue by quarter
quarter_revenue = (
    df.groupby("Quarter")["TotalPrice"]
    .sum()
    .sort_index()
)

print("\n--- REVENUE BY QUARTER ---")
print(quarter_revenue)
# Calculate weekday vs weekend revenue
weekend_revenue = (
    df.groupby("IsWeekend")["TotalPrice"]
    .sum()
)

print("\n--- WEEKDAY VS WEEKEND REVENUE ---")
print(weekend_revenue)
# Calculate revenue by order value category
order_value_revenue = (
    df.groupby("OrderValueCategory")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY ORDER VALUE CATEGORY ---")
print(order_value_revenue)
# Calculate number of unique orders by time of day
orders_by_time = (
    df.groupby("TimeOfDay")["InvoiceNo"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n--- ORDERS BY TIME OF DAY ---")
print(orders_by_time)
# Calculate number of unique orders by day of week
orders_by_day = (
    df.groupby("DayOfWeek")["InvoiceNo"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n--- ORDERS BY DAY OF WEEK ---")
print(orders_by_day)
# Calculate monthly order trend
monthly_orders = (
    df.groupby("YearMonth")["InvoiceNo"]
    .nunique()
    .sort_index()
)

print("\n--- MONTHLY ORDER TREND ---")
print(monthly_orders)
# Calculate monthly unique customer trend
monthly_customers = (
    df.groupby("YearMonth")["CustomerID"]
    .nunique()
    .sort_index()
)

print("\n--- MONTHLY CUSTOMER TREND ---")
print(monthly_customers)
# Calculate monthly average order value
monthly_order_values = (
    df.groupby(["YearMonth", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("YearMonth")
    .mean()
    .sort_index()
)

print("\n--- MONTHLY AVERAGE ORDER VALUE ---")
print(monthly_order_values)
# Calculate monthly quantity sold
monthly_quantity = (
    df.groupby("YearMonth")["Quantity"]
    .sum()
    .sort_index()
)

print("\n--- MONTHLY QUANTITY SOLD ---")
print(monthly_quantity)
# Calculate monthly revenue growth rate
monthly_revenue_growth = monthly_revenue.pct_change() * 100

print("\n--- MONTHLY REVENUE GROWTH RATE (%) ---")
print(monthly_revenue_growth.round(2))
# Calculate monthly order growth rate
monthly_order_growth = monthly_orders.pct_change() * 100

print("\n--- MONTHLY ORDER GROWTH RATE (%) ---")
print(monthly_order_growth.round(2))
# Calculate monthly customer growth rate
monthly_customer_growth = monthly_customers.pct_change() * 100

print("\n--- MONTHLY CUSTOMER GROWTH RATE (%) ---")
print(monthly_customer_growth.round(2))
# Calculate revenue by customer type
customer_type_revenue = (
    df.groupby("CustomerType")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- REVENUE BY CUSTOMER TYPE ---")
print(customer_type_revenue)
# Calculate unique customers by country
customers_by_country = (
    df.groupby("Country")["CustomerID"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 COUNTRIES BY CUSTOMER COUNT ---")
print(customers_by_country)
# Calculate unique orders by country
orders_by_country = (
    df.groupby("Country")["InvoiceNo"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 COUNTRIES BY ORDER COUNT ---")
print(orders_by_country)
# Calculate average order value by country
country_order_values = (
    df.groupby(["Country", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("Country")
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 COUNTRIES BY AVERAGE ORDER VALUE ---")
print(country_order_values)
# Calculate top 10 customers by order frequency
top_customers_frequency = (
    df.groupby("CustomerID")["InvoiceNo"]
    .nunique()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 CUSTOMERS BY ORDER FREQUENCY ---")
print(top_customers_frequency)
# Calculate top 10 customers by total quantity purchased
top_customers_quantity = (
    df.groupby("CustomerID")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 CUSTOMERS BY QUANTITY PURCHASED ---")
print(top_customers_quantity)
# Calculate top 10 customers by average order value
customer_average_order_value = (
    df.groupby(["CustomerID", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("CustomerID")
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 CUSTOMERS BY AVERAGE ORDER VALUE ---")
print(customer_average_order_value)
# Calculate repeat customer rate
customer_order_counts = df.groupby("CustomerID")["InvoiceNo"].nunique()

repeat_customers = (customer_order_counts > 1).sum()
total_unique_customers = customer_order_counts.count()

repeat_customer_rate = (
    repeat_customers / total_unique_customers
) * 100

print("\n--- REPEAT CUSTOMER RATE ---")
print(f"Total Unique Customers: {total_unique_customers:,}")
print(f"Repeat Customers: {repeat_customers:,}")
print(f"Repeat Customer Rate: {repeat_customer_rate:.2f}%")
# Calculate one-time customer rate
one_time_customers = (customer_order_counts == 1).sum()

one_time_customer_rate = (
    one_time_customers / total_unique_customers
) * 100

print("\n--- ONE-TIME CUSTOMER RATE ---")
print(f"One-Time Customers: {one_time_customers:,}")
print(f"One-Time Customer Rate: {one_time_customer_rate:.2f}%")
# Calculate revenue contribution of top 10 customers
customer_total_revenue = (
    df.groupby("CustomerID")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

top_10_customer_revenue = customer_total_revenue.head(10).sum()

top_10_revenue_contribution = (
    top_10_customer_revenue / total_revenue
) * 100

print("\n--- TOP 10 CUSTOMER REVENUE CONTRIBUTION ---")
print(f"Top 10 Customer Revenue: £{top_10_customer_revenue:,.2f}")
print(f"Revenue Contribution: {top_10_revenue_contribution:.2f}%")
# Calculate revenue contribution of top 10 products
product_total_revenue = (
    df.groupby("Description")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

top_10_product_revenue = product_total_revenue.head(10).sum()

top_10_product_contribution = (
    top_10_product_revenue / total_revenue
) * 100

print("\n--- TOP 10 PRODUCT REVENUE CONTRIBUTION ---")
print(f"Top 10 Product Revenue: £{top_10_product_revenue:,.2f}")
print(f"Revenue Contribution: {top_10_product_contribution:.2f}%")
# Calculate revenue contribution of top 10 countries
country_total_revenue = (
    df.groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

top_10_country_revenue = country_total_revenue.head(10).sum()

top_10_country_contribution = (
    top_10_country_revenue / total_revenue
) * 100

print("\n--- TOP 10 COUNTRY REVENUE CONTRIBUTION ---")
print(f"Top 10 Country Revenue: £{top_10_country_revenue:,.2f}")
print(f"Revenue Contribution: {top_10_country_contribution:.2f}%")
# Identify the highest revenue month
best_revenue_month = monthly_revenue.idxmax()
best_revenue_value = monthly_revenue.max()

print("\n--- HIGHEST REVENUE MONTH ---")
print(f"Best Revenue Month: {best_revenue_month}")
print(f"Revenue: £{best_revenue_value:,.2f}")
# Identify the lowest revenue month
lowest_revenue_month = monthly_revenue.idxmin()
lowest_revenue_value = monthly_revenue.min()

print("\n--- LOWEST REVENUE MONTH ---")
print(f"Lowest Revenue Month: {lowest_revenue_month}")
print(f"Revenue: £{lowest_revenue_value:,.2f}")
# Identify the month with the highest number of orders
best_order_month = monthly_orders.idxmax()
best_order_count = monthly_orders.max()

print("\n--- HIGHEST ORDER MONTH ---")
print(f"Highest Order Month: {best_order_month}")
print(f"Number of Orders: {best_order_count:,}")
# Identify the month with the lowest number of orders
lowest_order_month = monthly_orders.idxmin()
lowest_order_count = monthly_orders.min()

print("\n--- LOWEST ORDER MONTH ---")
print(f"Lowest Order Month: {lowest_order_month}")
print(f"Number of Orders: {lowest_order_count:,}")
# Identify the month with the highest number of unique customers
best_customer_month = monthly_customers.idxmax()
best_customer_count = monthly_customers.max()

print("\n--- HIGHEST CUSTOMER MONTH ---")
print(f"Highest Customer Month: {best_customer_month}")
print(f"Unique Customers: {best_customer_count:,}")
# Identify the month with the lowest number of unique customers
lowest_customer_month = monthly_customers.idxmin()
lowest_customer_count = monthly_customers.min()

print("\n--- LOWEST CUSTOMER MONTH ---")
print(f"Lowest Customer Month: {lowest_customer_month}")
print(f"Unique Customers: {lowest_customer_count:,}")
# Identify the day of the week with the highest revenue
best_revenue_day = day_revenue.idxmax()
best_revenue_day_value = day_revenue.max()

print("\n--- HIGHEST REVENUE DAY OF WEEK ---")
print(f"Best Revenue Day: {best_revenue_day}")
print(f"Revenue: £{best_revenue_day_value:,.2f}")
# Identify the day of the week with the lowest revenue
lowest_revenue_day = day_revenue.idxmin()
lowest_revenue_day_value = day_revenue.min()

print("\n--- LOWEST REVENUE DAY OF WEEK ---")
print(f"Lowest Revenue Day: {lowest_revenue_day}")
print(f"Revenue: £{lowest_revenue_day_value:,.2f}")
# Identify the time of day with the highest revenue
best_time_of_day = time_of_day_revenue.idxmax()
best_time_revenue = time_of_day_revenue.max()

print("\n--- HIGHEST REVENUE TIME OF DAY ---")
print(f"Best Time of Day: {best_time_of_day}")
print(f"Revenue: £{best_time_revenue:,.2f}")
# Identify the time of day with the lowest revenue
lowest_time_of_day = time_of_day_revenue.idxmin()
lowest_time_revenue = time_of_day_revenue.min()

print("\n--- LOWEST REVENUE TIME OF DAY ---")
print(f"Lowest Time of Day: {lowest_time_of_day}")
print(f"Revenue: £{lowest_time_revenue:,.2f}")
# Identify the season with the highest revenue
best_revenue_season = season_revenue.idxmax()
best_season_revenue = season_revenue.max()

print("\n--- HIGHEST REVENUE SEASON ---")
print(f"Best Revenue Season: {best_revenue_season}")
print(f"Revenue: £{best_season_revenue:,.2f}")
# Identify the season with the lowest revenue
lowest_revenue_season = season_revenue.idxmin()
lowest_season_revenue = season_revenue.min()

print("\n--- LOWEST REVENUE SEASON ---")
print(f"Lowest Revenue Season: {lowest_revenue_season}")
print(f"Revenue: £{lowest_season_revenue:,.2f}")
# Identify the quarter with the highest revenue
best_revenue_quarter = quarter_revenue.idxmax()
best_quarter_revenue = quarter_revenue.max()

print("\n--- HIGHEST REVENUE QUARTER ---")
print(f"Best Revenue Quarter: Q{best_revenue_quarter}")
print(f"Revenue: £{best_quarter_revenue:,.2f}")
# Identify the quarter with the lowest revenue
lowest_revenue_quarter = quarter_revenue.idxmin()
lowest_quarter_revenue = quarter_revenue.min()

print("\n--- LOWEST REVENUE QUARTER ---")
print(f"Lowest Revenue Quarter: Q{lowest_revenue_quarter}")
print(f"Revenue: £{lowest_quarter_revenue:,.2f}")
# Identify the highest revenue country excluding the United Kingdom
international_revenue = (
    df[df["Country"] != "United Kingdom"]
    .groupby("Country")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

top_international_country = international_revenue.idxmax()
top_international_revenue = international_revenue.max()

print("\n--- TOP INTERNATIONAL MARKET ---")
print(f"Top Country: {top_international_country}")
print(f"Revenue: £{top_international_revenue:,.2f}")
# Compare UK revenue with international revenue
uk_revenue = df.loc[
    df["Country"] == "United Kingdom", "TotalPrice"
].sum()

international_total_revenue = df.loc[
    df["Country"] != "United Kingdom", "TotalPrice"
].sum()

print("\n--- UK VS INTERNATIONAL REVENUE ---")
print(f"United Kingdom Revenue: £{uk_revenue:,.2f}")
print(f"International Revenue: £{international_total_revenue:,.2f}")
# Calculate UK vs international revenue percentage
uk_revenue_percentage = (uk_revenue / total_revenue) * 100
international_revenue_percentage = (
    international_total_revenue / total_revenue
) * 100

print("\n--- UK VS INTERNATIONAL REVENUE PERCENTAGE ---")
print(f"United Kingdom: {uk_revenue_percentage:.2f}%")
print(f"International Markets: {international_revenue_percentage:.2f}%")
# Compare UK customers with international customers
uk_customers = df.loc[
    df["Country"] == "United Kingdom", "CustomerID"
].nunique()

international_customers = df.loc[
    df["Country"] != "United Kingdom", "CustomerID"
].nunique()

print("\n--- UK VS INTERNATIONAL CUSTOMER COUNT ---")
print(f"United Kingdom Customers: {uk_customers:,}")
print(f"International Customers: {international_customers:,}")
# Compare UK orders with international orders
uk_orders = df.loc[
    df["Country"] == "United Kingdom", "InvoiceNo"
].nunique()

international_orders = df.loc[
    df["Country"] != "United Kingdom", "InvoiceNo"
].nunique()

print("\n--- UK VS INTERNATIONAL ORDER COUNT ---")
print(f"United Kingdom Orders: {uk_orders:,}")
print(f"International Orders: {international_orders:,}")
# Calculate UK vs international average order value
uk_average_order_value = (
    df[df["Country"] == "United Kingdom"]
    .groupby("InvoiceNo")["TotalPrice"]
    .sum()
    .mean()
)

international_average_order_value = (
    df[df["Country"] != "United Kingdom"]
    .groupby("InvoiceNo")["TotalPrice"]
    .sum()
    .mean()
)

print("\n--- UK VS INTERNATIONAL AVERAGE ORDER VALUE ---")
print(f"United Kingdom Average Order Value: £{uk_average_order_value:,.2f}")
print(f"International Average Order Value: £{international_average_order_value:,.2f}")
# Calculate revenue per order by month
monthly_revenue_per_order = (
    monthly_revenue / monthly_orders
)

print("\n--- MONTHLY REVENUE PER ORDER ---")
print(monthly_revenue_per_order.round(2))
# Calculate revenue per customer by month
monthly_revenue_per_customer = (
    monthly_revenue / monthly_customers
)

print("\n--- MONTHLY REVENUE PER CUSTOMER ---")
print(monthly_revenue_per_customer.round(2))
# Calculate orders per customer by month
monthly_orders_per_customer = (
    monthly_orders / monthly_customers
)

print("\n--- MONTHLY ORDERS PER CUSTOMER ---")
print(monthly_orders_per_customer.round(2))
# Calculate quantity purchased per customer by month
monthly_quantity_per_customer = (
    monthly_quantity / monthly_customers
)

print("\n--- MONTHLY QUANTITY PER CUSTOMER ---")
print(monthly_quantity_per_customer.round(2))
# Calculate revenue by hour of day
hourly_revenue = (
    df.groupby("Hour")["TotalPrice"]
    .sum()
    .sort_index()
)

print("\n--- REVENUE BY HOUR OF DAY ---")
print(hourly_revenue)
# Identify the hour with the highest revenue
best_revenue_hour = hourly_revenue.idxmax()
best_hour_revenue = hourly_revenue.max()

print("\n--- HIGHEST REVENUE HOUR ---")
print(f"Best Revenue Hour: {best_revenue_hour}:00")
print(f"Revenue: £{best_hour_revenue:,.2f}")
# Identify the hour with the lowest revenue
lowest_revenue_hour = hourly_revenue.idxmin()
lowest_hour_revenue = hourly_revenue.min()

print("\n--- LOWEST REVENUE HOUR ---")
print(f"Lowest Revenue Hour: {lowest_revenue_hour}:00")
print(f"Revenue: £{lowest_hour_revenue:,.2f}")
# Calculate number of unique orders by hour of day
hourly_orders = (
    df.groupby("Hour")["InvoiceNo"]
    .nunique()
    .sort_index()
)

print("\n--- ORDERS BY HOUR OF DAY ---")
print(hourly_orders)
# Identify the hour with the highest number of orders
busiest_order_hour = hourly_orders.idxmax()
highest_hourly_orders = hourly_orders.max()

print("\n--- BUSIEST ORDER HOUR ---")
print(f"Busiest Order Hour: {busiest_order_hour}:00")
print(f"Number of Orders: {highest_hourly_orders:,}")
# Identify the hour with the lowest number of orders
quietest_order_hour = hourly_orders.idxmin()
lowest_hourly_orders = hourly_orders.min()

print("\n--- QUIETEST ORDER HOUR ---")
print(f"Quietest Order Hour: {quietest_order_hour}:00")
print(f"Number of Orders: {lowest_hourly_orders:,}")
# Calculate total quantity sold by hour of day
hourly_quantity = (
    df.groupby("Hour")["Quantity"]
    .sum()
    .sort_index()
)

print("\n--- QUANTITY SOLD BY HOUR OF DAY ---")
print(hourly_quantity)
# Identify the hour with the highest quantity sold
highest_quantity_hour = hourly_quantity.idxmax()
highest_hourly_quantity = hourly_quantity.max()

print("\n--- HIGHEST QUANTITY SOLD HOUR ---")
print(f"Highest Quantity Hour: {highest_quantity_hour}:00")
print(f"Quantity Sold: {highest_hourly_quantity:,}")
# Identify the hour with the lowest quantity sold
lowest_quantity_hour = hourly_quantity.idxmin()
lowest_hourly_quantity = hourly_quantity.min()

print("\n--- LOWEST QUANTITY SOLD HOUR ---")
print(f"Lowest Quantity Hour: {lowest_quantity_hour}:00")
print(f"Quantity Sold: {lowest_hourly_quantity:,}")
# Calculate average order value by hour of day
hourly_average_order_value = (
    df.groupby(["Hour", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("Hour")
    .mean()
    .sort_index()
)

print("\n--- AVERAGE ORDER VALUE BY HOUR ---")
print(hourly_average_order_value.round(2))
# Identify the hour with the highest average order value
highest_aov_hour = hourly_average_order_value.idxmax()
highest_hourly_aov = hourly_average_order_value.max()

print("\n--- HIGHEST AVERAGE ORDER VALUE HOUR ---")
print(f"Highest AOV Hour: {highest_aov_hour}:00")
print(f"Average Order Value: £{highest_hourly_aov:,.2f}")
# Identify the hour with the lowest average order value
lowest_aov_hour = hourly_average_order_value.idxmin()
lowest_hourly_aov = hourly_average_order_value.min()

print("\n--- LOWEST AVERAGE ORDER VALUE HOUR ---")
print(f"Lowest AOV Hour: {lowest_aov_hour}:00")
print(f"Average Order Value: £{lowest_hourly_aov:,.2f}")
# Calculate revenue by month name
month_name_revenue = (
    df.groupby("MonthName")["TotalPrice"]
    .sum()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
)

print("\n--- REVENUE BY MONTH NAME ---")
print(month_name_revenue)
# Identify the calendar month with the highest revenue
highest_revenue_month_name = month_name_revenue.idxmax()
highest_month_name_revenue = month_name_revenue.max()

print("\n--- HIGHEST REVENUE MONTH NAME ---")
print(f"Highest Revenue Month: {highest_revenue_month_name}")
print(f"Revenue: £{highest_month_name_revenue:,.2f}")
# Identify the calendar month with the lowest revenue
lowest_revenue_month_name = month_name_revenue.idxmin()
lowest_month_name_revenue = month_name_revenue.min()

print("\n--- LOWEST REVENUE MONTH NAME ---")
print(f"Lowest Revenue Month: {lowest_revenue_month_name}")
print(f"Revenue: £{lowest_month_name_revenue:,.2f}")
# Calculate unique orders by month name
month_name_orders = (
    df.groupby("MonthName")["InvoiceNo"]
    .nunique()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
)

print("\n--- ORDERS BY MONTH NAME ---")
print(month_name_orders)
# Identify the calendar month with the highest number of orders
highest_order_month_name = month_name_orders.idxmax()
highest_month_name_orders = month_name_orders.max()

print("\n--- HIGHEST ORDER MONTH NAME ---")
print(f"Highest Order Month: {highest_order_month_name}")
print(f"Number of Orders: {highest_month_name_orders:,}")
# Identify the calendar month with the lowest number of orders
lowest_order_month_name = month_name_orders.idxmin()
lowest_month_name_orders = month_name_orders.min()

print("\n--- LOWEST ORDER MONTH NAME ---")
print(f"Lowest Order Month: {lowest_order_month_name}")
print(f"Number of Orders: {lowest_month_name_orders:,}")
# Calculate unique customers by month name
month_name_customers = (
    df.groupby("MonthName")["CustomerID"]
    .nunique()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
)

print("\n--- CUSTOMERS BY MONTH NAME ---")
print(month_name_customers)
# Identify the calendar month with the highest number of unique customers
highest_customer_month_name = month_name_customers.idxmax()
highest_month_name_customers = month_name_customers.max()

print("\n--- HIGHEST CUSTOMER MONTH NAME ---")
print(f"Highest Customer Month: {highest_customer_month_name}")
print(f"Unique Customers: {highest_month_name_customers:,}")
# Identify the calendar month with the lowest number of unique customers
lowest_customer_month_name = month_name_customers.idxmin()
lowest_month_name_customers = month_name_customers.min()

print("\n--- LOWEST CUSTOMER MONTH NAME ---")
print(f"Lowest Customer Month: {lowest_customer_month_name}")
print(f"Unique Customers: {lowest_month_name_customers:,}")
# Calculate total quantity sold by month name
month_name_quantity = (
    df.groupby("MonthName")["Quantity"]
    .sum()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
)

print("\n--- QUANTITY SOLD BY MONTH NAME ---")
print(month_name_quantity)
# Identify the calendar month with the highest quantity sold
highest_quantity_month_name = month_name_quantity.idxmax()
highest_month_name_quantity = month_name_quantity.max()

print("\n--- HIGHEST QUANTITY SOLD MONTH ---")
print(f"Highest Quantity Month: {highest_quantity_month_name}")
print(f"Quantity Sold: {highest_month_name_quantity:,}")
# Identify the calendar month with the lowest quantity sold
lowest_quantity_month_name = month_name_quantity.idxmin()
lowest_month_name_quantity = month_name_quantity.min()

print("\n--- LOWEST QUANTITY SOLD MONTH ---")
print(f"Lowest Quantity Month: {lowest_quantity_month_name}")
print(f"Quantity Sold: {lowest_month_name_quantity:,}")
# Calculate average order value by month name
month_name_average_order_value = (
    df.groupby(["MonthName", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("MonthName")
    .mean()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
)

print("\n--- AVERAGE ORDER VALUE BY MONTH NAME ---")
print(month_name_average_order_value.round(2))
# Identify the calendar month with the highest average order value
highest_aov_month_name = month_name_average_order_value.idxmax()
highest_month_name_aov = month_name_average_order_value.max()

print("\n--- HIGHEST AVERAGE ORDER VALUE MONTH ---")
print(f"Highest AOV Month: {highest_aov_month_name}")
print(f"Average Order Value: £{highest_month_name_aov:,.2f}")
# Identify the calendar month with the lowest average order value
lowest_aov_month_name = month_name_average_order_value.idxmin()
lowest_month_name_aov = month_name_average_order_value.min()

print("\n--- LOWEST AVERAGE ORDER VALUE MONTH ---")
print(f"Lowest AOV Month: {lowest_aov_month_name}")
print(f"Average Order Value: £{lowest_month_name_aov:,.2f}")
# Calculate total revenue by year
yearly_revenue = (
    df.groupby("Year")["TotalPrice"]
    .sum()
    .sort_index()
)

print("\n--- REVENUE BY YEAR ---")
print(yearly_revenue)
# Calculate unique orders by year
yearly_orders = (
    df.groupby("Year")["InvoiceNo"]
    .nunique()
    .sort_index()
)

print("\n--- ORDERS BY YEAR ---")
print(yearly_orders)
# Calculate unique customers by year
yearly_customers = (
    df.groupby("Year")["CustomerID"]
    .nunique()
    .sort_index()
)

print("\n--- CUSTOMERS BY YEAR ---")
print(yearly_customers)
# Calculate total quantity sold by year
yearly_quantity = (
    df.groupby("Year")["Quantity"]
    .sum()
    .sort_index()
)

print("\n--- QUANTITY SOLD BY YEAR ---")
print(yearly_quantity)
# Calculate average order value by year
yearly_average_order_value = (
    df.groupby(["Year", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("Year")
    .mean()
    .sort_index()
)

print("\n--- AVERAGE ORDER VALUE BY YEAR ---")
print(yearly_average_order_value.round(2))
# Calculate revenue per customer by year
yearly_revenue_per_customer = (
    yearly_revenue / yearly_customers
)

print("\n--- REVENUE PER CUSTOMER BY YEAR ---")
print(yearly_revenue_per_customer.round(2))
# Calculate orders per customer by year
yearly_orders_per_customer = (
    yearly_orders / yearly_customers
)

print("\n--- ORDERS PER CUSTOMER BY YEAR ---")
print(yearly_orders_per_customer.round(2))
# Calculate quantity purchased per customer by year
yearly_quantity_per_customer = (
    yearly_quantity / yearly_customers
)

print("\n--- QUANTITY PER CUSTOMER BY YEAR ---")
print(yearly_quantity_per_customer.round(2))
# Calculate revenue by weekday in correct order
weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

weekday_revenue_ordered = (
    df.groupby("DayOfWeek")["TotalPrice"]
    .sum()
    .reindex(weekday_order)
)

print("\n--- REVENUE BY WEEKDAY (ORDERED) ---")
print(weekday_revenue_ordered)
# Calculate unique orders by weekday in correct order
weekday_orders_ordered = (
    df.groupby("DayOfWeek")["InvoiceNo"]
    .nunique()
    .reindex(weekday_order)
)

print("\n--- ORDERS BY WEEKDAY (ORDERED) ---")
print(weekday_orders_ordered)
# Calculate total quantity sold by weekday in correct order
weekday_quantity_ordered = (
    df.groupby("DayOfWeek")["Quantity"]
    .sum()
    .reindex(weekday_order)
)

print("\n--- QUANTITY SOLD BY WEEKDAY (ORDERED) ---")
print(weekday_quantity_ordered)
# Calculate average order value by weekday
weekday_average_order_value = (
    df.groupby(["DayOfWeek", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("DayOfWeek")
    .mean()
    .reindex(weekday_order)
)

print("\n--- AVERAGE ORDER VALUE BY WEEKDAY ---")
print(weekday_average_order_value.round(2))
# Identify the weekday with the highest average order value
highest_aov_weekday = weekday_average_order_value.idxmax()
highest_weekday_aov = weekday_average_order_value.max()

print("\n--- HIGHEST AVERAGE ORDER VALUE WEEKDAY ---")
print(f"Highest AOV Weekday: {highest_aov_weekday}")
print(f"Average Order Value: £{highest_weekday_aov:,.2f}")
# Identify the weekday with the lowest average order value
lowest_aov_weekday = weekday_average_order_value.idxmin()
lowest_weekday_aov = weekday_average_order_value.min()

print("\n--- LOWEST AVERAGE ORDER VALUE WEEKDAY ---")
print(f"Lowest AOV Weekday: {lowest_aov_weekday}")
print(f"Average Order Value: £{lowest_weekday_aov:,.2f}")
# Calculate unique customers by weekday in correct order
weekday_customers_ordered = (
    df.groupby("DayOfWeek")["CustomerID"]
    .nunique()
    .reindex(weekday_order)
)

print("\n--- CUSTOMERS BY WEEKDAY (ORDERED) ---")
print(weekday_customers_ordered)
# Identify the weekday with the highest number of unique customers
highest_customer_weekday = weekday_customers_ordered.idxmax()
highest_weekday_customers = weekday_customers_ordered.max()

print("\n--- HIGHEST CUSTOMER WEEKDAY ---")
print(f"Highest Customer Weekday: {highest_customer_weekday}")
print(f"Unique Customers: {highest_weekday_customers:,}")
# Identify the weekday with the lowest number of unique customers
lowest_customer_weekday = weekday_customers_ordered.idxmin()
lowest_weekday_customers = weekday_customers_ordered.min()

print("\n--- LOWEST CUSTOMER WEEKDAY ---")
print(f"Lowest Customer Weekday: {lowest_customer_weekday}")
print(f"Unique Customers: {lowest_weekday_customers:,}")
# Calculate revenue per customer by weekday
weekday_revenue_per_customer = (
    weekday_revenue_ordered / weekday_customers_ordered
)

print("\n--- REVENUE PER CUSTOMER BY WEEKDAY ---")
print(weekday_revenue_per_customer.round(2))
# Calculate orders per customer by weekday
weekday_orders_per_customer = (
    weekday_orders_ordered / weekday_customers_ordered
)

print("\n--- ORDERS PER CUSTOMER BY WEEKDAY ---")
print(weekday_orders_per_customer.round(2))
# Calculate quantity purchased per customer by weekday
weekday_quantity_per_customer = (
    weekday_quantity_ordered / weekday_customers_ordered
)

print("\n--- QUANTITY PER CUSTOMER BY WEEKDAY ---")
print(weekday_quantity_per_customer.round(2))
# Calculate revenue by time of day in correct order
time_of_day_order = ["Morning", "Afternoon", "Evening"]

time_of_day_revenue_ordered = (
    df.groupby("TimeOfDay")["TotalPrice"]
    .sum()
    .reindex(time_of_day_order)
)

print("\n--- REVENUE BY TIME OF DAY (ORDERED) ---")
print(time_of_day_revenue_ordered)
# Calculate unique orders by time of day
time_of_day_orders = (
    df.groupby("TimeOfDay")["InvoiceNo"]
    .nunique()
    .reindex(time_of_day_order)
)

print("\n--- ORDERS BY TIME OF DAY ---")
print(time_of_day_orders)
# Calculate total quantity sold by time of day
time_of_day_quantity = (
    df.groupby("TimeOfDay")["Quantity"]
    .sum()
    .reindex(time_of_day_order)
)

print("\n--- QUANTITY SOLD BY TIME OF DAY ---")
print(time_of_day_quantity)
# Calculate average order value by time of day
time_of_day_average_order_value = (
    df.groupby(["TimeOfDay", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("TimeOfDay")
    .mean()
    .reindex(time_of_day_order)
)

print("\n--- AVERAGE ORDER VALUE BY TIME OF DAY ---")
print(time_of_day_average_order_value.round(2))
# Calculate unique customers by time of day
time_of_day_customers = (
    df.groupby("TimeOfDay")["CustomerID"]
    .nunique()
    .reindex(time_of_day_order)
)

print("\n--- CUSTOMERS BY TIME OF DAY ---")
print(time_of_day_customers)
# Calculate revenue per customer by time of day
time_of_day_revenue_per_customer = (
    time_of_day_revenue_ordered / time_of_day_customers
)

print("\n--- REVENUE PER CUSTOMER BY TIME OF DAY ---")
print(time_of_day_revenue_per_customer.round(2))
# Calculate orders per customer by time of day
time_of_day_orders_per_customer = (
    time_of_day_orders / time_of_day_customers
)

print("\n--- ORDERS PER CUSTOMER BY TIME OF DAY ---")
print(time_of_day_orders_per_customer.round(2))
# Calculate quantity purchased per customer by time of day
time_of_day_quantity_per_customer = (
    time_of_day_quantity / time_of_day_customers
)

print("\n--- QUANTITY PER CUSTOMER BY TIME OF DAY ---")
print(time_of_day_quantity_per_customer.round(2))
# Calculate revenue by season in correct order
season_order = ["Winter", "Spring", "Summer", "Autumn"]

season_revenue_ordered = (
    df.groupby("Season")["TotalPrice"]
    .sum()
    .reindex(season_order)
)

print("\n--- REVENUE BY SEASON (ORDERED) ---")
print(season_revenue_ordered)
# Calculate unique orders by season
season_orders_ordered = (
    df.groupby("Season")["InvoiceNo"]
    .nunique()
    .reindex(season_order)
)

print("\n--- ORDERS BY SEASON (ORDERED) ---")
print(season_orders_ordered)
# Calculate total quantity sold by season
season_quantity_ordered = (
    df.groupby("Season")["Quantity"]
    .sum()
    .reindex(season_order)
)

print("\n--- QUANTITY SOLD BY SEASON (ORDERED) ---")
print(season_quantity_ordered)
# Calculate average order value by season
season_average_order_value = (
    df.groupby(["Season", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("Season")
    .mean()
    .reindex(season_order)
)

print("\n--- AVERAGE ORDER VALUE BY SEASON ---")
print(season_average_order_value.round(2))
# Calculate unique customers by season
season_customers_ordered = (
    df.groupby("Season")["CustomerID"]
    .nunique()
    .reindex(season_order)
)

print("\n--- CUSTOMERS BY SEASON (ORDERED) ---")
print(season_customers_ordered)
# Calculate revenue per customer by season
season_revenue_per_customer = (
    season_revenue_ordered / season_customers_ordered
)

print("\n--- REVENUE PER CUSTOMER BY SEASON ---")
print(season_revenue_per_customer.round(2))
# Calculate orders per customer by season
season_orders_per_customer = (
    season_orders_ordered / season_customers_ordered
)

print("\n--- ORDERS PER CUSTOMER BY SEASON ---")
print(season_orders_per_customer.round(2))
# Calculate quantity purchased per customer by season
season_quantity_per_customer = (
    season_quantity_ordered / season_customers_ordered
)

print("\n--- QUANTITY PER CUSTOMER BY SEASON ---")
print(season_quantity_per_customer.round(2))
# Calculate revenue by quarter in correct order
quarter_order = [1, 2, 3, 4]

quarter_revenue_ordered = (
    df.groupby("Quarter")["TotalPrice"]
    .sum()
    .reindex(quarter_order)
)

print("\n--- REVENUE BY QUARTER (ORDERED) ---")
print(quarter_revenue_ordered)
# Calculate unique orders by quarter
quarter_orders_ordered = (
    df.groupby("Quarter")["InvoiceNo"]
    .nunique()
    .reindex(quarter_order)
)

print("\n--- ORDERS BY QUARTER (ORDERED) ---")
print(quarter_orders_ordered)
# Calculate total quantity sold by quarter
quarter_quantity_ordered = (
    df.groupby("Quarter")["Quantity"]
    .sum()
    .reindex(quarter_order)
)

print("\n--- QUANTITY SOLD BY QUARTER (ORDERED) ---")
print(quarter_quantity_ordered)
# Calculate average order value by quarter
quarter_average_order_value = (
    df.groupby(["Quarter", "InvoiceNo"])["TotalPrice"]
    .sum()
    .groupby("Quarter")
    .mean()
    .reindex(quarter_order)
)

print("\n--- AVERAGE ORDER VALUE BY QUARTER ---")
print(quarter_average_order_value.round(2))
# Calculate unique customers by quarter
quarter_customers_ordered = (
    df.groupby("Quarter")["CustomerID"]
    .nunique()
    .reindex(quarter_order)
)

print("\n--- CUSTOMERS BY QUARTER (ORDERED) ---")
print(quarter_customers_ordered)
# Calculate revenue per customer by quarter
quarter_revenue_per_customer = (
    quarter_revenue_ordered / quarter_customers_ordered
)

print("\n--- REVENUE PER CUSTOMER BY QUARTER ---")
print(quarter_revenue_per_customer.round(2))
# Calculate orders per customer by quarter
quarter_orders_per_customer = (
    quarter_orders_ordered / quarter_customers_ordered
)

print("\n--- ORDERS PER CUSTOMER BY QUARTER ---")
print(quarter_orders_per_customer.round(2))
# Calculate quantity purchased per customer by quarter
quarter_quantity_per_customer = (
    quarter_quantity_ordered / quarter_customers_ordered
)

print("\n--- QUANTITY PER CUSTOMER BY QUARTER ---")
print(quarter_quantity_per_customer.round(2))
# Calculate revenue percentage by customer type
customer_type_revenue_percentage = (
    customer_type_revenue / total_revenue
) * 100

print("\n--- REVENUE PERCENTAGE BY CUSTOMER TYPE ---")
print(customer_type_revenue_percentage.round(2))
# Calculate transaction count by customer type
customer_type_transactions = (
    df.groupby("CustomerType")
    .size()
    .sort_values(ascending=False)
)

print("\n--- TRANSACTION COUNT BY CUSTOMER TYPE ---")
print(customer_type_transactions)
# Calculate transaction percentage by customer type
customer_type_transaction_percentage = (
    customer_type_transactions / customer_type_transactions.sum()
) * 100

print("\n--- TRANSACTION PERCENTAGE BY CUSTOMER TYPE ---")
print(customer_type_transaction_percentage.round(2))
# Calculate average revenue per transaction by customer type
customer_type_avg_transaction_value = (
    customer_type_revenue / customer_type_transactions
)

print("\n--- AVERAGE REVENUE PER TRANSACTION BY CUSTOMER TYPE ---")
print(customer_type_avg_transaction_value.round(2))
# Calculate total quantity sold by customer type
customer_type_quantity = (
    df.groupby("CustomerType")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- QUANTITY SOLD BY CUSTOMER TYPE ---")
print(customer_type_quantity)
# Calculate quantity percentage by customer type
customer_type_quantity_percentage = (
    customer_type_quantity / customer_type_quantity.sum()
) * 100

print("\n--- QUANTITY PERCENTAGE BY CUSTOMER TYPE ---")
print(customer_type_quantity_percentage.round(2))
# Calculate average quantity per transaction by customer type
customer_type_avg_quantity_per_transaction = (
    customer_type_quantity / customer_type_transactions
)

print("\n--- AVERAGE QUANTITY PER TRANSACTION BY CUSTOMER TYPE ---")
print(customer_type_avg_quantity_per_transaction.round(2))
# Calculate unique orders by customer type
customer_type_orders = (
    df.groupby("CustomerType")["InvoiceNo"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n--- UNIQUE ORDERS BY CUSTOMER TYPE ---")
print(customer_type_orders)
# Calculate order percentage by customer type
customer_type_order_percentage = (
    customer_type_orders / customer_type_orders.sum()
) * 100

print("\n--- ORDER PERCENTAGE BY CUSTOMER TYPE ---")
print(customer_type_order_percentage.round(2))
# Calculate average order value by customer type
customer_type_average_order_value = (
    customer_type_revenue / customer_type_orders
)

print("\n--- AVERAGE ORDER VALUE BY CUSTOMER TYPE ---")
print(customer_type_average_order_value.round(2))
# Calculate unique customers by customer type
customer_type_customers = (
    df.groupby("CustomerType")["CustomerID"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n--- UNIQUE CUSTOMERS BY CUSTOMER TYPE ---")
print(customer_type_customers)
# Calculate customer percentage by customer type
customer_type_customer_percentage = (
    customer_type_customers / customer_type_customers.sum()
) * 100

print("\n--- CUSTOMER PERCENTAGE BY CUSTOMER TYPE ---")
print(customer_type_customer_percentage.round(2))
# Calculate revenue per customer by customer type
customer_type_revenue_per_customer = (
    customer_type_revenue / customer_type_customers
)

print("\n--- REVENUE PER CUSTOMER BY CUSTOMER TYPE ---")
print(customer_type_revenue_per_customer.round(2))
# Calculate orders per customer by customer type
customer_type_orders_per_customer = (
    customer_type_orders / customer_type_customers
)

print("\n--- ORDERS PER CUSTOMER BY CUSTOMER TYPE ---")
print(customer_type_orders_per_customer.round(2))
# Calculate quantity per customer by customer type
customer_type_quantity_per_customer = (
    customer_type_quantity / customer_type_customers
)

print("\n--- QUANTITY PER CUSTOMER BY CUSTOMER TYPE ---")
print(customer_type_quantity_per_customer.round(2))
# Calculate transactions per customer by customer type
customer_type_transactions_per_customer = (
    customer_type_transactions / customer_type_customers
)

print("\n--- TRANSACTIONS PER CUSTOMER BY CUSTOMER TYPE ---")
print(customer_type_transactions_per_customer.round(2))
# Create customer type summary table
customer_type_summary = pd.DataFrame({
    "Revenue": customer_type_revenue,
    "Revenue_Percentage": customer_type_revenue_percentage,
    "Transactions": customer_type_transactions,
    "Transaction_Percentage": customer_type_transaction_percentage,
    "Orders": customer_type_orders,
    "Order_Percentage": customer_type_order_percentage,
    "Customers": customer_type_customers,
    "Customer_Percentage": customer_type_customer_percentage,
    "Quantity": customer_type_quantity,
    "Quantity_Percentage": customer_type_quantity_percentage,
    "Average_Order_Value": customer_type_average_order_value,
    "Revenue_Per_Customer": customer_type_revenue_per_customer,
    "Orders_Per_Customer": customer_type_orders_per_customer,
    "Quantity_Per_Customer": customer_type_quantity_per_customer,
    "Transactions_Per_Customer": customer_type_transactions_per_customer
})

print("\n--- CUSTOMER TYPE SUMMARY TABLE ---")
print(customer_type_summary.round(2))
# Save customer type summary table to CSV
customer_type_summary.to_csv(
    "outputs/customer_type_summary.csv",
    index=True
)

print("\nCustomer type summary saved successfully.")
# Create monthly analysis summary table
monthly_summary = pd.DataFrame({
    "Revenue": monthly_revenue,
    "Orders": monthly_orders,
    "Customers": monthly_customers,
    "Quantity": monthly_quantity,
    "Revenue_Per_Order": monthly_revenue_per_order,
    "Revenue_Per_Customer": monthly_revenue_per_customer,
    "Orders_Per_Customer": monthly_orders_per_customer,
    "Quantity_Per_Customer": monthly_quantity_per_customer
})

monthly_summary.to_csv(
    "outputs/monthly_summary.csv",
    index=True
)

print("\nMonthly summary saved successfully.")
# Create weekday analysis summary table
weekday_summary = pd.DataFrame({
    "Revenue": weekday_revenue_ordered,
    "Orders": weekday_orders_ordered,
    "Customers": weekday_customers_ordered,
    "Quantity": weekday_quantity_ordered,
    "Average_Order_Value": weekday_average_order_value,
    "Revenue_Per_Customer": weekday_revenue_per_customer,
    "Orders_Per_Customer": weekday_orders_per_customer,
    "Quantity_Per_Customer": weekday_quantity_per_customer
})

weekday_summary.to_csv(
    "outputs/weekday_summary.csv",
    index=True
)

print("\nWeekday summary saved successfully.")
# Create time-of-day analysis summary table
time_of_day_summary = pd.DataFrame({
    "Revenue": time_of_day_revenue_ordered,
    "Orders": time_of_day_orders,
    "Customers": time_of_day_customers,
    "Quantity": time_of_day_quantity,
    "Average_Order_Value": time_of_day_average_order_value,
    "Revenue_Per_Customer": time_of_day_revenue_per_customer,
    "Orders_Per_Customer": time_of_day_orders_per_customer,
    "Quantity_Per_Customer": time_of_day_quantity_per_customer
})

time_of_day_summary.to_csv(
    "outputs/time_of_day_summary.csv",
    index=True
)

print("\nTime-of-day summary saved successfully.")
# Create seasonal analysis summary table
season_summary = pd.DataFrame({
    "Revenue": season_revenue_ordered,
    "Orders": season_orders_ordered,
    "Customers": season_customers_ordered,
    "Quantity": season_quantity_ordered,
    "Average_Order_Value": season_average_order_value,
    "Revenue_Per_Customer": season_revenue_per_customer,
    "Orders_Per_Customer": season_orders_per_customer,
    "Quantity_Per_Customer": season_quantity_per_customer
})

season_summary.to_csv(
    "outputs/season_summary.csv",
    index=True
)

print("\nSeason summary saved successfully.")
# Create quarterly analysis summary table
quarter_summary = pd.DataFrame({
    "Revenue": quarter_revenue_ordered,
    "Orders": quarter_orders_ordered,
    "Customers": quarter_customers_ordered,
    "Quantity": quarter_quantity_ordered,
    "Average_Order_Value": quarter_average_order_value,
    "Revenue_Per_Customer": quarter_revenue_per_customer,
    "Orders_Per_Customer": quarter_orders_per_customer,
    "Quantity_Per_Customer": quarter_quantity_per_customer
})

quarter_summary.to_csv(
    "outputs/quarter_summary.csv",
    index=True
)

print("\nQuarter summary saved successfully.")# Create yearly analysis summary table
yearly_summary = pd.DataFrame({
    "Revenue": yearly_revenue,
    "Orders": yearly_orders,
    "Customers": yearly_customers,
    "Quantity": yearly_quantity,
    "Average_Order_Value": yearly_average_order_value,
    "Revenue_Per_Customer": yearly_revenue_per_customer,
    "Orders_Per_Customer": yearly_orders_per_customer,
    "Quantity_Per_Customer": yearly_quantity_per_customer
})

yearly_summary.to_csv(
    "outputs/yearly_summary.csv",
    index=True
)

print("\nYearly summary saved successfully.")
# Create hourly analysis summary table
hourly_summary = pd.DataFrame({
    "Revenue": hourly_revenue,
    "Orders": hourly_orders,
    "Quantity": hourly_quantity,
    "Average_Order_Value": hourly_average_order_value
})

hourly_summary.to_csv(
    "outputs/hourly_summary.csv",
    index=True
)

print("\nHourly summary saved successfully.")
# Create month-name analysis summary table
month_name_summary = pd.DataFrame({
    "Revenue": month_name_revenue,
    "Orders": month_name_orders,
    "Customers": month_name_customers,
    "Quantity": month_name_quantity,
    "Average_Order_Value": month_name_average_order_value
})

month_name_summary.to_csv(
    "outputs/month_name_summary.csv",
    index=True
)

print("\nMonth-name summary saved successfully.")
# Create country analysis summary table
country_summary = df.groupby("Country").agg(
    Revenue=("TotalPrice", "sum"),
    Orders=("InvoiceNo", "nunique"),
    Customers=("CustomerID", "nunique"),
    Quantity=("Quantity", "sum")
)

country_summary["Average_Order_Value"] = (
    country_summary["Revenue"] / country_summary["Orders"]
)

country_summary = country_summary.sort_values(
    "Revenue",
    ascending=False
)

country_summary.to_csv(
    "outputs/country_summary.csv",
    index=True
)

print("\nCountry summary saved successfully.")
# Create top 10 countries by revenue table
top_10_countries_revenue = country_summary.head(10)

top_10_countries_revenue.to_csv(
    "outputs/top_10_countries_revenue.csv",
    index=True
)

print("\nTop 10 countries by revenue saved successfully.")
# Create top 10 countries by number of orders table
top_10_countries_orders = (
    country_summary
    .sort_values("Orders", ascending=False)
    .head(10)
)

top_10_countries_orders.to_csv(
    "outputs/top_10_countries_orders.csv",
    index=True
)

print("\nTop 10 countries by orders saved successfully.")
# Create top 10 countries by number of unique customers table
top_10_countries_customers = (
    country_summary
    .sort_values("Customers", ascending=False)
    .head(10)
)

top_10_countries_customers.to_csv(
    "outputs/top_10_countries_customers.csv",
    index=True
)

print("\nTop 10 countries by customers saved successfully.")
# Create top 10 countries by quantity sold table
top_10_countries_quantity = (
    country_summary
    .sort_values("Quantity", ascending=False)
    .head(10)
)

top_10_countries_quantity.to_csv(
    "outputs/top_10_countries_quantity.csv",
    index=True
)

print("\nTop 10 countries by quantity saved successfully.")
# Create top 10 countries by average order value table
top_10_countries_aov = (
    country_summary
    .sort_values("Average_Order_Value", ascending=False)
    .head(10)
)

top_10_countries_aov.to_csv(
    "outputs/top_10_countries_aov.csv",
    index=True
)

print("\nTop 10 countries by average order value saved successfully.")
# Create product-level analysis summary table
product_summary = df.groupby(["StockCode", "Description"]).agg(
    Revenue=("TotalPrice", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("InvoiceNo", "nunique"),
    Customers=("CustomerID", "nunique")
)

product_summary["Revenue_Per_Order"] = (
    product_summary["Revenue"] / product_summary["Orders"]
)

product_summary = product_summary.sort_values(
    "Revenue",
    ascending=False
)

product_summary.to_csv(
    "outputs/product_summary.csv",
    index=True
)

print("\nProduct summary saved successfully.")
# Create top 10 products by revenue table
top_10_products_revenue = (
    product_summary
    .sort_values("Revenue", ascending=False)
    .head(10)
)

top_10_products_revenue.to_csv(
    "outputs/top_10_products_revenue.csv",
    index=True
)

print("\nTop 10 products by revenue saved successfully.")
# Create top 10 products by quantity sold table
top_10_products_quantity = (
    product_summary
    .sort_values("Quantity", ascending=False)
    .head(10)
)

top_10_products_quantity.to_csv(
    "outputs/top_10_products_quantity.csv",
    index=True
)

print("\nTop 10 products by quantity saved successfully.")
# Create top 10 products by number of unique orders table
top_10_products_orders = (
    product_summary
    .sort_values("Orders", ascending=False)
    .head(10)
)

top_10_products_orders.to_csv(
    "outputs/top_10_products_orders.csv",
    index=True
)

print("\nTop 10 products by orders saved successfully.")
# Create top 10 products by number of unique customers table
top_10_products_customers = (
    product_summary
    .sort_values("Customers", ascending=False)
    .head(10)
)

top_10_products_customers.to_csv(
    "outputs/top_10_products_customers.csv",
    index=True
)

print("\nTop 10 products by customers saved successfully.")
# Create top 10 products by revenue per order table
top_10_products_revenue_per_order = (
    product_summary
    .sort_values("Revenue_Per_Order", ascending=False)
    .head(10)
)

top_10_products_revenue_per_order.to_csv(
    "outputs/top_10_products_revenue_per_order.csv",
    index=True
)

print("\nTop 10 products by revenue per order saved successfully.")
# Create overall KPI summary table
overall_kpi_summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Orders",
        "Total Customers",
        "Total Quantity",
        "Average Order Value"
    ],
    "Value": [
        total_revenue,
        df["InvoiceNo"].nunique(),
        df["CustomerID"].nunique(),
        df["Quantity"].sum(),
        total_revenue / df["InvoiceNo"].nunique()
    ]
})

overall_kpi_summary.to_csv(
    "outputs/overall_kpi_summary.csv",
    index=False
)

print("\nOverall KPI summary saved successfully.")
# Create key business insights file
highest_revenue_country = country_summary["Revenue"].idxmax()
highest_revenue_product = product_summary["Revenue"].idxmax()
highest_revenue_month = monthly_revenue.idxmax()
highest_revenue_weekday = weekday_revenue_ordered.idxmax()

with open("outputs/key_business_insights.txt", "w", encoding="utf-8") as file:
    file.write("KEY BUSINESS INSIGHTS\n")
    file.write("=====================\n\n")

    file.write(f"Highest Revenue Country: {highest_revenue_country}\n")
    file.write(f"Highest Revenue Product: {highest_revenue_product}\n")
    file.write(f"Highest Revenue Month: {highest_revenue_month}\n")
    file.write(f"Highest Revenue Weekday: {highest_revenue_weekday}\n")

print("\nKey business insights saved successfully.")
# Calculate additional key business insights
highest_revenue_hour = hourly_revenue.idxmax()
highest_revenue_season = season_revenue_ordered.idxmax()
highest_revenue_quarter = quarter_revenue_ordered.idxmax()
highest_customer_type = customer_type_revenue.idxmax()

with open("outputs/key_business_insights.txt", "a", encoding="utf-8") as file:
    file.write("\nADDITIONAL BUSINESS INSIGHTS\n")
    file.write("============================\n\n")

    file.write(f"Highest Revenue Hour: {highest_revenue_hour}\n")
    file.write(f"Highest Revenue Season: {highest_revenue_season}\n")
    file.write(f"Highest Revenue Quarter: Q{highest_revenue_quarter}\n")
    file.write(f"Highest Revenue Customer Type: {highest_customer_type}\n")

print("\nAdditional business insights saved successfully.")# Create data quality summary table
data_quality_summary = pd.DataFrame({
    "Column": df.columns,
    "Missing_Values": df.isnull().sum().values,
    "Unique_Values": df.nunique().values,
    "Data_Type": df.dtypes.astype(str).values
})

data_quality_summary.to_csv(
    "outputs/data_quality_summary.csv",
    index=False
)

print("\nData quality summary saved successfully.")
# Create dataset overview summary
dataset_overview = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Unique Orders",
        "Unique Customers",
        "Unique Products",
        "Countries"
    ],
    "Value": [
        len(df),
        len(df.columns),
        df["InvoiceNo"].nunique(),
        df["CustomerID"].nunique(),
        df["StockCode"].nunique(),
        df["Country"].nunique()
    ]
})

dataset_overview.to_csv(
    "outputs/dataset_overview.csv",
    index=False
)

print("\nDataset overview saved successfully.")
# Create dataset date-range summary
# Create dataset date-range summary
invoice_dates = pd.to_datetime(df["InvoiceDate"])

date_range_summary = pd.DataFrame({
    "Metric": [
        "Start Date",
        "End Date",
        "Total Days Covered"
    ],
    "Value": [
        invoice_dates.min().strftime("%Y-%m-%d"),
        invoice_dates.max().strftime("%Y-%m-%d"),
        (invoice_dates.max() - invoice_dates.min()).days
    ]
})

date_range_summary.to_csv(
    "outputs/date_range_summary.csv",
    index=False
)

print("\nDate-range summary saved successfully.")
# Create revenue descriptive statistics summary
revenue_statistics = df["TotalPrice"].describe().reset_index()

revenue_statistics.columns = [
    "Statistic",
    "Value"
]

revenue_statistics.to_csv(
    "outputs/revenue_statistics.csv",
    index=False
)

print("\nRevenue statistics saved successfully.")
# Create quantity descriptive statistics summary
quantity_statistics = df["Quantity"].describe().reset_index()

quantity_statistics.columns = [
    "Statistic",
    "Value"
]

quantity_statistics.to_csv(
    "outputs/quantity_statistics.csv",
    index=False
)

print("\nQuantity statistics saved successfully.")
# Create unit price descriptive statistics summary
unit_price_statistics = df["UnitPrice"].describe().reset_index()

unit_price_statistics.columns = [
    "Statistic",
    "Value"
]

unit_price_statistics.to_csv(
    "outputs/unit_price_statistics.csv",
    index=False
)

print("\nUnit price statistics saved successfully.")
# Create correlation matrix for key numerical variables
correlation_matrix = df[
    ["Quantity", "UnitPrice", "TotalPrice"]
].corr()

correlation_matrix.to_csv(
    "outputs/correlation_matrix.csv",
    index=True
)

print("\nCorrelation matrix saved successfully.")
# Create daily sales summary
daily_sales_summary = (
    df.assign(Date=pd.to_datetime(df["InvoiceDate"]).dt.date)
    .groupby("Date")
    .agg(
        Revenue=("TotalPrice", "sum"),
        Orders=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
        Quantity=("Quantity", "sum")
    )
)

daily_sales_summary.to_csv(
    "outputs/daily_sales_summary.csv",
    index=True
)

print("\nDaily sales summary saved successfully.")
# Create weekly sales summary
weekly_sales_summary = (
    df.assign(
        Week=pd.to_datetime(df["InvoiceDate"]).dt.to_period("W").astype(str)
    )
    .groupby("Week")
    .agg(
        Revenue=("TotalPrice", "sum"),
        Orders=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
        Quantity=("Quantity", "sum")
    )
)

weekly_sales_summary.to_csv(
    "outputs/weekly_sales_summary.csv",
    index=True
)

print("\nWeekly sales summary saved successfully.")
# Calculate daily average order value
daily_aov_summary = daily_sales_summary.copy()

daily_aov_summary["Average_Order_Value"] = (
    daily_aov_summary["Revenue"] /
    daily_aov_summary["Orders"]
)

daily_aov_summary.to_csv(
    "outputs/daily_aov_summary.csv",
    index=True
)

print("\nDaily average order value summary saved successfully.")
# Calculate weekly average order value
weekly_aov_summary = weekly_sales_summary.copy()

weekly_aov_summary["Average_Order_Value"] = (
    weekly_aov_summary["Revenue"] /
    weekly_aov_summary["Orders"]
)

weekly_aov_summary.to_csv(
    "outputs/weekly_aov_summary.csv",
    index=True
)

print("\nWeekly average order value summary saved successfully.")
# Create monthly revenue growth analysis
monthly_growth_summary = pd.DataFrame({
    "Revenue": monthly_revenue
})

monthly_growth_summary["Revenue_Growth_Percentage"] = (
    monthly_growth_summary["Revenue"]
    .pct_change(fill_method=None) * 100
)

monthly_growth_summary.to_csv(
    "outputs/monthly_growth_summary.csv",
    index=True
)

print("\nMonthly growth summary saved successfully.")
# Create monthly order growth analysis
monthly_order_growth_summary = pd.DataFrame({
    "Orders": monthly_orders
})

monthly_order_growth_summary["Order_Growth_Percentage"] = (
    monthly_order_growth_summary["Orders"]
    .pct_change(fill_method=None) * 100
)

monthly_order_growth_summary.to_csv(
    "outputs/monthly_order_growth_summary.csv",
    index=True
)

print("\nMonthly order growth summary saved successfully.")
# Create monthly customer growth analysis
monthly_customer_growth_summary = pd.DataFrame({
    "Customers": monthly_customers
})

monthly_customer_growth_summary["Customer_Growth_Percentage"] = (
    monthly_customer_growth_summary["Customers"]
    .pct_change(fill_method=None) * 100
)

monthly_customer_growth_summary.to_csv(
    "outputs/monthly_customer_growth_summary.csv",
    index=True
)

print("\nMonthly customer growth summary saved successfully.")
# Create monthly quantity growth analysis
monthly_quantity_growth_summary = pd.DataFrame({
    "Quantity": monthly_quantity
})

monthly_quantity_growth_summary["Quantity_Growth_Percentage"] = (
    monthly_quantity_growth_summary["Quantity"]
    .pct_change(fill_method=None) * 100
)

monthly_quantity_growth_summary.to_csv(
    "outputs/monthly_quantity_growth_summary.csv",
    index=True
)

print("\nMonthly quantity growth summary saved successfully.")
# Create combined monthly growth summary
combined_monthly_growth = pd.DataFrame({
    "Revenue": monthly_revenue,
    "Revenue_Growth_Percentage":
        monthly_growth_summary["Revenue_Growth_Percentage"],
    "Orders": monthly_orders,
    "Order_Growth_Percentage":
        monthly_order_growth_summary["Order_Growth_Percentage"],
    "Customers": monthly_customers,
    "Customer_Growth_Percentage":
        monthly_customer_growth_summary["Customer_Growth_Percentage"],
    "Quantity": monthly_quantity,
    "Quantity_Growth_Percentage":
        monthly_quantity_growth_summary["Quantity_Growth_Percentage"]
})

combined_monthly_growth.to_csv(
    "outputs/combined_monthly_growth.csv",
    index=True
)

print("\nCombined monthly growth summary saved successfully.")
# Identify best and worst monthly revenue growth
valid_revenue_growth = combined_monthly_growth[
    "Revenue_Growth_Percentage"
].dropna()

best_revenue_growth_month = valid_revenue_growth.idxmax()
best_revenue_growth_value = valid_revenue_growth.max()

worst_revenue_growth_month = valid_revenue_growth.idxmin()
worst_revenue_growth_value = valid_revenue_growth.min()

print("\n--- MONTHLY REVENUE GROWTH HIGHLIGHTS ---")
print(
    f"Best Revenue Growth Month: {best_revenue_growth_month} "
    f"({best_revenue_growth_value:.2f}%)"
)
print(
    f"Worst Revenue Growth Month: {worst_revenue_growth_month} "
    f"({worst_revenue_growth_value:.2f}%)"
)
# Create monthly revenue growth highlights summary
revenue_growth_highlights = pd.DataFrame({
    "Metric": [
        "Best Revenue Growth Month",
        "Best Revenue Growth Percentage",
        "Worst Revenue Growth Month",
        "Worst Revenue Growth Percentage"
    ],
    "Value": [
        str(best_revenue_growth_month),
        round(best_revenue_growth_value, 2),
        str(worst_revenue_growth_month),
        round(worst_revenue_growth_value, 2)
    ]
})

revenue_growth_highlights.to_csv(
    "outputs/revenue_growth_highlights.csv",
    index=False
)

print("\nRevenue growth highlights saved successfully.")
# Identify best and worst monthly order growth
valid_order_growth = combined_monthly_growth[
    "Order_Growth_Percentage"
].dropna()

best_order_growth_month = valid_order_growth.idxmax()
best_order_growth_value = valid_order_growth.max()

worst_order_growth_month = valid_order_growth.idxmin()
worst_order_growth_value = valid_order_growth.min()

print("\n--- MONTHLY ORDER GROWTH HIGHLIGHTS ---")
print(
    f"Best Order Growth Month: {best_order_growth_month} "
    f"({best_order_growth_value:.2f}%)"
)
print(
    f"Worst Order Growth Month: {worst_order_growth_month} "
    f"({worst_order_growth_value:.2f}%)"
)
# Create monthly order growth highlights summary
order_growth_highlights = pd.DataFrame({
    "Metric": [
        "Best Order Growth Month",
        "Best Order Growth Percentage",
        "Worst Order Growth Month",
        "Worst Order Growth Percentage"
    ],
    "Value": [
        str(best_order_growth_month),
        round(best_order_growth_value, 2),
        str(worst_order_growth_month),
        round(worst_order_growth_value, 2)
    ]
})

order_growth_highlights.to_csv(
    "outputs/order_growth_highlights.csv",
    index=False
)

print("\nOrder growth highlights saved successfully.")# Identify best and worst monthly customer growth
valid_customer_growth = combined_monthly_growth[
    "Customer_Growth_Percentage"
].dropna()

best_customer_growth_month = valid_customer_growth.idxmax()
best_customer_growth_value = valid_customer_growth.max()

worst_customer_growth_month = valid_customer_growth.idxmin()
worst_customer_growth_value = valid_customer_growth.min()

print("\n--- MONTHLY CUSTOMER GROWTH HIGHLIGHTS ---")
print(
    f"Best Customer Growth Month: {best_customer_growth_month} "
    f"({best_customer_growth_value:.2f}%)"
)
print(
    f"Worst Customer Growth Month: {worst_customer_growth_month} "
    f"({worst_customer_growth_value:.2f}%)"
)
# Create monthly customer growth highlights summary
customer_growth_highlights = pd.DataFrame({
    "Metric": [
        "Best Customer Growth Month",
        "Best Customer Growth Percentage",
        "Worst Customer Growth Month",
        "Worst Customer Growth Percentage"
    ],
    "Value": [
        str(best_customer_growth_month),
        round(best_customer_growth_value, 2),
        str(worst_customer_growth_month),
        round(worst_customer_growth_value, 2)
    ]
})

customer_growth_highlights.to_csv(
    "outputs/customer_growth_highlights.csv",
    index=False
)

print("\nCustomer growth highlights saved successfully.")# Identify best and worst monthly quantity growth
valid_quantity_growth = combined_monthly_growth[
    "Quantity_Growth_Percentage"
].dropna()

best_quantity_growth_month = valid_quantity_growth.idxmax()
best_quantity_growth_value = valid_quantity_growth.max()

worst_quantity_growth_month = valid_quantity_growth.idxmin()
worst_quantity_growth_value = valid_quantity_growth.min()

print("\n--- MONTHLY QUANTITY GROWTH HIGHLIGHTS ---")
print(
    f"Best Quantity Growth Month: {best_quantity_growth_month} "
    f"({best_quantity_growth_value:.2f}%)"
)
print(
    f"Worst Quantity Growth Month: {worst_quantity_growth_month} "
    f"({worst_quantity_growth_value:.2f}%)"
)# Create monthly quantity growth highlights summary
quantity_growth_highlights = pd.DataFrame({
    "Metric": [
        "Best Quantity Growth Month",
        "Best Quantity Growth Percentage",
        "Worst Quantity Growth Month",
        "Worst Quantity Growth Percentage"
    ],
    "Value": [
        str(best_quantity_growth_month),
        round(best_quantity_growth_value, 2),
        str(worst_quantity_growth_month),
        round(worst_quantity_growth_value, 2)
    ]
})

quantity_growth_highlights.to_csv(
    "outputs/quantity_growth_highlights.csv",
    index=False
)

print("\nQuantity growth highlights saved successfully.")# Create combined monthly growth highlights summary
combined_growth_highlights = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Best_Growth_Month": [
        str(best_revenue_growth_month),
        str(best_order_growth_month),
        str(best_customer_growth_month),
        str(best_quantity_growth_month)
    ],
    "Best_Growth_Percentage": [
        round(best_revenue_growth_value, 2),
        round(best_order_growth_value, 2),
        round(best_customer_growth_value, 2),
        round(best_quantity_growth_value, 2)
    ],
    "Worst_Growth_Month": [
        str(worst_revenue_growth_month),
        str(worst_order_growth_month),
        str(worst_customer_growth_month),
        str(worst_quantity_growth_month)
    ],
    "Worst_Growth_Percentage": [
        round(worst_revenue_growth_value, 2),
        round(worst_order_growth_value, 2),
        round(worst_customer_growth_value, 2),
        round(worst_quantity_growth_value, 2)
    ]
})

combined_growth_highlights.to_csv(
    "outputs/combined_growth_highlights.csv",
    index=False
)

print("\nCombined growth highlights saved successfully.")
# Create top 5 months by revenue summary
top_5_revenue_months = (
    monthly_revenue
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_5_revenue_months.columns = [
    "YearMonth",
    "Revenue"
]

top_5_revenue_months.to_csv(
    "outputs/top_5_revenue_months.csv",
    index=False
)

print("\nTop 5 revenue months saved successfully.")
# Create top 5 months by number of unique orders
top_5_order_months = (
    monthly_orders
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_5_order_months.columns = [
    "YearMonth",
    "Orders"
]

top_5_order_months.to_csv(
    "outputs/top_5_order_months.csv",
    index=False
)

print("\nTop 5 order months saved successfully.")
# Create top 5 months by number of unique customers
top_5_customer_months = (
    monthly_customers
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_5_customer_months.columns = [
    "YearMonth",
    "Customers"
]

top_5_customer_months.to_csv(
    "outputs/top_5_customer_months.csv",
    index=False
)

print("\nTop 5 customer months saved successfully.")
# Create top 5 months by total quantity sold
top_5_quantity_months = (
    monthly_quantity
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_5_quantity_months.columns = [
    "YearMonth",
    "Quantity"
]

top_5_quantity_months.to_csv(
    "outputs/top_5_quantity_months.csv",
    index=False
)

print("\nTop 5 quantity months saved successfully.")
# Create combined top 5 monthly performance summary
top_5_monthly_performance = pd.DataFrame({
    "Rank": range(1, 6),

    "Revenue_Month": top_5_revenue_months["YearMonth"].astype(str),
    "Revenue": top_5_revenue_months["Revenue"].values,

    "Orders_Month": top_5_order_months["YearMonth"].astype(str),
    "Orders": top_5_order_months["Orders"].values,

    "Customers_Month": top_5_customer_months["YearMonth"].astype(str),
    "Customers": top_5_customer_months["Customers"].values,

    "Quantity_Month": top_5_quantity_months["YearMonth"].astype(str),
    "Quantity": top_5_quantity_months["Quantity"].values
})

top_5_monthly_performance.to_csv(
    "outputs/top_5_monthly_performance.csv",
    index=False
)

print("\nCombined top 5 monthly performance saved successfully.")# Create bottom 5 months by total revenue
bottom_5_revenue_months = (
    monthly_revenue
    .sort_values(ascending=True)
    .head(5)
    .reset_index()
)

bottom_5_revenue_months.columns = [
    "YearMonth",
    "Revenue"
]

bottom_5_revenue_months.to_csv(
    "outputs/bottom_5_revenue_months.csv",
    index=False
)

print("\nBottom 5 revenue months saved successfully.")# Create bottom 5 months by number of unique orders
bottom_5_order_months = (
    monthly_orders
    .sort_values(ascending=True)
    .head(5)
    .reset_index()
)

bottom_5_order_months.columns = [
    "YearMonth",
    "Orders"
]

bottom_5_order_months.to_csv(
    "outputs/bottom_5_order_months.csv",
    index=False
)

print("\nBottom 5 order months saved successfully.")
# Create bottom 5 months by number of unique customers
bottom_5_customer_months = (
    monthly_customers
    .sort_values(ascending=True)
    .head(5)
    .reset_index()
)

bottom_5_customer_months.columns = [
    "YearMonth",
    "Customers"
]

bottom_5_customer_months.to_csv(
    "outputs/bottom_5_customer_months.csv",
    index=False
)

print("\nBottom 5 customer months saved successfully.")# Create bottom 5 months by total quantity sold
bottom_5_quantity_months = (
    monthly_quantity
    .sort_values(ascending=True)
    .head(5)
    .reset_index()
)

bottom_5_quantity_months.columns = [
    "YearMonth",
    "Quantity"
]

bottom_5_quantity_months.to_csv(
    "outputs/bottom_5_quantity_months.csv",
    index=False
)

print("\nBottom 5 quantity months saved successfully.")# Create combined bottom 5 monthly performance summary
bottom_5_monthly_performance = pd.DataFrame({
    "Rank": range(1, 6),

    "Revenue_Month": bottom_5_revenue_months["YearMonth"].astype(str),
    "Revenue": bottom_5_revenue_months["Revenue"].values,

    "Orders_Month": bottom_5_order_months["YearMonth"].astype(str),
    "Orders": bottom_5_order_months["Orders"].values,

    "Customers_Month": bottom_5_customer_months["YearMonth"].astype(str),
    "Customers": bottom_5_customer_months["Customers"].values,

    "Quantity_Month": bottom_5_quantity_months["YearMonth"].astype(str),
    "Quantity": bottom_5_quantity_months["Quantity"].values
})

bottom_5_monthly_performance.to_csv(
    "outputs/bottom_5_monthly_performance.csv",
    index=False
)

print("\nCombined bottom 5 monthly performance saved successfully.")# Create best vs worst monthly performance comparison
monthly_performance_comparison = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Best_Month": [
        str(top_5_revenue_months.iloc[0]["YearMonth"]),
        str(top_5_order_months.iloc[0]["YearMonth"]),
        str(top_5_customer_months.iloc[0]["YearMonth"]),
        str(top_5_quantity_months.iloc[0]["YearMonth"])
    ],
    "Best_Value": [
        top_5_revenue_months.iloc[0]["Revenue"],
        top_5_order_months.iloc[0]["Orders"],
        top_5_customer_months.iloc[0]["Customers"],
        top_5_quantity_months.iloc[0]["Quantity"]
    ],
    "Worst_Month": [
        str(bottom_5_revenue_months.iloc[0]["YearMonth"]),
        str(bottom_5_order_months.iloc[0]["YearMonth"]),
        str(bottom_5_customer_months.iloc[0]["YearMonth"]),
        str(bottom_5_quantity_months.iloc[0]["YearMonth"])
    ],
    "Worst_Value": [
        bottom_5_revenue_months.iloc[0]["Revenue"],
        bottom_5_order_months.iloc[0]["Orders"],
        bottom_5_customer_months.iloc[0]["Customers"],
        bottom_5_quantity_months.iloc[0]["Quantity"]
    ]
})

monthly_performance_comparison.to_csv(
    "outputs/monthly_performance_comparison.csv",
    index=False
)

print("\nMonthly performance comparison saved successfully.")# Calculate best vs worst monthly performance difference
monthly_performance_difference = monthly_performance_comparison.copy()

monthly_performance_difference["Difference"] = (
    monthly_performance_difference["Best_Value"] -
    monthly_performance_difference["Worst_Value"]
)

monthly_performance_difference["Difference_Percentage"] = (
    monthly_performance_difference["Difference"] /
    monthly_performance_difference["Worst_Value"]
) * 100

monthly_performance_difference.to_csv(
    "outputs/monthly_performance_difference.csv",
    index=False
)

print("\nMonthly performance difference saved successfully.")# Calculate best-to-worst monthly performance ratio
monthly_performance_ratio = monthly_performance_comparison.copy()

monthly_performance_ratio["Best_to_Worst_Ratio"] = (
    monthly_performance_ratio["Best_Value"] /
    monthly_performance_ratio["Worst_Value"]
)

monthly_performance_ratio.to_csv(
    "outputs/monthly_performance_ratio.csv",
    index=False
)
# Create monthly performance range summary
monthly_performance_range = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Minimum_Value": [
        monthly_revenue.min(),
        monthly_orders.min(),
        monthly_customers.min(),
        monthly_quantity.min()
    ],
    "Maximum_Value": [
        monthly_revenue.max(),
        monthly_orders.max(),
        monthly_customers.max(),
        monthly_quantity.max()
    ]
})

monthly_performance_range["Range"] = (
    monthly_performance_range["Maximum_Value"] -
    monthly_performance_range["Minimum_Value"]
)

monthly_performance_range.to_csv(
    "outputs/monthly_performance_range.csv",
    index=False
)

print("\nMonthly performance range saved successfully.")
print("\nMonthly performance ratio saved successfully.")# Create monthly average performance summary
monthly_average_performance = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Monthly_Average": [
        monthly_revenue.mean(),
        monthly_orders.mean(),
        monthly_customers.mean(),
        monthly_quantity.mean()
    ]
})

monthly_average_performance.to_csv(
    "outputs/monthly_average_performance.csv",
    index=False
)

print("\nMonthly average performance saved successfully.")# Create monthly median performance summary
monthly_median_performance = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Monthly_Median": [
        monthly_revenue.median(),
        monthly_orders.median(),
        monthly_customers.median(),
        monthly_quantity.median()
    ]
})

monthly_median_performance.to_csv(
    "outputs/monthly_median_performance.csv",
    index=False
)

print("\nMonthly median performance saved successfully.")# Create monthly standard deviation performance summary
monthly_std_performance = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Monthly_Standard_Deviation": [
        monthly_revenue.std(),
        monthly_orders.std(),
        monthly_customers.std(),
        monthly_quantity.std()
    ]
})

monthly_std_performance.to_csv(
    "outputs/monthly_std_performance.csv",
    index=False
)

print("\nMonthly standard deviation performance saved successfully.")# Create monthly coefficient of variation summary
monthly_cv_performance = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Coefficient_of_Variation_Percentage": [
        (monthly_revenue.std() / monthly_revenue.mean()) * 100,
        (monthly_orders.std() / monthly_orders.mean()) * 100,
        (monthly_customers.std() / monthly_customers.mean()) * 100,
        (monthly_quantity.std() / monthly_quantity.mean()) * 100
    ]
})

monthly_cv_performance.to_csv(
    "outputs/monthly_cv_performance.csv",
    index=False
)

print("\nMonthly coefficient of variation saved successfully.")# Create combined monthly statistical summary
monthly_statistical_summary = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Mean": [
        monthly_revenue.mean(),
        monthly_orders.mean(),
        monthly_customers.mean(),
        monthly_quantity.mean()
    ],
    "Median": [
        monthly_revenue.median(),
        monthly_orders.median(),
        monthly_customers.median(),
        monthly_quantity.median()
    ],
    "Standard_Deviation": [
        monthly_revenue.std(),
        monthly_orders.std(),
        monthly_customers.std(),
        monthly_quantity.std()
    ],
    "Coefficient_of_Variation_Percentage": [
        (monthly_revenue.std() / monthly_revenue.mean()) * 100,
        (monthly_orders.std() / monthly_orders.mean()) * 100,
        (monthly_customers.std() / monthly_customers.mean()) * 100,
        (monthly_quantity.std() / monthly_quantity.mean()) * 100
    ]
})

monthly_statistical_summary.to_csv(
    "outputs/monthly_statistical_summary.csv",
    index=False
)

print("\nMonthly statistical summary saved successfully.")# Identify most and least variable monthly metrics
cv_values = monthly_statistical_summary.set_index(
    "Metric"
)["Coefficient_of_Variation_Percentage"]

most_variable_metric = cv_values.idxmax()
most_variable_cv = cv_values.max()

least_variable_metric = cv_values.idxmin()
least_variable_cv = cv_values.min()

print("\n--- MONTHLY VARIABILITY HIGHLIGHTS ---")
print(
    f"Most Variable Metric: {most_variable_metric} "
    f"({most_variable_cv:.2f}%)"
)
print(
    f"Most Stable Metric: {least_variable_metric} "
    f"({least_variable_cv:.2f}%)"
)# Create monthly variability highlights summary
monthly_variability_highlights = pd.DataFrame({
    "Metric": [
        "Most Variable Metric",
        "Most Variable CV Percentage",
        "Most Stable Metric",
        "Most Stable CV Percentage"
    ],
    "Value": [
        most_variable_metric,
        round(most_variable_cv, 2),
        least_variable_metric,
        round(least_variable_cv, 2)
    ]
})

monthly_variability_highlights.to_csv(
    "outputs/monthly_variability_highlights.csv",
    index=False
)

print("\nMonthly variability highlights saved successfully.")# Create monthly quartile performance summary
monthly_quartile_summary = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Q1_25_Percentile": [
        monthly_revenue.quantile(0.25),
        monthly_orders.quantile(0.25),
        monthly_customers.quantile(0.25),
        monthly_quantity.quantile(0.25)
    ],
    "Q2_Median": [
        monthly_revenue.quantile(0.50),
        monthly_orders.quantile(0.50),
        monthly_customers.quantile(0.50),
        monthly_quantity.quantile(0.50)
    ],
    "Q3_75_Percentile": [
        monthly_revenue.quantile(0.75),
        monthly_orders.quantile(0.75),
        monthly_customers.quantile(0.75),
        monthly_quantity.quantile(0.75)
    ]
})

monthly_quartile_summary.to_csv(
    "outputs/monthly_quartile_summary.csv",
    index=False
)

print("\nMonthly quartile summary saved successfully.")# Create monthly interquartile range summary
monthly_iqr_summary = monthly_quartile_summary.copy()

monthly_iqr_summary["IQR"] = (
    monthly_iqr_summary["Q3_75_Percentile"] -
    monthly_iqr_summary["Q1_25_Percentile"]
)

monthly_iqr_summary.to_csv(
    "outputs/monthly_iqr_summary.csv",
    index=False
)

print("\nMonthly IQR summary saved successfully.")
# Create monthly outlier boundary summary using the IQR method
monthly_outlier_boundaries = monthly_iqr_summary.copy()

monthly_outlier_boundaries["Lower_Bound"] = (
    monthly_outlier_boundaries["Q1_25_Percentile"] -
    1.5 * monthly_outlier_boundaries["IQR"]
)

monthly_outlier_boundaries["Upper_Bound"] = (
    monthly_outlier_boundaries["Q3_75_Percentile"] +
    1.5 * monthly_outlier_boundaries["IQR"]
)

monthly_outlier_boundaries.to_csv(
    "outputs/monthly_outlier_boundaries.csv",
    index=False
)

print("\nMonthly outlier boundaries saved successfully.")
# Identify monthly revenue outliers using IQR boundaries
revenue_lower_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Revenue",
    "Lower_Bound"
].iloc[0]

revenue_upper_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Revenue",
    "Upper_Bound"
].iloc[0]

monthly_revenue_outliers = monthly_revenue[
    (monthly_revenue < revenue_lower_bound) |
    (monthly_revenue > revenue_upper_bound)
].reset_index()

monthly_revenue_outliers.columns = [
    "YearMonth",
    "Revenue"
]

monthly_revenue_outliers.to_csv(
    "outputs/monthly_revenue_outliers.csv",
    index=False
)

print("\nMonthly revenue outliers saved successfully.")
print(
    f"Number of monthly revenue outliers: "
    f"{len(monthly_revenue_outliers)}"
)# Identify monthly order outliers using IQR boundaries
orders_lower_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Orders",
    "Lower_Bound"
].iloc[0]

orders_upper_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Orders",
    "Upper_Bound"
].iloc[0]

monthly_order_outliers = monthly_orders[
    (monthly_orders < orders_lower_bound) |
    (monthly_orders > orders_upper_bound)
].reset_index()

monthly_order_outliers.columns = [
    "YearMonth",
    "Orders"
]

monthly_order_outliers.to_csv(
    "outputs/monthly_order_outliers.csv",
    index=False
)

print("\nMonthly order outliers saved successfully.")
print(
    f"Number of monthly order outliers: "
    f"{len(monthly_order_outliers)}"
)# Identify monthly customer outliers using IQR boundaries
customers_lower_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Customers",
    "Lower_Bound"
].iloc[0]

customers_upper_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Customers",
    "Upper_Bound"
].iloc[0]

monthly_customer_outliers = monthly_customers[
    (monthly_customers < customers_lower_bound) |
    (monthly_customers > customers_upper_bound)
].reset_index()

monthly_customer_outliers.columns = [
    "YearMonth",
    "Customers"
]

monthly_customer_outliers.to_csv(
    "outputs/monthly_customer_outliers.csv",
    index=False
)

print("\nMonthly customer outliers saved successfully.")
print(
    f"Number of monthly customer outliers: "
    f"{len(monthly_customer_outliers)}"
)
# Identify monthly quantity outliers using IQR boundaries
quantity_lower_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Quantity",
    "Lower_Bound"
].iloc[0]

quantity_upper_bound = monthly_outlier_boundaries.loc[
    monthly_outlier_boundaries["Metric"] == "Quantity",
    "Upper_Bound"
].iloc[0]

monthly_quantity_outliers = monthly_quantity[
    (monthly_quantity < quantity_lower_bound) |
    (monthly_quantity > quantity_upper_bound)
].reset_index()

monthly_quantity_outliers.columns = [
    "YearMonth",
    "Quantity"
]

monthly_quantity_outliers.to_csv(
    "outputs/monthly_quantity_outliers.csv",
    index=False
)

print("\nMonthly quantity outliers saved successfully.")
print(
    f"Number of monthly quantity outliers: "
    f"{len(monthly_quantity_outliers)}"
)
# Create combined monthly outlier count summary
monthly_outlier_count_summary = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Outlier_Count": [
        len(monthly_revenue_outliers),
        len(monthly_order_outliers),
        len(monthly_customer_outliers),
        len(monthly_quantity_outliers)
    ]
})

monthly_outlier_count_summary.to_csv(
    "outputs/monthly_outlier_count_summary.csv",
    index=False
)

print("\nMonthly outlier count summary saved successfully.")# Identify metric with the most monthly outliers
max_outlier_count = monthly_outlier_count_summary[
    "Outlier_Count"
].max()

metrics_with_most_outliers = monthly_outlier_count_summary[
    monthly_outlier_count_summary["Outlier_Count"] == max_outlier_count
]["Metric"].tolist()

most_outlier_metrics_text = ", ".join(metrics_with_most_outliers)

print("\n--- MONTHLY OUTLIER HIGHLIGHTS ---")
print(
    f"Metric(s) With Most Outliers: {most_outlier_metrics_text}"
)
print(
    f"Highest Outlier Count: {max_outlier_count}"
)# Create monthly outlier highlights summary
monthly_outlier_highlights = pd.DataFrame({
    "Metric": [
        "Metric(s) With Most Outliers",
        "Highest Outlier Count"
    ],
    "Value": [
        most_outlier_metrics_text,
        max_outlier_count
    ]
})

monthly_outlier_highlights.to_csv(
    "outputs/monthly_outlier_highlights.csv",
    index=False
)

print("\nMonthly outlier highlights saved successfully.")# Create monthly outlier percentage summary
monthly_outlier_percentage_summary = pd.DataFrame({
    "Metric": [
        "Revenue",
        "Orders",
        "Customers",
        "Quantity"
    ],
    "Total_Months": [
        len(monthly_revenue),
        len(monthly_orders),
        len(monthly_customers),
        len(monthly_quantity)
    ],
    "Outlier_Count": [
        len(monthly_revenue_outliers),
        len(monthly_order_outliers),
        len(monthly_customer_outliers),
        len(monthly_quantity_outliers)
    ]
})

monthly_outlier_percentage_summary["Outlier_Percentage"] = (
    monthly_outlier_percentage_summary["Outlier_Count"] /
    monthly_outlier_percentage_summary["Total_Months"]
) * 100

monthly_outlier_percentage_summary.to_csv(
    "outputs/monthly_outlier_percentage_summary.csv",
    index=False
)

print("\nMonthly outlier percentage summary saved successfully.")# Identify highest and lowest monthly outlier percentages
outlier_percentage_values = (
    monthly_outlier_percentage_summary
    .set_index("Metric")["Outlier_Percentage"]
)

highest_outlier_percentage_metric = outlier_percentage_values.idxmax()
highest_outlier_percentage = outlier_percentage_values.max()

lowest_outlier_percentage_metric = outlier_percentage_values.idxmin()
lowest_outlier_percentage = outlier_percentage_values.min()

print("\n--- MONTHLY OUTLIER PERCENTAGE HIGHLIGHTS ---")
print(
    f"Highest Outlier Percentage Metric: "
    f"{highest_outlier_percentage_metric} "
    f"({highest_outlier_percentage:.2f}%)"
)

print(
    f"Lowest Outlier Percentage Metric: "
    f"{lowest_outlier_percentage_metric} "
    f"({lowest_outlier_percentage:.2f}%)"
)# Create monthly outlier percentage highlights summary
monthly_outlier_percentage_highlights = pd.DataFrame({
    "Metric": [
        "Highest Outlier Percentage Metric",
        "Highest Outlier Percentage",
        "Lowest Outlier Percentage Metric",
        "Lowest Outlier Percentage"
    ],
    "Value": [
        highest_outlier_percentage_metric,
        round(highest_outlier_percentage, 2),
        lowest_outlier_percentage_metric,
        round(lowest_outlier_percentage, 2)
    ]
})

monthly_outlier_percentage_highlights.to_csv(
    "outputs/monthly_outlier_percentage_highlights.csv",
    index=False
)

print("\nMonthly outlier percentage highlights saved successfully.")# Create monthly outlier status summary
monthly_outlier_status = monthly_outlier_count_summary.copy()

monthly_outlier_status["Outlier_Status"] = (
    monthly_outlier_status["Outlier_Count"]
    .apply(lambda x: "Outliers Detected" if x > 0 else "No Outliers")
)

monthly_outlier_status.to_csv(
    "outputs/monthly_outlier_status.csv",
    index=False
)

print("\nMonthly outlier status summary saved successfully.")# Create monthly outlier severity summary
monthly_outlier_severity = monthly_outlier_percentage_summary.copy()

def classify_outlier_severity(percentage):
    if percentage == 0:
        return "None"
    elif percentage <= 10:
        return "Low"
    elif percentage <= 20:
        return "Moderate"
    else:
        return "High"

monthly_outlier_severity["Outlier_Severity"] = (
    monthly_outlier_severity["Outlier_Percentage"]
    .apply(classify_outlier_severity)
)

monthly_outlier_severity.to_csv(
    "outputs/monthly_outlier_severity.csv",
    index=False
)

print("\nMonthly outlier severity summary saved successfully.")# Create monthly outlier severity count summary
severity_order = ["None", "Low", "Moderate", "High"]

monthly_outlier_severity_count = (
    monthly_outlier_severity["Outlier_Severity"]
    .value_counts()
    .reindex(severity_order, fill_value=0)
    .reset_index()
)

monthly_outlier_severity_count.columns = [
    "Outlier_Severity",
    "Metric_Count"
]

monthly_outlier_severity_count.to_csv(
    "outputs/monthly_outlier_severity_count.csv",
    index=False
)

print("\nMonthly outlier severity count summary saved successfully.")# Create final monthly outlier analysis summary
final_monthly_outlier_summary = monthly_outlier_severity[
    [
        "Metric",
        "Total_Months",
        "Outlier_Count",
        "Outlier_Percentage",
        "Outlier_Severity"
    ]
].copy()

final_monthly_outlier_summary["Outlier_Percentage"] = (
    final_monthly_outlier_summary["Outlier_Percentage"].round(2)
)

final_monthly_outlier_summary.to_csv(
    "outputs/final_monthly_outlier_summary.csv",
    index=False
)

print("\nFinal monthly outlier analysis summary saved successfully.")# Create final monthly performance summary
final_monthly_performance_summary = monthly_statistical_summary.merge(
    monthly_performance_range[
        ["Metric", "Minimum_Value", "Maximum_Value", "Range"]
    ],
    on="Metric",
    how="left"
)

final_monthly_performance_summary.to_csv(
    "outputs/final_monthly_performance_summary.csv",
    index=False
)

print("\nFinal monthly performance summary saved successfully.")# Create final monthly analysis dashboard data
final_monthly_analysis_dashboard = final_monthly_performance_summary.merge(
    final_monthly_outlier_summary[
        [
            "Metric",
            "Outlier_Count",
            "Outlier_Percentage",
            "Outlier_Severity"
        ]
    ],
    on="Metric",
    how="left"
)

final_monthly_analysis_dashboard.to_csv(
    "outputs/final_monthly_analysis_dashboard.csv",
    index=False
)

print("\nFinal monthly analysis dashboard data saved successfully.")# Create final project KPI summary
final_project_kpi_summary = pd.DataFrame({
    "KPI": [
        "Average Monthly Revenue",
        "Average Monthly Orders",
        "Average Monthly Customers",
        "Average Monthly Quantity",
        "Highest Revenue Month",
        "Highest Orders Month",
        "Highest Customers Month",
        "Highest Quantity Month"
    ],
    "Value": [
        monthly_revenue.mean(),
        monthly_orders.mean(),
        monthly_customers.mean(),
        monthly_quantity.mean(),
        str(top_5_revenue_months.iloc[0]["YearMonth"]),
        str(top_5_order_months.iloc[0]["YearMonth"]),
        str(top_5_customer_months.iloc[0]["YearMonth"]),
        str(top_5_quantity_months.iloc[0]["YearMonth"])
    ]
})

final_project_kpi_summary.to_csv(
    "outputs/final_project_kpi_summary.csv",
    index=False
)

print("\nFinal project KPI summary saved successfully.")
# Create final project summary
final_project_summary = pd.DataFrame({
    "Summary_Item": [
        "Most Variable Metric",
        "Most Stable Metric",
        "Metric With Most Outliers",
        "Highest Outlier Percentage Metric",
        "Lowest Outlier Percentage Metric"
    ],
    "Value": [
        most_variable_metric,
        least_variable_metric,
        most_outlier_metrics_text,
        highest_outlier_percentage_metric,
        lowest_outlier_percentage_metric
    ]
})

final_project_summary.to_csv(
    "outputs/final_project_summary.csv",
    index=False
)

print("\nFinal project summary saved successfully.")# Create final analysis completion checklist
final_analysis_checklist = pd.DataFrame({
    "Analysis_Area": [
        "Growth Analysis",
        "Top Performing Months",
        "Bottom Performing Months",
        "Statistical Analysis",
        "Quartile Analysis",
        "IQR Analysis",
        "Outlier Analysis",
        "Outlier Percentage Analysis",
        "Final KPI Summary",
        "Final Project Summary"
    ],
    "Status": [
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed",
        "Completed"
    ]
})

final_analysis_checklist.to_csv(
    "outputs/final_analysis_checklist.csv",
    index=False
)

print("\nFinal analysis completion checklist saved successfully.")# Create final analysis output index
final_analysis_output_index = pd.DataFrame({
    "Output_File": [
        "combined_growth_highlights.csv",
        "top_5_monthly_performance.csv",
        "bottom_5_monthly_performance.csv",
        "monthly_performance_comparison.csv",
        "monthly_performance_difference.csv",
        "monthly_performance_ratio.csv",
        "monthly_statistical_summary.csv",
        "monthly_iqr_summary.csv",
        "final_monthly_outlier_summary.csv",
        "final_monthly_analysis_dashboard.csv",
        "final_project_kpi_summary.csv",
        "final_project_summary.csv",
        "final_analysis_checklist.csv"
    ],
    "Purpose": [
        "Best and worst growth comparison",
        "Top performing months",
        "Bottom performing months",
        "Best vs worst monthly performance",
        "Best vs worst performance difference",
        "Best to worst performance ratio",
        "Monthly statistical measures",
        "Monthly interquartile range analysis",
        "Final monthly outlier summary",
        "Combined monthly dashboard data",
        "Final project KPI summary",
        "Final project findings",
        "Analysis completion checklist"
    ]
})

final_analysis_output_index.to_csv(
    "outputs/final_analysis_output_index.csv",
    index=False
)

print("\nFinal analysis output index saved successfully.")# Mark Exploratory Data Analysis as completed
eda_completion_status = pd.DataFrame({
    "Project_Stage": [
        "Exploratory Data Analysis (EDA)"
    ],
    "Status": [
        "Completed"
    ]
})

eda_completion_status.to_csv(
    "outputs/eda_completion_status.csv",
    index=False
)

print("\n========================================")
print("EXPLORATORY DATA ANALYSIS COMPLETED")
print("========================================")
print("EDA completion status saved successfully.")