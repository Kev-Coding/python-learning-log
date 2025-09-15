import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

def simulate_data():
    """
    Simulates a DataFrame with 50 rows of correlated sensor data, including noise,
    outliers, and flatline signals. This will be for 2 sensors.
    """
    np.random.seed(42)  # For reproducibility. Ensures the random numbers are the same each time.

    # Generate a numerical timestamp in seconds (Unix epoch time).
    # This is the best practice for filtering and ML models.
    sim_time = pd.date_range("2023-01-01", periods=50, freq="min").astype(np.int64) // 10**9
    
    # Use a range for simulating the correlated data.
    time_series = np.arange(50)

    # --- Simulate correlated sensor signals with noise ---
    # np.random.normal(mean, standard_deviation, size)
    # The `loc` (mean) is 20, and the `scale` (standard deviation) is 0.1.
    # A smaller standard deviation creates a tighter correlation.
    flow_rate = np.sin(0.2 * time_series) + np.random.normal(20, 0.1, size=time_series.size)
    pressure = np.cos(0.2 * time_series) + np.random.normal(20, 0.1, size=time_series.size)

    # --- Introduce anomalies and flatline signals ---
    
    # Introduce outliers: an unusually high reading and an unusually low reading.
    flow_rate[10] += 3
    pressure[20] -= 3
    
    # Introduce a flatline signal by setting consecutive readings to the same value.
    flow_rate[30:35] = flow_rate[30]

    # Assemble the data into a DataFrame.
    data = pd.DataFrame({
        'Timestamp': sim_time,
        'Flow_Rate': flow_rate,
        'Pressure': pressure
    })
    
    # Return the simulated DataFrame.
    return data

def main():
    """
    This is the main function that executes our data simulation and saves the data to a CSV.
    """
    # Simulate the data
    df = simulate_data()
    
    # Display the first few rows of the DataFrame to confirm the data
    print("--- First 5 rows of simulated data ---")
    print(df.head())
    
    # Save the data to a CSV file for future use in the project.
    # The 'index=False' argument prevents pandas from writing the DataFrame index to the CSV file.
    df.to_csv('simulated_sensor_data.csv', index=False)
    print("\nSimulated data saved to 'simulated_sensor_data.csv'.")
    
    # Now, we would call the next function in our pipeline to analyze the data.
    # For now, we will just print a message to show the next step.
    print("\nReady for the next step: Data Analysis.")

if __name__ == "__main__":
    main()

