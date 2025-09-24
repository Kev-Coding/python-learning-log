import pandas as pd
import sqlite3

# --- READ CSV ---
print("\n--- Reading CSV ---")
df_csv = pd.read_csv("simulated_sensor_data.csv")
print("CSV shape:", df_csv.shape)
print("CSV columns:", df_csv.columns.tolist())
print(df_csv.head(), "\n")

# --- READ SQLITE / DB ---
print("--- Reading SQLite / DB ---")
conn = sqlite3.connect("database_conn_lesson.db.sqlite")   # or flow_data.db
# List tables
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in DB:", tables)

# Pick first table and read
table_name = tables.iloc[0, 0]
df_db = pd.read_sql(f"SELECT * FROM {table_name}", conn)
print("DB shape:", df_db.shape)
print("DB columns:", df_db.columns.tolist())
print(df_db.head(), "\n")

# Pick second table and read
table2_name = tables.iloc[2, 0]
df2_db = pd.read_sql(f"SELECT * FROM {table2_name}", conn)
print("DB shape:", df2_db.shape)
print("DB columns:", df2_db.columns.tolist())
print(df2_db.head(), "\n")

conn.close()