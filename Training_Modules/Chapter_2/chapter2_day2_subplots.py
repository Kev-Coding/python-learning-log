import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame with two groups
data = {
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1, 58.9],
    'Pressure': [25.5, 30.1, 45.4, 32.2, 29.5]
}

df = pd.DataFrame(data)

# # Firt subplot: Line chart of Flow Rate vs Index
# plt.subplot(2, 1, 1)  # (rows, columns, panel number)
# plt.plot(df.index, df['Flow_Rate'], marker='o', linestyle='-', color='b')
# plt.xlabel("Index")        # X-axis label
# plt.ylabel("Flow Rate")    # Y-axis label 
# plt.title("Flow Rate vs Index")  # Title of the plot
# plt.grid(True)  # Add grid for better readability
# plt.tight_layout()  # Adjust layout to prevent overlap
# # Second subplot: Scatter plot of Flow Rate vs Pressure
# plt.subplot(2, 1, 2)  # (rows, columns, panel number)
# plt.scatter(df['Pressure'], df['Flow_Rate'], color='r', marker='x')
# plt.xlabel("Pressure")        # X-axis label
# plt.ylabel("Flow Rate")    # Y-axis label
# plt.title("Flow Rate vs Pressure")  # Title of the plot
# plt.grid(True)  # Add grid for better readability
# plt.tight_layout()  # Adjust layout to prevent overlap
# plt.show()

# use subplots with a figure with two plots stacked on top of each other
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))  # 2 rows, 1 column

# First subplot: Line chart of Flow Rate vs Index
ax1.plot(df.index, df['Flow_Rate'], marker='o', linestyle='-', color='b')
ax1.set_xlabel("Index")        # X-axis label
ax1.set_ylabel("Flow Rate")    # Y-axis label
ax1.set_title("Flow Rate vs Index")  # Title of the plot
ax1.grid(True)  # Add grid for better readability

# Second subplot: Scatter plot of Flow Rate vs Pressure
ax2.scatter(df['Pressure'], df['Flow_Rate'], color='r', marker='x')
ax2.set_xlabel("Pressure")        # X-axis label
ax2.set_ylabel("Flow Rate")    # Y-axis label
ax2.set_title("Flow Rate vs Pressure")  # Title of the plot
ax2.grid(True)  # Add grid for better readability

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()