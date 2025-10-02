import time
import random

# Use a 'with' statement to open and handle the file
with open('flow_meter_data.txt', 'a') as file:
    # Use a loop to simulate a data stream
    for i in range(10): 
        # Generate a random float to simulate a reading
        flow_rate = round(random.uniform(40.0, 60.0), 2)
        # Create a string to write to the file
        data_line = f"Timestamp: {time.time()} | Flow Rate: {flow_rate} GPM\n"
        print(data_line)
        # Write the string to the file
        file.write(data_line)
        time.sleep(0.5)

print("Data simulation complete. 'flow_meter_data.txt' has been created.")