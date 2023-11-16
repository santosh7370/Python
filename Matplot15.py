import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.fill_between(x, y1, y2, color='skyblue', alpha=0.4, label='Filled Area')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Filled Area Plot')
plt.legend()
plt.show()
