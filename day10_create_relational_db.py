import sqlite3

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

# 1. Create the `plcs` table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS plcs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    );
""")

# 2. Create the `reactors` table with a foreign key to the `plcs` table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reactors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        plc_id INTEGER,
        FOREIGN KEY (plc_id) REFERENCES plcs(id)
    );
""")

# 3. Create the `readings` table with a foreign key to the `reactors` table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS readings (
        id INTEGER PRIMARY KEY,
        timestamp TEXT NOT NULL,
        tag_name TEXT NOT NULL,
        value REAL NOT NULL,
        units TEXT NOT NULL,
        reactor_id INTEGER,
        FOREIGN KEY (reactor_id) REFERENCES reactors(id)
    );
""")

connection.commit()
connection.close()

print("Relational database structure created successfully.")

import sqlite3
import random
import time

connection = sqlite3.connect('relational_tags.db')
cursor = connection.cursor()

# Insert the parent PLC and reactors
cursor.execute("INSERT OR IGNORE INTO plcs (name) VALUES ('MPS226');")
plc_id = cursor.execute("SELECT id FROM plcs WHERE name='MPS226'").fetchone()[0]

cursor.execute("INSERT OR IGNORE INTO reactors (name, plc_id) VALUES ('RCT1', ?);", (plc_id,))
reactor1_id = cursor.execute("SELECT id FROM reactors WHERE name='RCT1' AND plc_id=?", (plc_id,)).fetchone()[0]

# Generate and insert simulated data for Reactor 1
readings = []
for i in range(20):
    timestamp = str(time.time())
    
    # Simulate AGIT readings (0-100 RPM)
    agit_value = random.uniform(0, 100)
    readings.append((timestamp, 'AGIT', agit_value, 'RPM', reactor1_id))

    # Simulate TEMP readings (-15-100 deg C)
    temp_value = random.uniform(-15, 100)
    readings.append((timestamp, 'TEMP', temp_value, 'deg C', reactor1_id))

    # Simulate PRES readings (-15-100 PSI)
    pres_value = random.uniform(-15, 100)
    readings.append((timestamp, 'PRES', pres_value, 'PSI', reactor1_id))
    time.sleep(0.5)

cursor.executemany(
    "INSERT INTO readings (timestamp, tag_name, value, units, reactor_id) VALUES (?, ?, ?, ?, ?);",
    readings
)

connection.commit()
connection.close()

print("Database populated with simulated data.")