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

# We'll use a single line of code to do all the conversions
# First, we localize the data to UTC (the source timezone)
# Then, we convert it to the destination timezone ('US/Central')
df['Timestamp'] = df['Timestamp'].dt.tz_localize('UTC').dt.tz_convert('US/Central')

print("\n--- Converted and Final DataFrame ---")
print(df)
print("\nFinal Timestamp dtype:", df['Timestamp'].dtype)