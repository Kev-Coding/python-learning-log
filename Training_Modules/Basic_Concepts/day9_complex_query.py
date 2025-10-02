# File: day9_complex_query.py
import sqlite3

connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()
# This query originally used averages greater than 50. This did not return any results.
# This query filters for averages greater than 44
query = "SELECT tagname, AVG(value) FROM flow_data GROUP BY tagname HAVING AVG(value) > 44;"
cursor.execute(query)
results = cursor.fetchall()

print("Tags with Avg Flow > 44 GPM")
print("----------------------------")
for row in results:
    print(f"Tag: {row[0]}, Average Value: {row[1]:.2f}")

connection.close()