import sqlite3

# 1. Connect to the database.
connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

# 2. Define the SQL query.
# `SELECT *` means select all columns.
# `FROM flow_data` specifies our table.
query = "SELECT * FROM flow_data LIMIT 10;"

# 3. Execute the query.
cursor.execute(query)

# 4. Fetch all the results from the query.
results = cursor.fetchall()

# 5. Print a header for the output.
print("Timestamp | Tagname | Value | Units")
print("-" * 40)

# 6. Loop through the results and print each row.
for row in results:
    print(row)

# 7. Close the connection.
connection.close()