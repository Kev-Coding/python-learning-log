import pandas as pd
import numpy as np

# Load the CSV file. This is an excellent practice for a modular pipeline.
df = pd.read_csv('simulated_sensor_data.csv')

# --- PART 1: Data Cleaning and Flatline Detection ---

# Use .dropna() as you did. It's the correct first step.
df = df.dropna().copy()
print("--- DataFrame after dropping rows with missing values ---")
print(df)

# We are going to explicitly select only the numerical columns before calling .diff().
# This avoids the TypeError from the 'Timestamp' column.
numerical_cols = ['Flow_Rate', 'Pressure']

# The `.diff()` method will now only operate on the selected columns.
# The `any(axis=1)` method checks for a change in ANY of the selected columns.
# We use the `~` to get the rows where the data has changed.
mask = (df[numerical_cols].diff() != 0).any(axis=1)

# We always keep the first row because the diff() method will give it a NaN.
# The mask.iloc[0] = True ensures the first row is always True.
mask.iloc[0] = True

# We apply the mask to get a clean DataFrame.
df_clean = df[mask].copy()

print("\n--- DataFrame after removing flatline signals ---")
print(df_clean)

# We can also verify that the flatline signals were removed by printing the
# full DataFrame and then the cleaned DataFrame.