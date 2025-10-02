import time
import random

# Use a 'with' statement to open and handle the file
with open('flow_meter_data2.csv', 'w') as file:
    # Write the header row first
    file.write("Timestamp,Flow Rate\n")

    # Use a loop to simulate a data stream
    for i in range(10):
        # Generate a random float for flow rate
        flow_rate = round(random.uniform(40.0, 60.0), 2)
        # Create a string with a comma to separate the values
        data_line = f"{time.time()},{flow_rate}\n"

        # Write the string to the file
        file.write(data_line)
        time.sleep(0.5)

print("Data simulation complete. 'flow_meter_data2.csv' has been created.")