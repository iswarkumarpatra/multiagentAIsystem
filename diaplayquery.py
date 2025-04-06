import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Query to fetch details of Tushar
cursor.execute("SELECT * FROM customers WHERE Customer_ID = ?", ("Tushar",))

# Fetch result
tushar_data = cursor.fetchone()

# Close connection
conn.close()

# Display the result
if tushar_data:
    print("Tushar's Data:", tushar_data)
else:
    print("No record found for Tushar")
