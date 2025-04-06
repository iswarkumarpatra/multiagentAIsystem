import sqlite3
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Fetch first 5 customers
cursor.execute("SELECT * FROM customers LIMIT 5")
customers = cursor.fetchall()
print("Customers Data:\n", customers)

# Fetch first 5 products
cursor.execute("SELECT * FROM products LIMIT 5")
products = cursor.fetchall()
print("Products Data:\n", products)

conn.close()
