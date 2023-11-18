import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)
r = 2 + np.cos(theta)

plt.polar(theta, r)
plt.title('Polar Plot')
plt.show()
