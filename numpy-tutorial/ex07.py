#  Exercise 07:  Find duplicate records in a numpy array

# np.random.seed(100)
# a = np.random.randint(0, 5, 10)
# print('Array: ', a)
# Output:
# #> [False  True False  True False False  True  True  True  True]

import numpy as np

a = np.random.seed(100)
a = np.random.randint(0, 5, 10)

out = np.full(a.shape[0], True)                 # Create All True Array
uniques = np.unique(a, return_index=True)[1]    # Find Unique Elements
out[uniques] = False                   # Mark Them as False


print(out)