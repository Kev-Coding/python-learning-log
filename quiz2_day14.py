# I am importing pandas as pd for later use in the code.
import pandas as pd
# Import the numpy library for numerical operations.
# It's good practice to import numpy explicitly, even though pandas uses it.
import numpy as np
# Load the CSV data into a DataFrame. The DataFrame automatically
# creates an index and uses the first row as column names.
df = pd.read_csv('flow_meter_data2.csv')

# We use the explicit numpy import to calculate the mean of the timestamp.
# Note: df['Timestamp'].mean() would also work, but np.mean() is a core NumPy function.
average_timestamp = np.mean(filtered_df['Timestamp'])

# Create a new dataframe containing only the rows where the Flow Rate is above 55 GPM.
filtered_df = df[df['Flow Rate'] > 55]
# Print the new dataframe to the terminal.
print(filtered_df)
# print the filtered_df calculate the average time stamp and the standard deviation of the flow rate
print(f"Average Timestamp:  {filtered_df['Timestamp'].mean()}")
print(f"Flow Rate Standard Deviation: {filtered_df['Flow Rate'].std()}")
#Create a new column in filtered_df called Alarm_Status that contains the string 'High Flow Alarm' for every row.
filtered_df['Alarm_Status'] = 'High Flow Alarm'
print(filtered_df)