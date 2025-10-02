import sqlite3

# 1. Connect to the database.
connection = sqlite3.connect('flow_meter_data.db')
cursor = connection.cursor()

# 2. Define the table.
create_table_sql = """
CREATE TABLE IF NOT EXISTS flow_data (
    timestamp TEXT NOT NULL,
    tagname TEXT NOT NULL,
    value REAL NOT NULL,
    units TEXT
);
"""
cursor.execute(create_table_sql)

# 3. Create a list to hold all our data.
data_to_insert = []

# 4. Open and parse all raw data from the text file.
try:
    with open('flow_meter_data.txt', 'r') as file:
        for line in file:
            # Check for a valid data line.
            if '|' in line:
                parts = line.strip().split('|')
                timestamp = parts[0].split(': ')[1]
                flow_part = parts[1].split(': ')[1]
                flow_rate_value = float(flow_part.split(' ')[0])
                units = flow_part.split(' ')[1]

                # Append the parsed data as a tuple to our list.
                data_to_insert.append((timestamp, 'Flow Rate', flow_rate_value, units))

    # 5. Use `executemany()` to insert all rows at once.
    insert_data_sql = """
    INSERT INTO flow_data (timestamp, tagname, value, units) VALUES (?, ?, ?, ?);
    """
    cursor.executemany(insert_data_sql, data_to_insert)

    # 6. Commit the changes to the database.
    connection.commit()
    print("Database has been populated successfully.")

except FileNotFoundError:
    print("Error: The 'flow_meter_data.txt' file was not found. Please make sure it is in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")
    # Rollback changes if an error occurs.
    connection.rollback()
finally:
    # 7. Close the connection.
    connection.close()