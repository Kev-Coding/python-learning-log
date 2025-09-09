import pandas as pd
import numpy as np

# Create a sample DataFrame with intentional data problems
data = {
    'Timestamp': [1757308800, 1757312400, 1757316000, 1757319600, 1757323200],
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1, 58.9],
    'Pressure': [25.5, 30.1, np.nan, 32.2, 29.5]  # The 'np.nan' is a missing value
}

df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)
#fill missing values in pressure column with mean of the column
filled_df = df.fillna(df['Pressure'].mean())
print("\n--- DataFrame after filling missing values in 'Pressure' column ---")
print(filled_df)

dropped_df = df.dropna()
print("\n--- DataFrame after dropping rows with missing values ---")
print(dropped_df)

# Convert 'Timestamp' from Unix epoch to human-readable datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
filled_df['Timestamp'] = pd.to_datetime(filled_df['Timestamp'], unit='s')
dropped_df['Timestamp'] = pd.to_datetime(dropped_df['Timestamp'], unit='s')

print("\n--- DataFrame after converting 'Timestamp' to datetime format ---")
print(df)
print(filled_df)
print(dropped_df)
