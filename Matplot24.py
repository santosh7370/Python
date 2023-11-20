import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 100)
y = np.log10(x)

plt.plot(x, y)
plt.xscale('log')
plt.xlabel('X-axis (log scale)')
plt.ylabel('Y-axis')
plt.title('Logarithmic Scale Plot')
plt.show()
