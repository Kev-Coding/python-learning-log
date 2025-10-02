import pandas as pd
import sqlite3


def run_etl_pipeline():
    """
    Runs a full ETL (Extract, Transform, Load) pipeline for practice.
    This function demonstrates converting data from CSV to SQL and back.
    """
    # Define file and table names for clarity.
    csv_file = 'simulated_sensor_data.csv'
    db_file = 'converted_to_sqlite.db.sqlite'
    sql_table = 'sensor_data'
    new_csv_file = 'sqlite_to_csv.csv'

    # --- EXTRACT (from CSV) ---
    print("--- Reading data from CSV ---")
    df_csv = pd.read_csv(csv_file)
    print("CSV shape:", df_csv.shape, "\n")

    # --- LOAD (to SQLite) ---
    print("--- Loading data into SQLite ---")
    # Using a try...finally block ensures the connection is always closed.
    conn = sqlite3.connect(db_file)
    try:
        # The 'if_exists=replace' parameter is key for a repeatable process.
        df_csv.to_sql(sql_table, conn, if_exists='replace', index=False)
        print("Data successfully loaded into the SQLite database.\n")
    finally:
        conn.close()

    # --- EXTRACT (from SQLite) ---
    print("--- Reading data from SQLite back into a DataFrame ---")
    conn = sqlite3.connect(db_file)
    try:
        # Use pd.read_sql() to pull the data with a simple query.
        df_sql = pd.read_sql(f"SELECT * FROM {sql_table}", conn)
        print("Data read from SQLite shape:", df_sql.shape, "\n")
    finally:
        conn.close()

    # --- LOAD (to new CSV) ---
    print("--- Saving data from DataFrame to a new CSV ---")
    df_sql.to_csv(new_csv_file, index=False)
    print("Full ETL cycle complete. Data saved to:", new_csv_file)


if __name__ == "__main__":
    run_etl_pipeline()