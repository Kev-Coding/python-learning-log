import sqlite3

# Connect to the new relational database
connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

# Query the sqlite_master table to get all table names
query = "SELECT name FROM sqlite_master WHERE type='table';"

cursor.execute(query)
results = cursor.fetchall()

print("Tables in this database:")
print("------------------------")
for row in results:
    # The result is a tuple, so we access the first item
    print(row[0])

connection.close()

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

query = "SELECT * FROM sqlite_master;"
cursor.execute(query)
results = cursor.fetchall()

print("Full sqlite_master table:")
for row in results:
    print(row)

connection.close()

# This is a much cleaner way to inspect the database.

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

query = "SELECT * FROM sqlite_master;"
cursor.execute(query)
results = cursor.fetchall()

print("Full sqlite_master table:")
print("-----------------------------------------------------------------------------------------------------------------")
print("{:<10} {:<20} {:<15} {:<10} {:<30}".format("Type", "Name", "Table Name", "Root Page", "SQL"))
print("-----------------------------------------------------------------------------------------------------------------")

# ... previous code ...

for row in results:
    # Tuple unpacking to assign each item to a variable
    data_type, name, tbl_name, rootpage, sql = row
    
    # Use a conditional expression to replace None with a dash
    formatted_sql = sql if sql is not None else "-"

    # Use an f-string to print the formatted data
    print(f"{data_type:<10} {name:<20} {tbl_name:<15} {rootpage:<10} {formatted_sql:<30}")

connection.close()