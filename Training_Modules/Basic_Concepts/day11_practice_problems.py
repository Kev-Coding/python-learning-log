# File: day11_join_all_tables.py
import sqlite3

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

# This query joins three tables together
query = """
-- This comments out single lines /*..*/ comments out multi-line
/*
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
    t.tag_name = 'TEMP' OR
    t.tag_name = 'AGIT'
GROUP BY
    p.name, r.name, t.tag_name, t.units;
*/    
/*Problem 1: JOIN with WHERE
Goal: Retrieve all the temperature (TEMP) and agitator (AGIT) readings for Reactor 1 (RCT1).

This problem requires you to join the readings and reactors tables, then use a WHERE clause to filter for the specific tag names and reactor name.
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
    plcs AS p ON r.plc_id = p.id
WHERE
    t.tag_name = 'TEMP' OR
    t.tag_name = 'AGIT'

ORDER BY
    p.name, r.name, t.tag_name, t.units
*/
/*Problem 2: JOIN with GROUP BY
Goal: Find the average value for each tag name (AGIT, TEMP, PRES) from Reactor 1 (RCT1).

This problem requires you to use the JOIN and WHERE clauses from the first problem, but you will also need to add a GROUP BY clause with an aggregation function to get the average.


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
/* Did not konw that WHERE was not needed when you are getting all values
Also could have used IN operator to make the where clause more concise.
Would have looked like this:
WHERE
    t.tag_name IN ('TEMP', 'AGIT', 'PRES')*/
GROUP BY
    p.name, r.name, t.tag_name, t.units;
*/
/* Problem 3: JOIN with GROUP BY and HAVING
Goal: Find the average agitator speed (AGIT) for Reactor 1, but only if the average speed is greater than 50.

This is the most complex problem. It combines all the concepts: JOIN to connect the tables, WHERE to filter for the correct reactor and tag, GROUP BY and AVG() to calculate the average, and a HAVING clause to filter the final result.
*/
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
    p.name, r.name, t.tag_name, t.units;
HAVING
    AVG(t.value) > 50
"""

cursor.execute(query)
results = cursor.fetchall()

print("PLC Name | Reactor Name | Tag Name | Value | Units")
print("--------------------------------------------------")
for row in results:
    print(row)

connection.close()