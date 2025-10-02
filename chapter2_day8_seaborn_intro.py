import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Seaborn is almost always imported as sns
import seaborn as sns 

# Create a sample DataFrame with simulated, correlated data
data = {
    'Flow_Rate': [52.1, 44.5, 55.4, 46.1, 58.9, 53.0, 47.5, 51.2, 49.8, 54.3],
    'Pressure': [25.5, 29.1, 35.4, 30.2, 38.5, 33.0, 31.5, 34.2, 32.8, 36.3]
}

df = pd.DataFrame(data)

# --- TASK 1: Create a simple Flow Rate Distribution Plot ---
# We use Matplotlib to show the figure, but Seaborn draws the histogram.
plt.figure(figsize=(7, 5))
sns.histplot(data=df, x='Flow_Rate', kde=True) # kde=True adds a smooth curve of the distribution
plt.title('Flow Rate Distribution (EDA)')
plt.show()


# --- TASK 2: Create a Correlation Scatter Plot ---
# We use the 'data' parameter to pass the whole DataFrame.
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x='Flow_Rate', y='Pressure', hue='Flow_Rate') # hue colors points by flow_rate
plt.title('Flow Rate vs. Pressure (Quick Correlation Check)')
plt.show()

