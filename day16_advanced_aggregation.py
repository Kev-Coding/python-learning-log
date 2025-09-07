import pandas as pd
import numpy as np

# Create a sample DataFrame with multiple groups for a controlled test.
data = {
    'Timestamp': pd.to_datetime(['2025-09-07 08:00', '2025-09-07 09:00', '2025-09-07 10:00',
                               '2025-09-07 11:00', '2025-09-07 12:00', '2025-09-07 13:00',
                               '2025-09-07 14:00', '2025-09-07 15:00', '2025-09-07 16:00',
                               '2025-09-07 17:00']),
    'Process_Line': ['Line A', 'Line B', 'Line A', 'Line B', 'Line A', 'Line B', 'Line A', 'Line B', 'Line A', 'Line B'],
    'Shift': ['Shift 1', 'Shift 1', 'Shift 1', 'Shift 1', 'Shift 2', 'Shift 2', 'Shift 2', 'Shift 2', 'Shift 2', 'Shift 2'],
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1, 58.9, 52.3, 50.1, 48.2, 53.4, 47.9],
    'Pressure': [25.5, 30.1, 28.9, 32.2, 29.5, 31.1, 27.8, 30.5, 26.7, 33.1]
}

df = pd.DataFrame(data)

# --- TASK 1: Group by multiple columns and get the mean ---
print("--- Grouped by Process_Line and Shift with mean aggregation ---")
# When you pass a list of column names to .groupby(), Pandas creates a
# MultiIndex, which is a hierarchical index for your summarized data.
# The .agg() method is then used to apply the 'mean' function to the selected columns.
multi_grouped_mean = df.groupby(['Process_Line', 'Shift'])[['Flow_Rate', 'Pressure']].agg('mean')
print(multi_grouped_mean)

# --- TASK 2: Custom Aggregation ---

# We define the function to be a custom aggregation.
# It receives a Series (a column from a single group) as its argument.
def flow_in_spec(series):
    """
    Returns True if the mean of the series is between 45 and 55, otherwise returns False.
    """
    # The key here is to calculate the mean of the series first.
    mean_value = series.mean()
    # Then, we check if that single mean value is within our specified range.
    return mean_value >= 45 and mean_value <= 55

# Group the data by multiple columns
grouped_data = df.groupby(['Process_Line', 'Shift'])

# Apply the custom 'flow_in_spec' function to the 'Flow_Rate' column of each group.
in_spec_status = grouped_data['Flow_Rate'].agg(flow_in_spec)

print("\n--- Custom Aggregation: Flow In Spec Status ---")
print(in_spec_status)