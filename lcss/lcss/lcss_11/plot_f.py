import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
import random
###################################################################
# we discover that if f global suit '->', opacity can be proved.  #
###################################################################

###################################################################
# we find dt-cs satisfy the condition of field                    #
###################################################################


# system2
alpha = 0.05
Te=15
ah=3.6e-3
Th=55
ae=0.008

Y, X = np.mgrid[17:25:100j, 17:25:100j]
U = (1-2*alpha-ae-ah*0.5)*X+ alpha*Y+ ae*Te + 2.5 * 0.5
V = (1-2*alpha-ae-ah*0.5)*X+ alpha*Y+ ae*Te + 2.5 * 0.5

# system1
# Y, X = np.mgrid[0:0.1:100j, 1:5:100j]
# U = X + Y
# V = 0.05*np.exp(Y) + 0.01
# U = U - Y
# V = V - X
# speed = np.sqrt(U**2 + V**2)

# system1
# Z,Y, X = np.mgrid[0:2:100j,0:2:100j, 0:2:100j]
# U = X - Y
# V = Y - Z
# W = -X - 2*Y + X*X*X
# U = U - X
# V = V - Y
# W = W - Z
# speed = np.sqrt(U**2 + V**2 + W**2)

# system1
# Y, X = np.mgrid[0:0.1:100j, 0:10:100j]
# U = X + 0.5*Y
# V = Y
# U = U - Y
# V = V - X
# speed = np.sqrt(U**2 + V**2)


# system3  non-linear
# PI = 3.14
# Y, X = np.mgrid[0 : PI:100j, 0:5:100j]
# U = X + Y * np.cos(Y)
# V = X + Y * np.sin(Y)
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)


# system4  non-linear
# m = 0.0076
# g = 9.8
# l = 0.041
# J = 0.00024
# km = 11
# tol = 0.4
# u = 1
# pi = 3.14
# Y, X = np.mgrid[-3:3:100j, -pi:pi:100j]
# U = (X + Y)
# V = m * g * l * 1/J * np.sin(X) - 1/tol * Y + km * 1/tol * u + Y
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)

#system non-linear
# pi = 3.14
# Y, X = np.mgrid[0:1.6:100j, 0:1.6:100j]
# U = 0.1 * X
# V = np.sin(0.25*pi*X ) + 1
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)

#system non-linear
# pi = 3.14
# Y, X = np.mgrid[-2:2:100j, -2:0:100j]
# # U = np.exp(-X) - 1 + X + 0.01 + 0.01*Y
# U = np.exp(-X) - 1 + X  + 0.01*Y + 0.5
# V = -np.sin(X) * np.sin(X) + Y
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)
#
#
#
# system5   #xuebai  #success
# Y, X = np.mgrid[2:12:100j, 0:0.1:100j]
# U = -2*X + Y
# V = X + 2*Y
# U = U - X
# V = V - Y

# system6   #xuebai  #success
# Y, X = np.mgrid[2:15:100j, 0:0.1:100j]
# U =  Y
# V =  X
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)

# system7   #hscc
# Y, X = np.mgrid[-2:2:100j, -2:2:100j]
# U =  X + Y
# V =   -X - 0.5*X*X*X + Y
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)

# # system8   #Li wang
# Y, X = np.mgrid[0:8:100j, 0:0.5:100j]
# # Y, X = np.mgrid[4:8:100j,0:1:100j]
# U =  X + Y + 0.04
# V =  X  - X*X*X + 0.01
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)

# system9   #xuebai
# Y, X = np.mgrid[0:8:100j, 0:1:100j]
# U =  X + Y
# V =    Y*Y
# # U = U - X
# # V = V - Y
# speed = np.sqrt(U**2 + V**2)

# system10   # 1-D
# Y, X = np.mgrid[0:10:100j, 0:10:100j]
# k0 = 4
# w = 1
# U =   k0 + np.sin(w*X)
# V =  0
# U = U - X
# V = V - Y
# speed = np.sqrt(U**2 + V**2)


# # system11   #1506.05885
# Y, X = np.mgrid[-12:12:100j, -12:12:100j]
# Y, X = np.mgrid[3:10:100j,0.5:1:100j]
# U =  X*Y
# V =  X
# # U = U - X
# # V = V - Y
# speed = np.sqrt(U**2 + V**2)


fig = plt.figure(figsize=(7, 9))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])
#  Varying density along a streamline
ax0 = fig.add_subplot(gs[0, 0])
ax0.streamplot(X, Y,U, V, density=[0.5, 1])
ax0.set_title('Varying Density')

plt.tight_layout()
plt.show()