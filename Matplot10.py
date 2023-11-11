import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values1 = [3, 7, 2, 5]
values2 = [2, 5, 1, 6]

plt.bar(categories, values1, label='Group 1')
plt.bar(categories, values2, label='Group 2', bottom=values1)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()
