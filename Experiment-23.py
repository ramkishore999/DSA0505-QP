import matplotlib.pyplot as plt

with open('test.txt', 'w') as f:
    f.write("1 2\n2 4\n3 1")

x = []
y = []
with open('test.txt', 'r') as f:
    for line in f:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()