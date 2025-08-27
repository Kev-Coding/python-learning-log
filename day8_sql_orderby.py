import sqlite3

connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

# Query to find the 5 most recent readings, sorting by timestamp in descending order
query = "SELECT timestamp, tagname, value, units FROM flow_data ORDER BY timestamp DESC LIMIT 5;"

cursor.execute(query)
results = cursor.fetchall()

print("5 Most Recent Readings")
print("----------------------")
for row in results:
    print(row)

connection.close()