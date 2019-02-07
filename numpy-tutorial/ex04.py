# Exercise 04:  Stack them (arrays) up!

# Stack the arrays a and b vertically
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)
# Try creating this output:

# #> [[0 1 2 3 4]
#       [5 6 7 8 9]
#       [1 1 1 1 1]
#       [1 1 1 1 1]]

import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2,-1)
print(np.vstack((a,b)))
