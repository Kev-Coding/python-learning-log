import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# The .close() method closes the connection to the database.
conn.close()

print("Database 'database_conn_lesson.db.sqlite' created with 'sensor_data' table.")



