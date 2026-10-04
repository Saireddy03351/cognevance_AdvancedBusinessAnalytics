from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_FILE = PROJECT_ROOT / "data" / "Online_Retail.xlsx"

# Load dataset
print("Loading dataset...")

df = pd.read_excel(RAW_DATA_FILE)

print("Dataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Remove duplicate records
rows_before = len(df)

df = df.drop_duplicates()

rows_after = len(df)

print("\nDuplicate Removal:")
print(f"Rows before: {rows_before}")
print(f"Rows after: {rows_after}")
print(f"Duplicates removed: {rows_before - rows_after}")
# Remove records with missing CustomerID
rows_before = len(df)

df = df.dropna(subset=["CustomerID"])

rows_after = len(df)

print("\nMissing CustomerID Removal:")
print(f"Rows before: {rows_before}")
print(f"Rows after: {rows_after}")
print(f"Rows removed: {rows_before - rows_after}")
# Remove cancelled transactions
rows_before = len(df)

df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

rows_after = len(df)

print("\nCancelled Transaction Removal:")
print(f"Rows before: {rows_before}")
print(f"Rows after: {rows_after}")
print(f"Cancelled rows removed: {rows_before - rows_after}")
# Remove invalid quantity records
rows_before = len(df)

df = df[df["Quantity"] > 0]

rows_after = len(df)

print("\nInvalid Quantity Removal:")
print(f"Rows before: {rows_before}")
print(f"Rows after: {rows_after}")
print(f"Invalid quantity rows removed: {rows_before - rows_after}")
# Remove invalid unit price records
rows_before = len(df)

df = df[df["UnitPrice"] > 0]

rows_after = len(df)

print("\nInvalid Unit Price Removal:")
print(f"Rows before: {rows_before}")
print(f"Rows after: {rows_after}")
print(f"Invalid price rows removed: {rows_before - rows_after}")
# Convert InvoiceDate to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nInvoiceDate Conversion:")
print(f"InvoiceDate data type: {df['InvoiceDate'].dtype}")
# Create TotalPrice feature
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

print("\nTotalPrice Feature Created:")
print(df[["Quantity", "UnitPrice", "TotalPrice"]].head())
# Create Year feature
df["Year"] = df["InvoiceDate"].dt.year

print("\nYear Feature Created:")
print(df[["InvoiceDate", "Year"]].head())
# Create Month feature
df["Month"] = df["InvoiceDate"].dt.month

print("\nMonth Feature Created:")
print(df[["InvoiceDate", "Month"]].head())
# Create MonthName feature
df["MonthName"] = df["InvoiceDate"].dt.month_name()

print("\nMonthName Feature Created:")
print(df[["InvoiceDate", "Month", "MonthName"]].head())
# Create DayOfWeek feature
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

print("\nDayOfWeek Feature Created:")
print(df[["InvoiceDate", "DayOfWeek"]].head())
# Create Hour feature
df["Hour"] = df["InvoiceDate"].dt.hour

print("\nHour Feature Created:")
print(df[["InvoiceDate", "Hour"]].head())
# Create Quarter feature
df["Quarter"] = df["InvoiceDate"].dt.quarter

print("\nQuarter Feature Created:")
print(df[["InvoiceDate", "Quarter"]].head())
# Create IsWeekend feature
df["IsWeekend"] = df["InvoiceDate"].dt.dayofweek.isin([5, 6]).astype(int)

print("\nIsWeekend Feature Created:")
print(df[["InvoiceDate", "DayOfWeek", "IsWeekend"]].head())
# Create YearMonth feature
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

print("\nYearMonth Feature Created:")
print(df[["InvoiceDate", "YearMonth"]].head())
# Create Season feature
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["Season"] = df["Month"].apply(get_season)

print("\nSeason Feature Created:")
print(df[["InvoiceDate", "Month", "Season"]].head())
# Create TimeOfDay feature
def get_time_of_day(hour):
    if hour < 12:
        return "Morning"
    elif hour < 17:
        return "Afternoon"
    else:
        return "Evening"

df["TimeOfDay"] = df["Hour"].apply(get_time_of_day)

print("\nTimeOfDay Feature Created:")
print(df[["InvoiceDate", "Hour", "TimeOfDay"]].head())
# Create OrderValueCategory feature
def get_order_value_category(total_price):
    if total_price < 20:
        return "Low"
    elif total_price < 100:
        return "Medium"
    else:
        return "High"

df["OrderValueCategory"] = df["TotalPrice"].apply(get_order_value_category)

print("\nOrderValueCategory Feature Created:")
print(df[["TotalPrice", "OrderValueCategory"]].head())
# Create CustomerType feature based on transaction value
def get_customer_type(total_price):
    if total_price >= 100:
        return "High Value"
    elif total_price >= 50:
        return "Medium Value"
    else:
        return "Regular"

df["CustomerType"] = df["TotalPrice"].apply(get_customer_type)

print("\nCustomerType Feature Created:")
print(df[["CustomerID", "TotalPrice", "CustomerType"]].head())
# Save the cleaned and feature-engineered dataset
OUTPUT_FILE = PROJECT_ROOT / "data" / "Online_Retail_Processed.csv"

df.to_csv(OUTPUT_FILE, index=False)

print("\nProcessed Dataset Saved Successfully!")
print(f"File: {OUTPUT_FILE}")
print(f"Final Shape: {df.shape}")