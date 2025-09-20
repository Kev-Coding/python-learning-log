import sqlite3
import random
import time

# --- A function to create and populate the database ---
def create_and_populate_db():
    """
    Creates a new SQLite database, a table, and inserts sample data.
    """
    # Use the sqlite3.connect() function to connect to a database file.
    conn = sqlite3.connect('database_conn_lesson.db.sqlite')
    cursor = conn.cursor()

    # Create the table from yesterday's lesson.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY,
        timestamp INTEGER,
        flow_rate REAL
    )
    ''')
    conn.commit()

    # --- Create a list of sample data ---
    start_timestamp = int(time.time())
    sample_data = [
        (start_timestamp + i * 60, round(random.uniform(18.0, 22.0), 2))
        for i in range(10)
    ]
    
    # --- Write the SQL INSERT statement ---
    # The '?' placeholders are a key security feature.
    insert_data_sql = "INSERT INTO sensor_data (timestamp, flow_rate) VALUES (?,?);"

    # --- Use executemany to insert the data ---
    # This is the most efficient way to insert multiple rows.
    cursor.executemany(insert_data_sql, sample_data)

    # Commit and close the connection.
    conn.commit()
    conn.close()

# --- A function to read the data from the database ---
def read_and_print_db():
    """
    Connects to the database, reads all data, and prints it.
    """
    # Connect to the database.
    conn = sqlite3.connect('database_conn_lesson.db.sqlite')
    cursor = conn.cursor()
    
    # Execute the query.
    query = "SELECT * FROM sensor_data"
    cursor.execute(query)

    # Print the results.
    print("Index | Timestamp | Flow Rate")
    print("-" * 30)

    results = cursor.fetchall()
    for row in results:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    
    conn.close()

# --- The main function to run the script ---
if __name__ == "__main__":
    create_and_populate_db()
    print("Data successfully inserted into the database.")
    read_and_print_db()