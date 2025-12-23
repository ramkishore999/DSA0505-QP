import matplotlib.pyplot as plt
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Number of points
n = 50

# Generate random distributions for X and Y coordinates
x = np.random.rand(n)
y = np.random.rand(n)

# Generate random distribution for the sizes (area) of the "balls"
# Multiplying by a constant and squaring creates a visible range of sizes
sizes = (30 * np.random.rand(n))**2 

# Generate random colors for each ball
colors = np.random.rand(n)

# Create the scatter plot
# s=sizes sets the size of the markers
# c=colors sets the color mapping
# alpha=0.5 makes them semi-transparent to show overlaps
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, edgecolor='black')

# Add suitable labels and a title
plt.xlabel('X - Random Position')
plt.ylabel('Y - Random Position')
plt.title('Scatter Plot with Randomly Sized Balls')

# Maintain the grid style established in previous exercises
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Display the plot
plt.show()