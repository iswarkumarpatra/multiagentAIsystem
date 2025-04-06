import pandas as pd
import sqlite3

# Load cleaned customer data
customer_df = pd.read_csv("customer_data_collection.csv", dtype=str)

# Load cleaned product data
product_df = pd.read_csv("product_recommendation_data.csv", dtype=str)

conn = sqlite3.connect("ecommerce.db")

# Insert customers
customer_df.to_sql('customers', conn, if_exists='replace', index=False, dtype={
    "Customer_ID": "TEXT",
    "Age": "INTEGER",
    "Gender": "TEXT",
    "Location": "TEXT",
    "Browsing_History": "TEXT",
    "Purchase_History": "TEXT",
    "Customer_Segment": "TEXT",
    "Avg_Order_Value": "REAL",
    "Holiday": "TEXT",
    "Season": "TEXT"
})

# Insert products
product_df.to_sql('products', conn, if_exists='replace', index=False, dtype={
    "product_id": "TEXT",
    "category": "TEXT"
})

conn.commit()
conn.close()

print("✅ Data inserted successfully!")
