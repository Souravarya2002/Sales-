import pandas as pd

# Load data
df = pd.read_csv("sales.csv")

# Clean and prepare data
df['Revenue'] = df['Quantity'] * df['Price']

# 1. Total Revenue
total_revenue = df['Revenue'].sum()
print(f"📦 Total Revenue: ₹{total_revenue}")

# 2. Average Order Value
average_value = df['Revenue'].mean()
print(f"💰 Average Order Value: ₹{average_value:.2f}")

# 3. Top Selling Products
top_products = df.groupby("Product")['Revenue'].sum().sort_values(ascending=False)
print("\n🔥 Top Products by Revenue:")
print(top_products)

# 4. Sales by Category
category_sales = df.groupby("Category")['Revenue'].sum()
print("\n📂 Revenue by Category:")
print(category_sales)

# 5. Optional: Export to Excel
df.to_excel("sales_analysis_output.xlsx", index=False)
print("\n✅ Analysis exported to 'sales_analysis_output.xlsx'")
