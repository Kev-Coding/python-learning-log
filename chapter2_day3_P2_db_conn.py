import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# create a list of tuples with timestamp as an int and flow_rate as a float.

import time
import random

# Start from a base Unix timestamp (approximately 10 mins ago)
start_timestamp = 1758404597  

# Generate 10 data points, 1-minute apart
sample_data = [
    (start_timestamp + i * 60, round(random.uniform(18.0, 22.0), 2))
    for i in range(10)
]



# --- TASK 1: Connect to a database and create a cursor ---
# We use the sqlite3.connect() function to connect to a database file.
# If the file does not exist, it will be created automatically.
conn = sqlite3.connect('database_conn_lesson.db.sqlite')

# A cursor is an object that you'll use to execute SQL commands.
cursor = conn.cursor()

# --- TASK 2: Execute a SQL command to create a table ---
# We use a multi-line string (triple quotes) for clarity.
# The 'id' column is a PRIMARY KEY, which ensures each row has a unique identifier.
# The 'IF NOT EXISTS' part prevents the script from crashing if the table already exists.
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY, 
    timestamp INTEGER,
    flow_rate REAL
)
''')
# --- TASK 3: Commit and close the connection ---
# The .commit() method saves all changes to the database file.
conn.commit()


insert_data_sql = '''
               INSERT INTO sensor_data (timestamp, flow_rate) VALUES (?,?);               
               ''' 

cursor.executemany(insert_data_sql, sample_data)

query = "SELECT * FROM sensor_data"

# 3. Execute the query.
cursor.execute(query)

print("Index | Timestamp | Flow Rate")
print("-" * 30)

results = cursor.fetchall()
for row in results:
    print(row)

# The .close() method closes the connection to the database.
conn.close()



