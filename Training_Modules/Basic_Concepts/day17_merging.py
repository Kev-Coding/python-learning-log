import pandas as pd
import numpy as np

# Create DataFrame 1 (Flow Meter Readings)
flow_data = {
    'Timestamp': pd.to_datetime(['2025-09-08 08:00', '2025-09-08 09:00', '2025-09-08 10:00', '2025-09-08 11:00']),
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1]
}
flow_df = pd.DataFrame(flow_data)

# Create DataFrame 2 (Pressure Readings)
# Notice that one timestamp is missing from this DataFrame
pressure_data = {
    'Timestamp': pd.to_datetime(['2025-09-08 08:00', '2025-09-08 10:00', '2025-09-08 11:00']),
    'Pressure': [25.5, 28.9, 32.2]
}
pressure_df = pd.DataFrame(pressure_data)


# --- TASK 1: Perform an Inner Merge ---
# This merge keeps only the rows with a matching 'Timestamp' in both DataFrames.
# It is the most restrictive merge type.
print("\n--- Inner Merge (default) ---")
merged_inner = pd.merge(flow_df, pressure_df, on='Timestamp', how='inner')
print(merged_inner)

# --- TASK 2: Perform a Left Merge ---
# This merge keeps all rows from the left DataFrame (`flow_df`).
# A NaN value is inserted where there is no matching Timestamp in the right DataFrame.
print("\n--- Left Merge ---")
merged_left = pd.merge(flow_df, pressure_df, on='Timestamp', how='left')
print(merged_left)

# --- TASK 3: Perform an Outer Merge ---
# This merge keeps all rows from both DataFrames, filling in NaN for non-matching rows.
# It is the least restrictive merge type.
print("\n--- Outer Merge ---")
merged_outer = pd.merge(flow_df, pressure_df, on='Timestamp', how='outer')
print(merged_outer)

# --- TASK 4: Perform a Right Merge ---
# This merge keeps all rows from the right DataFrame (`pressure_df`).
# A NaN value is inserted where there is no matching Timestamp in the left DataFrame.
print("\n--- Right Merge ---")
merged_right = pd.merge(flow_df, pressure_df, on='Timestamp', how='right')
print(merged_right)