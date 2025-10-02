import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Sample data
data = {
    'Timestamp': pd.to_datetime([
        '2025-09-07 08:00', '2025-09-07 09:00', '2025-09-07 10:00',
        '2025-09-07 11:00', '2025-09-07 12:00', '2025-09-07 13:00',
        '2025-09-07 14:00', '2025-09-07 15:00'
    ]),
    'Flow_Rate': [45.2, 51.1, 52.3, 50.1, 48.9, 44.5, 55.4, 56.1],
    'Process_Line': ['Line A', 'Line B', 'Line A', 'Line B',
                     'Line A', 'Line B', 'Line A', 'Line B'],
    'Shift': ['Shift 1', 'Shift 1', 'Shift 2', 'Shift 2',
              'Shift 1', 'Shift 1', 'Shift 2', 'Shift 2']
}

df = pd.DataFrame(data)

# Group by Shift and Process_Line
grouped = df.groupby(['Shift', 'Process_Line'])['Flow_Rate'].mean().unstack()
print(grouped)

grouped.plot(kind='bar', figsize=(8,5), color=['skyblue', 'orange'])
plt.title("Average Flow Rate by Shift and Process Line (Pandas)")
plt.ylabel("Flow Rate")
plt.grid(axis='y')
plt.show()



# Get X positions for bars
x = np.arange(len(grouped.index))  # Shift positions
width = 0.35  # Bar width

plt.figure(figsize=(8,5))

# Plot Line A
plt.bar(x - width/2, grouped['Line A'], width, label='Line A', color='skyblue', hatch='//')

# Plot Line B
plt.bar(x + width/2, grouped['Line B'], width, label='Line B', color='orange', hatch='xx')

# Customize axes
plt.xticks(x, grouped.index)  # Use Shift labels
plt.title("Average Flow Rate by Shift and Process Line (Matplotlib)")
plt.ylabel("Flow Rate")
plt.legend()
plt.grid(axis='y')

plt.show()