import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

plt.barh(categories, values)
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart')
plt.show()
