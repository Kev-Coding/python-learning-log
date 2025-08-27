import sqlite3

connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

query = "SELECT SUM(value) FROM flow_data;"
cursor.execute(query)
result = cursor.fetchone()

print(f"Total volume passed: {result[0]:.2f} GPM-seconds")

connection.close()
print(type(result))  # This will print <class 'float'>