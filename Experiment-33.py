import matplotlib.pyplot as plt
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Generate a random distribution of 50 points for X and Y
x = np.random.randn(50)
y = np.random.randn(50)

# Create the scatter plot with empty circles
# facecolors='none' makes the circles empty
# edgecolors sets the color of the circle borders
plt.scatter(x, y, facecolors='none', edgecolors='blue', s=80)

# Add suitable labels and a title
plt.xlabel('X - Random Distribution')
plt.ylabel('Y - Random Distribution')
plt.title('Scatter Plot with Empty Circles')

# Optional: Add a grid to match previous lab exercises
plt.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.show()