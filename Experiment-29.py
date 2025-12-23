import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Define a list of colors for each bar
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan']

# Create the bar chart with custom colors
plt.bar(languages, popularity, color=colors, edgecolor='black')

# Set labels and title
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages\n' + 'with Unique Colors for Each Bar')

# Configure grid lines as seen in your previous samples
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Display the chart
plt.show()