import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create the horizontal bar chart
# barh is used for horizontal bars
plt.barh(languages, popularity, color='green', edgecolor='black')

# Set labels for axes and the title
plt.xlabel('Popularity')
plt.ylabel('Languages')
plt.title('Popularity of Programming Languages\n' + 'Worldwide, Oct 2017 compared to a year ago')

# Turn on minor ticks and configure the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Invert the y-axis so Java is at the top (optional)
plt.gca().invert_yaxis()

# Display the chart
plt.show()