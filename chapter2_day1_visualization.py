import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame with two groups
data = {
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1, 58.9],
    'Pressure': [25.5, 30.1, 45.4, 32.2, 29.5]
}

df = pd.DataFrame(data)
# Use plt.plot() to create a line chart. We'll plot Flow_Rate on the Y-axis and the DataFrame's index on the X-axis.
# Use plt.show() to display the plot.
plt.plot(df.index, df['Flow_Rate'], marker='o', linestyle='-', color='b')

# Add axis labels
plt.xlabel("Index")        # X-axis label
plt.ylabel("Flow Rate")    # Y-axis label
plt.title("Flow Rate vs Index")  # Title of the plot

plt.show()

plt.scatter(df['Pressure'], df['Flow_Rate'], color='r', marker='x')
plt.xlabel("Pressure")        # X-axis label
plt.ylabel("Flow Rate")    # Y-axis label
plt.title("Flow Rate vs Pressure")  # Title of the plot
plt.show()

plt.plot(df.index, df['Flow_Rate'], marker='o', linestyle='-', color='b', label='Flow Rate')
plt.plot(df.index, df['Pressure'], marker='s', linestyle='--', color='r', label='Pressure')

plt.xlabel("Index")
plt.ylabel("Measurement Value")
plt.title("Flow Rate vs Pressure Over Time")

plt.legend()   # <-- this shows the labels from above on the plot

plt.show()