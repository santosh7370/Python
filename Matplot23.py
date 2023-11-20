import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
error = [0.5, 0.3, 0.2, 0.8, 0.1]

plt.errorbar(x, y, yerr=error, fmt='o', capsize=5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Error Bar Plot')
plt.show()
