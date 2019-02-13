# Exercise 01: Linear circle graph

# Plot this linear graph using matplotlib with this data
# import numpy as np
# x = np.arange(1,11) 
# y = 2 * x + 5 

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11)
y = 2 * x + 5

plt.plot(x, y, 'bo')
plt.ylabel('y axis caption')
plt.xlabel('x axis caption')
plt.show()