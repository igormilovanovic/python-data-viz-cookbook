import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# add figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

coords = [
    (1., 0.),  # start position
    (0., 1.),
    (0., 2.),  # left side
    (1., 3.),
    (2., 3.),
    (3., 2.),  # top right corner
    (3., 1.),  # right side
    (2., 0.),
    (0., 0.),  # ignored
    ]

line_cmds = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

# construct path
path = Path(coords, line_cmds)
# construct path patch 
patch = patches.PathPatch(path, lw=1,
                          facecolor='#A1D99B', edgecolor='#31A354')
# add it to *ax* axes
ax.add_patch(patch)

ax.text(1.1, 1.4, 'Python', fontsize=24)
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 4)
plt.show()