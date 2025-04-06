import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Drop table if it exists (to avoid schema mismatch)
cursor.execute("DROP TABLE IF EXISTS customers")

# Create customers table with correct columns
cursor.execute('''
    CREATE TABLE customers (
        Customer_ID TEXT PRIMARY KEY,
        Age INTEGER,
        Gender TEXT,
        Location TEXT,
        Browsing_History TEXT,
        Purchase_History TEXT,
        Customer_Segment TEXT,
        Avg_Order_Value REAL,
        Holiday TEXT,
        Season TEXT
    )
''')

# Drop and recreate products table
cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute('''
    CREATE TABLE products (
        product_id TEXT PRIMARY KEY,
        category TEXT
    )
''')

conn.commit()
conn.close()

print("✅ Database tables recreated successfully!")
