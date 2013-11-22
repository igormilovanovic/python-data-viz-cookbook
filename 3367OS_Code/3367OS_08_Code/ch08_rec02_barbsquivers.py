import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 8) 
y = np.linspace(  0, 20, 8)

# make 2D coordinates
X, Y = np.meshgrid(x, y)

U, V = X + 25, Y - 35


# plot the barbs
plt.subplot(1,2,1)
plt.barbs(X, Y, U, V, flagcolor='green', alpha=0.75)
plt.grid(True, color='gray')

# compare that with quiver / arrows 
plt.subplot(1,2,2)
plt.quiver(X, Y, U, V, facecolor='red', alpha=0.75)

# misc settings
plt.grid(True, color='grey')
plt.show()
