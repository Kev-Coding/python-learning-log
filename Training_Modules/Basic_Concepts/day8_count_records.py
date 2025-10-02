import sqlite3

connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

query = "SELECT COUNT(*) FROM flow_data;"
cursor.execute(query)
result = cursor.fetchone()

print(f"Total records in the database: {result[0]}")

connection.close()
print(type(result[0]))  # This will print <class 'int'>