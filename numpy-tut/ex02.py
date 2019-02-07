# convert a 1D array to a 2D array with 2 rows using arange

# Declare and initialize an array as done below
# np.arange(10)
# Try recreating this output:
# #>[[0 1 2 3 4]
#    [5 6 7 8 9]]

import numpy as np 

arr = np.arange(10)
new = np.reshape(arr, (-1, 5))

print(new)