import pandas as pd

# Load datasets
customer_df = pd.read_csv("C:\E\multiagentAIsystem\customer_data_collection.csv")
product_df = pd.read_csv("C:\E\multiagentAIsystem\product_recommendation_data.csv")

# Display first few rows
print("Customer Data:\n", customer_df.head())
print("\nProduct Recommendation Data:\n", product_df.head())

# Show column names
print("\nCustomer Data Columns:", customer_df.columns)
print("Product Data Columns:", product_df.columns)

# Remove duplicates
customer_df.drop_duplicates(inplace=True)

# Drop null values
customer_df.dropna(inplace=True)

# Save cleaned customer data
customer_df.to_csv("C:\E\multiagentAIsystem\customer_data_collection.csv", index=False)

print("Customer data cleaned and saved!")
# Remove duplicates
product_df.drop_duplicates(inplace=True)

# Drop null values
product_df.dropna(inplace=True)

# Save cleaned product data
product_df.to_csv("C:\E\multiagentAIsystem\product_recommendation_data.csv", index=False)

print("Product data cleaned and saved!")

