from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.arange(0, 0.5, 0.1),
                      np.arange(0, 0.5, 0.1),
                      np.arange(0, 0.5, 0.1))

u = -y
v = -z
w = -x - 2*y - z+x*x*x

ax.quiver(x, y, z, u, v, w, length=0.1)

plt.show()