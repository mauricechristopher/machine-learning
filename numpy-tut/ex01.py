# Declare and initialize an array as done below
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Then, extract all odd numbers from arr to achieve the desired output.

# Desired output:
# #> [1 3 5 7 9]

import numpy as np 

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = np.delete(arr, [0, 2, 4, 6, 8])

print(arr)
        