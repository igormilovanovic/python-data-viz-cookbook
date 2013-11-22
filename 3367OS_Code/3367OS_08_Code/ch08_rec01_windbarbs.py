import matplotlib.pyplot as plt
import numpy as np

# north-south speed
# we define speed of the wind from south to north 
# in knots (nautical miles per hour)
V = [0, -5, -10, -15, -30, -40, -50, -60, -100]

# helper to coordinate size of other values with size of V vector
SIZE = len(V)

# east-west speed
# we define speed of the wind in east-west direction
# here, the "horizontal" speed component is 0
# our staff part of the wind barbs is vertical
U = np.zeros(SIZE)

# lon, lat
# we define linear distribution in horizontal manner 
# of wind barbs, to spot increase in speed as we read figure from left to right
y = np.ones(SIZE) 
x = [0, 5, 10, 15, 30, 40, 50, 60, 100]

# plot the barbs
plt.barbs(x, y, U, V, length=9)

# misc settings
plt.xticks(x)
plt.ylim(0.98, 1.05)

plt.show()
