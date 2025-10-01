import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame with simulated, correlated data
data = {
    'Time_Index': np.arange(10),
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1, 58.9, 53.0, 47.5, 51.2, 49.8, 54.3],
    'Pressure': [25.5, 29.1, 35.4, 30.2, 38.5, 33.0, 31.5, 34.2, 32.8, 36.3]
}

df = pd.DataFrame(data)

# --- TASK 1: Create the figure and two axes (plots) ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))


# --- TASK 2: Plot the Time Series (Top Panel) ---
# Use ax1 methods for the top plot.
ax1.plot(df['Time_Index'], df['Flow_Rate'], label='Flow Rate (GPM)', color='b', marker='o')
ax1.plot(df['Time_Index'], df['Pressure'], label='Pressure (PSI)', color='r', linestyle='--')
ax1.set_title('Process Trend Over Time')
ax1.set_ylabel('Process Value')
ax1.legend()
ax1.grid(True)


# --- TASK 3: Plot the Correlation (Bottom Panel) ---
# Use ax2 methods for the bottom plot.
ax2.scatter(df['Flow_Rate'], df['Pressure'], color='g', marker='x')
ax2.set_title('Flow Rate vs. Pressure (Correlation)')
ax2.set_xlabel('Flow Rate (GPM)')
ax2.set_ylabel('Pressure (PSI)')
ax2.grid(True)


# --- TASK 4: Final Cleanup ---
# Adjust spacing to prevent titles and labels from overlapping.
plt.tight_layout()

# Display the resulting report.
plt.show()