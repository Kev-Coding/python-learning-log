import sqlite3
import pandas as pd

# --- Connect to the database ---
conn = sqlite3.connect('database_conn_lesson.db.sqlite')
cursor = conn.cursor()

# Query all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:", tables)

# The pd.read_sql_query() function is the most efficient way to run a SQL
# query and load the results directly into a DataFrame.
# You correctly used a WHERE clause to filter the data at the source.
query = "SELECT * FROM sensor_data WHERE flow_rate > 20.0;"
df = pd.read_sql_query(query, conn)

# --- TASK 2: Print the results and data types ---
print("--- DataFrame from SQL Query ---")
print(df)
print("\nDataFrame Info:")
# The .info() method is great for seeing the data types of your DataFrame.
df.info()

# --- TASK 3: Close the connection ---
# The .close() method closes the connection to the database.
conn.close()









