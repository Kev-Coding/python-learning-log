# import pandas as pd
# import numpy as np
# from functools import reduce

# from capstone_project import simulate_data # We will use reduce to combine our masks


# # Load the CSV file. This is an excellent practice for a modular pipeline.
# df = pd.read_csv('simulated_sensor_data.csv')

# # --- PART 1: Data Cleaning and Flatline Detection ---

# # Use .dropna() as you did. It's the correct first step.
# df = df.dropna().copy()
# print("--- DataFrame after dropping rows with missing values ---")
# print(df)
# def analyze_data(df):
#     """
#     Performs data cleaning, statistical analysis, and correlation measurement.
#     """
#     # --- PART 1: Data Cleaning and Flatline Detection ---

#     # We make a copy to ensure we do not get the SettingWithCopyWarning
#     df_clean = df.copy()

#     # Get a list of the numerical columns to check for flatlines
#     cols_to_check = ['Timestamp', 'Flow_Rate', 'Pressure']
    
#     # The `diff()` method calculates the difference between consecutive rows.
#     # The `ne(0)` method is a clean way of writing `!= 0`.
#     # The `.any(axis=1)` method checks if ANY value in a row is non-zero.
#     # This is a robust and scalable way to detect flatlines.
#     flatline_mask = df_clean[cols_to_check].diff().ne(0).any(axis=1)
    
#     # We must explicitly set the first row to True because diff() will
#     # always return a NaN for that row, causing the mask to be False.
#     flatline_mask.iloc[0] = True

#     # We use `.loc` and our mask to select only the rows that are NOT flatlined.
#     cleaned_df = df_clean.loc[flatline_mask].copy()

#     # We can also reset the index for cleaner output.
#     cleaned_df = cleaned_df.reset_index(drop=True)

#     print("--- DataFrame after removing flatline signals ---")
#     print(cleaned_df)
    
#     return cleaned_df
# def main():

#     # Run the analysis
#     cleaned_df = analyze_data(df)
    
#     # You can now continue with your next tasks here...

# if __name__ == "__main__":
#     main()