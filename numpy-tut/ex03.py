# # Create a 2d array with 3 rows and 4 columns

# myList = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]

# Inspect its shape, datatype, size, number dimensions

import numpy as np

arr = np.array([[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]])

print("Array:", arr)
print("Shape:",arr.shape)
print("Size:", arr.size)
print("Datatype:", arr.dtype.name)
print("Num. of Dimensions:", arr.ndim)