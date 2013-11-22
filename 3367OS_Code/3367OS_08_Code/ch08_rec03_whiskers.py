'''
Chapter 08: Demonstration of box and whisker plot
'''
import matplotlib.pyplot as plt

# define data
PROCESSES = {
    "A": [12, 15, 23, 24, 30, 31, 33, 36, 50, 73],
    "B": [6, 22, 26, 33, 35, 47, 54, 55, 62, 63],
    "C": [2, 3, 6, 8, 13, 14, 19, 23, 60, 69],
    "D": [1, 22, 36, 37, 45, 47, 48, 51, 52, 69],
    }

DATA = PROCESSES.values()
LABELS = PROCESSES.keys()

plt.boxplot(DATA, widths=0.3)

# set ticklabel to process name
plt.gca().xaxis.set_ticklabels(LABELS)

# some makeup (removing chartjunk)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('left')
plt.gca().grid(axis='y', color='gray')

# set axes labels
plt.ylabel("Errors observed over defined period.")
plt.xlabel("Process observed over defined period.")

plt.show()
