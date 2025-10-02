# I am importing pandas as pd for later use in the code.
import pandas as pd
# Load the CSV data into a DataFrame. The DataFrame automatically
# creates an index and uses the first row as column names.
df = pd.read_csv('flow_meter_data2.csv')
# Create a new dataframe containing only the rows where the Flow Rate is above 55 GPM.
high_flow_df = df[df['Flow Rate'] > 55]
# Print the new dataframe to the terminal.
print(high_flow_df)
filtered_df = df[df['Flow Rate'] > 45]
print(filtered_df)
# A list of dictionaries, where each dictionary represents an alarm.
# This data structure is a common way to store multiple records in Python.
alarms = [
    {"tag": "FT-101", "status": "Active", "priority": "Low"},
    {"tag": "PT-202", "status": "Active", "priority": "High"},
    {"tag": "LT-303", "status": "Inactive", "priority": "Medium"},
    {"tag": "TT-404", "status": "Active", "priority": "High"},
]

# The `for` loop iterates through the list, assigning each dictionary
# in the list to the variable 'alarm' for each iteration.
for alarm in alarms:
    # We use a conditional statement to check the value of the 'priority' key
    # within each alarm dictionary.
    if alarm["priority"] == "High":
        # The f-string formats the output dynamically based on the alarm's tag.
        print(f"Alarm {alarm['tag']} is high priority!")
    elif alarm["priority"] == "Medium":
        print(f"Alarm {alarm['tag']} is medium priority.")
    else:  # The 'else' block catches any other priority, in this case, "Low".
        print(f"Alarm {alarm['tag']} is low priority.")