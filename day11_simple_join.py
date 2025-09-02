import sqlite3

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

# The query joins the 'readings' and 'reactors' tables
query = """
SELECT
    readings.tag_name,
    readings.value,
    reactors.name
FROM
    readings
JOIN
    reactors ON readings.reactor_id = reactors.id;
"""

cursor.execute(query)
results = cursor.fetchall()

print("Tag Name | Value | Reactor Name")
print("------------------------------")
for row in results:
    print(row)

connection.close()