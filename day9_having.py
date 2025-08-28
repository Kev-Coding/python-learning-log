# File: day9_having.py
import sqlite3

connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

# Query to find tags with more than 15 readings
query = "SELECT tagname, COUNT(tagname) FROM flow_data GROUP BY tagname HAVING COUNT(tagname) > 15;"
cursor.execute(query)
results = cursor.fetchall()

print("Tags with > 15 Records")
print("----------------------")
for row in results:
    print(row)

connection.close()