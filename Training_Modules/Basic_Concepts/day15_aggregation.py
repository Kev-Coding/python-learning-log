import pandas as pd
import numpy as np

# Create a sample DataFrame with two groups
# This is a good way to test your code when you don't have a real file yet
data = {
    'Timestamp': pd.to_datetime(['2025-09-05 08:00', '2025-09-05 09:00', '2025-09-05 10:00',
                               '2025-09-05 11:00', '2025-09-05 12:00', '2025-09-05 13:00',
                               '2025-09-05 14:00', '2025-09-05 15:00']),
    'Flow_Rate': [45.2, 51.1, 52.3, 50.1, 48.9, 44.5, 55.4, 56.1],
    'Process_Line': ['Line A', 'Line B', 'Line A', 'Line B', 'Line A', 'Line B', 'Line A', 'Line B'],
    'Shift': ['Shift 1', 'Shift 1', 'Shift 2', 'Shift 2', 'Shift 1', 'Shift 1', 'Shift 2', 'Shift 2']
}

df = pd.DataFrame(data)

#print df and its structure.
# print(df)
# print(df.info())

# --- TASK 1: Group by a single column and get the mean ---
# Your code for this task goes here...
df_grouped = df.groupby('Process_Line').mean(numeric_only=True)
print("\n--- Grouped by Process_Line with mean aggregation ---")
print(df_grouped)


# --- TASK 2: Group by a different column and get multiple aggregations ---
# Your code for this task goes here...
df_grouped_multi_agg = df.groupby('Shift').agg({'Flow_Rate': ['mean', 'max', 'min', 'std']})
print("\n--- Grouped by Shift with multiple aggregations ---")
print(df_grouped_multi_agg)