import pandas as pd
import sqlite3

# convert .csv to .sqlite. Could state create a .sqlite from a .csv
df_csv = pd.read_csv('simulated_sensor_data.csv')
conn = sqlite3.connect('converted_to_sqlite.db.sqlite')
df_csv.to_sql('csv_to_sqlite', conn, if_exists = 'replace', index= False)
# --- Verify by reading back ---
df_check = pd.read_sql("SELECT * FROM csv_to_sqlite", conn)
print("Converted CSV → SQLite file created!")
print("From SQLite:", df_check, "\n")
# --- READ SQLITE / DB ---
print("--- Reading SQLite / DB ---")
conn = sqlite3.connect("converted_to_sqlite.db.sqlite")   # or flow_data.db
# List tables
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in DB:", tables)
conn.close()





