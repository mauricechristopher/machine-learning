# Exercise 04: Scatter plot with groups

# Plot a scatter plot with this data:

# # Create data
# N = 60
# g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
# g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
# g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))
 
# data = (g1, g2, g3)
# colors = ("red", "green", "blue")
# groups = ("coffee", "tea", "water")

import numpy as np
import matplotlib.pyplot as plt

# Create data
N = 60
g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))
 
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("coffee", "tea", "water")
 
# Create plot
plot = plt.figure()
sub = plot.add_subplot(1, 1, 1, facecolor="1.0")
 
for data, color, group in zip(data, colors, groups):
    x, y = data
    sub.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('Matplot scatter plot')
plt.legend(loc=2)

plt.show()