import sqlite3

# 1. Connect to the database file. If it doesn't exist, this will create it.
connection = sqlite3.connect('flow_meter_data.db')

# 2. Create a cursor object.
cursor = connection.cursor()

# 3. Use the `CREATE TABLE` command to define the structure, now including a `units` column.
create_table_sql = """
CREATE TABLE IF NOT EXISTS flow_data (
    timestamp TEXT NOT NULL,
    tagname TEXT NOT NULL,
    value REAL NOT NULL,
    units TEXT
);
"""
cursor.execute(create_table_sql)

# 4. Open and read your raw data from the text file.
try:
    with open('flow_meter_data.txt', 'r') as file:
        # 5. Loop through each line in the file.
        for line in file:
            # A simple check to skip any lines that don't contain the pipe character.
            if '|' in line:
                # Strip whitespace and split the line by the pipe character.
                parts = line.strip().split('|')

        # Extract the timestamp value. We split by ':' and take the second part.
        timestamp = parts[0].split(': ')[1]

        # Extract the flow rate and units. We split by ':' and then by ' '.
        flow_part = parts[1].split(': ')[1]
        flow_rate_value = float(flow_part.split(' ')[0])
        units = flow_part.split(' ')[1]

        # Define the SQL command to insert our record.
        insert_data_sql = """
        INSERT INTO flow_data (timestamp, tagname, value, units) VALUES (?, ?, ?, ?);
        """

        # Execute the command with our extracted values.
        cursor.execute(insert_data_sql, (timestamp, 'Flow Rate', flow_rate_value, units))


    # 6. Commit the changes to the database.
    connection.commit()
    print("Database has been populated successfully.")

except FileNotFoundError:
    print("Error: The 'flow_meter_data.txt' file was not found. Please make sure it is in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 7. Close the connection.
    connection.close()
