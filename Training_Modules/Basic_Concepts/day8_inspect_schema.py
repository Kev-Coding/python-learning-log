import sqlite3

# Connect to the database
connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

# The PRAGMA command to get info about the 'flow_data' table
query = "PRAGMA table_info(flow_data);"

cursor.execute(query)
results = cursor.fetchall()

# Print the header
print("Column Info")
print("-----------")

# Loop through the results and print the column details
for row in results:
    # Each row contains details about a column
    print(f"Name: {row[1]}, Data Type: {row[2]}, Not Null: {bool(row[3])}, Primary Key: {bool(row[5])}")

connection.close()
