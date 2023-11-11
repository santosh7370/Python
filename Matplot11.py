import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100, 5)  # Random data with 5 columns

plt.boxplot(data, labels=['A', 'B', 'C', 'D', 'E'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()
