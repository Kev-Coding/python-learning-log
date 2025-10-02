import pandas as pd
import sqlite3

conn = sqlite3.connect('converted_to_sqlite.db.sqlite')
df_sqlite = pd.read_sql('Select * FROM csv_to_sqlite', conn)
# convert to csv from sqlite
df_sqlite.to_csv('sqlite_to_csv.csv', index = False)
print("Converted SQLite → CSV file created!")
conn.close()


df_csv1 = pd.read_csv('sqlite_to_csv.csv')
print("CSV shape:", df_csv1.shape)
print("CSV columns:", df_csv1.columns.tolist())
print(df_csv1.head(), "\n")

conn1 = sqlite3.connect('database_conn_lesson.db.sqlite')
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn1)
print("Tables in DB:", tables)
df_sqlite1 = pd.read_sql('SELECT * FROM cleaned_data', conn1)
df_sqlite1.to_csv('clean_data_to_csv.csv', index=False)
conn1.close()

df_csv2 = pd.read_csv('clean_data_to_csv.csv')
print("CSV shape:", df_csv2.shape)
print("CSV columns:", df_csv2.columns.tolist())
print(df_csv2.head(), "\n")