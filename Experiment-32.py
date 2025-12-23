import matplotlib.pyplot as plt
import numpy as np

# Set a seed for reproducibility (optional)
np.random.seed(42)

# Generate a random distribution of 100 points for X and Y
# np.random.randn generates values from a normal distribution
x = np.random.randn(100)
y = np.random.randn(100)

# Create the scatter plot
plt.scatter(x, y, color='blue', alpha=0.5)

# Add suitable labels and a title
plt.xlabel('X - Random Distribution')
plt.ylabel('Y - Random Distribution')
plt.title('Scatter Plot of Random X and Y Distributions')

# Display the plot
plt.show()