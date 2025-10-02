import pandas as pd
import numpy as np

time = pd.date_range("2023-01-01", periods=50, freq="min", tz="UTC")

np.random.seed(42)
for i in range(50):
    print(np.random.rand())
print(time)



# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original array shape:", arr.shape)
print("Original array:\n", arr)

# Flatten it
flat = arr.flatten()
print("\nFlattened array shape:", flat.shape)
print("Flattened array:\n", flat)