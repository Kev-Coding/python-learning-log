import sqlite3

connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

query = "SELECT AVG(value) FROM flow_data;"
cursor.execute(query)
result = cursor.fetchone()

print(f"Average flow rate: {result[0]:.2f} GPM")

connection.close()
print(type(result[0]))  # This will print <class 'float'>