import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create the bar chart
plt.bar(languages, popularity, color='blue', edgecolor='black')

# Set labels for axes and the title
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Language\n' + 'Worldwide, Oct 2017 compared to a year ago')

# Turn on minor ticks and configure the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Display the chart
plt.show()