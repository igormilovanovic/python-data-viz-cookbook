import matplotlib.pyplot as pl
import numpy as np

# generate uniformly distributed 
# 256 points from -pi to pi, inclusive
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

# these are vectorised versions
# of math.cos, and math.sin in built-in Python maths
# compute cos for every x
y = np.cos(x)

# compute sin for every x
y1 = np.sin(x)

# plot both cos and sin
pl.plot(x, y)
pl.plot(x, y1)

pl.show()
