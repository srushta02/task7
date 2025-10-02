# Import required libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table and insert sample data if needed
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert dummy data (comment this out if already inserted)
cursor.executemany("""
INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)
""", [
    ("Apples", 10, 2.5),
    ("Bananas", 20, 1.2),
    ("Oranges", 15, 1.8),
    ("Apples", 5, 2.5),
    ("Bananas", 10, 1.2),
    ("Oranges", 8, 1.8),
])
conn.commit()

# Step 2: Query to get sales summary
query = """
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# Step 3: Print results
print("Sales Summary:\n")
print(df)

# Step 4: Plot bar chart of revenue by product
df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.tight_layout()
plt.show()

# Close database connection
conn.close()
