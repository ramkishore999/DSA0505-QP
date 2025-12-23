import matplotlib.pyplot as plt

# Create the figure and a 2x3 grid of subplots
fig = plt.figure(figsize=(10, 8))

# Define the large top plot (spanning all 3 columns of the top row)
ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=3)
ax1.set_title("Main Large Plot")

# Define the three smaller bottom plots
ax2 = plt.subplot2grid((2, 3), (1, 0))
ax3 = plt.subplot2grid((2, 3), (1, 1))
ax4 = plt.subplot2grid((2, 3), (1, 2))

# Adjust layout so they don't overlap
plt.tight_layout()
plt.show()