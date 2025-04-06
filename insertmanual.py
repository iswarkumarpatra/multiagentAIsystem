import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Define manual customer data
customer_data = [
    #("Tushar", 20, "Male", "Balasore", "Marvel Comics, Graphic", "Mattress, Headphones", "Comic Enthusiast", 5000.75, "Christmas", "Winter"),
    ("Iswar", 20, "Male", "Balasore", "Iron man shirt, Flowers", "Mattress, Headphones", "Comic Enthusiast", 5000.75, "Christmas", "Winter"),
    
]

# SQL query to insert data
insert_query = """
INSERT INTO customers (Customer_ID, Age, Gender, Location, Browsing_History, Purchase_History, 
                       Customer_Segment, Avg_Order_Value, Holiday, Season) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Execute insertion for each record
cursor.executemany(insert_query, customer_data)

# Commit changes
conn.commit()

# Close connection
conn.close()

print("✅ Data inserted successfully!")
