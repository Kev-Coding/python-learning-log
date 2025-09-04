import pandas as pd
df = pd.read_csv('flow_meter_data2.csv')

# --- TASK 1: Select a single column ---
# You can access a column using bracket notation with the column's name.
flow_rate_column = df['Flow Rate']
print("--- Selecting a single column ---")
print(flow_rate_column)

# --- TASK 2: Filter rows based on a condition ---
# This is a key data engineering skill. We create a boolean Series
# where each row is True or False based on the condition.
is_flow_high = df['Flow Rate'] > 50

# Then, we use that boolean Series to filter the DataFrame.
filtered_df = df[is_flow_high]
print("\n--- Filtering rows with a condition ---")
print(filtered_df)

# --- TASK 3: Create a new calculated column ---
# We can create a new column and assign it a value based on a calculation.
# This is much more efficient than using a for loop.
df['Flow Rate m3/h'] = df['Flow Rate'] * 0.227125
print("\n--- Creating a new calculated column ---")
print(df)