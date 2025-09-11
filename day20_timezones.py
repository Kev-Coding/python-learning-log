import pandas as pd
import numpy as np

# Create a sample DataFrame with a timezone-naive datetime column
data = {
    'Timestamp': pd.to_datetime(['2025-09-08 12:00:00', '2025-09-08 13:00:00', '2025-09-08 14:00:00']),
    'Flow_Rate': [52.1, 44.5, 55.4]
}

df = pd.DataFrame(data)

print("--- Original Timezone-Naive DataFrame ---")
print(df)
print("\nTimestamp dtype:", df['Timestamp'].dtype)

# task 1 - Make a new column that is timezone-aware. Do not assign a timezone yet and print the df.
df['Timestamp_Aware'] = df['Timestamp'].dt.tz_localize('UTC')
print(df)

# task 2 - Create a new "Timestamp_CST" the timezone-aware column to 'America/Chicago' timezone and print the df.
df['Timestamp_CST'] = df['Timestamp_Aware'].dt.tz_convert('America/Chicago')
print(df)

# task 3 - create a new 'Timestamp_Naive' column from the 'Timestamp_CST' column that is timezone-naive and print the df.
df['Timestamp_Naive'] = df['Timestamp_CST'].dt.tz_localize(None)
print(df)