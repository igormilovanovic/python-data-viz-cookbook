import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Red Yellow Green diverging colormap
red_yellow_green = ['#d73027', '#f46d43', '#fdae61',
                    '#fee08b', '#ffffbf', '#d9ef8b',
                    '#a6d96a', '#66bd63', '#1a9850']

sample_size = 1000
fig, ax = plt.subplots(1)

for i in range(9):
    y = np.random.normal(size=sample_size).cumsum()
    x = np.arange(sample_size)
    ax.scatter(x, y, label=str(i), linewidth=0.1, edgecolors='grey', 
               facecolor=red_yellow_green[i])

ax.legend()
plt.show()
