import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec


# set random valueto ensure reproducibility
random_rep = np.random.RandomState(19680801) 

frame_per_second = 1000
a = np.linspace(0, 0.3, 301)
b = np.array([2, 8]).reshape(-1, 1)
c = np.array([150, 140]).reshape(-1, 1)
d = (b * np.exp(2j * np.pi * c * a)).sum(axis = 0) + 5 * random_rep.randn(*a.shape)

figure, (a0, a1) = plt.subplots(ncols = 2,
								constrained_layout = True)

e = np.arange(-50, 30, 10)
f = (e[0], e[-1])
g = np.arange(-500, 550, 200)

a0.psd(d, NFFT = 301, 
	Fs = frame_per_second,
	window = mlab.window_none, 
	pad_to = 1024,
	scale_by_freq = True)

a0.set_title('Periodo-gram')
a0.set_yticks(e)
a0.set_xticks(g)
a0.grid(True)
a0.set_ylim(f)

a1.psd(d, NFFT = 150,
	Fs = frame_per_second,
	window = mlab.window_none, 
	pad_to = 512, 
	noverlap = 75,
	scale_by_freq = True)

a1.set_title('Welch')
a1.set_xticks(g)
a1.set_yticks(e)

# overwriting the y-label added by `psd`
a1.set_ylabel('')
a1.grid(True)
a1.set_ylim(f)

plt.show()
