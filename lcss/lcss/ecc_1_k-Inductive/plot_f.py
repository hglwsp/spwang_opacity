import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


Y, X = np.mgrid[0:0.1:100j, 0:10:100j]
U = X + Y + 0.02
V = Y + 0.04
speed = np.sqrt(U**2 + V**2)

fig = plt.figure(figsize=(7, 9))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])

#  Varying density along a streamline
ax0 = fig.add_subplot(gs[0, 0])
ax0.streamplot(X, Y, U, V, density=[0.5, 1])
ax0.set_title('Varying Density')

plt.tight_layout()
plt.show()