import sqlite3
# Connect to your database
connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

# The query uses a WHERE clause to filter for values greater than 50
query = "SELECT timestamp, value, units FROM flow_data WHERE value > 50;"

cursor.execute(query)
results = cursor.fetchall()

print("Flow Rates > 50 GPM")
print("--------------------")
for row in results:
    print(row)

connection.close()