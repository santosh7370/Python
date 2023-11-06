import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

# set random state for reproducibility
np.random.seed(19695601)

diff = 0.01
ax = np.arange(0, 10, diff)
n = np.random.randn(len(ax))
by = np.exp(-ax / 0.05)

cn = np.convolve(n, by) * diff
cn = cn[:len(ax)]
s = 0.1 * np.sin(2 * np.pi * ax) + cn

plt.subplot(211)
plt.plot(ax, s)
plt.subplot(212)
plt.psd(s, 512, 1 / diff)

plt.show()
