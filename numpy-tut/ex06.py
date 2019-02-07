# Exercise 06:  Drop all missing values from a numpy array

# np.array([1,2,3,np.nan,5,6,7,np.nan])
# Output: 
# [ 1.  2.  3.  5.  6.  7.]

import numpy as np

arr = np.array([1,2,3,np.nan,5,6,7,np.nan])
arr = arr[~np.isnan(arr)]

print(arr)