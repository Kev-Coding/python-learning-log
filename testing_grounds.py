import pandas as pd
import numpy as np

time = pd.date_range("2023-01-01", periods=50, freq="min", tz="UTC")

np.random.seed(42)
for i in range(50):
    print(np.random.rand())
print(time)