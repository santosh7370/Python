import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
u = np.cos(x)
v = np.sin(2 * x)

plt.quiver(x, y, u, v, scale=5, color='r', width=0.01)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quiver Plot')
plt.show()
