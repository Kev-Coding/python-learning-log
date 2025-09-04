# Import the pandas library with the standard alias 'pd'
import pandas as pd

# Load the CSV data into a DataFrame. The DataFrame automatically
# creates an index and uses the first row as column names.
df = pd.read_csv('flow_meter_data2.csv')

# --- Basic Data Inspection ---

# Prints the entire DataFrame to the terminal.
print(df)

# The .head() method displays the top 5 rows of the DataFrame by default.
# It is used for a quick check to ensure the data was loaded correctly.
print("\n--- Using .head() to inspect the first 5 rows ---")
print(df.head())

# The .tail() method displays the last 5 rows of the DataFrame.
# It's useful for checking the end of a dataset.
print("\n--- Using .tail() to inspect the last 5 rows ---")
print(df.tail())

# --- Descriptive Statistics ---

# Selects the 'Flow Rate' column and calculates the mean (average).
# The .mean() method is a key statistical metric for a process's average behavior.
print("\n--- Calculating the Mean (Average) Flow Rate ---")
print(df['Flow Rate'].mean())

# The .max() and .min() methods find the highest and lowest values in a column.
# This is used to check the data range and identify potential outliers.
print("\n--- Finding the Minimum and Maximum Flow Rate ---")
print(f"Maximum Flow Rate: {df['Flow Rate'].max()} GPM")
print(f"Minimum Flow Rate: {df['Flow Rate'].min()} GPM")

# The .std() method calculates the standard deviation.
# This metric shows how spread out the data is from the average,
# indicating process stability.
print("\n--- Calculating the Standard Deviation of the Flow Rate ---")
print(df['Flow Rate'].std())

# You can also use methods on a subset of the DataFrame, as shown here.
print("\n--- Using .head() on a single column ---")
print(df['Flow Rate'].head())