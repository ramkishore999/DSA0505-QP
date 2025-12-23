import matplotlib.pyplot as plt
import numpy as np

# Sample Data
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)
std_men = (4, 3, 4, 1, 5)
std_women = (3, 5, 2, 3, 3)

x = np.arange(len(groups))  # The label locations
width = 0.35  # The width of the bars

# Create the plot
fig, ax = plt.subplots()

# Plot Men's bars with error bars
p1 = ax.bar(x, means_men, width, yerr=std_men, label='Men', color='blue', edgecolor='black', capsize=5)

# Plot Women's bars on top of Men's bars using the 'bottom' parameter
p2 = ax.bar(x, means_women, width, yerr=std_women, bottom=means_men, label='Women', color='red', edgecolor='black', capsize=5)

# Add labels, title, and custom x-axis tick labels
ax.set_ylabel('Scores')
ax.set_xlabel('Groups')
ax.set_title('Scores by Group and Gender (Stacked with Error Bars)')
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend()

# Configure the grid as seen in your previous lab exercises
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Add score labels on top of the stacked bars
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p2)

plt.tight_layout()
plt.show()