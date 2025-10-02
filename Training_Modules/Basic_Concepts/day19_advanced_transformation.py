import pandas as pd
import numpy as np

# Create a sample DataFrame for this lesson
data = {
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1, 58.9],
    'Pressure': [25.5, 78.1, 45.4, 66.2, 90.5],
    'Status': ['Running', 'Running', 'Running', 'Idle', 'Running']
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)

#create a new column called "Flow_Status" that categorizes the flow rate as "High Flow" if it is above 55 and "Normal" otherwise.
df['Flow_Status'] = np.where(df['Flow_Rate'] > 55, 'High Flow', 'Normal')

print("--- Transformed DataFrame ---")
print(df)

df['Pressure_Status'] = np.where(df['Pressure'] > 70, 'High Pressure', 'Normal')
print("--- DataFrame with Pressure Status ---")
print(df)   

# move "Flow_Status" column after "Flow_Rate"
df = df[['Flow_Rate', 'Flow_Status', 'Pressure', 'Pressure_Status', 'Status']]
print("--- DataFrame with Reordered Columns ---")
print(df)   

# change the name of "Status" column to "Machine_Status"
df = df.rename(columns={'Status': 'Machine_Status'})
print("--- DataFrame with Renamed Column ---")
print(df)

# convert all values in "Machine_Status" column to uppercase
df['Machine_Status'] = df['Machine_Status'].str.upper()     
print("--- DataFrame with Uppercase Machine_Status ---")
print(df)

# Using a custom function to categorize pressure levels.
def pressure_to_category(pressure):
    if pressure < 30:
        return 'Low'
    elif 30 <= pressure < 70:
        return 'Medium'
    else:
        return 'High'
    
 # Apply the function to create a new column "Pressure_Category"  
df['Pressure_Category'] = df['Pressure'].apply(pressure_to_category)
print("--- DataFrame with Pressure Category ---")
print(df)   

# Create a new DataFrame that only contains readings where 'Status' is 'Running'.
# We explicitly call .copy() to ensure we are working with an independent DataFrame.
running_df = df[df['Machine_Status'] == 'RUNNING'].copy()

# Reorder columns for better readability.
running_df = running_df[['Flow_Rate', 'Flow_Status', 'Pressure', 'Pressure_Status', 'Pressure_Category', 'Machine_Status']]

print("--- DataFrame with Running Status ---")
print(running_df)
