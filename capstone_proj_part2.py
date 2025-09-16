import pandas as pd
import numpy as np

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

def main():

    # Run the analysis
    cleaned_df = analyze_data(df)
    
    # You can now continue with your next tasks here...

if __name__ == "__main__":
    main()
