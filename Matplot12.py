import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100, 5)  # Random data with 5 columns

plt.violinplot(data, showmeans=True)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Violin Plot')
plt.show()
