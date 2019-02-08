# Create a one-dimensional labeled array capable of holding any data type using a Series.

import pandas as pd
import numpy as np 

arr = np.array([3, 5, 7, 4, "sfd"])
ser = pd.Series(arr, index=['A', 'B', 'C', 'D'])
print(ser)