import matplotlib.pyplot as plt
import numpy as np

# Sample Data
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)

# Setting the positions and width for the bars
x = np.arange(len(groups))  # The label locations
width = 0.35  # The width of the bars

# Create the plot
fig, ax = plt.subplots()

# Plotting the bars for men and women side-by-side
rects1 = ax.bar(x - width/2, means_men, width, label='Men', color='blue', edgecolor='black')
rects2 = ax.bar(x + width/2, means_women, width, label='Women', color='red', edgecolor='black')

# Add labels, title, and custom x-axis tick labels
ax.set_ylabel('Scores')
ax.set_xlabel('Groups')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend()

# Turn on minor ticks and configure the grid as seen in previous exercises
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Add values on top of the bars (optional)
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()