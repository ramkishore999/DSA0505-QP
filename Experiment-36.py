import matplotlib.pyplot as plt
import numpy as np

# Sample Data for three groups
# Group 1: High weight, varied height
weight1 = [67, 57.2, 59.6, 59.64, 55.8, 61.2, 60.45, 61, 56.23, 56]
height1 = [101.7, 197.6, 98.3, 125.1, 113.7, 157.7, 136, 148.9, 125.3, 114.9]

# Group 2: Mid weight, higher height
weight2 = [61.9, 64, 62.1, 64.2, 62.3, 65.4, 62.4, 61.4, 62.5, 63.6]
height2 = [152.8, 155.3, 135.1, 125.2, 151.3, 135, 182.2, 195.9, 165.1, 125.1]

# Group 3: Lower weight, consistent height
weight3 = [68.2, 67.2, 68.4, 68.7, 71, 71.3, 70.8, 70, 71.1, 71.7]
height3 = [165.8, 170.9, 192.8, 135.4, 161.4, 136.1, 167.1, 154.9, 151.1, 145.7]

# Create the scatter plots
plt.scatter(weight1, height1, marker='*', color='red', label='Group 1')
plt.scatter(weight2, height2, marker='o', color='green', label='Group 2')
plt.scatter(weight3, height3, marker='x', color='blue', label='Group 3')

# Set labels and title
plt.xlabel('Weight (kg)', fontsize=12)
plt.ylabel('Height (cm)', fontsize=12)
plt.title('Weight vs Height Comparison by Group', fontsize=14)

# Add a legend to identify the groups
plt.legend()

# Maintain visual consistency with previous lab standards
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Display the plot
plt.tight_layout()
plt.show()