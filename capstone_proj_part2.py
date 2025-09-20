import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file. This is an excellent practice for a modular pipeline.
df = pd.read_csv('simulated_sensor_data.csv')

# --- PART 1: Data Cleaning and Flatline Detection ---

# Use .dropna() as you did. It's the correct first step.
df = df.dropna().copy()
print("--- DataFrame after dropping rows with missing values ---")
print(df)

def analyze_data(df):
    """
    Performs data cleaning, statistical analysis, and correlation measurement.
    """
    # --- PART 1: Data Cleaning and Flatline Detection ---

    # We make a copy to ensure we do not get the SettingWithCopyWarning
    df_clean = df.copy()

    # We now create a mask for each column.
    flow_changed = (df["Flow_Rate"] != df["Flow_Rate"].shift()) | df.index.isin([0])
    pressure_changed = (df["Pressure"] != df["Pressure"].shift()) | df.index.isin([0])
    time_changed = (df["Timestamp"] != df["Timestamp"].shift()) | df.index.isin([0])

    # We combine the masks with the AND operator (`&`).
    # This creates a final mask that is True only if both Flow_Rate AND Pressure changed.
    final_mask = flow_changed & pressure_changed & time_changed

    # The first row of the DataFrame will always have a NaN, so we must manually set it to True.
    # final_mask.iloc[0] = True

    # We use `.loc` and our mask to select only the rows that are NOT flatlined.
    cleaned_df = df_clean.loc[final_mask].copy()

    # We can also reset the index for cleaner output.
    cleaned_df = cleaned_df.reset_index(drop=True)

    print("--- DataFrame after removing flatline signals ---")
    print(cleaned_df)

    # --- PART 2: Statistical Analysis ---



    # Calculate mean and standard deviation for Flow_Rate and Pressure
    stats = {
        "Flow_Rate": {
            "mean": cleaned_df["Flow_Rate"].mean(),
            "std": cleaned_df["Flow_Rate"].std()
        },
        "Pressure": {
            "mean": cleaned_df["Pressure"].mean(),
            "std": cleaned_df["Pressure"].std()
        }
    }
    # Print the statistics
    print("--- Statistical Analysis ---")       
    for key, value in stats.items():
        print(f"{key} - Mean: {value['mean']}, Std: {value['std']}")


    # remove outliers using z-score method
    z_scores = np.abs((cleaned_df[["Flow_Rate", "Pressure"]] - cleaned_df[["Flow_Rate", "Pressure"]].mean()) / cleaned_df[["Flow_Rate", "Pressure"]].std())
    cleaned_df = cleaned_df[(z_scores < 3).all(axis=1)]

    # We can also reset the index for cleaner output.
    cleaned_df = cleaned_df.reset_index(drop=True)
    print("--- DataFrame after removing outliers ---")
    print(cleaned_df)

    # --- PART 3: Correlation Measurement ---

    correlation_matrix = cleaned_df[["Flow_Rate", "Pressure"]].corr()
    print("--- Correlation Matrix ---")
    print(correlation_matrix)

    # Use .describe() to get a quick overview of the statistics.
    print("--- Statistical Overview ---")
    print(cleaned_df[["Flow_Rate", "Pressure"]].describe()) 

    return cleaned_df
#This was added after the project was completed.
# As I learn more about plotting, I will update this function to make it better.
# --- PART 4: Data Visualization ---
def visualize_data(cleaned_df): 
    """
    Visualizes the cleaned data using subplots.
    """
    # use subplots with a figure with two plots stacked on top of each other
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))  # 2 rows, 1 column

    # First subplot: Line chart of Flow Rate vs Timestamp
    ax1.plot(pd.to_datetime(cleaned_df['Timestamp'], unit='s'), cleaned_df['Flow_Rate'], marker='o', linestyle='-', color='b', label='Flow Rate')
    ax1.plot(pd.to_datetime(cleaned_df['Timestamp'], unit='s'), cleaned_df['Pressure'], marker='x', linestyle='--', color='r', label='Pressure')
    ax1.set_xlabel("Timestamp")        # X-axis label
    ax1.set_ylabel("Flow Rate & Pressure")    # Y-axis label
    ax1.set_title("Flow Rate & Pressure vs Timestamp")  # Title of the plot
    ax1.grid(True)  # Add grid for better readability
    ax1.legend()  # <-- this shows the labels from above on the plot

    # Second subplot: Scatter plot of Flow Rate vs Pressure
    ax2.scatter(cleaned_df['Pressure'], cleaned_df['Flow_Rate'], color='r', marker='x')
    ax2.set_xlabel("Pressure")        # X-axis label
    ax2.set_ylabel("Flow Rate")    # Y-axis label
    ax2.set_title("Correlation between Flow Rate and Pressure")  # Title of the plot
    ax2.grid(True)  # Add grid for better readability

    plt.tight_layout()  # Adjust layout to prevent overlap
    
    plt.show()

def main():

    # Run the analysis
    cleaned_df = analyze_data(df)

    # Visualize the cleaned data
    visualize_data(cleaned_df)
    
    # You can now continue with your next tasks here...

if __name__ == "__main__":
    main()
