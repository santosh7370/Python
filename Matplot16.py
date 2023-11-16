import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.step(x, y, label='Step Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Step Plot')
plt.legend()
plt.show()
