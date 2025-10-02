import sqlite3

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

# This query joins three tables together
query = """
SELECT
    p.name AS plc_name,
    r.name AS reactor_name,
    t.tag_name,
    t.value,
    t.units
FROM
    readings AS t
JOIN
    reactors AS r ON t.reactor_id = r.id
JOIN
    plcs AS p ON r.plc_id = p.id;
"""

cursor.execute(query)
results = cursor.fetchall()

print("PLC Name | Reactor Name | Tag Name | Value | Units")
print("--------------------------------------------------")
for row in results:
    print(row)

connection.close()