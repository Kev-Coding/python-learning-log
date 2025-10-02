import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame for grouping practice
data = {
    'Timestamp': pd.to_datetime(['2025-09-07 08:00', '2025-09-07 09:00', '2025-09-07 10:00',
                               '2025-09-07 11:00', '2025-09-07 12:00', '2025-09-07 13:00',
                               '2025-09-07 14:00', '2025-09-07 15:00']),
    'Flow_Rate': [45.2, 51.1, 52.3, 50.1, 48.9, 44.5, 55.4, 56.1],
    'Process_Line': ['Line A', 'Line B', 'Line A', 'Line B', 'Line A', 'Line B', 'Line A', 'Line B'],
    'Shift': ['Shift 1', 'Shift 1', 'Shift 2', 'Shift 2', 'Shift 1', 'Shift 1', 'Shift 2', 'Shift 2']
}

df = pd.DataFrame(data)

# --- TASK 1: Simple Grouping (Current Report) ---
shift_averages = df.groupby('Shift')['Flow_Rate'].mean()
print("Shift Averages:\n", shift_averages)

plt.figure(figsize=(8, 5))
plt.bar(shift_averages.index, shift_averages.values, color='skyblue')
plt.xlabel('Shift')
plt.ylabel('Average Flow Rate')
plt.title('Average Flow Rate per Shift (Total)')
plt.grid(axis='y')
plt.show()

# --- NEW TASK: Multi-Level Grouping and Bar Chart ---

# 1. Group by BOTH Shift AND Process_Line
line_shift_averages = df.groupby(['Shift', 'Process_Line'])['Flow_Rate'].mean()
print(line_shift_averages)
# 2. Use .unstack() to put Process_Line into separate columns (required for plotting side-by-side bars)
line_shift_report = line_shift_averages.unstack()
print(line_shift_report)

print("\nLine & Shift Averages (Unstacked):\n", line_shift_report)

# 3. Plot the Multi-Level Report

line_shift_report.plot(kind='bar', figsize=(8, 5))

plt.xlabel('Shift')
plt.ylabel('Average Flow Rate')
plt.title('Average Flow Rate per Line and Shift')
plt.grid(axis='y')
plt.legend(title='Process Line')
plt.show()