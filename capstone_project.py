import pandas as pd
import numpy as np

def simulate_data():
    """
    Simulates a DataFrame with 50 rows of correlated sensor data, including noise,
    outliers, and flatline signals. This will be for 2 sensors. 
    """
    np.random.seed(42)  # For reproducibility

    # Generate time points in UTC
    sim_time = pd.date_range("2023-01-01", periods=50, freq="min", tz="UTC")
    time = np.arange(50)

    # Simulate base signals for two sensors
    sensor1 = np.sin(0.2 * time) + np.random.normal(20, 0.3, size=time.size)
    sensor2 = np.cos(0.2 * time) + np.random.normal(20, 0.3, size=time.size)

    # Introduce outliers
    sensor1[10] += 3
    sensor2[20] -= 3
    
    # Introduce flatline signals
    sensor1[30:35] = 0

    
    data = pd.DataFrame({
        'time': sim_time,
        'sensor1': sensor1,
        'sensor2': sensor2
    })
    
    return data

def main():
    # Simulate the data
    df = simulate_data()
    
    # Display the first few rows of the DataFrame
    print(df)
    
    # Save to CSV for further analysis if needed
    df.to_csv('simulated_sensor_data.csv', index=False)
    print("Simulated data saved to 'simulated_sensor_data.csv'.") 

if __name__ == "__main__":
    main()

