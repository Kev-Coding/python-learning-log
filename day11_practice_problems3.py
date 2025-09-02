# File: day11_join_all_tables.py
import sqlite3

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

# This query joins three tables together
query = """
SELECT
    p.name AS plc_name,
    r.name AS reactor_name,
    t.tag_name,
    AVG(t.value) AS avg_value,
    t.units
FROM
    readings AS t
JOIN
    reactors AS r ON t.reactor_id = r.id
JOIN
    plcs AS p ON r.plc_id = p.id
WHERE
    t.tag_name IN ('AGIT')
GROUP BY
    p.name, r.name, t.tag_name, t.units
HAVING
    AVG(t.value) > 25
"""
cursor.execute(query)
results = cursor.fetchall()

print("PLC Name | Reactor Name | Tag Name | Value | Units")
print("--------------------------------------------------")
for row in results:
    print(row)

connection.close()