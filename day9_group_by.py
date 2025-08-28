# File: day9_group_by.py
import sqlite3

connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

# The query uses a GROUP BY to count each tag
query = "SELECT tagname, COUNT(tagname) FROM flow_data GROUP BY tagname;"
cursor.execute(query)
results = cursor.fetchall()

print("Records Per Tag")
print("---------------")
for row in results:
    print(row)

connection.close()