import random
import time
from datetime import datetime

# Simulate a flow meter
tag = "FT-101"
units = "gpm" 

print("Starting Flow Logger for", tag)
print("Press CTRL+C to stop\n")

# Run a fake logger loop (like historian sampling)
try:
    while True:
        # Generate a random flow value (simulate sensor signal)
        value = round(random.uniform(40.0, 60.0), 2)

        # Timestamp
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log the value
        print(f"{ts} | {tag} | {value} {units}")

        # Wait 2 seconds before next sample
        time.sleep(2)

except KeyboardInterrupt:
    print("\nFlow Logger stopped.")

#Stretch goals if you want:
#
#Save each line to a text file (with open("log.txt", "a") as f: …).
#
#Change the time.sleep(2) to 1 second for faster sampling.
#
#Add a “status” field like RUNNING or FAULT.