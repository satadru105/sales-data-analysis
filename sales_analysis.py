
# Week 3 Internship Project: Sales Data Analysis
# Purpose: Clean sales data, calculate metrics, and generate a report.

from pathlib import Path
import pandas as pd

# Keep project files in the same folder as this Python script.
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "sales_data.csv"
REPORT_FILE = BASE_DIR / "analysis_report.md"

# Step 1: Load the CSV dataset.
try:
    df = pd.read_csv(INPUT_FILE)
except FileNotFoundError:
    print("Error: sales_data.csv was not found.")
    raise SystemExit(1)

# Step 2: Check that the required columns exist.
required_columns = ["Product", "Quantity", "Unit_Price"]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    print(f"Missing required columns: {missing_columns}")
    raise SystemExit(1)

# Step 3: Explore the original dataset.
print("\n===== ORIGINAL DATA =====")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nColumn data types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

original_rows = len(df)

# Step 4: Remove exact duplicate rows.
df = df.drop_duplicates().copy()
duplicates_removed = original_rows - len(df)

# Step 5: Convert numeric columns safely.
for col in ["Quantity", "Unit_Price"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert date values when the column exists.
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Step 6: Handle missing and invalid data.
# Product names cannot be used for product-level analysis if missing.
df["Product"] = df["Product"].astype("string").str.strip()
df["Product"] = df["Product"].replace("", pd.NA)
df = df.dropna(subset=["Product"])

# A sale requires a valid positive quantity and unit price.
df = df[
    (df["Quantity"] > 0)
    & (df["Unit_Price"] >= 0)
].copy()

# Calculate revenue from quantity and price to ensure consistency.
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Remove rows with missing values in essential numeric fields.
df = df.dropna(subset=["Quantity", "Unit_Price"]).copy()

# Stop if there is no valid data to analyze.
if df.empty:
    print("No valid sales records remain after cleaning.")
    raise SystemExit(1)

# Step 7: Calculate sales metrics.
total_revenue = df["Total_Sales"].sum()
total_units = df["Quantity"].sum()
average_order_value = df["Total_Sales"].mean()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

# Find the product with the highest total revenue.
product_sales = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_product = product_sales.index[0]
best_product_revenue = product_sales.iloc[0]

# Find the product with the highest quantity sold.
product_units = df.groupby("Product")["Quantity"].sum()
most_units_product = product_units.idxmax()
most_units = product_units.max()

# Step 8: Display the results.
print("\n===== SALES ANALYSIS RESULTS =====")
print(f"Valid sales records: {len(df)}")
print(f"Duplicate rows removed: {duplicates_removed}")
print(f"Total revenue: Rs. {total_revenue:,.2f}")
print(f"Total units sold: {total_units:,.0f}")
print(f"Average sale value: Rs. {average_order_value:,.2f}")
print(f"Highest sale: Rs. {highest_sale:,.2f}")
print(f"Lowest sale: Rs. {lowest_sale:,.2f}")
print(f"Top product by revenue: {best_product}")
print(f"Top product revenue: Rs. {best_product_revenue:,.2f}")
print(f"Most units sold: {most_units_product} ({most_units:,.0f})")

print("\n===== REVENUE BY PRODUCT =====")
print(product_sales.to_string())

# Step 9: Create a formatted Markdown report.
report = f"""# Sales Data Analysis Report

## 1. Project Overview

This project uses Python and Pandas to clean and analyze
a sample sales dataset and identify useful business insights.

## 2. Data Cleaning

- Original rows: {original_rows}
- Exact duplicate rows removed: {duplicates_removed}
- Valid rows analyzed: {len(df)}
- Missing product names were excluded.
- Invalid or missing quantities were excluded.
- Missing or invalid unit prices were excluded.
- Revenue was recalculated using Quantity × Unit_Price.

## 3. Key Performance Metrics

| Metric | Result |
|---|---:|
| Total revenue | Rs. {total_revenue:,.2f} |
| Total units sold | {total_units:,.0f} |
| Average sale value | Rs. {average_order_value:,.2f} |
| Highest sale | Rs. {highest_sale:,.2f} |
| Lowest sale | Rs. {lowest_sale:,.2f} |
| Valid sales records | {len(df)} |

## 4. Product Performance

**Top product by revenue:** {best_product}

**Revenue from this product:** Rs. {best_product_revenue:,.2f}

**Product with most units sold:** {most_units_product}

**Units sold:** {most_units:,.0f}

### Revenue by Product

| Product | Revenue (Rs.) |
|---|---:|
{chr(10).join(f"| {product} | {revenue:,.2f} |" for product, revenue in product_sales.items())}

## 5. Business Insights

- Total recorded revenue is Rs. {total_revenue:,.2f}.
- {best_product} generated the highest product revenue.
- {most_units_product} had the highest total quantity sold.
- Average sale value was Rs. {average_order_value:,.2f}.

## 6. Conclusion

Pandas helped load, clean, group, and summarize sales records.
These results can help a business understand product performance
and make more informed inventory and sales decisions.

## 7. Tools Used

- Python
- Pandas
- CSV
- Markdown

## 8. Validation

The report was generated from the cleaned dataset.
Revenue was recalculated from quantity multiplied by unit price.
"""

# Step 10: Save the report.
REPORT_FILE.write_text(report, encoding="utf-8")

print("\nReport successfully saved to the project directory.")
